# Integrantes Grupo
# - Gonzalez Ramirez Carlos Antonio
# - Iza Isa Elizabeth Ines
# - Montenegro Gonzalez Joseph Esteban
# - Ochoa Briones Daniela Melissa
# - Zambrano Tumbaco Maria Angelica


class Archivo:
    @classmethod
    def guardar(cls, objeto):
        exito = False
        archivo = None
        try:
            archivo = open('persona.txt', 'a')
            archivo.write(objeto.__str__())
            archivo.write('\n')
            exito = True
        except Exception as e:
            print(e)
            exito = False
        finally:
            if archivo:
                archivo.close()
            return exito