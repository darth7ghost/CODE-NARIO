console.log("ci")
//Respuestas correctas
let correctas = [1,2,2,3,1,3,2,2,3,1];
//Respuestas del usuario
let opcion_elegida = [];

let cantidad_correctas = 0;

const navToggle = document.querySelector(".nav-toggle");
const links = document.querySelector(".links");

navToggle.addEventListener("click", function () {
  links.classList.toggle("show-links");
});

//Funcion que toma el num. de pregunta y el input elegido de esa pregunta
function respuesta(num_pregunta, seleccionada){
  //Se guarda la respuesta elegida
  opcion_elegida[num_pregunta] = seleccionada.value;
  //Colorear los otros inputs al seleccionar una opcion
  //Seleccionar el section correspondiente
  id="p"+num_pregunta;
  labels = document.getElementById(id).childNodes;
  labels[3].style.backgroundColor = "#021631";
  labels[5].style.backgroundColor = "#021631";
  labels[7].style.backgroundColor = "#021631";

  //Color al label seleccionado
  seleccionada.parentNode.style.backgroundColor = "#2C74B3"
}

