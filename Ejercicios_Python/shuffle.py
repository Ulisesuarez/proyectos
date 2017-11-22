import random
import os
playList = {}
# playList ={ 1: "titulo cancion", 2: "titulo cancion" ... }


"""libreria = {"California_Uber_Alles":
               {"track-number": 3, "artist": "Dead Kennedys", "album": "Dead Kennedys", "location":"/home/ulises/Micarpeta/proyectos/Ejercicios_Pyhton/biblioteca/California_Uber_Alles.mp3"},
           "Seattle_Party":
               {"track-number": 1, "artist": "Chastity Belt", "album": "No regrets", "location": "/home/ulises/Micarpeta/proyectos/Ejercicios_Pyhton/biblioteca/Seattle_Party.flac"},
           "King_Kunta":
               {"track-number": 3, "artist": "Kendrick Lamar", "album": "To Pimp A Butterfly", "location": "/home/ulises/Micarpeta/proyectos/Ejercicios_Pyhton/biblioteca/King_Kunta.mp3"},  
           "Gorilaz - Clint Eastwood.mp3":
               {"track-number": 3, "artist": "Kendrick Lamar", "album": "To Pimp A Butterfly", "location": "/home/ulises/Música/gorillaz/Gorilaz - Clint Eastwood.mp3"}
           }"""


def checkSeleccionaCancionRandom(cancion, libreria):
    
    assert isinstance(cancion, str)
    assert isinstance(libreria, dict)

    if cancion not in libreria:
        return False
    else:
        return True

def checkIndices(indices):
    for i in indices:
        if indices.count(i)>1:
            return False
        """incidencias=0
        for j in range(0,len(indices)):
        
            if i==indices[j]:
                incidencias=incidencias+1
        if incidencias>1:
            return False"""
    return True

def checkCancionRepetida(playlist):
    
    for i in playlist:
        if playList.count(i)>1:
            return False
        """incidencias=0
        for j in range(0,len(playlist)):
        
            if i==playlist[j]:
                incidencias=incidencias+1
        if incidencias>1:
            return False"""
    return True


    

"""def creadorIndicesRandom(libreria):
   assert isinstance(libreria,dict),"no es un diccionario!"
   indices=[]
   indiceRandom=random.randrange(1,len(libreria)+1)
   indices.append(indiceRandom)
   while len(indices)!=len(libreria):
        while indiceRandom in indices:
           indiceRandom=random.randrange(1,len(libreria)+1)
        indices.append(indiceRandom)  
   assert isinstance(indices,list),"creadorIndicesRandom no devuelve una lista"
   assert indices!=[],"lista indices vacía"
   assert  checkIndices(indices) ,"indice repetido"
   return indices"""

def creadorIndicesRandom2(libreria):
    assert isinstance(libreria,dict)," libreria no es un diccionario!"
    assert isinstance(random.sample(range(1,len(libreria)+1), len(libreria)),list),"creadorIndicesRandom2 no devuelve una lista"
    assert random.sample(range(1,len(libreria)+1), len(libreria))!=[],"lista indices vacía"
    assert  checkIndices(random.sample(range(1,len(libreria)+1), len(libreria))) ,"indice repetido"
    return random.sample(range(1,len(libreria)+1), len(libreria))

def getLocalización(libreria,cancion):
    assert isinstance(cancion,str),"canción no es una string"
    return libreria[cancion]["location"]

def creadorListaTitulos(libreria, playList):
   assert isinstance(libreria,dict),"libreria no es un diccionario!"
   assert isinstance(playList,dict),"playList no es un diccionario"
   indices=creadorIndicesRandom2(libreria)
   i=0
   for key in libreria.keys():
       playList[indices[i]]=key
       i=i+1
       
       
   assert playList, "La lista(diccionario playList) está vacía"
   assert checkCancionRepetida, "Hay canciones repetidas"   
   return playList

"""def iniciarPlayList(numeroCancion):
    
    # simulare que el diccionario playList es una lista playList[integer]
    # donde la clave es un numero entero que incremento cada vez
    # que añado una cancion a la playList
    claveDiccionarioPlayList = numeroCancion

    def appendCancion(cancion, playList):

        assert isinstance(playList, dict), "playList no es un diccionario"
        # la cancion no debe estar ya en la playList
        assert cancion not in list(playList.values())

        # closure: claveDiccionarioPlayList recuerda su ultimo valor
        # cada vez que invocamos a appendCancion()
        # De este modo, incremento la clave del diccionario en uno
        # y coloco la cancion en esa "posicion" de la lista que simula
        # el diccionario implementado de este modo.
        nonlocal claveDiccionarioPlayList
        claveDiccionarioPlayList += 1
        # asocio el valor titulo de la cancion a la clave integer
        playList[claveDiccionarioPlayList] = str(cancion)
        return claveDiccionarioPlayList

    return appendCancion"""
