
##################### Librerías #######################
import locale # Librería para separador de miles
locale.setlocale(locale.LC_ALL, '')  # Use '' for auto, or force e.g. to 'en_US.UTF-8'

##################### Clases #######################
class Persona:
	#### Constructor ####
	def __init__(self, _name, _age, _inst):
		#### Atributos ####
		self.name = _name
		self.age = _age
		self.inst = _inst
	#### Métodos ####
	def ShowInfo(self):
		print("\n", self.name, "tiene", self.age, "años.")

class Estudiante(Persona):
	#### Constructor ####
	def __init__(self, _name, _age, _inst, _prom):
		#### Herencia ####
		super().__init__(_name, _age, _inst)
		self.prom = _prom

	def ShowInfo(self):
		#### Herencia ####
		super().ShowInfo()
		print("Estudia en", self.inst)

class Empleado(Persona):
	#### Constructor ####
	def __init__(self, _name, _age, _inst, _salary):
		#### Herencia ####
		super().__init__(_name, _age, _inst)
		self.salary = _salary

	def ShowInfo(self):
		#### Herencia ####
		super().ShowInfo()
		print("Trabaja en", self.inst)

class Universitario(Estudiante):
	def __init__(self, _name, _age, _inst, _prom, _carreer):
		super().__init__(_name, _age, _inst, _prom)
		self.carreer = _carreer

	def ShowInfo(self):
		super().ShowInfo()
		print("En el programa curricular", self.carreer, ", con un promedio de", self.prom, "\n")

class Bachiller(Estudiante):
	def __init__(self, _name, _age, _inst, _prom, _grade):
		super().__init__(_name, _age, _inst, _prom)
		self.grade = _grade

	def ShowInfo(self):
		super().ShowInfo()
		print("Está en el grado", self.grade, ", con un promedio de", self.prom, "\n")

class Profesor(Empleado):
	def __init__(self, _name, _age, _inst, _salary, _asig):
		super().__init__(_name, _age, _inst, _salary)
		self.asig = _asig

	def ShowInfo(self):
		super().ShowInfo()
		print("Dicta la asignatura", self.asig, ", con un salario de $", self.salary, "\n")

class Directivo(Empleado):
	def __init__(self, _name, _age, _inst, _salary, _office):
		super().__init__(_name, _age, _inst, _salary)
		self.office = _office

	def ShowInfo(self):
		super().ShowInfo()
		print("Tiene un salario de $", self.salary, "y su oficina es la", self.office, "\n")

##################### Procedimientos #######################
def Registro():
	#### Título de la sección ####
	print("\nREGISTRO DE USUARIO\n")
	
	#### Variables que se asignarán a la clase persona ####
	name = input("Nombre: ")
	age = input("Edad: ")
	inst = input("Instirución educativa: ")

	#### Menú del ROL ####
	print("\n", "ROL", "\n", "0: Universitario.", "\n", "1: Bachiller.", "\n", "2: Profesor.", "\n", "3: Directivo.")
	
	#### Rol del usuario ####
	rol = int(input("Escriba el número del Rol: "))
	
	#### Verifica si es Estudiante #### 
	if rol == 0 or rol == 1:
		prom = float(input("Promedio: "))
		if rol == 0:
			carreer = input("Carrera: ")
			x = Universitario(name, age, inst, prom, carreer)
		else:
			grade = input("Grado: ")
			x = Bachiller(name, age, inst, prom, grade)

	#### Verifica si es Empleado ####
	elif rol == 2 or rol == 3:
		salary = int(input("Salario: "))
		salary = f"{salary:,}"
		if rol == 2:
			asig = input("Asignatura dictada: ")
			x = Profesor(name, age, inst, salary, asig)
		else:
			office = input("Oficina: ")
			x = Directivo(name, age, inst, salary, office)

	else:
		print("Número no válido")
			
	#### Muestra la información del objeto creado ####
	x.ShowInfo()
	Menu()

##################### Menú #######################
def Menu():
	#### Menú INICIO ####
	print("\n", "Menú", "\n", "0: Hacer Registro.", "\n", "~: Cualquier otro número para salir.")
	menu = int(input("Escriba el número del menú: "))

	if menu == 0:
		Registro()
	elif menu != 5:
		print("Hasta la próxima :)")
	
##################### Inicio de ejecución #######################
Menu()

#u = Estudiante("Julián Rave", 25, "Universidad Nacional", 3.6)
#u = Universitario("Julián Rave", 25, "Universidad Nacional", 3.6, "Ingeniería Electrónica")
#u = Bachiller("Carolina Pérez", 14, "Ravasco", 4.6, "8vo")
#u = Profesor("Daniel Castillo", 27, "Platzi", 2200000, "Programación")
#u.ShowInfo()
#u = Directivo("Juliana Acosta", 25, "Transportadoras S.A", 1800000, "C203")
#u.ShowInfo()