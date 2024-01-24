# Integrantes Grupo
# - Gonzalez Ramirez Carlos Antonio
# - Iza Isa Elizabeth Ines
# - Montenegro Gonzalez Joseph Esteban
# - Ochoa Briones Daniela Melissa
# - Zambrano Tumbaco Maria Angelica


import pyodbc as bd
from Datos.conexion import Conexion
from Dominio.persona import Persona


class PersonaDAO:
    _SELECCIONAR = 'select * from personas'
    _SELECCIONAR_PERSONA = "SELECT * FROM PERSONAS WHERE cedula = ?"
    _INSERTAR = "INSERT INTO Personas (nombre,apelLido, cedula, fecha_nacimiento"\
           ",email ,peso ,estatura) VALUES (?,?,?,?,?,?,?)"
    _ELIMINAR = "delete from personas where cedula = ? "
    _ACTUALIZAR = "update Personas set nombre = ?,apellido = ?," \
                  "edad = ?,fecha_nacimiento = ?," \
                  "email = ?,peso = ?, estatura = ? where cedula = ?"
    @classmethod
    def insertar(cls, Persona):
        mensaje = ''
        exito= False
        try:
            with Conexion.obtenerCursor() as cursor:
                valores = (Persona.nombre, Persona.apellido,
                          Persona.cedula, Persona.fecha_nacimiento, Persona.email, Persona.peso, Persona.estatura)
                cursor.execute(cls._INSERTAR, valores)
                mensaje = 'Se guardo con exito'
                exito = True
        except bd.IntegrityError as e:
            if e.__str__().find('Cedula') > 0:
                mensaje = 'Cedula ya Ingresada'
            elif e.__str__().find('Email') > 0:
                mensaje = 'Email ya Ingresado'
            else:
                mensaje = 'Error de Integridad'
            exito = False
        except Exception as e:
            mensaje = 'Fallo Ingreso'
            exito = False
            print(e)
            print(type(e))
        finally:
            return {'mensaje': mensaje, 'exito': exito}

    @classmethod
    def actualizar_persona_por_cedula(cls, Persona):
        mensaje = ''
        exito = False
        try:
            with Conexion.obtenerCursor() as cursor:
                valores = (Persona.nombre, Persona.apellido,
                           Persona.cedula, Persona.fecha_nacimiento, Persona.email, Persona.peso, Persona.estatura)
                registro = cursor.execute(cls._ACTUALIZAR, valores)
                if registro.rowcount == 1:
                    exito = True
                    mensaje = 'Se Actualizo con exito'
                else:
                    exito= False
                    mensaje = 'No se actualizo'
        except Exception as e:
            mensaje = 'Fallo la actualización en la base de datos'
            exito = False
            print(e)
            print(type(e))
        finally:
            return {'mensaje': mensaje, 'exito': exito}

    @classmethod
    def seleccionar_persona_por_cedula(cls, Persona):
        persona_encontrada = None
        try:
            with Conexion.obtenerCursor() as cursor:
                valores = (Persona.cedula,)
                registro = cursor.execute(cls._SELECCIONAR_PERSONA, valores)
                persona_encontrada = registro.fetchone()
        except Exception as e:
            persona_encontrada=None
        finally:
            return persona_encontrada

    @classmethod
    def seleccionar(cls):
        lista_persona = list()
        try:
            with Conexion.obtenerCursor() as cursor:
                registro = cursor.execute(cls._SELECCIONAR)
                tupla_personas = registro.fetchall()
                for registro in tupla_personas:
                    Persona = Persona()
                    #Persona.id_persona = registro[0]
                    Persona.nombre = registro[0]
                    Persona.apellido = registro[1]
                    Persona.cedula = registro[2]
                    #Persona.edad = registro[4] #5
                    Persona.fecha_nacimiento = registro[3]
                    Persona.email = registro[4]
                    Persona.peso = registro[5]
                    Persona.estatura = registro[6]
                    lista_persona.append(Persona)
        except Exception as e:
            lista_persona = list ()
        finally:
            return lista_persona

    @classmethod
    def eliminar_persona_por_cedula(cls, Persona):
        respuesta = False
        try:
            with Conexion.obtenerCursor() as cursor:
                valores = (Persona.cedula)
                registro = cursor.execute(cls._ELIMINAR, valores)
                if registro.rowcount == 1:
                    respuesta = True
                else:
                    respuesta = False
                print(registro.rowcount)
        except Exception as e:
            respuesta = False
        finally:
            return respuesta

if __name__ == '_main_':
    p1=Persona(cedula='1112222222')
    PersonaDAO.eliminar_persona_por_cedula(Persona=p1)