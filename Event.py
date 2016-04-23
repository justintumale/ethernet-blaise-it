#ARRIVAL
#TRANSMIT_ATTEMPT
#TRANSMIT_COMPLETE
#RECEPTION_COMPLETE
#COLISSION_DETECT
#JAMMING_END

class Event:
    '''
    Represents an event in a CSMA_CD network
    '''
    def __init__(self, time, stationID, msg):
        '''
        Creates an Event with specified event time, station, and associated message
        :param time:
        :param stationID:
        :param msg:
        :return:
        '''
        pass
    
    ARRIVAL = 1
    COLLISION_DETECT = 5
    JAMMING_END = 6
    RECEPTION_COMPLETE = 4
    TRANSMIT_ATTEMPT = 2
    TRANSMIT_COMPLETE = 3