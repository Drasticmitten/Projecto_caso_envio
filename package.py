class Package(object):
    """
     Class used to represent a Package
    """

    W_GR_100 = 10

    def __init__(self, id: int = 0, weight: float = 1.0, description: str = "Description", cost: float = 1.0):
        """ Package constructor object.
        :param id : id of package
        :type id : int
        :param weight : weitght of package
        :type weight: float
        :param description : description of package
        :type description : str
        :param cost : cost of package
        :type cost : float
        :rtype : object
        """
        self._id = 0 if id == None else id
        self._weight = 1 if weight == 0 else weight
        self._description = 'description' if 'description' == None else description
        self._cost = 1.0 if cost == 0.0 else cost

    @property
    def id(self) -> int:
        """ Returns the id of the package.
        :returns : id of package.
        :rtype : int
        """
        return self._id

    @id.setter
    def id(self, id):
        sel._id = 0 if id == None else id

    @property
    def weight(self, weight) -> float:
        """ Returns the weight of the package
        :returns : weight of package
        :rtype : float
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        self._weight = 1 if weight == 0 else weight

    @property
    def description(self) -> str:
        """ Returns the weight of the package
        :returns : description of package
        :rtype : str
        """
        return self._description

    @description.setter
    def description(self, description):
        self._description = 'description' if 'description' == None else description

    @property 
    def cost(self) -> float:
        """ Returns the cost of the package
        :returns : cost of package
        :rtype : float
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        self._cost = 1.0 if cost == 0.0 else cost

    def _Str_(self):
        print("Id: ", self._id, "\nWeight: ", self._weight, "\nW_GR_100:",
              self.W_GR_100, "\nDescription:", self._description, "\nCost: ", self._cost)

    def _equal_(self, objeto):
        return self._id == objeto._id

    def calculate(self):
        print(f"El costo de envío es del {self._description} es $ ",
              self._cost * self._weight)