def imprimirCancionesReproducidas(playList):
    
    assert isinstance(playList, dict)

    # Recorro el objeto iterable view keys() del diccionario playList
    # Antes lo he ordenado.
    for numeroCancion in sorted(playList.keys()):
        # muestro la posicion en la que fue elegida la cancion
        # y el titulo de la cancion
        print(str(numeroCancion) + ": " + str(playList[numeroCancion]))

def lanzarVLC(libreria,playList):
    
    # Las canciones han de estar en un directorio llamado biblioteca
    # en el directorio de la aplicacion.
    # Han de ser expresamente las incluidas en el diccionario libreria.
    # La extensión a este  programa es incluir la capa de acceso a datos
    # para extraer los titulos de las canciones y las rutas
    # a los ficheros del fichero XML playlist.xspf que genera VLC
    # o Rhythmbox con las canciones de la biblioteca

    import subprocess
    import shlex
    import os

    linuxPathVLC = "/usr/bin/vlc"
    lineaComandoVLC = [linuxPathVLC]
    separador = " "

    for numeroCancion in sorted(playList.keys()):
        tituloCancion = playList[numeroCancion]
        try:
            
            rutaAccesoFichero = getLocalización(libreria,tituloCancion)
            print(tituloCancion,getLocalización(libreria,tituloCancion))
        except KeyError:
            print("la cancion " + str(tituloCancion) + " no se encuentra en la biblioteca")
        else:
            # compruebo si la ruta de acceso al fichero cancion es correcto
            if os.path.exists(str(rutaAccesoFichero)):
                # anhado la ruta de acceso a la cancion
                # a la linea de comandos para invocar a VLC
                #lineaComandoVLC = lineaComandoVLC + separador + str(rutaAccesoFichero)
                lineaComandoVLC.append(str(rutaAccesoFichero))
            else:
                print("no lo encuentro",os.path.exists(str(rutaAccesoFichero)))
                pass

    # Popen necesita una lista de string
    # Esta libreria optimiza la division de los strings que forman
    # la entrada de un comando en argumentos
    #args = shlex.split(lineaComandoVLC)
    #print("somos los args",args)

    try:
        # lanzo el subproceso VLC con las opciones adecuada:
        # la ruta de acceso a las canciones de la playList
        procesoVLC = subprocess.Popen(lineaComandoVLC)
        # procesoVLC = subprocess.Popen(["/usr/bin/vlc", "California_Uber_Alles.mp3", "Seattle_Party.flac"])
    except OSError:
        print("el fichero no existe")
    except ValueError:
        print("argumentos invalidos")
    else:
        print("lanzando VLC con lista aleatoria")

def ObtenerLibreriaGrupo():
    libreria=dict()
    musicaPath="/home/ulises/Música/"
    musicaArbol=os.walk(musicaPath)
    
    for path,sub,fileList in musicaArbol:
        for grupo in sub:
         print(grupo)
        break
    while True:
        print("¿Que quieres escuchar?")
        NombreGrupo=input()

        if os.path.exists(musicaPath+NombreGrupo):
            grupoPath=musicaPath+NombreGrupo
            grupoArbol=os.walk(grupoPath)
            
            for path,sub,fileList in grupoArbol:
                if len(sub)>0:#nuevo ¿?
                    for disco in sub:
                        print(disco)
                    while True:
                        print("¿Que disco de "+ NombreGrupo+" quieres escuchar?")
                        InputUsuarioDisco=input()
                        nombreDisco=""
                        for disco in sub:
                            if InputUsuarioDisco in disco:
                                nombreDisco=disco
                        
                        if nombreDisco=="":
                            print("Introduce  el nombre exacto de la carpeta por favor:")
                            nombreDisco=input()
                        #print(os.path.exists(musicaPath+NombreGrupo+"/"+nombreDisco),musicaPath+NombreGrupo+"/"+nombreDisco)
                        if os.path.exists(grupoPath+"/"+nombreDisco):
                            discoPath=grupoPath+"/"+nombreDisco
                            for path,sub,fileList in os.walk(discoPath):
                                thePath=path
                                listFilename=fileList
                                for fileName in listFilename:
                                     print(path,sub,fileName )
                                     if ".mp3" in fileName or ".flac" in fileName:
                                         libreria[fileName]={"location":thePath+'/'+fileName}
                                     print (libreria)
                            return libreria

                            #break
                        else: 
                            print("puedes volver a escribirlo")
                thepath=path
                listfilename=fileList
            for fileName in listfilename:
                print(path,sub,fileName )
                if ".mp3" in fileName or ".flac" in fileName:
                    libreria[fileName]={"location":thepath+'/'+fileName}
            print (libreria)
            return libreria
            #break
        else:
            print("introduce de nuevo el nombre del grupo, no encuentro la carpeta")
    return libreria
   
def playShuffleVLC(playList):
    libreria=ObtenerLibreriaGrupo()
    
    creadorListaTitulos(libreria, playList)

    imprimirCancionesReproducidas(playList)

    lanzarVLC(libreria,playList)     

playShuffleVLC(playList)
#print(creadorIndicesRandom(libreria))
#print(creadorIndicesRandom2(libreria))
#print(listaTitulos(libreria,playList))