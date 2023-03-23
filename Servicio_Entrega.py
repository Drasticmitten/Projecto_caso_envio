class Package():
    W_GR_100 = 10

    def __init__(self, id=0, weight=1.0, description="Description", cost=1.0):
        self._id = 0 if id == None else id
        self._weight = 1 if weight == 0 else weight
        self._description = 'description' if 'description' == None else description
        self._cost = 1.0 if cost == 0.0 else cost

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = 0 if id == None else id

    def get_weight(self, weight):
        return self._weight

    def set_weight(self, weight):
        self._weight = 1 if weight == 0 else weight

    def set_description(self, description):
        self._description = 'description' if 'description' == None else description

    def get_description(self):
        return self._description

    def set_cost(self, cost):
        self._cost = 1.0 if cost == 0.0 else cost

    def get_cost(self):
        return self._cost

    def _Str_(self):
        print("Id: ", self._id, "\nWeight: ", self.weight, "\nW_GR_100:",
              W_GR_100, "\nDescription:", self._description, "\nCost: ", self._cost)

    def calculate(self):
        print(f"El costo de envío es del {self._description} es $ ",
              self._cost * self._weight)


class StandardPackage(Package):

    def __init__(self,
                 id=0,
                 weight=1.0,
                 description="Description",
                 cost=1.0,
                 fixedfee=1.0):
        super().__init__(id, weight, description, cost)
        self.__fixedfee = 1.0 if fixedfee == 0.0 else fixedfee

    def _Str_(self):
        super()._Str_()
        print("\nFixed Fee", self.__fixedfee)

    def calculate(self):
        print(f"El costo de envío de {self.__description} es de $ ",
              (self.__fixedfee + self.__cost) * self.__weight)


class OverWeightPackage(Package):

    def __init__(self,
                 id=0,
                 weight=1.0,
                 description="Description",
                 cost=1.0,
                 overweight=1.0):
        super().__init__(id, weight, description, cost)
        self.__overweight = 1.0 if overweight == 0.0 else overweight

    def _Str_(self):
        super()._Str_()
        print("\nOverweight", self.__overweight)

    def calculate(self):
        print(f"El costo por sobre peso de {self.__description} es de $ ",
              (self.__overweight + self.__overweight) * self.__cost)


class Person():

    def __init__(self, name="name", lastname="lastname", dni=0, phone=0):
        self._name = "name" if name == None else name
        self._lastname = "lastname" if lastname == None else lastname
        self._dni = 0 if dni == None else dni
        self._phone = 0 if phone == None else phone

    def set_name(self, name):
        self._name = "name" if name == None else name

    def get_name(self):
        return self._name

    def set_last_name(self, lastname):
        self._lastname = "lastname" if lastname == None else lastname

    def get_last_name(self):
        return self._lastname

    def set_dni(self, dni):
        self._dni = 0 if dni == None else dni

    def get_dni(self):
        return self._dni

    def set_phone(self, phone):
        self._phone = 0 if phone == None else phone

    def get_phone(self):
        return self._phone

    def _Str_(self):
        print("Name: ", self._name, "\nLast Name: ",
              self._lastname, "\nDNI : ", self._dni, "\nPhone: ", self.phone)


class Address():

    def __init__(self,
                 house_number=0,
                 kind_street="kind of street",
                 street_name="street name",
                 address=0,
                 postal_code=0):
        self.__house_number = 0 if house_number == None else house_number
        self.__kind_street = "kind of street" if kind_street == None else kind_street
        self.__street_name = "street name " if street_name == None else street_name
        self.__address = 0 if address == None else address
        self.__postal_code = 0 if postal_code == None else postal_code

    def set_house_number(self, house_number):
        self.__house_number = "number" if house_number == None else house_number

    def get_house_number(self):
        return self.__house_number

    def set_kind_street(self, kind_street):
        self.__kind_street = "kind of street" if kind_street == None else kind_street

    def get_kind_street(self):
        return self.__kind_street

    def set_street_name(self, street_name):
        self.__street_name = "street name " if street_name == None else street_name

    def get_street_name(self):
        return self.__street_name

    def set_address(self, address):
        self.__address = 0 if address == None else address

    def get_address(self):
        return self.__address

    def set_postal_code(self, postal_code):
        self.__postal_code = 0 if postal_code == None else postal_code

    def get_postal_code(self):
        return self.__postal_code

    def _Str_(self):
        print("House number: ", self.house_number, "\nKind Street: ",
              self.__kind_street, "\nStreet Name: ", self.__street_name,
              "\nAddress:", self.__address, "\nPostal code: ", self.__postal_code)


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
                 items=[Package]):
        super().__init__(name, lastname, dni, phone)
        self.__id = 0 if id == None else id

        self.__date = "00/00/00" if date == None else date
        self.__time = "00:00" if time == None else time
        self.__sender = Person() if sender == None else sender
        self.__receiver = Person() if receiver == None else receiver

        self.__sender_add = Address() if sender_add == None else sender_add
        self.__receiver_add = Address() if receiver_add == None else receiver_add
        self.__contact = Person() if contact == None else contact
        self.__items = [Package] if items == None else items

    def set_id(self, id):
        self.__id = 0 if id == None else id

    def get_id(self):
        return self.__id

    def set_date(self, date):
        self.__date = "00/00/00" if date == None else date

    def get_date(self):
        return self.__date

    def set_time(self, time):
        self.__time = "00:00" if time == None else time

    def get_time(self):
        return self.__time

    def set_sender(self, sender):
        self.__sender = Person() if sender == None else sender

    def get_sender(self):
        return self.__sender

    def set_receiver(self, receiver):
        self.__receiver = Person() if receiver == None else receiver

    def get_receiver(self):
        return self.__receiver

    def set_sender_add(self, sender_add):
        self.__sender_add = Address if sender_add == None else sender_add

    def get_sender_add(self):
        return self.__sender_add

    def set_receiver_add(self, receiver_add):
        self.__receiver_add = Address if receiver_add == None else receiver_add

    def get_receiver_add(self):
        return self.__receiver_add

    def set_contact(self, contact):
        self.__contact = Person if contact == None else contact

    def get_contact(self):
        return self.__contact

    def set_items(self, items):
        self.__items = [Package] if items == None else items

    def get_items(self):
        return self.__items

    def _Str_(self):
        super()._Str_()
        print("Id: ", self.__id, "\nDate: ", self.__date, "\nTime: ",
              self.__time, "\nSender information: ", self.__sender._Str_(),
              "\nReceiver information: ", self.__receiver._Str_(),
              "\nSender Addres", self.__sender_add._Str_(), 
              "\nReceiver Address: ", self.__receiver_add._Str_(),
              "\nContact information: ", self.__contact._Str_())
        for i in range(0 , len( self.__items )):
            print(f"Package {i} information : ", self.__items[i]._Str_() , "\n")

Enviador = Person('David', 'Carrero', 1027210319, 3135885916)
Receptor = Person('Juan', 'Cardona', 1020202, 3202020)
ADD_SEN = Address(50, "Avenida", "Pastrana", 10202, 1040)
Galletas = Package(1020, 20, "Galletas", 20)

Paquete = []
Paquete.append(Galletas)

Delivor = Delivor("Paquetes", "A domicilio", 1027210319, 3022432177, 402042020,
                  "15/12/2004", '8:00', Enviador, Receptor, ADD_SEN, ADD_SEN,
                  Enviador, Paquete)

# Delivor.get_Receiver().set_Name("David")
print("Quien lo envía ", Delivor.get_receiver().get_name())
