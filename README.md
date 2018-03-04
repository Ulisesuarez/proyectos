# Mi primer respositorio

En él se incluyen actividades de las siguientes asignaturas:
- Programación: Ejercicios de **Pyhton**
- Lenguaje de Marcas: Webs sencillas en **html** y **css**
- Bases de datos: Modelos **SQL**

A modo de clarificación adjunto una *TABLE* (uso *anglicisms* para ver el poder de las cursivas) donde incluyo las carpetas existentes en el repositorio.

| Carpetas |Asignatura      | Enlace|
|--------|-------|--------|
| Ejercicios Python |Programación      |https://github.com/Ulisesuarez/proyectos/tree/provisional/Ejercicios%20Pyhton|
|web|Lenguaje de Marcas|https://github.com/Ulisesuarez/proyectos/tree/provisional/web|

A continuación algunos ejemplos de la humildad de mis programas:

#### Calcular factorial en Python:

```python

def factorial(numer):
	fact=1
    while numer >0:
    	fact=numer*fact
    	numer=numer-1
    return fact

```
#### Fragmento de una Web:
```xml
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">



<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<title>Historias de ayer y hoy</title>
<meta name="description" content="Aquí podras encontrar reseñas de obras literarias de autorias diversas que conisdero destacables" />
<meta name="keywords" content="Literatura,Libros,Obras,Escritura,"/>
<link rel="stylesheet" type="text/css" href="theme.css"/>
</head>

<body>

<div class="superior">
    <div class="cabezera"><img title="libros" src="https://i.imgur.com/nJW8TU5.png" alt="Libros de tapa duro apilados uno al lado del otro" style="width:1000px;height:130px;"/>
    </div>


    <br/>
    <h1>Historias de ayer y hoy </h1>
</div>
<div class="lateral">
    <ul class="menu">

        <li><a href="WebPractica.html">Inicio</a></li>
        <li> </li>
        <li><a href="About.html">Acerca del autor</a></li>

  </ul>
</div>

<div class="About">

    <p> Las leyendas cuentan que esta página se escribió sola</p>

</div>

</body>

</html>
```






