<template>
  <v-container grid-list-md text-xs-center>
    <v-layout wrap>
      <v-flex id="cabf" xs12 sm12 md12>
        <img id="cabecera" src="../assets/HLogotext.jpg" title="Ignorantia Universitae" alt="Ignorantia Universitae">
        <v-flex xs12 sm12 md12><v-card-text><span class="subcab">Elevando barreras al conocimiento</span></v-card-text></v-flex>
      </v-flex>
      <v-flex xs12 sm12 md12>
        <v-toolbar dense id="tbmenu" >
          <v-toolbar-title class="hidden-sm-and-down">IGNORANTIA</v-toolbar-title>
          <v-spacer class="hidden-sm-and-down">{{parseXml()}}</v-spacer>
          <v-btn color="white" href="#Home" flat><span class="boton">HOME</span></v-btn>
          <v-btn color="white"  href="#Test" flat><span class="boton">APRENDE</span></v-btn>
          <v-btn color="white"  href="#About" flat><span class="boton">ABOUT</span></v-btn>
        </v-toolbar>
      </v-flex>
      <v-flex v-if="noFin" id="padre" xs12 sm12 md12>
        <v-card id="contenedor" dark class="secondary">
          <v-card-text id="p1" class="px-0">{{pregunta}}</v-card-text>
          <img v-if="showImage" id="img1" v-bind:src=src title="codigo1" :alt=src>
          <v-flex xs12 sm12 md12>
            <v-btn id="b0" @click="setButtonAnswer(0)" class="resp"></v-btn>
          <v-btn id="b1" @click="setButtonAnswer(1)" class="resp"></v-btn></v-flex>
        </v-card>
        <v-btn id="boton" @click="siguiente"></v-btn>
      </v-flex>
      <v-flex id="secondParent"  xs12 sm12 md12><v-card id="second" dark class="secondary"></v-card></v-flex>
      </v-layout>
  </v-container>
 </template>

<script>

