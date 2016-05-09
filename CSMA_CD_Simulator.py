import queue, Station
import Event
import time
import sys
import Frame
import Transmission
import random

class CSMA_CD_Simulator:

    '''
    Discrete event simulation of a CSMA/CD network
    '''

    evtQ = ''
    q_size = 0
    distance = 0
    stations = []
    simTime = 0
    positionToStation = {}
    idToStation = {}
    last_event = Event.Event(None, None, None, None)
    list_of_transmissions = []
    back_off_time = random.uniform(.01, .98)


    def __init__(self, distance):
        '''
        load the simulator with the given list of ARRIVAL events,
        and initialize the list of in-progress transmission events'
        :return:
        '''
        self.distance = distance
        self.simTime = 0
        self.evtQ = queue.Queue()
        self.list_of_transmissions.clear()

    def set_back_off_time(self, custom_time):
        self.back_off_time = custom_time

    def addEvent(self, evt):
        '''
        Add the event to self.evtQ, maintaining the event queue in
        order of increasing event time
        '''
        self.evtQ.put(evt)
        self.q_size += 1
        self.set_back_off_time(random.uniform(.01, .98))

    def addStation(self, station):
        self.stations.append(station)
        self.positionToStation[station.position] = station
        self.idToStation[station.stationNum] = station


    def cancelCompletion(self, messageID):
        '''
        Cancel both the TRANSMIT_COMPLETE and RECEPTION_COMPLETE
        events associated with message _messageID_
        '''
        pass


    def media_busy(self, position, simTime):
        '''
        Return True if a current or recently-completed transmission
        is detected at _position_ at simulation time _simTime_
        '''
        sender_station_id = self.last_event.stationId
        sender_station = self.idToStation[sender_station_id]
        distance = abs(sender_station.position - position)
        sender_event_time = self.last_event.time
        propagation_delay = distance / 200

        #packet_size = sys.getsizeof(self.last_event.msg) + 26
        packet_size = len(self.last_event.msg.message) + 26

        transmission_delay = (packet_size * 8)/100

        if simTime < (sender_event_time + propagation_delay) or simTime > (sender_event_time + propagation_delay + transmission_delay ):
            return False

        else:
            return True


    def processSingleEvent(self):
        '''
        Process the first event in the event queue,
        possibly changing state, scheduling new events, or
        cancelling future events
        '''
        event = self.evtQ.get()
        self.q_size -= 1
        self.simTime = event.time
        self.last_event = event

        #ARRIVAL EVENTS###########################################################################
        if event.eventType == 1 or event.eventType == 2:

            #frame (frameNo, message, senderId, destId)
            #event ( eventType_, time, stationId, msg):

            #IF MEDIA IS NOT BUSY
            if self.media_busy(event.stationId, event.time) == False:

                #IF THERE IS AN ONGOING TRANSMISSION
                if len(self.list_of_transmissions) > 0:
                    self.list_of_transmissions.clear()
                    event_ = self.evtQ.get()

                    #clear the reception complete and transmission complete from the queue
                    while self.evtQ._qsize() != 0:
                        self.evtQ.get()

                    #schedule collision 1- from the current station
                    colEvent1 = Event.Event(Event.Event.COLLISION_DETECT,event.time, event.stationId, event.msg)
                    #schedule collision 2- from the ongoing transmission
                    colEvent2 = Event.Event(Event.Event.COLLISION_DETECT,event_.time, event_.stationId, event_.msg)

                    self.evtQ.put(colEvent1)
                    self.evtQ.put(colEvent2)

                #IF THERE IS NOT AN ONGOING TRANSMISSION
                elif (self.media_busy(event.stationId, event.time) == False) and len(self.list_of_transmissions)== 0:
                                                        #the transmission complete = arrival time + transmission delay
                                                        #transmission delay = (packet size * 8) / bitrate (100)

                    transmission_delay = (41*8)/100
                    transmission_complete_time = event.time + transmission_delay

                    msg1 = Frame.Frame(2,'Hello Station 2',1,2)
                    next_event = Event.Event(Event.Event.TRANSMIT_COMPLETE, transmission_complete_time, 1, msg1)
                    self.evtQ.put(next_event)
                    self.q_size += 1

                    #reception complete = arrival time + transmission delay + propagation delay
                        #transmission delay = (packet size * 8) / bitrate (100 bits per microsecond)
                        #propagation delay = (locationReceiver - locationSender) / propagation speed (600 meters per microsecond
                    # )
                    distance_between_stations = abs(self.idToStation[event.msg.senderId].position - self.idToStation[event.msg.destId].position)
                    reception_complete_time = event.time + transmission_delay +  distance_between_stations
                    msg2 = Frame.Frame(3,'Hello Station 2',1,2)
                    next_event2 = Event.Event(Event.Event.RECEPTION_COMPLETE, reception_complete_time, 1, msg2)
                    self.evtQ.put(next_event2)
                    self.q_size += 1


                    #create a new transmission
                    new_transmission = Transmission.Transmission(event.time,reception_complete_time ,1)
                    self.list_of_transmissions.append(new_transmission)




            #IF MEDIA IS BUSY
            else:
                re_msg = Frame.Frame(event.msg.frameNo,event.msg.message, event.msg.senderId, event.msg.destId)

                if (self.last_event == None):
                    re_evt = Event.Event(Event.Event.TRANSMIT_ATTEMPT, event.time + self.back_off_time, event.stationId, re_msg)
                    self.evtQ.put(re_evt)
                else:
                    re_evt = Event.Event(Event.Event.TRANSMIT_ATTEMPT, self.last_event.time + self.back_off_time, event.stationId, re_msg)
                    self.evtQ.put(re_evt)


        #TRANSMISSION COMPLETE###########################################################################
        if event.eventType == 3:
            self.list_of_transmissions.clear()
            print('trans complete')

        #COLLISION DETECT################################################################################
        if event.eventType == 5:
            jam_event = Event.Event(Event.Event.JAMMING_END, event.time, event.stationId, event.msg)
            self.evtQ.put(jam_event)

        #JAMMING END################################################################################
        if event.eventType == 6:
            new_attempt = Event.Event(Event.Event.TRANSMIT_ATTEMPT, event.time, event.stationId, event.msg)
            self.evtQ.put(new_attempt)

    def run(self):
        '''
        Process all the events in the event queue,
        possibly changing state, scheduling new events, or
        cancelling future events at each event
        '''
        pass

