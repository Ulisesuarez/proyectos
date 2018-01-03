
var bienvenidaFlag=true;
function bienvenida() {
    

                
    const mensaje = '\u00BFEst\u00E1s agobiado? \n\n\u00BFNo cre\u00EDas que Dual fuera tan duro? \n\nHazte un favor, \u00A1organ\u00EDzate!';
           
           document.getElementById("exp").style.borderColor="white";
           if (bienvenidaFlag){
            bienvenidaFlag=false;   
            alert(mensaje);
        }
           
        }

function fInput(title){
    
    var person = prompt("de que d\u00EDa a que d\u00EDa es?", "dd/mm - dd/mm");
    if (person != null) {
        document.getElementById("titulo").innerHTML =person;
    }

}
function define(td){
    var person = prompt("Que har\u00E9?", "Estudiar");
    if (person != null) {
        td.innerHTML =person;
    }
}

function ratonEncimaHoraHead(){

    var horas = document.getElementsByClassName("hora");
    
    for (hora in horas) {

        horas[hora].style.backgroundColor= "#8a2be2";
        horas[hora].style.fontSize="1em";



       
    } 
       
}

function ratonFueraHoraHead(){
    var horas = document.getElementsByClassName("hora");
    
    for (hora in horas) {
        
        horas[hora].style.backgroundColor= "rgb(133, 154, 214)";
        horas[hora].style.fontSize="0.8em";
        


        
}}

function ratonEncimaDias(cell){
    var indiceCol= cell.cellIndex
    console.log(indiceCol)
    for (fila in document.getElementById("tablaHorario").rows){
        if (fila==0){
            fila=1
        }
        document.getElementById("tablaHorario").rows[fila].cells[indiceCol].style.backgroundColor="green"
        document.getElementById("tablaHorario").rows[fila].cells[indiceCol].style.fontWeight="bold"
    }
}

function ratonFueraDias(cell){
    var indiceCol= cell.cellIndex
    console.log(indiceCol)
    for (fila in document.getElementById("tablaHorario").rows){
        if (fila==0){
            fila=1
        }
        document.getElementById("tablaHorario").rows[fila].cells[indiceCol].style.backgroundColor="aquamarine"
        document.getElementById("tablaHorario").rows[fila].cells[indiceCol].style.fontWeight="normal"
    }
}

function ratonEncimaHora(cell){
    console.log(cell);
    var indiceFila= cell.parentElement.rowIndex;
    console.log("indicefila"+indiceFila);
    for (columna in document.getElementById("tablaHorario").rows[indiceFila].cells){
        console.log(columna);
        if (columna==0){
            columna=1;}
            document.getElementById("tablaHorario").rows[indiceFila].cells[columna].style.backgroundColor="plum" ;
        }
      
         
    }

function ratonFueraHora(cell){
        console.log(cell);
        var indiceFila= cell.parentElement.rowIndex;
        console.log("indicefila"+indiceFila);
        for (columna in document.getElementById("tablaHorario").rows[indiceFila].cells){
            console.log(columna);
            if (columna==0){
                columna=1;}
                document.getElementById("tablaHorario").rows[indiceFila].cells[columna].style.backgroundColor="aquamarine" ;
            }
          
             
        }
    
function ratonFuera(cell){
    cell.style.backgroundColor="aquamarine";
    cell.style.fontWeight="normal";
    document.getElementById("tablaHorario").style.borderCollapse="collapse";
    cell.style.borderStyle="solid";
    
        
}

function ratonEncima(cell){
cell.style.backgroundColor="rgb(199, 98, 199)";
cell.style.fontWeight="bold";
document.getElementById("tablaHorario").style.borderCollapse="separate";
cell.style.borderStyle="dashed";
  
}

function expandInfo(cell){
    var name=cell.innerHTML
    if (name[0]=="B"){
        name="BBDD"
    }
    if (name[0]=="P"){
        name="Prog"
    }
    if (name[0]=="L"){
        name="LLMM"
    }
    if (name[0]=="A"){
        name="A"
    }
    if (name[0]=="T"){
        name="T"
    }
    var explicaciones={"BBDD":"En <b>Bases de Datos</b> se trabajan las nociones fundamentales acerca de la consulta, creaci&oacute;n y modificaci&oacute;n de bases de datos utilizando MYSQL como lenguaje",
"FOL":"<b>Formaci&oacute;n y Orientaci&oacute;n Laboral</b>: Introducci&oacute;n a las gestiones propias de un trabajador, calcular n&oacute;minas, vacaciones, derechos... ",
"SI":"<b>Sistemas Inform&aacute;ticos</b>: Aprender fundamentos sobre hardware y control de sistemas operativos",
"Prog":"<b>Programaci&oacute;n</b>: Python  iteradores, estructuras if-else, tipos de datos (diccionarios, listas, strings, decimales),\nJava: programaci&oacute;n orientada a objetos",
"LLMM":"<b>Lenguaje de Marcas</b>: Aprender html, css, javaScript, XML, y como integrar estas herramientas para desarrollar p&aacute;ginas Web cumpliendo los estandares de calidad de la W3C",
"ED":"<b>Entornos de desarrollo</b>: se aprende a utilizar herramientas como GIT (control de versiones), editores de texto especializados, pair-programing, fundamentos SOLID",
"A":"Puedes <b>dormir</b> pero te recomiendo totalmente la deprivaci&oacute;n de sue&ntilde;o con tal de mantener una eficacia ef&iacute;mera hasta el momento de tu cese",
"T":"<b>Tutor&iacute;a</b>: no requerida hasta la fecha, resoluci&oacute;n de dudas por parte del profesorado"}
    console.log(name)
    console.log(explicaciones)
    document.getElementById("exp").innerHTML=explicaciones[name]
    document.getElementById("exp").style.borderColor="black"
}

    
    /*for (fila in document.getElementById("tablaHorario").rows[indiceCol].cells){
      
        document.getElementById("tablaHorario").rows[indiceCol].cells[fila].style.backgroundColor="green"  
    }
    
}*/