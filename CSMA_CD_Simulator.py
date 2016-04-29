import queue, Station
import Event
import time
import sys
import Frame

class CSMA_CD_Simulator:

    '''
    Discrete event simulation of a CSMA/CD network
    '''

    #TODO createEventQueue
    #TODO haveAStationTransmitAFrame
    #TODO haveAStationReceiveAFrame
    #TODO calculateIfClearToSend
        #TODO handleTransmissionAttempts
    #TODO updateEventQueue

    #TODO calculateCurrentPositionOfSignal ---> speed *

    evtQ = queue.Queue()
    q_size = 0
    distance = 0
    stations = []
    simTime = 0
    positionToStation = {}
    idToStation = {}
    last_event = Event.Event(None, None, None, None)

   # def __init__(self, arrivalEvents):
        #'''
        #load the simulator with the given list of ARRIVAL events,
        #and initialize the list of in-progress transmission events'
        #:return:
        #'''
     #   pass


    def __init__(self, distance):
        '''
        load the simulator with the given list of ARRIVAL events,
        and initialize the list of in-progress transmission events'
        :return:
        '''
        self.distance = distance
        self.simTime = 0
        self.evtQ = queue.Queue()

    def addEvent(self, evt):
        '''
        Add the event to self.evtQ, maintaining the event queue in
        order of increasing event time
        '''
        self.evtQ.put(evt)
        self.q_size += 1

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
        print('q size', self.evtQ._qsize())
        event = self.evtQ.get()
        self.q_size -= 1
        print('q size', self.evtQ._qsize())
        print('event details', event.eventType)


        self.simTime = event.time
        self.last_event = event
        print("last event event type" , event.eventType)
        if event.eventType == 1:
            print('EVENT MATCH !!')
            msg1 = Frame.Frame(2,'Hello Station 2',1,2)
            next_event = Event.Event(Event.Event.TRANSMIT_COMPLETE,126.73, 1, msg1)
            self.evtQ.put(next_event)
            print('new q size', self.evtQ._qsize())
            self.q_size += 1

            msg2 = Frame.Frame(3,'Hello Station 2',1,2)
            next_event2 = Event.Event(Event.Event.RECEPTION_COMPLETE, 126.73, 1, msg2)
            self.evtQ.put(next_event2)
            self.q_size += 1
            print('new q size 2', self.evtQ._qsize())

            print('QUEUE SIZE', self.evtQ._qsize())

    def run(self):
        '''
        Process all the events in the event queue,
        possibly changing state, scheduling new events, or
        cancelling future events at each event
        '''
        pass