export default {

  data: function () {
    return {
      name: 'test',
      pregunta: '',
      src: '',
      ArrayRespuestas: [],
      indice: 0,
      XMLparseado: null,
      tipoActual: '',
      showImage: true,
      respuestaButton: {
        valor: '',
        correct: ''
      },
      respuestaDataLits: {
        valor: '',
        correct: '',
        identificador: ''
      },
      arrayPreguntas: [],
      noFin: true,
      espaciar: false,
      puntuacion: 10
    }
  },
  methods: {
    parseXml () {
      let sel = this
      let xhttp = new XMLHttpRequest()
      xhttp.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200) {
          sel.gestionarXml(this.responseXML)
          sel.XMLparseado = this.responseXML
        } else {
        }
      }
      xhttp.open('GET', 'https://rawgit.com/Ulisesuarez/TESTGO/master/ignorantia/src/assets/preguntas.xml', true)
      xhttp.send()
    },
    gestionarXml (xmldoc) {
      let flagRespuestas
      if (document.getElementById('formulario')) {
        let oldform = document.getElementById('formulario')
        oldform.parentNode.removeChild(oldform)
      }
      this.$data.pregunta = this.indice + 1 + ') ' + xmldoc.getElementsByTagName('question')[this.indice].childNodes[1].innerHTML
      if (xmldoc.getElementsByTagName('question')[this.indice].childNodes[5].localName === 'image') {
        this.showImage = true
        flagRespuestas = xmldoc.getElementsByTagName('question')[this.indice].childNodes[5]
        this.$data.src = xmldoc.getElementsByTagName('question')[this.indice].childNodes[5].innerHTML.toString()
        document.getElementById('img1').style.width = 80 + '%'
      } else {
        this.showImage = false
        flagRespuestas = xmldoc.getElementsByTagName('question')[this.indice].childNodes[3]
        this.$data.src = ''
      }
      let formnode = document.createElement('FORM')
      formnode.style.textAlign = 'left'
      formnode.style.marginLeft = 10 + '%'
      formnode.id = 'formulario'
      this.tipoActual = xmldoc.getElementsByTagName('question')[this.indice].childNodes[3].innerHTML

      switch (this.tipoActual) {
        case 'radio':
          this.radio(formnode, flagRespuestas)
          break
        case 'select multiple':
          this.selectMultiple(formnode, flagRespuestas)
          break
        case 'text':
          this.text(formnode, flagRespuestas)
          break
        case 'select':
          this.selectMultiple(formnode, flagRespuestas)
          break
        case 'button':
          this.button(flagRespuestas)
          break
        case 'datalist':
          this.dataList(formnode, flagRespuestas)
          break
        case 'checkbox':
          this.radio(formnode, flagRespuestas)
          break
        default:
      }
      if (document.getElementById('boton')) {
        let submit = document.getElementById('boton')
        submit.innerHTML = 'Contestar'
        submit.style.marginLeft = 70 + '%'
        submit.style.fontWeight = 'bold'
      }
      if (document.getElementById('contenedor')) {
        document.getElementById('contenedor').appendChild(formnode)
      }
    },
    siguiente () {
      if (this.indice === 10) {
        this.tipoActual = ''
        this.mostrarCorreccion()
      }
      switch (this.tipoActual) {
        case 'radio':
          this.checkRadio()
          break
        case 'select multiple':
          this.checkSelectMultiple()
          break
        case 'text':
          this.checkText()
          break
        case 'select':
          this.checkSelectMultiple()
          break
        case 'button':
          this.checkButton()
          break
        case 'datalist':
          this.checkDataLits()
          break

        default:
      }
    },
    mostrarCorreccion () {
      this.noFin = false
      let wrong
      for (let i = 0; i < 10; i++) {
        let container = document.getElementById('second')
        let clon = container.cloneNode(true)
        let textoPregunta = document.createElement('v-card-text')
        let imagenPregunta = document.createElement('IMG')
        let valorRespuesta = 0
        let flagRespuestas
        textoPregunta.innerHTML = i + 1 + ') ' + this.XMLparseado.getElementsByTagName('question')[i].childNodes[1].innerHTML
        if (this.XMLparseado.getElementsByTagName('question')[i].childNodes[5].localName === 'image') {
          imagenPregunta.style.display = 'block'
          flagRespuestas = this.XMLparseado.getElementsByTagName('question')[i].childNodes[5]
          imagenPregunta.src = this.XMLparseado.getElementsByTagName('question')[i].childNodes[5].innerHTML.toString()
          imagenPregunta.style.width = 80 + '%'
          imagenPregunta.style.marginLeft = 10 + '%'
        } else {
          imagenPregunta.style.display = 'none'
          flagRespuestas = this.XMLparseado.getElementsByTagName('question')[i].childNodes[3]
        }
        clon.appendChild(textoPregunta)
        clon.appendChild(imagenPregunta)
        if (flagRespuestas.nextSibling.nextSibling != null) {
          while (flagRespuestas.nextSibling.nextSibling && flagRespuestas.nextSibling.nextSibling.localName === 'option') {
            this.espaciar = false
            flagRespuestas = flagRespuestas.nextSibling.nextSibling
            let respuestas = document.createElement('P')
            respuestas.style.textAlign = 'left'
            respuestas.style.marginLeft = 10 + '%'
            respuestas.setAttribute('value', i + 1 + '-' + valorRespuesta)
            respuestas.setAttribute('name', 'answer')
            if (flagRespuestas.attributes.correct.nodeValue === 'y') {
              respuestas.setAttribute('correct', 'y')
              respuestas.style.backgroundColor = 'green'
            } else {
              respuestas.setAttribute('correct', 'n')
            }
            if (Array.isArray(this.ArrayRespuestas[i])) {
              for (let subi = 0; subi < this.ArrayRespuestas[i].length; subi++) {
                if (this.ArrayRespuestas[i][subi].valor === i + 1 + '-' + valorRespuesta) {
                  respuestas.style.textDecoration = 'underline'
                  if (this.ArrayRespuestas[i][subi].correct === 'n') {
                    this.puntuacion = this.puntuacion - 1 / this.ArrayRespuestas[i].length
                    respuestas.style.backgroundColor = 'red'
                  }
                } else {
                  if (this.ArrayRespuestas[i][subi].identificador &&
                    this.ArrayRespuestas[i][subi].identificador === i + 1 + '-' + valorRespuesta &&
                    this.ArrayRespuestas[i][subi].valor !== this.ArrayRespuestas[i][subi].correct) {
                    this.puntuacion = this.puntuacion - 1 / this.ArrayRespuestas[i].length
                    let wrong = document.createElement('P')
                    wrong.innerHTML = this.ArrayRespuestas[i][subi].valor
                    wrong.style.backgroundColor = 'red'
                    wrong.style.marginLeft = 10 + '%'
                    wrong.style.textAlign = 'left'
                    wrong.style.width = 40 + '%'
                    wrong.style.display = 'inline-block'
                    wrong.style.textDecoration = 'underline'
                    respuestas.style.width = 40 + '%'
                    respuestas.style.display = 'inline-block'
                    clon.appendChild(wrong)
                    if (subi === this.ArrayRespuestas[i].length - 1) {
                      this.espaciar = true
                    }
                  } else {
                    if (this.ArrayRespuestas[i][subi].identificador &&
                      this.ArrayRespuestas[i][subi].identificador === i + 1 + '-' + valorRespuesta &&
                      this.ArrayRespuestas[i][subi].valor === this.ArrayRespuestas[i][subi].correct) {
                      respuestas.style.textDecoration = 'underline'
                    }
                  }
                }
              }
            } else {
              if (this.ArrayRespuestas[i].valor === i + 1 + '-' + valorRespuesta) {
                respuestas.style.textDecoration = 'underline'
                if (this.ArrayRespuestas[i].correct === 'n') {
                  respuestas.style.backgroundColor = 'red'
                  this.puntuacion = this.puntuacion - 1
                }
              } else {
                if (this.ArrayRespuestas[i].identificador &&
                  this.ArrayRespuestas[i].identificador === i + 1 + '-' + valorRespuesta &&
                  this.ArrayRespuestas[i].valor !== this.ArrayRespuestas[i].correct) {
                  this.puntuacion = this.puntuacion - 1
                  wrong = document.createElement('P')
                  wrong.innerHTML = this.ArrayRespuestas[i].valor
                  if (wrong.innerHTML === flagRespuestas.childNodes[0].nodeValue.slice(0)) {
                    respuestas.style.display = 'none'
                  }
                  wrong.style.backgroundColor = 'red'
                  wrong.style.marginLeft = 10 + '%'
                  wrong.style.textAlign = 'left'
                  wrong.style.textDecoration = 'underline'
                  clon.appendChild(wrong)
                } else {
                  if (this.ArrayRespuestas[i].identificador &&
                    this.ArrayRespuestas[i].identificador === i + 1 + '-' + valorRespuesta &&
                    this.ArrayRespuestas[i].valor === this.ArrayRespuestas[i].correct) {
                    respuestas.style.textDecoration = 'underline'
                  }
                }
              }
            }
            respuestas.innerHTML = flagRespuestas.childNodes[0].nodeValue
            clon.appendChild(respuestas)
            if (this.espaciar) {
              clon.appendChild(document.createElement('P'))
            }
            valorRespuesta++
          }
        }
        document.getElementById('secondParent').appendChild(clon)
      }
      let Mensaje = document.createElement('H3')
      if (this.puntuacion === 10) {
        Mensaje.innerHTML = 'Felicidades! tu test está perfecto'
      } else {
        Mensaje.innerHTML = 'Has sacado un ' + this.puntuacion.toFixed(2) + ' sobre 10, a continuación ' +
        'puedes ver en que te has equivocado, tus respuestas están subrrayadas'
      }
      document.getElementById('secondParent').insertBefore(Mensaje, document.getElementById('secondParent').firstChild)
    },
    radio (formnode, flagRespuestas) {
      let valorRespuesta = 0
      if (flagRespuestas.nextSibling.nextSibling != null) {
        while (flagRespuestas.nextSibling.nextSibling && flagRespuestas.nextSibling.nextSibling.localName === 'option') {
          flagRespuestas = flagRespuestas.nextSibling.nextSibling
          let inputnode = document.createElement('INPUT')
          inputnode.setAttribute('type', this.tipoActual)
          inputnode.setAttribute('value', this.indice + 1 + '-' + valorRespuesta)
          inputnode.setAttribute('name', 'answer')
          if (flagRespuestas.attributes.correct.nodeValue === 'y') {
            inputnode.setAttribute('correct', 'y')
          } else {
            inputnode.setAttribute('correct', 'n')
          }
          let text = document.createElement('SPAN')
          text.innerHTML = flagRespuestas.childNodes[0].nodeValue
          text.style.marginLeft = '2%'
          formnode.appendChild(inputnode)
          formnode.appendChild(text)
          formnode.appendChild(document.createElement('BR'))
          valorRespuesta++
        }
      }
    },
    selectMultiple (formnode, flagRespuestas) {
      let valorRespuesta = 0
      let selectNode = document.createElement('SELECT')
      if (this.tipoActual === 'select multiple') {
        selectNode.setAttribute('multiple', '')
      } else {
        selectNode.setAttribute('class', 'uniSelect')
        selectNode.style.appearance = 'menulist !important'
        selectNode.style.MozAppearance = 'menulist !important'
      }
      selectNode.setAttribute('name', 'answer')
      selectNode.style.backgroundColor = '#68A6BF'
      selectNode.style.width = '80%'
      selectNode.style.whiteSpace = 'normal'
      if (flagRespuestas.nextSibling.nextSibling != null) {
        while (flagRespuestas.nextSibling.nextSibling && flagRespuestas.nextSibling.nextSibling.localName === 'option') {
          flagRespuestas = flagRespuestas.nextSibling.nextSibling
          let inputnode = document.createElement('OPTION')
          inputnode.setAttribute('value', this.indice + 1 + '-' + valorRespuesta)
          inputnode.style.backgroundColor = '#68A6BF'
          if (flagRespuestas.attributes.correct.nodeValue === 'y') {
            inputnode.setAttribute('correct', 'y')
          } else {
            inputnode.setAttribute('correct', 'n')
          }
          inputnode.setAttribute('title', flagRespuestas.childNodes[0].nodeValue)
          inputnode.innerHTML = flagRespuestas.childNodes[0].nodeValue
          inputnode.style.whiteSpace = 'normal'
          selectNode.appendChild(inputnode)
          valorRespuesta++
        }
      }
      formnode.appendChild(selectNode)
    },
    text (formnode, flagRespuestas) {
      let valorRespuesta = 0
      if (flagRespuestas.nextSibling.nextSibling != null) {
        while (flagRespuestas.nextSibling.nextSibling && flagRespuestas.nextSibling.nextSibling.localName === 'option') {
          flagRespuestas = flagRespuestas.nextSibling.nextSibling
          let inputnode = document.createElement('INPUT')
          inputnode.setAttribute('type', this.tipoActual)
          inputnode.style.marginLeft = '2%'
          inputnode.setAttribute('identificador', this.indice + 1 + '-' + valorRespuesta)
          if (valorRespuesta === 0 || valorRespuesta % 2 === 0) {
            inputnode.style.backgroundColor = '#68A6BF'
          } else {
            inputnode.style.backgroundColor = '#50bf90'
          }
          inputnode.setAttribute('name', 'answer')
          if (flagRespuestas.attributes.correct.nodeValue === 'y') {
            inputnode.setAttribute('correct', flagRespuestas.childNodes[0].nodeValue)
          } else {
            inputnode.setAttribute('correct', 'n')
          }
          let label = document.createElement('SPAN')
          label.innerText = 'Num. ' + String.fromCharCode(97 + valorRespuesta) + ':'
          formnode.appendChild(label)
          formnode.appendChild(inputnode)
          formnode.appendChild(document.createElement('BR'))
          valorRespuesta++
        }
      }
    },
    button (flagRespuestas) {
      document.getElementById('b0').style.display = 'inline-block'
      document.getElementById('b1').style.display = 'inline-block'
      document.getElementById('b0').style.backgroundColor = '#212121'
      document.getElementById('b1').style.backgroundColor = '#212121'
      this.respuestaButton.valor = ''
      let valorRespuesta = 0
      let arrayButtons = document.getElementsByClassName('resp')
      if (flagRespuestas.nextSibling.nextSibling != null) {
        for (let index = 0; index < 2; index++) {
          flagRespuestas = flagRespuestas.nextSibling.nextSibling
          arrayButtons[valorRespuesta].setAttribute('type', this.tipoActual)
          arrayButtons[valorRespuesta].setAttribute('name', 'resp')
          arrayButtons[valorRespuesta].setAttribute('valor', this.indice + 1 + '-' + valorRespuesta)
          arrayButtons[valorRespuesta].innerHTML = flagRespuestas.childNodes[0].nodeValue
          if (flagRespuestas.attributes.correct.nodeValue === 'y') {
            arrayButtons[valorRespuesta].setAttribute('correct', 'y')
          } else {
            arrayButtons[valorRespuesta].setAttribute('correct', 'n')
          }
          valorRespuesta++
        }
      }
    },
    setButtonAnswer (elboton) {
      this.respuestaButton.valor = document.getElementById('b' + elboton).attributes.valor.nodeValue
      this.respuestaButton.correct = document.getElementById('b' + elboton).attributes.correct.nodeValue
      document.getElementById('b0').style.backgroundColor = '#212121'
      document.getElementById('b1').style.backgroundColor = '#212121'
      document.getElementById('b' + elboton).style.backgroundColor = '#68A6BF'
    },
    dataList (formnode, flagRespuestas) {
      let sel = this
      let valorRespuesta = 0
      let inputnode = document.createElement('INPUT')
      inputnode.setAttribute('list', 'answers')
      inputnode.id = 'InputDL'
      inputnode.setAttribute('name', 'answer')
      inputnode.oninput = function () {
        sel.respuestaDataLits.valor = document.getElementById('InputDL').value
      }
      inputnode.style.backgroundColor = '#68A6BF'
      let datalist = document.createElement('DATALIST')
      datalist.id = 'answers'
      if (flagRespuestas.nextSibling.nextSibling != null) {
        while (flagRespuestas.nextSibling.nextSibling && flagRespuestas.nextSibling.nextSibling.localName === 'option') {
          let option = document.createElement('OPTION')
          flagRespuestas = flagRespuestas.nextSibling.nextSibling
          option.setAttribute('value', flagRespuestas.childNodes[0].nodeValue)
          option.setAttribute('class', 'datalist')
          option.setAttribute('identificador', this.indice + 1 + '-' + valorRespuesta)
          if (flagRespuestas.attributes.correct.nodeValue === 'y') {
            let valorCorrecto = flagRespuestas.childNodes[0].nodeValue
            option.setAttribute('correct', valorCorrecto)
            this.respuestaDataLits.correct = valorCorrecto
          } else {
            option.setAttribute('correct', 'n')
          }
          datalist.appendChild(option)
          valorRespuesta++
        }
      }
      inputnode.appendChild(datalist)
      formnode.appendChild(inputnode)
    },
    checkRadio () {
      let radios = document.getElementsByName('answer')
      let respuesta = ''
      let RespCorreccion = {}
      for (let i = 0, length = radios.length; i < length; i++) {
        if (radios[i].checked) {
          respuesta = radios[i].value
          RespCorreccion = {
            valor: respuesta,
            correct: radios[i].attributes.correct.nodeValue
          }
          break
        }
      }
      if (respuesta === '') {
        alert('Si no la sabes tendrás que escoger al azar')
      } else {
        this.ArrayRespuestas.push(RespCorreccion)
        this.indice++
        this.gestionarXml(this.XMLparseado)
      }
    },
    checkSelectMultiple () {
      let select = document.getElementsByName('answer')
      let respuestas = []
      let options = select[0]
      for (let i = 0, iLen = options.length; i < iLen; i++) {
        if (options[i].selected) {
          respuestas.push({
            valor: options[i].value,
            correct: options[i].attributes.correct.nodeValue
          })
        }
      }
      if (respuestas.length === 0) {
        alert('Si no la sabes tendrás que escoger al azar')
      } else {
        if (respuestas.length === 1) {
          respuestas = respuestas[0]
        }
        this.ArrayRespuestas.push(respuestas)
        this.indice++
        this.gestionarXml(this.XMLparseado)
      }
    },
    checkText () {
      let text = document.getElementsByName('answer')
      let respondidoTodas = true
      let respuestas = []
      let options = text
      for (let i = 0, iLen = options.length; i < iLen; i++) {
        if (options[i].value !== '' || options[i].textLength > 0) {
          respuestas.push({
            valor: options[i].value,
            correct: options[i].attributes.correct.nodeValue,
            identificador: options[i].attributes.identificador.nodeValue
          })
        } else {
          respondidoTodas = false
        }
      }
      if (!respondidoTodas) {
        alert('Si no los sabes tendrás que escribirlos al azar')
      } else {
        this.ArrayRespuestas.push(respuestas)
        this.indice++
        this.gestionarXml(this.XMLparseado)
      }
    },
    checkButton () {
      if (this.respuestaButton.valor === '') {
        alert('De esta tampoco te libras')
      } else {
        document.getElementById('b0').style.display = 'none'
        document.getElementById('b1').style.display = 'none'
        this.indice++
        this.ArrayRespuestas.push(Object.assign({}, this.respuestaButton))
        this.gestionarXml(this.XMLparseado)
      }
    },
    checkDataLits () {
      if (this.respuestaDataLits.valor === '') {
        alert('Inventatelo!')
      } else {
        switch (this.respuestaDataLits.valor) {
          case '%b':
            this.respuestaDataLits.identificador = '9-0'
            break
          case '%t':
            this.respuestaDataLits.identificador = '9-1'
            break
          case '%s':
            this.respuestaDataLits.identificador = '9-2'
            break
          default:
            this.respuestaDataLits.identificador = '9-2'
        }
        this.ArrayRespuestas.push(this.respuestaDataLits)
        this.indice++
        this.gestionarXml(this.XMLparseado)
      }
    }
  }
}

