from abc import  abstractmethod, ABC

class Band():
    instances = []

    def __init__(self , name , members):
        self.name = name
        self.members = members
        self.instances.append(self)

    def play_solos(self):
        list = []
        for i in self.members:
            list.append(i.play_solo())
        return(list)

    @abstractmethod
    def __repr__(self):
       return (f"{self.name}")

    @classmethod
    def to_list(cls):
        return cls.instances

    @abstractmethod
    def __str__(self):
        return (f" band {self.name}")


class Musician:
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def  play_solo(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def get_instrument(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass


class Guitarist(Musician):

    def get_instrument(self):
        return 'guitar'

    def __str__(self):
        return (f"My name is {self.name} and I play guitar")

    def __repr__(self):
        return (f"Guitarist instance. Name = {self.name}")

    def play_solo(self):
        return 'face melting guitar solo'


class Drummer(Musician):

    def __str__(self):
        return (f"My name is {self.name} and I play drums")

    def __repr__(self):
        return (f"Drummer instance. Name = {self.name}")

    def play_solo(self):
        return 'rattle boom crash'

    def get_instrument(self):
        return 'drums'

class Bassist(Musician):
        
    def get_instrument(self):
        return 'bass'

    def play_solo(self):
        return 'bom bom buh bom'

    def __repr__(self):
        return (f"Bassist instance. Name = {self.name}")

    def __str__(self):
        return (f"My name is {self.name} and I play bass")


