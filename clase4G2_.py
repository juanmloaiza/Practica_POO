#Clase tipo paciente con atributos como nombre,cedula,servicio,genero. Todos de manera privada
class Paciente:
    def _init_(self):  #constructor
        self.__nombre = ""
        self.__cedula = 0
        self.__genero = ""
        self.__servicio = ""

    # Métodos Getters
    def verNombre(self):
        return self.__nombre

    def verServicio(self):
        return self.__servicio

    def verGenero(self):
        return self.__genero

    def verCedula(self):
        return self.__cedula

    # Métodos Setters
    def asignarNombre(self, n):
        self.__nombre = n

    def asignarServicio(self, s):
        self.__servicio = s

    def asignarGenero(self, g):
        self.__genero = g

    def asignarCedula(self, c):
        self.__cedula = c


class Sistema:
    def _init_(self):
        # Atributos encapsulados
        self.__lista_pacientes = []
        self._numero_pacientes = len(self._lista_pacientes)

    # Método para ingresar un nuevo paciente al sistema
    def ingresarPaciente(self):
        nombre = input("Ingrese el nombre: ")
        cedula = int(input("Ingrese la cedula: "))
        genero = input("Ingrese el genero: ")
        servicio = input("Ingrese el servicio: ")

        p = Paciente()  # Polimorfismo: creación de un objeto Paciente
        p.asignarNombre(nombre)
        p.asignarCedula(cedula)
        p.asignarGenero(genero)
        p.asignarServicio(servicio)

        self.__lista_pacientes.append(p)
        self._numero_pacientes = len(self._lista_pacientes)

    # Método para ver el número total de pacientes en el sistema
    def verNumeroPacientes(self):
        return self.__numero_pacientes

    # Método para ver los datos de un paciente por cédula o nombre
    def verDatosPaciente(self):
        consulta = input("Ingrese la cedula o nombre a buscar: ")

        for paciente in self.__lista_pacientes:
            # Búsqueda por cédula o nombre parcial
            if consulta == str(paciente.verCedula()) or consulta.lower() in paciente.verNombre().lower():
                print("Nombre: " + paciente.verNombre())
                print("Cedula: " + str(paciente.verCedula()))
                print("Genero: " + paciente.verGenero())
                print("Servicio: " + paciente.verServicio())


def main():
    sistema = Sistema()
    sistema.ingresarPaciente()
    sistema.verDatosPaciente()


if _name_ == "_main_":
    main()


