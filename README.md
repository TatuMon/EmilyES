# EMI
## Emily es un bot que te permite abrir carpetas y aplicaciones usando tu voz.

(Emi is only available in spanish at the moment)

**Actualmente, Emi no funciona de una forma dinámica, por lo que tus programas necesitan estar en lugares específicos para que puedan ser abiertos por Emi.**

### Las rutas deben ser:
* Para OperaGX:
`C:\Users\<user>\AppData\Local\Programs\Opera GX\launcher.exe`

* Para Rainbow Six Siege:
No es necesario una ruta específica, pero si debes tenerlo en Steam y no en otra plataforma

* Para League of Legends:
`C:\Riot Games\Riot Client\RiotClientServices.exe`
Esta es la carpeta en la que se instala por defecto

* Para la carpeta de juegos:
`C:/Users/<user>/Desktop/Juegos`


Esto, obviamente, no va a quedar asi. Quiero que este bot sea lo más dinámico, cómodo y facil de usar posible, por lo que trataré de mejorarlo siempre que pueda.

### ¿Que necesito para que el código funcione?
* Python:
* Podes descargarlo desde [aca](https://www.python.org/downloads/)

* PyAudio 0.2.11:
Para que el programa pueda usar el microfono conectado a la computadora, debes tener instalado PyAudio, que lo podes conseguir usando este comando en cmd: `py -m pip install pyaudio`
Si lo anterior no funciona, podes descargar el archivo .whl desde [aca](https://www.lfd.uci.edu/~gohlke/pythonlibs/) y, abriendo una terminal donde lo descargaste, instalarlo usando `py -m pip install <nombre del archivo>`

* Speech Recognition:
Esta librería es necesaria para poder transcribir lo que el código capta con el microfono. Al igual que PyAudio, podes instalar usando pip con el comando `py -m pip install SpeechRecognition` y, si esto no funciona, puedes hacer lo mismo que con PyAudio
