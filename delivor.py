from person import Person
from address import Address
from package import Package
from standard_package import StandardPackage
from overweight_package import OverWeightPackage


class Delivor(Person):

    def __init__(self,
                 name='name',
                 lastname='lastname',
                 dni=0,
                 phone=0,
                 id=0,
                 date='00/00/00',
                 time='00:00',
                 sender=Person(),
                 receiver=Person(),
                 sender_add=Address(),
                 receiver_add=Address(),
                 contact=Person(),
                 items=[Package],
                 type: int = 0):
        super().__init__(name, lastname, dni, phone)
        self.__id = 0 if id == None else id

        self.__date = "00/00/00" if date == None else date
        self.__time = "00:00" if time == None else time
        self.__sender = Person() if sender == None else sender
        self.__receiver = Person() if receiver == None else receiver

        self.__sender_add = Address() if sender_add == None else sender_add
        self.__receiver_add = Address() if receiver_add == None else receiver_add
        self.__contact = Person() if contact == None else contact
        if (not type):
            self.__items = [StandardPackage] if items == None else items
        else:
            self.__items = [OverWeightPackage] if items == None else items

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id : str):
        self.__id = 0 if id == None else id

    @property
    def date(self) -> str:
        return self.__date

    @date.setter
    def date(self, date : str):
        self.__date = "00/00/00" if date == None else date

    @property
    def time(self) -> str:
        return self.__time

    @time.setter
    def time(self, time : str):
        self.__time = "00:00" if time == None else time

    @property
    def sender(self) -> Person:
        return self.__sender

    @sender.setter
    def sender(self, sender : object):
        self.__sender = Person() if sender == None else sender

    @property
    def receiver(self) -> Person:
        return self.__receiver

    @receiver.setter
    def receiver(self, receiver : object):
        self.__receiver = Person() if rece5iver == None else receiver

    @property
    def sender_add(self) -> Address:
        return self.__sender_add

    @sender_add.setter
    def sender_add(self, sender_add : object):
        self.__sender_add = Address if sender_add == None else sender_add

    @property
    def receiver_add(self) -> Address:
        return self.__receiver_add

    @receiver_add.setter
    def receiver_add(self, receiver_add : object):
        self.__receiver_add = Address if receiver_add == None else receiver_add

    @property
    def contact(self) -> Person:
        return self.__contact

    @contact.setter
    def contact(self, contact : object):
        self.__contact = Person if contact == None else contact

    @property
    def items(self) -> Package:
        return self.__items

    @items.setter
    def items(self, items : object):
        self.__items = [Package] if items == None else items

    def _Str_(self):
        super()._Str_()
        print("Id: ", self.__id, "\nDate: ", self.__date, "\nTime: ",
              self.__time, "\nSender information: ", self.__sender._Str_(),
              "\nReceiver information: ", self.__receiver._Str_(),
              "\nSender Addres", self.__sender_add._Str_(),
              "\nReceiver Address: ", self.__receiver_add._Str_(),
              "\nContact information: ", self.__contact._Str_())
        for i in range(0, len(self.__items)):
            print(f"Package {i} information : ", self.__items[i]._Str_(), "\n")

    def _equal_(self, objeto):
        return self.__id == objeto._id
