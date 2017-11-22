import os
import re

Musicapath=os.walk("/home/ulises/Música/")

for path,sub,fileList in Musicapath:
    print(sub)
    break

def ObtenerLibreriaGrupo():
    libreria={}
    while True:
        print("¿que quieres escuchar?")
        NombreGrupo=input()
        if os.path.exists("/home/ulises/Música/"+NombreGrupo):
            grupopath=os.walk("/home/ulises/Música/"+NombreGrupo)
            for path,sub,fileList in grupopath:
                thepath=path
                listfilename=fileList
            for fileName in fileList:
                print(path,sub,fileName )
                libreria[fileName]={"location":path+'/'+fileName}
            print (libreria)
            break
    else:
        print("introduce de nuevo el nombre del grupo, no encuentro la carpeta")