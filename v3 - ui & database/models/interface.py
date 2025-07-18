from abc import ABC, abstractmethod

class DriverBase(ABC):
    @abstractmethod
    def tampil_info(self):
        pass

    @abstractmethod
    def tambah_point(self, tambahan):
        pass