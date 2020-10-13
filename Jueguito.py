import sqlite3 
import time as t

#CONECCION Y CREACION DE LA BASE DE DATOS
#----------------------------------------------#
BaseDeDatos = sqlite3.connect("Base de Datos")
Partida = BaseDeDatos.cursor()

#Tabla Partidas
Partida.execute("""
CREATE TABLE IF NOT EXISTS Partidas(
    ID VARCHAR(6) PRIMARY KEY,
    NOMBRE VARCHAR(20) NOT NULL,
    VIDA INTEGER
)""")

#Tabla Inventario
Partida.execute("""
CREATE TABLE IF NOT EXISTS Inventario(
    ID_PARTIDA VARCHAR(6) PRIMARY KEY,
    ESPACIO_1 VARCHAR(20),
    ESPACIO_2 VARCHAR(20),
    ESPACIO_3 VARCHAR(20)
)""")
BaseDeDatos.commit()
#----------------------------------------------#

#VARIABLES DEL JUGADOR
#----------------------------------------------#
ID = ""
nombre = ""
inventario = []
vida = 0
#----------------------------------------------#

#FUNCIONES DE PARTIDA
#----------------------------------------------#
#Crear Partida Nueva
def CrearPartida(partida, avatar):
    try:
        if partida == "" or avatar == "":
            print("El ID o el Nombre son nulos.\nReingrese datos validos")
            err = True
            return err
        Partida.execute("INSERT INTO Partidas VALUES('"+partida+"', '"+avatar+"', 100)")
        Partida.execute("INSERT INTO Inventario VALUES('"+partida+"', 'empty', 'empty', 'empty')")
        BaseDeDatos.commit()
        
    except sqlite3.IntegrityError as err:
        print("La ID ya esta tomada")
        return err

#Cargar Partida Anterior
def CargarPartida(partida):
    global ID, nombre, vida, inventario
    if partida == "":
        print("El ID es nulo. Ingrese una ID válida")
        err = True
        return err
    Partida.execute("SELECT * FROM Partidas WHERE ID = '"+partida+"'")
    CARGA = Partida.fetchall()
    if CARGA:
        for datos in CARGA:
            ID = datos[0]
            nombre = datos[1]
            vida = datos[2]
    else:
        print("Perdon, no se encontró esa partida")
        err = True
        return err
    Partida.execute("SELECT ESPACIO_1, ESPACIO_2, ESPACIO_3 FROM Inventario WHERE ID_PARTIDA = '"+partida+"'")
    CARGA = Partida.fetchall()
    for datos in CARGA:
        inventario.append(datos[0])
        inventario.append(datos[1])
        inventario.append(datos[2])

error = True
#-------------------------------------------------------------#

#JUEGO
#-------------------------------------------------------------#
def DONNA(avatar):
    print("        ##################################################################")
    print("        | DONNA:  Buenas Capitán "+avatar+", en que puedo servirle?"+" "*(16-len(avatar))+"|")
    print("        ##################################################################")

def DatosDONNA(avatar, salud, equipo):
    print("        ##################################################################")
    print("        | DONNA:  Buenas Capitán "+avatar+", los datos sobre usted son: "+" "*(11-len(avatar))+"|")
    print("        |         Nombre: "+avatar+" "*(47-len(avatar))+"|")
    print("        |         Salud: "+str(salud)+" "*(48-len(str(salud)))+"|")
    print("        |         INVENTARIO:                                            |")
    for i in range (0,3):
        print("        |         "+str(i+1)+" -> "+equipo[i]+(" "*(50-len(equipo[i]))+"|"))
    print("        ##################################################################")


