
class LibraryError(Exception):
    def __init__(self, message, status):
        self.message = message
        self.status = status
        super().__init__(message)


def custom_error(message, status_code):
    return LibraryError(message, status_code)


def bad_request(message):
    return custom_error(message, 400)


def not_found(message):
    return custom_error(message, 404)


def conflict(message):
    return custom_error(message, 409)
