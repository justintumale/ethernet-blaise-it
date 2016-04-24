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
    time = ''
    stationId = 0
    msg = ''
    def __init__(self, time, stationId, msg):
        '''
        Creates an Event with specified event time, station, and associated message
        :param time:
        :param stationId:
        :param msg:
        :return:
        '''

        self.time = time
        self.stationId = stationId
        self.msg = msg

    ARRIVAL = 1
    COLLISION_DETECT = 5
    JAMMING_END = 6
    RECEPTION_COMPLETE = 4
    TRANSMIT_ATTEMPT = 2
    TRANSMIT_COMPLETE = 3