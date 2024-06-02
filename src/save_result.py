from abc import ABC, abstractmethod


class SaveResult(ABC):

    @abstractmethod
    def __init__(self):
        super().__init__()
        pass


class SaveResultInFile(SaveResult):

    def __init__(self):
        super().__init__()