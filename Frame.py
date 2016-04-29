class Frame:
    '''
    Represents a CSMA/CD frame that may have some transmission attempts
    '''
    frameNo = 0
    message = ''
    senderId = 0
    destId = 0

    def __init__(self, frameNo, message, senderId, destId):
        self.frameNo = frameNo
        self.message = message
        self.senderId = senderId
        self.destId = destId
