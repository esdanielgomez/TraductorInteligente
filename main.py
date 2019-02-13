import sys
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidget, QTableWidgetItem, QMainWindow
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtWidgets, QtMultimedia

from TextAPI import traducirTexto
from VozAPI import getAudioDeTexto, getTextoDeVoz, getVozPorIdiomaGeneroPersona

class TraductorInteligente(QMainWindow):

    def __init__(self, *args):

        super(TraductorInteligente, self).__init__(*args)
        loadUi('Interfaz.ui', self)

        idiomasEntrada = [
            self.tr('es-MX, Español latinoamerica'),
            self.tr('en-US, American English')
        ]

        idiomasSalida = [
            self.tr('en-US, American English'),
            self.tr('es-MX, Español latinoamerica')
    
        ]

        generos = [
            self.tr('M, Masculino'),
            self.tr('F, Femenino')
        ]

        self.comboIdiomaEntrada.addItems(idiomasEntrada)
        self.comboIdiomaSalida.addItems(idiomasSalida)
        self.comboGenero.addItems(generos)

        self.botonTraducir.clicked.connect(self.prcTraducir)
    
    def prcTraducir(self):
        self.labelEstado.setText("Escuchando voz...")
        
        if(self.comboIdiomaEntrada.currentText()=="es-MX, Español latinoamerica"): idiomaEntrada = "es-MX"
        elif(self.comboIdiomaEntrada.currentText()=="en-US, American English"): idiomaEntrada = "en-US"
        
        if(self.comboIdiomaSalida.currentText()=="es-MX, Español latinoamerica"): idiomaSalida = "es-MX"
        elif(self.comboIdiomaSalida.currentText()=="en-US, American English"): idiomaSalida = "en-US"

        if(self.comboGenero.currentText()=="F, Femenino"): generoVoz = "Femenino"
        elif(self.comboIdiomaSalida.currentText()=="M, Masculino"): generoVoz = "Masculino"

        mensajeCaptado = getTextoDeVoz(idiomaEntrada)
        self.labelInterpretado.setText(mensajeCaptado)
        print(mensajeCaptado)

        self.labelEstado.setText("Interpretando...")
        mensajeTraducido = traducirTexto(mensajeCaptado, idiomaEntrada, idiomaSalida)       
        self.labelTraducido.setText(mensajeTraducido)
        print(mensajeTraducido)

        nombreAgente = getVozPorIdiomaGeneroPersona(idiomaSalida,generoVoz)
        getAudioDeTexto(mensajeTraducido, nombreAgente, idiomaSalida)
        self.labelEstado.setText("Audio traducido satisfactoriamente.")

        
        filename = 'audio.wav'
        fullpath = QtCore.QDir.current().absoluteFilePath(filename) 
        url = QtCore.QUrl.fromLocalFile(fullpath)
        content = QtMultimedia.QMediaContent(url)
        player = QtMultimedia.QMediaPlayer()
        player.setMedia(content)
        player.play()

app = QApplication(sys.argv)
widget = TraductorInteligente()
widget.show()
app.exec_()