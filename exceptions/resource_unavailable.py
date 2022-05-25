class ResourceUnavl(Exception):

    def __init__(self, message):
        self.message = message