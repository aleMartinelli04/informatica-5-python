class StatusCodeException(Exception):
    def __init__(self, message: str, code: int):
        self.__message = message
        self.__code = code

    @property
    def message(self) -> str:
        return self.__message

    @property
    def code(self) -> int:
        return self.__code
