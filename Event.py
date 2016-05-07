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
    ARRIVAL = 1
    COLLISION_DETECT = 5
    JAMMING_END = 6
    RECEPTION_COMPLETE = 4
    TRANSMIT_ATTEMPT = 2
    TRANSMIT_COMPLETE = 3


    time = ''
    distance = 0
    stationId = 0
    msg = ''
    eventType = None

    def __init__(self, eventType_, time, stationId, msg):

        self.time = time
        #self.distance = distance
        self.stationId = stationId
        self.msg = msg
        #self.eventType = eventType

        if eventType_ == 1:
            self.eventType = 1
        elif eventType_ == 5:
            self.eventType = 5
        elif eventType_ == 6:
            self.eventType = 6
        elif eventType_ == 4:
            self.eventType = 4
        elif eventType_ == 2:
            self.eventType = 2
        elif eventType_ == 3:
            self.eventType = 3



