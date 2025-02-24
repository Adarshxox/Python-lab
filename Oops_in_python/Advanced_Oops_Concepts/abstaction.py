# ABSTRACTION

"Python doesnot support abstract class"
"This concept actually implementing using import abc module"

from abc import ABC,abstractmethod

class Vehicle(ABC):

    def start_engine(self):

        print("start engine")

    def stop_engine(self):

        print("stop engine")

    @abstractmethod

    def change_gear(self):

        pass

class car(Vehicle):

    def change_gear(self):
        
        print("change gear")

class truck(Vehicle):

    def change_gear(self):
        
        print("change gear")

c1 = car()

c1.start_engine()

c1.change_gear()

c1.stop_engine()