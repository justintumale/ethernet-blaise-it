class Frame:
    '''
    Represents a CSMA/CD frame that may have some transmission attempts
    '''

    def __init__(self, data_len, sender_id, destination_id):
        '''
        Create a new frame with specified data length and no transmission attempts
        :param data_len:
        :param sender_id:
        :param destination_id:
        :return:
        '''