from package import Package


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

    def _equal_(self, objeto):
        return super()._equal_(objeto)

    def calculate(self):
        print(f"El costo de envío de {self.__description} es de $ ",
              (self.__fixedfee + self.__cost) * self.__weight)
