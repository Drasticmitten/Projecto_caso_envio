class Person():

    def __init__(self, name="name", lastname="lastname", dni=0, phone=0):
        self._name = "name" if name == None else name
        self._lastname = "lastname" if lastname == None else lastname
        self._dni = 0 if dni == None else dni
        self._phone = 0 if phone == None else phone

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = "name" if name == None else name

    @property
    def last_name(self):
        return self._lastname

    @last_name.setter
    def last_name(self, lastname):
        self._lastname = "lastname" if lastname == None else lastname

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, dni):
        self._dni = 0 if dni == None else dni

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        self._phone = 0 if phone == None else phone

    def _Str_(self):
        print("Name: ", self._name, "\nLast Name: ",
              self._lastname, "\nDNI : ", self._dni, "\nPhone: ", self._phone)

    def _equal_(self, objeto):
        return self._dni == objeto._dni
