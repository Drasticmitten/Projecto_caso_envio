from package import Package


class OverWeightPackage(Package):

    def __init__(self,
                 id=0,
                 weight=1.0,
                 description="Description",
                 cost=1.0,
                 overweight=1.0):
        """ The overweight of the package.
        :param overweight: overweight of package.
        :type: float
        """
        super().__init__(id, weight, description, cost)
        self.__overweight = 1.0 if overweight == 0.0 else overweight
    
    @property
    def overweight(self) -> float:
        return self.__overweight
    
    @overweight.setter
    def overweight(self, overweight : float):
        self.__overweight = 1.0 if overweight == 0.0 else overweight

    def _Str_(self):
        """ Returns str of overweight package
        :returns: sting overwight package
        :rtype: str
        """
        super()._Str_()
        print("\nOverweight", self.__overweight)

    def calculate(self):
        print(f"El costo por sobre peso de {self.__description} es de $ ",
              (self.__overweight + self.__overweight) * self.__cost)

    def _equal_(self, objeto):
        """ Returns bool of equality of overweight package objects.
        :returns: bool overweight
        :rtype: bool
        """
        return super()._equal_(objeto) and self.__overweight == objeto.__overweight
