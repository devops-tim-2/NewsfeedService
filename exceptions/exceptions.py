class NotAuthorizedException(Exception):
    def __init__(self, message="You are not authorized to access this endpoint"):
        self.message = message
        super().__init__(self.message)

class TokenExpiredException(Exception):
    def __init__(self, message="JWT token has expired."):
        self.message = message
        super().__init__(self.message)