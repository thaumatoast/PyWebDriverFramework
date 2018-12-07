class SessionException(Exception):
    pass


class StoreException(Exception):
    pass


class DriverEnvironmentException(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return "Message: %s\n" % self.message
