
class Address(object):

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

    @property
    def house_number(self) -> int:
        return self.__house_number

    @house_number.setter
    def house_number(self, house_number : str):
        self.__house_number = "number" if house_number == None else house_number

    @property
    def kind_street(self) -> str:
        return self.__kind_street

    @kind_street.setter
    def kind_street(self, kind_street : str):
        self.__kind_street = "kind of street" if kind_street == None else kind_street

    @property
    def street_name(self) -> str:
        return self.__street_name

    @street_name.setter
    def street_name(self, street_name : str):
        self.__street_name = "street name " if street_name == None else street_name

    @property
    def address(self) -> int:
        return self.__address

    @address.setter
    def address(self, address : object):
        self.__address = 0 if address == None else address

    @property
    def postal_code(self) -> int:
        return self.__postal_code

    @postal_code.setter
    def postal_code(self, postal_code : int):
        self.__postal_code = 0 if postal_code == None else postal_code

    def _Str_(self):
        print("House number: ", self.__house_number, "\nKind Street: ",
              self.__kind_street, "\nStreet Name: ", self.__street_name,
              "\nAddress:", self.__address, "\nPostal code: ", self.__postal_code)

    def _equal_(self, objeto):
        return (self.__house_number == objeto.__house_number and
                self.__kind_street == objeto.__kind_street and
                self.__street_name == objeto.__street_name and
                self.__address == objeto.__address and
                self.__postal_code == objeto.__postal_code)
