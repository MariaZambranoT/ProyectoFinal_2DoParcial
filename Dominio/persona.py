# Integrantes Grupo
# - Gonzalez Ramirez Carlos Antonio
# - Iza Isa Elizabeth Ines
# - Montenegro Gonzalez Joseph Esteban
# - Ochoa Briones Daniela Melissa
# - Zambrano Tumbaco Maria Angelica

from datetime import datetime
from statistics import mean, mode


class Persona:
    def __init__(self, cedula=None, nombre=None, apellido=None, email=None, fecha_nacimiento=None,
                 peso=None, estatura=None, id_persona=None):
        self._id_persona = id_persona
        self._cedula = cedula
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
       # self._edad = edad
        self._fecha_nacimiento = fecha_nacimiento
        self._peso = peso
        self._estatura = estatura

    def calcular_edad(self):
        if self._fecha_nacimiento:
            try:
                fecha_nacimiento = datetime.strptime(self._fecha_nacimiento, '%m-%d-%Y')
                hoy = datetime.now()
                print(f"Fecha de nacimiento: {fecha_nacimiento}")
                print(f"Hoy: {hoy}")
                edad = hoy.year - fecha_nacimiento.year - (
                        (hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
                return edad
            except ValueError as e:
                print(f"Error al calcular la edad: {e}")
        return None

    def calcular_peso_por_edad(self):
        edad = self.calcular_edad()
        if edad is not None:
            # Lógica para calcular el peso basado en la edad
            if edad < 18:
                return 50  # Ejemplo: Peso ajustado para menores de 18 años
            elif 18 <= edad < 60:
                return 70  # Ejemplo: Peso ajustado para adultos (18-59 años)
            else:
                return 65  # Ejemplo: Peso ajustado para adultos mayores (60 años o más)
        else:
                return None


    def calcular_promedio(self, lista):
        try:
            return mean([float(item) for item in lista])
        except ZeroDivisionError:
            return None


    def calcular_media(self, lista):
        try:
            return mean(lista)
        except ValueError:
            return None

    def calcular_moda(self, lista):
        try:
            return mode(lista)
        except ValueError:
            return None

    def calcular_minimo(self, lista):
        try:
            return min(lista)
        except ValueError:
            return None

    def calcular_maximo(self, lista):
        try:
            return max(lista)
        except ValueError:
            return None

    @property
    def id_persona(self):
        return self._id_persona

    @id_persona.setter
    def id_persona(self, id_persona):
        self._id_persona = id_persona

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, cedula):
        self._cedula = cedula

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, fecha_nacimiento):
        self._fecha_nacimiento = fecha_nacimiento

    @property
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self, peso):
        self._peso = peso

    @property
    def estatura(self):
        return self._estatura

    @estatura.setter
    def estatura(self, estatura):
        self._estatura = estatura

    def __str__(self):
        return f'Persona {self.__dict__.__str__()}'

if __name__ == '_main_':
    p1 = Persona(cedula='012345689', nombre='Maria', apellido='Zambrano')
    print(p1)