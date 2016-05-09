class Transmission:
    '''
    Represents an ongoing Ethernet transmission, which could be a
    frame or a jamming signal
    '''
    startTime = 0
    endTime = 0
    messageID = 0

    def __init__(self, startTime, endTime, messageID):
        '''
        Initialize the object  with the time the transmission started,
        the time the transmission will end, and  the ID of the message.
        '''
        self.startTime = startTime
        self.endTime = endTime
        self.messageID = messageID