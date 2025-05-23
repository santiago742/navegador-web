#Importar modulos necesarios
import sys #para acceder a arumentos del sistema

#modulos de pyqt5 para ;la interfaz y navegacion web
from PyQt5.QtCore import QUrl# funciona para poder ocupar la url de e navegador
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QLineEdit, QAction
from PyQt5.QtWebEngineWidgets import QWebEngineView#para poder mostrar el navegador

#Clase principal del navegador que hereda de QMainWindow
class NavegadorWeb(QMainWindow):
    def __init__(self):#constructor de la clase
        super().__init__() #Inicializa la clase QMainWindow

        #Configuramos la ventana principal
        self.setWindowTitle("Navegador Web con PyQt5") # Titulo de la ventana
        self.setGeometry(100, 100, 1024, 768) # posicion y tamaño de la ventana 

        #Creamos el visor web donde se mostraran las paginas
        self.navegador = QWebEngineView()
        self.navegador.setUrl(QUrl("https://www.minecraft.net/es-es")) #Pagina de inicio

        #Creamos la barra de herramientas de navegacion 
        barra_navegacion = QToolBar("Barra de Navegación")
        self.addToolBar(barra_navegacion) #Añadimos la barra a la ventana

        #Boton para ir hacia atras 
        boton_atras = QAction("⇜",self)
        boton_atras.setStatusTip("Atrás")
        boton_atras.triggered.connect(self.navegador.back)#Conectamos a la funcion back del navegador
        barra_navegacion.addAction(boton_atras) #añadimos el boton a la  barra

        #boton para ir hacia adelante
        boton_adelante = QAction("⇝",self)
        boton_adelante.setStatusTip("Adelante")
        boton_adelante.triggered.connect(self.navegador.forward)
        barra_navegacion.addAction(boton_adelante)

        #Boton para recargar la pagina
        boton_recargar = QAction("↺",self)
        boton_recargar.setStatusTip("Recargar")
        boton_recargar.triggered.connect(self.navegador.reload)
        barra_navegacion.addAction(boton_recargar)

        #Campoi de texto para ingresar direcciones web
        self.barra_direcciones = QLineEdit()
        self.barra_direcciones.setPlaceholderText("Escribe una URL y presiona Enter")
        self.barra_direcciones.returnPressed.connect(self.carga_url) #Llama a cargar_url() al presionar Enter
        barra_navegacion.addWidget(self.barra_direcciones)#Añadimos el campo a la barra 
        #Añadimos la barra de direcciones cuando cambia la URL

        self.navegador.urlChanged.connect(self.actualizar_barra_direcciones)

        #colocamos el navegador como el widget principal de la ventana
        self.setCentralWidget(self.navegador)

    #funcion que carga la RL ingresada en el campo de texto
    def carga_url(self):
        url = self.barra_direcciones.text() #obtenemos el texto escrito
        if url:
            #si no empieza con https, le añadimos http:// por defecto
            if not url.startswith("http://") and not url.startswith("https://"):
                url = "http://" + url
            self.navegador.setUrl(QUrl(url)) #Cargamos la URL en el navegador

    #Funcionn que actualiza la barra de direcciones cuando cambia la pagina
    def actualizar_barra_direcciones(self, url):
        self.barra_direcciones.setText(url.toString()) # Mostramos la URL actual
        self.barra_direcciones.setCursorPosition(0) # Colocamos el cursor al principio

#Codigo que se ejecuta si el archivo es el programa principal
if __name__ == "__main__":
    app = QApplication(sys.argv)      #Creamos la aplicacion Qt
    ventana = NavegadorWeb()          #Creamos la ventana del navegador
    ventana.show()                    #Mostramos la ventana
    sys.exit(app.exec_())             #Iniciamos el bucle de eventos

          