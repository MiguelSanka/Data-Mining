console.log("Hola mundo");

//Declaración de variables
var total = 0; //monto + lo que sumas

var boton = document.getElementById("calcularBtn");
var montoInput = document.getElementById("montoInput");
var monto = montoInput.value
var parrafoTotal = document.getElementById("parrafoTotal");

var totalMsg = parrafoTotal.innerText;

var lista = document.getElementById("lista");
var descripcionInput = document.getElementById("descripcionInput");
var descripcion = document.getElementById("descripcion");

var elemento = document.getElementById
//Declaración de funciones
function imprimirMonto()
{
    monto = parseInt(montoInput.value);
    console.log(monto);
}

function mensajeClick()
{
    alert("hiciste clic en del boton")
    //console.log("hiciste click en el boton");
}

function calcularMonto()
{
    monto = parseInt(montoInput.value)
    total = total + monto;

    //forma 1
    totalMsg = "Total " + total;
    parrafoTotal.innerText = totalMsg;

    //forma 2
    //parrafoTotal.innerText = "Total: " + total;
}