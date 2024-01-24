

import sys
from PySide6.QtWidgets import QApplication
from Servicio.persona_principal import PersonaPrincipal


app = QApplication()
MainWindow = PersonaPrincipal()
MainWindow.show()
sys.exit(app.exec())

