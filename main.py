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
        elif(self.comboGenero.currentText()=="M, Masculino"): generoVoz = "Masculino"

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
        import pyaudio
        import wave

        CHUNK = 1024

        wf = wave.open(filename, 'rb')

        # instantiate PyAudio (1)
        p = pyaudio.PyAudio()

        # open stream (2)
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        # read data
        data = wf.readframes(CHUNK)

        # play stream (3)
        while len(data) > 0:
            stream.write(data)
            data = wf.readframes(CHUNK)

        # stop stream (4)
        stream.stop_stream()
        stream.close()

        # close PyAudio (5)
        p.terminate()


app = QApplication(sys.argv)
widget = TraductorInteligente()
widget.show()
app.exec_()