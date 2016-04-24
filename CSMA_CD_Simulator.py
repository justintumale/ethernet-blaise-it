import queue
import Event
import time
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

    #Create Event Queue
    EventQueue = queue.Queue()

    #Create Stations
    class station:
        stationId = 0
        def __init__(self, stationId):
            self.stationId = stationId

    S1 = station(1)
    S2 = station(2)
    S3 = station(3)
    S4 = station(4)

    #Create sample simulated events
    event1 = Event.Event(time.time(), S1.stationId, "Hello simulator.")

    #add event to EventQueue
    EventQueue.put(event1)

    #Test event queue
    print('Testing . . . . . .')
    event_test = EventQueue.get()
    print(event_test.time)
    print(event_test.stationId)
    print(event_test.msg)


    def __init__(self):
        '''
        load the simulator with the given list of ARRIVAL events,
        and initialize the list of in-progress transmission events'
        :return:
        '''
        pass

    def detect_collision_time1(self, transmit_event1, transmit_event2):
        '''
        Returns the expected time of the COLLISION_DETECT event
        at station 1 resulting from the two transmission events, where
        transmit_event1 is the transmission from station 1 and transmit_event2
        is the transmission from station 2
        :param transmit_event1:
        :param transmit_event2:
        :return:
        '''
        pass

    def detect_collision_time2(self, transmit_event1, transmit_event2):
        '''
        Returns the expected time of the COLLISION_DETECT event
        at station 2 resulting from the two transmission events, where
        transmit_event1 is the transmission from station 1 and transmit_event2
        is the transmission from station 2
        :param transmit_event1:
        :param transmit_event2:
        :return:
        '''
        pass

    def receive_completion_time(self, transmit_event):
        '''
        Returns the expected time of the RECEPTION_COMPLETE event
        marking the end of the reception of transmit_event
        :param transmit_event:
        :return:
        '''
        pass

    def run(self):
        '''
        Process all the events, possibly changing state at each event
        :return:
        '''
        pass

    def transmit_completion_time(self, transmit_event):
        '''
        Returns the expected time of the TRANSMIT_COMPLETE event marking the end of transmission
        of transmit_event
        :param transmit_event:
        :return:
        '''
        pass






