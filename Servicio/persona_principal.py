# Integrantes Grupo
# - Gonzalez Ramirez Carlos Antonio
# - Iza Isa Elizabeth Ines
# - Montenegro Gonzalez Joseph Esteban
# - Ochoa Briones Daniela Melissa
# - Zambrano Tumbaco Maria Angelica

import re

from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox, QLabel
from GUI.vtn_principal import Ui_MainWindow
from PySide6 import QtGui
from Datos.archivo import Archivo
from Datos.persona_dao import PersonaDAO
from Dominio.persona import Persona
from statistics import mean, median, mode
from datetime import datetime




class PersonaPrincipal(QMainWindow):
    def __init__(self):
        self._listado_persona = PersonaDAO.seleccionar() or []
        super(PersonaPrincipal, self).__init__()
        self.ui = Ui_MainWindow()  # Mueve esta línea fuera del método __init__
        self.ui.setupUi(self)
        self._Persona = None
        self.ui.txt_cedula.setValidator(QtGui.QIntValidator())
        self.ui.txt_consulta_cedula.setValidator(QtGui.QIntValidator())
        self.ui.btn_agregar.clicked.connect(self.agregar)
        self.ui.btn_limpiar.clicked.connect(self.limpiar_formulario)
        self.ui.btn_consultar.clicked.connect(self.consultar)
        self.ui.btn_calcular.clicked.connect(self.calcular_estadisticas)
        self.ui.lbl_edad_resultado = self.findChild(QLabel, 'lbl_edad_resultado')
        self.ui.lbl_media_resultado = self.findChild(QLabel, 'lbl_media_resultado')
        self.ui.lbl_mediana_resultado = self.findChild(QLabel, 'lbl_mediana_resultado')
        self.ui.lbl_moda_resultado = self.findChild(QLabel, 'lbl_moda_resultado')
        self.ui.lbl_promedio_resultado = self.findChild(QLabel, 'lbl_promedio_resultado')
        self._listado_persona = PersonaDAO.seleccionar()
        self._contador = 0

        rx = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        validator = QtGui.QRegularExpressionValidator(rx, self)
        self.ui.txt_email.setValidator(validator)

        self.ui.btn_calcular.clicked.connect(self.calcular_estadisticas)
    def agregar(self):
        if self.validar_formulario():
            self.capturar_datos()
            print(self._Persona)
            respuesta = PersonaDAO.insertar(self._Persona)
            if respuesta['exito']:
                 self.ui.statusbar.showMessage(respuesta['mensaje'], timeout=5000)
                 self.limpiar_formulario()
            else:
                 QMessageBox.critical(self, 'Error', respuesta['mensaje'] + '\nError al guardar los datos en la Base de Datos.')
        else:
            QMessageBox.warning(self, 'Advertencia', 'Falta de llenar los datos obligatorios.')
            print('Faltan datos')

    def calcular_estadisticas(self):
        print("Botón de calcular presionado")
        self._listado_persona = PersonaDAO.seleccionar() or []
        personas_con_fecha = [persona for persona in self._listado_persona if persona.fecha_nacimiento is not None]
        print("Personas con fecha:", personas_con_fecha)
        # Verifica si hay personas con fecha de nacimiento registrada
        if not personas_con_fecha:
            QMessageBox.warning(self, 'Advertencia', 'No hay personas con fecha de nacimiento registrada.')
            return

        # Obtén la lista de fechas de nacimiento de todas las personas
        fechas_nacimiento = [persona.fecha_nacimiento for persona in personas_con_fecha]
        print("Fechas de nacimiento:", fechas_nacimiento)
        # Calcula la media de las edades
        edades = [persona.calcular_edad() for persona in personas_con_fecha]
        #edades = [self.calcular_edad(fecha) for fecha in fechas_nacimiento]
        print("Edades:", edades)
        media_edades = mean(edades)

        # Calcula la mediana de las edades
        mediana_edades = median(edades)

        # Calcula la moda de las edades
        moda_edades = mode(edades)

        # Calcula el promedio de las edades
        promedio_edades = sum(edades) / len(edades)
        # Muestra los resultados
        self.actualizar_etiquetas_resultado(edades, media_edades, mediana_edades, moda_edades, promedio_edades)
        mensaje = f"Media de edades: {media_edades}\n"
        mensaje += f"Mediana de edades: {mediana_edades}\n"
        mensaje += f"Moda de edades: {moda_edades}\n"
        mensaje += f"Promedio de edades: {promedio_edades}\n"

        QMessageBox.information(self, 'Estadísticas', mensaje)

    def actualizar_etiquetas_resultado(self, edades, media, mediana, moda, promedio):
        if edades:
            mensaje_edad = f"Rango de edades: {min(edades)} - {max(edades)} ({len(edades)} personas)"
        else:
            mensaje_edad = "No hay personas con fecha de nacimiento registrada."

        self.ui.lbl_edad_resultado.setText(f"Edad: {mensaje_edad}")
        self.ui.lbl_media_resultado.setText(f"Media: {media}" if media else "Media: No disponible")
        self.ui.lbl_mediana_resultado.setText(f"Mediana: {mediana}" if mediana else "Mediana: No disponible")
        self.ui.lbl_moda_resultado.setText(f"Moda: {moda}" if moda else "Moda: No disponible")
        self.ui.lbl_promedio_resultado.setText(f"Promedio: {promedio}" if promedio else "Promedio: No disponible")
        self.actualizar_etiquetas_resultado(edades, media, mediana, moda, promedio)

    def calcular_edad(self, fecha_nacimiento):
        # Convierte la cadena de fecha a objeto datetime
        fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%Y-%m-%d').date()

        # Obtiene la fecha actual
        fecha_actual = datetime.now().date()

        # Calcula la diferencia de años
        edad = fecha_actual.year - fecha_nacimiento.year - (
                    (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))

        return edad


    def limpiar_formulario(self):
        self.ui.txt_consulta_cedula.setText('')
        self.ui.txt_cedula.setText('')
        self.ui.txt_nombre.setText('')
        self.ui.txt_apellido.setText('')
        self.ui.txt_peso.setText('')
        self.ui.txt_estatura.setText('')
        self.ui.txt_email.setText('')
        self._Persona = None


    def capturar_datos(self):
        if not self._Persona:
            self._Persona = Persona()
        self._Persona.nombre = self.ui.txt_nombre.text()
        self._Persona.apellido = self.ui.txt_apellido.text()
        self._Persona.email = self.ui.txt_email.text()
        self._Persona.cedula = self.ui.txt_cedula.text()
        self._Persona.fecha_nacimiento = self.ui.date_fecha_nacimiento.text()
        #self._Persona.edad = self.ui.spb_edad.text()
        self._Persona.peso = self.ui.txt_peso.text()
        self._Persona.estatura = self.ui.txt_estatura.text()

    def validar_formulario(self):
        return (self.ui.txt_nombre.text() != '' and self.ui.txt_apellido.text() != '' and
                len(self.ui.txt_cedula.text()) == 10)

    def validar_email(self, email):
        expresionRegular = r"(?:[a-z0-9!#$%&'*+/=?^_{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_{|}~-]+)|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])\")@(?:(?:[a-z0-9](?:[a-z0-9-][a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-][a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
        return re.search(expresionRegular, email)

    def consultar(self):
        consulta_cedula = self.ui.txt_consulta_cedula.text()
        self._Persona = Persona()
        self._Persona = Persona(cedula=consulta_cedula)
        tupla_persona = PersonaDAO.seleccionar_persona_por_cedula(self._Persona)
        self._Persona.id_persona = tupla_persona[0]
        self._Persona.nombre = tupla_persona[1]
        self._Persona.apellido = tupla_persona[2]
        self._Persona.cedula = tupla_persona[3]
        #self._Persona.edad = tupla_persona[5]
        self._Persona.fecha_nacimiento = tupla_persona[4]
        self._Persona.email = tupla_persona[5]
        self._Persona.peso = tupla_persona[6]
        self._Persona.estatura = tupla_persona[7]
        self.llenar_formulario()
        print(self._Persona)

    def llenar_formulario(self):
        self.ui.txt_cedula.setText(self._Persona.cedula)
        self.ui.txt_nombre.setText(self._Persona.nombre)
        self.ui.txt_apellido.setText(self._Persona.apellido)
        self.ui.txt_peso.setText(self._Persona.peso)
        self.ui.txt_estatura.setText(self._Persona.estatura)
        self.ui.txt_email.setText(self._Persona.email)


