$("#btnInformacion").click(function (event) {
  event.preventDefault();
  var indicador = $("#txtIndicador").val();

// Validar si el indicador contiene al menos una letra en mayúscula.
if(/[A-Z]/.test(indicador)) {
  $("#info").html("<p class='error-mensaje'>El nombre del Pokemon debe estar en minúsculas.</p>");
  return;
}

$.ajax({
  url: "https://pokeapi.co/api/v2/pokemon/" + indicador,
  data: {
    format: "json",
  },
  error: function () {
    $("#info").html("<p class='error-mensaje'>Pokemon no encontrado!!!!</p>");
  },
  dataType: "json",
  success: function (data) {
    console.log(data);
      console.log(data);
      var $nombre_pokemon = data.name;
      var $imagen_pokemon = data.sprites.other["official-artwork"].front_default;
      var $tipos_pokemon = data.types.map(function (tipo) { return tipo.type.name; }).join(", ");
      // console.log($fecha)
      $("#info").empty();
      $("#info")
        .append($nombre_pokemon + "<br>")
        .append("<img src='" + $imagen_pokemon + "' alt='" + $nombre_pokemon + "'>")
        .append("<p>Tipo: " + $tipos_pokemon + "</p>");
    },
    type: "GET",
  });
});

$("#btnLimpiar").click(function (event) {
  event.preventDefault();
  $("#info").empty();
});