def Juego(partida, avatar, salud, equipo, nuevo = True):
    print("\n\n       BIENVENIDO CAPITAN "+avatar+"")
    print("""
       ##################################################################
       | COMANDO: Usted fue seleccionado para liderar el primer programa|
       |          espacial con mision a MARTE llamado 'Mars Attack'     |
       |          (si, no somos muy originales).                        |
       ##################################################################
       """)
    t.sleep(7)
    print("""
       ##################################################################
       | COMANDO: Una vez que llegue a la superficie marciana, habrá    |
       |          completado la mision.                                 |
       |          Objetivo: Sobrevivir haciendo mantenimiento a la nave |
       |          y realizando tareas.                                  |
       ##################################################################
       """)
    t.sleep(7)
    print("""
       ##################################################################
       | COMANDO: Junto a usted, como asistente, tiene a Donna.         |
       |          La inteligencia artificial creada para acompañar a    |
       |          nuestros astronautas y ayudarlos a sobrellevar la     |
       |          soledad del viaje. Di Hola Donna!!!                   |
       ##################################################################
       """)
    t.sleep(7)
    print("""
       ##################################################################
       | DONNA:   Hola, soy Donna, y me alegro de tenerte como capitán. |
       ##################################################################
       """)
    t.sleep(3)
    print("""
       ##################################################################
       | COMANDO: Es una monada, seguro te va a caer bien.              |
       |          Ella guarda el registro de tu traje, salud e          |
       |          inventario. ASI QUE HAZLE CASO!!!! costó unos 3 años  |
       |          de trabajo perfeccionarla.                            |
       ##################################################################
       """)
    t.sleep(7)
    print("""
       ##################################################################
       | COMANDO: Bueno, lo voy dejando para que se familiarize con la  |
       |          nave y con Donna. Ella se encargará de contarle el    |
       |          funcionamiento de los comandos y demás.               |
       |          ¡¡¡Buena suerte Capitán!!!                            |
       ##################################################################
        """)
    t.sleep(7)
    print("""
        #####################################
        ...CONEXION CON COMANDO FINALIZADA...
        #####################################
        """)
    t.sleep(3)
    print("""
        ##################################################################
        | DONNA:  Bueno, supongo que queras conocer las distintas        |
        |         modalidades que puedes usar. A ver, empecemos con algo |
        |         basico: "LLAMARME".                                    |
        ################################################################## 
        """)
    t.sleep(7)
    print("""
        ##################################################################
        | DONNA:  Para llamarme solo tienes que decir: `OK DONNA` y      |
        |         automaticamente apareceré para servirte.               |
        |         ¡VAMOS! Intentalo, para practicar...                   |
        ##################################################################
        """)
    comando = "EMPTY"
    repitio = False
    while(comando.upper() != "OK DONNA"):
        if repitio:
           print("Trate de decir `OK DONNA`")
        comando = input("Di algo: ")
        repitio = True
    repitio = False
    DONNA(avatar)
    t.sleep(2)
    print("""
        ##################################################################
        | DONNA:  ¡BUEN TRABAJO! Ahora sabes como llamarme, ¿Fácil no?   |
        |         Bueno, además de solamente aparecer, tambien puedo     |
        |         mostrarle informacion sobre usted. Para ello di        |
        |         `DATOS` una vez me hayas llamado.                      |
        |         ¡VAMOS! Practiquemos ...                               |
        ##################################################################
        """)
    while(comando.upper() != "DATOS"):
        if repitio:
           print("Trate de decir `DATOS`")
        comando = input("Di algo: ")
        repitio = True
    repitio = False
    DatosDONNA(avatar, salud, equipo)
    t.sleep(2)
     
#MENU
#-------------------------------------------------------------#
if __name__ == "__main__":
    print("Aventuras Espaciales!!!!")
    print("1.Nueva Partida")
    print("2.Continuar partida")
    eleccion = int(input("Elija: "))
    while eleccion not in range(1, 3):
        print("Eleccion Invalida")
        eleccion=int(input("Ingrese una opción valida: "))

##Opcion de CREAR PARTIDA NUEVA
    if eleccion == 1:
        while error:
            ID = input("Ingrese el nombre de Partida (6 caracteres max.): ")
            nombre = input("Ingrese nombre de su Avatar: ")
            error = CrearPartida(ID, nombre)
        vida = 100
        inventario = ['empty','empty','empty']
        Juego(ID, nombre, vida, inventario, True)

##Opcion de CONTINUAR UNA PARTIDA
    else:
        while error:
            ID = input("Ingrese la ID de la partida: ")
            error = CargarPartida(ID)
        Juego(ID, nombre, vida, inventario, False)
#-------------------------------------------------------------#

#JUEGO
#-------------------------------------------------------------#

