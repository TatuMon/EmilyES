import os
import subprocess

def openOpera():
    subprocess.call(["C:\\Users\yoh1n\AppData\Local\Programs\Opera GX\launcher.exe"])

def openRainbow():
    subprocess.run("start steam://run/359550", shell=True)

def openLoL():
    subprocess.Popen(["C:\Riot Games\Riot Client\RiotClientServices.exe", "--launch-product=league_of_legends", "--launch-patchline=live"])

def openGames():
    os.startfile("C:/Users/yoh1n/Desktop/Juegos")

def activateCommand(words:list):
    print("Comando solicitado: " + " ".join(words))
    if(words[0] == "Emeli" or words[0] == "Emily" or words[0] == "Emely"):
        print("Hola!\n\nEstas son las opciones disponibles:\n\t1- abrir opera\n\t2- abrir discord\n\t3- abrir juegos")

        if(words[1] == "abrir" or words[1] == "abrí" or words[1] == "abrime"):
            if(words[2] == "ópera" or words[2] == "opera"):
                print("Abriendo OperaGX")
                openOpera()    
            elif(words[2] == "Rainbow"):
                print("Abriendo Rainbow Six Siege")
                openRainbow()
            elif(words[2] == "lol"):
                print("Abriendo League of Legends")
                openLoL()
            elif(words[2] == "juegos"):
                print("Abriendo la carpeta de juegos")
                openGames()
            else:
                print("Comando inválido")