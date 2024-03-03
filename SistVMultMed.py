import datetime #importación del modilo datime para la fecha en el formato pedido
#No se evidencia uso de herencias ya que no hay clases hijas que heredan
#Tampoco se evidencia uso de polimorfismos

class Medicamento:
    def _init_(self):  #constructor
        self.__nombre = ""
        self.__dosis = 0
    #Métodos set y get para los atributos de medicamento
    #encapsulamiento privado
    def verNombre(self):
        return self.__nombre

    def verDosis(self):
        return self.__dosis

    def asignarNombre(self, med):
        self.__nombre = med

    def asignarDosis(self, med):
        self.__dosis = med

class Mascota:
    def _init_(self):  #constructor
        self.__nombre = ""
        self.__historia = 0
        self.__tipo = ""
        self.__peso = ""
        self.__fecha_ingreso = datetime.datetime.now().strftime("%d/%m/%Y")
        self.__lista_medicamentos = []
    #encapsulamiento privado
    #metodos set y get para los atributos de mascota
    def verNombre(self):
        return self.__nombre

    def verHistoria(self):
        return self.__historia

    def verTipo(self):
        return self.__tipo

    def verPeso(self):
        return self.__peso

    def verFecha(self):
        return self.__fecha_ingreso

    def verLista_Medicamentos(self):
        return self.__lista_medicamentos

    def asignarNombre(self, n):
        self.__nombre = n

    def asignarHistoria(self, nh):
        self.__historia = nh

    def asignarTipo(self, t):
        self.__tipo = t

    def asignarPeso(self, p):
        self.__peso = p

    def asignarFecha(self, f):
        self.__fecha_ingreso = f

    def asignarLista_Medicamentos(self, n):
        self.__lista_medicamentos = n

    def agregarMedicamento(self, medicamento):
        # Verificar si el medicamento ya existe en la lista
        for med in self.__lista_medicamentos:
            if medicamento.verNombre() == med.verNombre():
                print("¡Error! Ya existe un medicamento con el mismo nombre.")
                return False

        # Agregar medicamento a la lista
        self.__lista_medicamentos.append(medicamento)
        print("Medicamento agregado con éxito.")
        return True

    def eliminarMedicamento(self, nombre_medicamento):
        for med in self.__lista_medicamentos:
            if nombre_medicamento == med.verNombre():
                self.__lista_medicamentos.remove(med)
                print("Medicamento eliminado con éxito.")
                return True

        print("No se ha encontrado un medicamento con ese nombre.")
        return False

class SistemaVeterinario:
    def _init_(self):
        self.__lista_mascotas = []

    def verificarExiste(self, historia):
        for m in self.__lista_mascotas:
            if historia == m.verHistoria():
                return True
        return False

    def verNumeroMascotas(self):
        return len(self.__lista_mascotas)

    def ingresarMascota(self, mascota):
        self.__lista_mascotas.append(mascota)

    def verFechaIngreso(self, historia):
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                return masc.verFecha()
        return None

    def verMedicamento(self, historia):
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                return masc.verLista_Medicamentos()
        return None

    def eliminarMedicamentoMascota(self, historia, nombre_medicamento):
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                return masc.eliminarMedicamento(nombre_medicamento)

        print("No se ha encontrado una mascota con esa historia clínica.")
        return False

def main():
    servicio_hospitalario = SistemaVeterinario()

    while True:
        menu = int(input('''Ingrese una opción: 
                       1- Ingresar una mascota 
                       2- Ver fecha de ingreso 
                       3- Ver número de mascotas en el servicio 
                       4- Ver medicamentos que se están administrando
                       5- Agregar medicamento a mascota
                       6- Eliminar medicamento de mascota
                       7- Salir 
                       Usted ingresó la opción: '''))

        if menu == 1:  # Ingresar una mascota
            if servicio_hospitalario.verNumeroMascotas() >= 10:
                print("No hay espacio ...")
                continue
            historia = int(input("Ingrese la historia clínica de la mascota: "))

            if servicio_hospitalario.verificarExiste(historia) == False:
                nombre = input("Ingrese el nombre de la mascota: ")
                tipo = input("Ingrese el tipo de mascota (felino o canino): ")
                peso = int(input("Ingrese el peso de la mascota: "))
                fecha = input("Ingrese la fecha de ingreso (dia/mes/año): ")
#se usa el modulo datetime para exigir la fecha en el formato deseado DD/MM/AA
                try:
                    datetime.datetime.strptime(fecha, "%d/%m/%Y")
                except ValueError:
                    print("Error: El formato de fecha ingresado no es válido. Use dd/mm/aaaa.")
                    continue

                nm = int(input("Ingrese cantidad de medicamentos: "))
                lista_med = []

                for i in range(0, nm):
                    nombre_medicamentos = input("Ingrese el nombre del medicamento: ")
                    dosis = int(input("Ingrese la dosis: "))
                    medicamento = Medicamento()
                    medicamento.asignarNombre(nombre_medicamentos)
                    medicamento.asignarDosis(dosis)
                    lista_med.append(medicamento)

                mas = Mascota()
                mas.asignarNombre(nombre)
                mas.asignarHistoria(historia)
                mas.asignarPeso(peso)
                mas.asignarTipo(tipo)
                mas.asignarFecha(fecha)
                mas.asignarLista_Medicamentos(lista_med)
                servicio_hospitalario.ingresarMascota(mas)

            else:
                print("Ya existe la mascota con el número de historia clínica")

        elif menu == 2:  # Ver fecha de ingreso
            q = int(input("Ingrese la historia clínica de la mascota: "))
            fecha = servicio_hospitalario.verFechaIngreso(q)

            if fecha != None:
                print("La fecha de ingreso de la mascota es: " + fecha)
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        elif menu == 3:  # Ver número de mascotas en el servicio
            numero = servicio_hospitalario.verNumeroMascotas()
            print("El número de mascotas en el sistema es: " + str(numero))

        elif menu == 4:  # Ver medicamentos que se están administrando
            q = int(input("Ingrese la historia clínica de la mascota: "))
            medicamento = servicio_hospitalario.verMedicamento(q)

            if medicamento != None:
                print("Los medicamentos suministrados son: ")
                for m in medicamento:
                    print(f"\n- {m.verNombre()}")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        elif menu == 5:  # Agregar medicamento a mascota
            q = int(input("Ingrese la historia clínica de la mascota: "))
            mascota = None

            for masc in servicio_hospitalario.verMedicamento(q):
                if q == masc.verHistoria():
                    mascota = masc

            if mascota is not None:
                nombre_medicamento = input("Ingrese el nombre del medicamento: ")
                dosis = int(input("Ingrese la dosis: "))
                medicamento = Medicamento()
                medicamento.asignarNombre(nombre_medicamento)
                medicamento.asignarDosis(dosis)

                mascota.agregarMedicamento(medicamento)
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        elif menu == 6:  # Eliminar medicamento de mascota
            q = int(input("Ingrese la historia clínica de la mascota: "))
            nombre_medicamento = input("Ingrese el nombre del medicamento a eliminar: ")

            resultado_operacion = servicio_hospitalario.eliminarMedicamentoMascota(q, nombre_medicamento)

            if resultado_operacion == True:
                print("Medicamento eliminado de la mascota con éxito")
            else:
                print("No se ha podido eliminar el medicamento")

        elif menu == 7:
            print("Usted ha salido del sistema de servicio de hospitalización...")
            break

        else:
            print("Usted ingresó una opción no válida, inténtelo nuevamente...")

if _name_ == '_main_':
    main()