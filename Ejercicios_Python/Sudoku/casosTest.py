import importlib
import sys

try:
    print("¿Cómo se llama el archivo donde tienes los casos test? (asegurate de que no cargues otro!)")
    nombreTestPrograma=input()

    nombreTestPrograma=importlib.import_module(nombreTestPrograma)
    dicTest=nombreTestPrograma.__dict__
except:
    print("Cuando sepas como se llama el archivo donde tienes los casos tests vuelves")
    sys.exit()
    

#import datostest

#dicTest=datostest.__dict__
#print(dicTest)

def tester(*args):
    
    expected=args[0]
    func=args[1]
    args=args[2:]
    args2=[]
    for ar in args:
        if ar in dicTest.keys():
            args2.append(dicTest[ar])
        else:
            print(ar+" no existe, revisa los nombres de las variables utilizadas en los casos test (datostest.py)")
            return None
    args2=tuple(args2)

    #print (func(*args2) == expected)    
    assert (func(*args2) == expected)

