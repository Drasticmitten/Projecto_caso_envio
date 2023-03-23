class Person():

    def __init__(self, name="name", lastname="lastname", dni=0, phone=0):
        """ Person constructor object.
        :param name: name of package.
        :type name: str
        :param lastname: lastname of person.
        :type lastname: str
        :param dni: dni of person.
        :type dni: int
        :param phone: phone of person.
        :type phone: str
        :returns: Person object.
        :rtype: object
        """
        self._name = "name" if name == None else name
        self._lastname = "lastname" if lastname == None else lastname
        self._dni = 0 if dni == None else dni
        self._phone = 0 if phone == None else phone

    @property
    def name(self):
        """ Returns the name of the Person
        :returns : name of Person
        :rtype : str
        """
        return self._name

    @name.setter
    def name(self, name):
        """ The name of the person
        :param name : name of Person
        :type : str
        """
        self._name = "name" if name == None else name

    @property
    def last_name(self):
        """ Returns the last name of the Person
        :returns : last_name of Person
        :rtype : str
        """
        return self._lastname

    @last_name.setter
    def last_name(self, lastname):
        """ The last name of the person
        :param lastname : last name of Person
        :type : str
        """
        self._lastname = "lastname" if lastname == None else lastname

    @property
    def dni(self):
        """ Returns the DNI of the Person
        :returns : dni of Person
        :rtype : int
        """
        return self._dni

    @dni.setter
    def dni(self, dni):
        """ The DNI of the person
        :param dni: dni of Person
        :type : int
        """
        self._dni = 0 if dni == None else dni

    @property
    def phone(self):
        """ Returns the phone of the Person
        :returns : phone of Person
        :rtype : int
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """ The phone of the person
        :param phone: phone of Person
        :type : int
        """
        self._phone = 0 if phone == None else phone

    def _Str_(self):
        """ Returns str of person
        :returns: sting person
        :rtype: str
        """
        print("Name: ", self._name, "\nLast Name: ",
              self._lastname, "\nDNI : ", self._dni, "\nPhone: ", self._phone)

    def _equal_(self, objeto):
        """ Returns bool of equality of Person objects.
        :returns: bool Person
        :rtype: bool
        """
        return self._dni == objeto._dni
