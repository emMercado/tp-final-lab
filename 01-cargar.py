from PyQt5.QtWidgets import QMainWindow, QApplication,QMessageBox
from PyQt5 import uic
import sqlite3

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("00-cargar.ui", self)

        self.conexion = sqlite3.connect('00-base.db')
        self.cursor = self.conexion.cursor()

        self.on_cargar()
        self.on_reset()
        self.flag = True

        self.cancelar.clicked.connect(self.on_cancelar)
        self.eliminar.clicked.connect(self.on_eliminar)
        self.nuevo.clicked.connect(self.on_nuevo)
        self.editar.clicked.connect(self.on_editar)
        self.aceptar.clicked.connect(self.on_aceptar)


    def on_limpiar(self):
        self.nombre.setText(str(""))
        self.apellido.setText(str(""))
        self.email.setText(str(""))
        self.tel.setText(str(""))
        self.dir.setText(str(""))
        self.fechaNac.setText(str(""))
        self.altura.setText(str(""))
        self.peso.setText(str(""))

    def on_reset(self):
        self.nuevo.setEnabled(True)
        self.editar.setEnabled(True)
        self.eliminar.setEnabled(True)
        self.aceptar.setEnabled(False)
        self.cancelar.setEnabled(False)
        self.nombre.setDisabled(True)
        self.apellido.setDisabled(True)
        self.email.setDisabled(True)
        self.tel.setDisabled(True)
        self.dir.setDisabled(True)
        self.fechaNac.setDisabled(True)
        self.altura.setDisabled(True)
        self.peso.setDisabled(True)

    def on_cancelar(self):
        self.on_limpiar()
        self.on_reset()

    def on_recargar_tabla(self):
        self.tabla.clear()
        self.on_cargar()

    def on_fin_accion(self):
        self.aceptar.setEnabled(False)
        self.cancelar.setEnabled(False)
        self.nuevo.setEnabled(True)

    def on_nuevo(self):
        self.flag = True
        self.nuevo.setEnabled(False)
        self.editar.setEnabled(False)
        self.eliminar.setEnabled(False)
        self.aceptar.setEnabled(True)
        self.cancelar.setEnabled(True)
        self.aceptar.setEnabled(True)
        self.cancelar.setEnabled(True)
        self.nombre.setDisabled(False)
        self.apellido.setDisabled(False)
        self.email.setDisabled(False)
        self.tel.setDisabled(False)
        self.dir.setDisabled(False)
        self.fechaNac.setDisabled(False)
        self.altura.setDisabled(False)
        self.peso.setDisabled(False)

    def on_editar(self):
        self.nuevo.setEnabled(False)
        self.editar.setEnabled(True)
        self.eliminar.setEnabled(False)
        self.aceptar.setEnabled(True)
        self.cancelar.setEnabled(True)
        self.nombre.setDisabled(False)
        self.apellido.setDisabled(False)
        self.email.setDisabled(False)
        self.tel.setDisabled(False)
        self.dir.setDisabled(False)
        self.fechaNac.setDisabled(False)
        self.altura.setDisabled(False)
        self.peso.setDisabled(False)
        self.flag=False
        print(self.flag)
        ids = self.tabla.selectedItems()[0]

        llenar = self.cursor.execute("SELECT * FROM usuarios WHERE id=" + ids.text()[0] )

        for fila in llenar:
            self.nombre.setText(fila[1])
            self.apellido.setText(fila[2])
            self.email.setText(fila[3])
            self.tel.setText(fila[5])
            self.fechaNac.setText(fila[6])
            self.dir.setText(fila[4])
            self.peso.setText(str(fila[8]))
            self.altura.setText(str(fila[7]))

    def on_actualizar(self):
        self.flag=False
        ids = self.tabla.selectedItems()[0]
        nombre = str(self.nombre.text())
        apellido = str(self.apellido.text())
        email = str(self.email.text())
        tel = str(self.tel.text())
        dir = str(self.dir.text())
        fechaNac = str(self.fechaNac.text())
        altura = (self.altura.text())
        peso = (self.peso.text())

        self.tabla.addItem(str(nombre  + "   " + apellido + "   " + email + "   " + dir + "   " + tel + "   " + fechaNac+ "   " + altura+ "   " + peso ))

        self.on_limpiar()
        self.cursor.execute("UPDATE usuarios SET nombre='"+nombre+"', apellido='"+apellido+"', email='"+email+"', direccion='"+dir+"', telefono='"+tel+"', fecha='"+fechaNac+"', altura='"+altura+"', peso='"+peso +"' WHERE id="+ids.text()[0])
        self.conexion.commit()

    def on_eliminar(self):
        mensaje = QMessageBox()
        mensaje.setWindowTitle('Quitar.')
        mensaje.setIcon(QMessageBox.Question)
        mensaje.setInformativeText('¿Esta seguro de querer quitar la fila?')
        mensaje.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        resultado = mensaje.exec()
        if resultado == QMessageBox.Ok:
            ids = self.tabla.selectedItems()[0]
            usuario = self.tabla.currentRow()

            self.tabla.takeItem(usuario)
            self.cursor.execute("DELETE FROM usuarios WHERE id = " + ids.text()[0])
            self.conexion.commit()
            self.on_reset()
        elif resultado == QMessageBox.Cancel:
            self.on_reset()
        self.on_recargar_tabla()

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
            self.tabla.addItem(str(id+"   "+nombre  + "   " + apellido + "   " + email + "   " + dir + "   " + tel + "   " + fechaNac+ "   " + altura+ "   " + peso ))

    def on_aceptar(self):
        print(self.flag)
        if self.flag == True:
            self.on_crear()
            self.on_recargar_tabla()
        elif self.flag == False:
            self.on_actualizar()
            self.on_recargar_tabla()

    def on_crear(self):
        nombre = str(self.nombre.text())
        apellido = str(self.apellido.text())
        email = str(self.email.text())
        tel = str(self.tel.text())
        dir = str(self.dir.text())
        fechaNac = str(self.fechaNac.text())
        altura = str(self.altura.text())
        peso = str(self.peso.text())

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



    def closeEvent(self, event):
        self.conexion.close()


app = QApplication([])

win = MiVentana()
win.show()

app.exec_()