$("#formulario1").validate({
    rules: {
        "txtJefe": {
            required: true,
            minlength: 3
        },
        "txtActivable": {
            required: true,
            minlength: 3
        },
        "txtObjeto": {
            required: true,
            minlength: 3
        },
    }, // --> Fin de reglas
    messages: {
        "txtJefe": {
            required: 'Ingrese Jefe',
            minlength: 'Min. 3 caract'
        },
        "txtActivable": {
            required: 'Ingrese Activable',
            minlength: 'Min. 3 caract'
        },
        "txtObjeto": {
            required: 'Ingrese Objeto',
            minlength: 'Min. 3 caract'
        },
    } //-->Fin de mensajes

});


$(document).ready(function() {
    $("#btn-registrar").click(function(e) {
      e.preventDefault();
      if ($("#formulario1").valid()) {
        window.location.href = "{% url 'home' %}";
      }
    });
  });