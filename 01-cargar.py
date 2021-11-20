from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5 import uic
import sqlite3


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()

        # Cargar interfaz de usuario
        uic.loadUi("00-cargar.ui", self)

        # Conectar a la base de datos
        self.conexion = sqlite3.connect('00-base.db')
        self.cursor = self.conexion.cursor()

        #self.cursor.execute('select * from usuarios')
        #usuarios = self.cursor.fetchall()
        #print(usuarios)
        self.on_cargar()

        #self.cancelar.setEnabled(True)

        # Crear las columnas
        #self.tabla.setColumnCount(4)

        # Nombrar las columnas
        #self.tabla.setHorizontalHeaderLabels(('id', 'Nombre', 'Apellido', 'e-mail'))

        #self.cancelar.clicked.connect(self.on_cancelar)
        #self.eliminar.clicked.connect(self.on_eliminar)
        self.nuevo.clicked.connect(self.on_nuevo)
        self.editar.clicked.connect(self.on_editar)
        self.aceptar.clicked.connect(self.on_aceptar)

        self.nuevo.setEnabled(True)
        self.editar.setEnabled(False)
        self.eliminar.setEnabled(False)
        self.aceptar.setEnabled(False)
        self.cancelar.setEnabled(False)
    
    def on_fin_accion(self):
        self.aceptar.setEnabled(False)
        self.cancelar.setEnabled(False)
        self.nuevo.setEnabled(True)

    def on_nuevo(self):
        self.nuevo.setEnabled(False)
        self.aceptar.setEnabled(True)
        self.cancelar.setEnabled(True)
        print('nuevo')
    
    def on_editar(self):
        print('editar')

    def on_editar2(self):
        row = self.tabla.currentRow()
        print(row)
        nombre = str(self.nombre.text())
        apellido = str(self.apellido.text())
        email = str(self.email.text())
        tel = str(self.nombre.text())
        dir = str(self.nombre.text())
        fechaNac = str(self.nombre.text())
        altura = str(self.nombre.text())
        peso = str(self.nombre.text())
        self.tabla.takeItem(self.tabla.currentRow())
        self.tabla.addItem(str(id+"   "+nombre  + "   " + apellido + "   " + email + "   " + dir + "   " + tel + "   " + fechaNac+ "   " + altura+ "   " + peso ))
        self.nombre.setText(str(""))
        self.apellido.setText(str(""))

    def on_eliminar(self):
        self.tabla.takeItem(self.tabla.currentRow())

    def on_cargar(self):
        self.cursor.execute('select * from usuarios')
        usuarios = self.cursor.fetchall()
        for usuario in usuarios:
            id = str(usuario[0])
            nombre = usuario[1]
            apellido = usuario[2]
            email = usuario[3]
            tel = usuario[4]
            dir = usuario[5]
            fechaNac = str(usuario[6])
            altura = str(usuario[7])
            peso = str(usuario[8])
            #print(peso,altura)
            self.tabla.addItem(str(id+"   "+nombre  + "   " + apellido + "   " + email + "   " + dir + "   " + tel + "   " + fechaNac+ "   " + altura+ "   " + peso ))

    def on_aceptar(self):
        if self.editar.setEnabled(False) == self.editar.setEnabled(False):
            self.on_crear()
            self.on_fin_accion()
        

    def on_crear(self):
        nombre = str(self.nombre.text())
        apellido = str(self.apellido.text())
        email = str(self.email.text())
        tel = str(self.tel.text())
        dir = str(self.dir.text())
        fechaNac = str(self.fechaNac.text())
        altura = (self.altura.text())
        peso = (self.peso.text())

        self.tabla.addItem(str(nombre  + "   " + apellido + "   " + email + "   " + dir + "   " + tel + "   " + fechaNac+ "   " + altura+ "   " + peso ))

        self.nombre.setText(str(""))
        self.apellido.setText(str(""))
        self.email.setText(str(""))
        self.tel.setText(str(""))
        self.dir.setText(str(""))
        self.fechaNac.setText(str(""))
        self.altura.setText(str(""))
        self.peso.setText(str(""))

        # Agregar usuario
        self.cursor.execute("insert into usuarios (nombre,apellido,email,direccion,telefono,fecha,altura,peso) values ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')".format(nombre, apellido, email, tel,dir,fechaNac,altura,peso))
        self.conexion.commit()

        # Vaciar y volver a cargar tabla
        #self.tabla.setRowCount(0)
        #self.on_cargar()


    def closeEvent(self, event):
        self.conexion.close()


app = QApplication([])

win = MiVentana()
win.show()

app.exec_()