</script>

<style>
  #img1{
    width: 50%;
    height: 50%;
  }
  #cabecera{
    width:100%;
  }
  #cabf{
    margin-bottom: -3.5em;
  }
  .subcab{
      font-family: 'Avenir', Helvetica, Arial, serif;
      float:right;
      position:relative;
      left:0.8em;
      top:-3.5em;
      z-index: 999;
      font-weight: bold;
      color:#7D0000;
      font-size:1.2em ;
      margin-bottom: -5em;
    }

  @media only screen and (max-width: 900px) {
    .subcab{
      float:right;
      top:-3em;
      left:1em;
      z-index: 999;
      font-size:0.8em ;

    }
  }

 @media only screen and (max-width: 599px) {
  .subcab{
    float:right;
    top:-3.4em;
    left:1em;
    z-index: 999;
    font-size:0.6em ;

  }
  }
  @media only screen and (max-width: 320px) {
    .subcab{
      float:right;
      top:-3.5em;
      left:1.2em;
      z-index: 999;
      font-size:0.6em ;

    }
  }
  #tbmenu{
    background-color:#68A6BF ;
    color:white;
    margin-top:-50%;
  }
  .boton {
  font-weight: bold;
  }
  select{

    -moz-appearance: menulist !important;
    -webkit-appearance: menulist !important;
    appearance: menulist !important;
  }
  .uniSelect{

    -moz-appearance: menulist !important;
    -webkit-appearance: menulist !important;
    appearance: menulist !important;
  }
  #formulario{
    padding-top: 1.5%;
    padding-bottom: 2%;
  }
  #b0{
    display: none;
  }
  #b1{
    display: none;
  }
</style>
