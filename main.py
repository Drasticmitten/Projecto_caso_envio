from package import Package
from person import Person
from address import Address
from delivor import Delivor


def main():
    enviador = Person('David', 'Carrero', 1027210319, 3135885916)
    receptor = Person('Juan', 'Cardona', 1020202, 3202020)
    add_sen = Address(50, "Avenida", "Pastrana", 10202, 1040)
    galletas = Package(1020, 20, "Galletas", 20)

    paquete = []
    paquete.append(galletas)

    delivor = Delivor("Paquetes", "A domicilio", 1027210319, 3022432177, 402042020,
                      "15/12/2004", '8:00', enviador, receptor, add_sen, add_sen,
                      enviador, paquete, 10)

    delivor._Str_()


if __name__ == "__main__":
    main()
