"Escribe un programa que calcule lo que tiene que cobrar un empleado sabiendo \
que se le tiene que aplicar al sueldo una retención del 20%."

class Empleado():
  _tablaEmpleados=[]
  
  def __init__(self):
    self.nombre=''
    self.apellidos=''
    self.NomAp=''
    self.NIF
    self.sueldoBruto=0.0
    self.sueldoNeto=0
    
  def NIF(self):
    
    print("Introduce tu NIF")
    self.NIF=input()

  def sueldoB(self):
    print("Introduce tu Sueldo Bruto")
    self.sueldoBruto=float(input())
    
    
  def CalculoSueldoNeto(self):
    self.sueldoNeto=self.sueldoBruto-0.2*self.sueldoBruto
    print("tu Sueldo neto será"+str(self.sueldoNeto))
    
  def TablaEmpleados(self):
    yaEsta=False
    for i in Empleado._tablaEmpleados:
          if self.NIF==Empleado._tablaEmpleados[i].NIF: 
            yaEsta=True
            break
          elif not yaEsta and i==len(Empleado._tablaEmpleados)-1:
            Empleado._tablaEmpleados.append(self)
            
  def NombreYApellido(self):
    print("Introduce tu Nombre y Apellidos")
    self.NomAp=input()
    Espacio=' '
    i=0
    nombresvarios=[]
    while self.NomAp(Espacio,i)!=-1:
      ini=self.NomAp.find(Espacio,i)
      nombresvarios.append(self.NomAp[i,ini])
      i=i+ini
    if len(nombresvarios)==3:
      self.nombre=nombresvarios[0]
      self.apellidos=nombresvarios[1]+" "+nombresvarios[2]
    else:
      print ("Tu nombre contiene algún nombre compuesto, porfavor ayudame a superar esto!! /n")
      print ("Introduce solo tu nombre")
      self.nombre=str(input)
      print ("Introduce solo tus apellidos")
      self.apellidos=str(input)
      
      
  
          
Luis=Empleado()

Luis.NIF()
Luis.sueldoB()
Luis.CalculoSueldoNeto()
Luis.NombreYApellido()
Luis.TablaEmpleados()

    
    