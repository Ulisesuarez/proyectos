import xml.etree.ElementTree as ET

tree = ET.parse("/home/ulises/Micarpeta/proyectos/Ejercicios_Pyhton/menu_xml.xml")
root = tree.getroot()
print(root.tag)
print(root.attrib)

for element in root.iter("food"):
   
   nombre = element.find('name').text
   precio = element.find('price').text
   print("plato:{}  precio:{}".format(nombre,precio))