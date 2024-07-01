window.SnipcartSettings = {
    publicApiKey: 'OWY5M2M5YTUtMzdmYy00MGU4LWE2MTQtMDgwMjNjMGY4ZmM1NjM4NTE0MTEzODIyMzc0Mjg0',
    loadStrategy: 'on-user-interaction',
};

(()=>{var c,d;(d=(c=window.SnipcartSettings).version)!=null||(c.version="3.0");var s,S;(S=(s=window.SnipcartSettings).timeoutDuration)!=null||(s.timeoutDuration=2750);var l,p;(p=(l=window.SnipcartSettings).domain)!=null||(l.domain="cdn.snipcart.com");var w,u;(u=(w=window.SnipcartSettings).protocol)!=null||(w.protocol="https");var f=window.SnipcartSettings.version.includes("v3.0.0-ci")||window.SnipcartSettings.version!="3.0"&&window.SnipcartSettings.version.localeCompare("3.4.0",void 0,{numeric:!0,sensitivity:"base"})===-1,m=["focus","mouseover","touchmove","scroll","keydown"];window.LoadSnipcart=o;document.readyState==="loading"?document.addEventListener("DOMContentLoaded",r):r();function r(){window.SnipcartSettings.loadStrategy?window.SnipcartSettings.loadStrategy==="on-user-interaction"&&(m.forEach(t=>document.addEventListener(t,o)),setTimeout(o,window.SnipcartSettings.timeoutDuration)):o()}var a=!1;function o(){if(a)return;a=!0;let t=document.getElementsByTagName("head")[0],e=document.querySelector("#snipcart"),i=document.querySelector(`src[src^="${window.SnipcartSettings.protocol}://${window.SnipcartSettings.domain}"][src$="snipcart.js"]`),n=document.querySelector(`link[href^="${window.SnipcartSettings.protocol}://${window.SnipcartSettings.domain}"][href$="snipcart.css"]`);e||(e=document.createElement("div"),e.id="snipcart",e.setAttribute("hidden","true"),document.body.appendChild(e)),v(e),i||(i=document.createElement("script"),i.src=`${window.SnipcartSettings.protocol}://${window.SnipcartSettings.domain}/themes/v${window.SnipcartSettings.version}/default/snipcart.js`,i.async=!0,t.appendChild(i)),n||(n=document.createElement("link"),n.rel="stylesheet",n.type="text/css",n.href=`${window.SnipcartSettings.protocol}://${window.SnipcartSettings.domain}/themes/v${window.SnipcartSettings.version}/default/snipcart.css`,t.prepend(n)),m.forEach(g=>document.removeEventListener(g,o))}function v(t){!f||(t.dataset.apiKey=window.SnipcartSettings.publicApiKey,window.SnipcartSettings.addProductBehavior&&(t.dataset.configAddProductBehavior=window.SnipcartSettings.addProductBehavior),window.SnipcartSettings.modalStyle&&(t.dataset.configModalStyle=window.SnipcartSettings.modalStyle),window.SnipcartSettings.currency&&(t.dataset.currency=window.SnipcartSettings.currency),window.SnipcartSettings.templatesUrl&&(t.dataset.templatesUrl=window.SnipcartSettings.templatesUrl))}})();

mapboxgl.accessToken = 'pk.eyJ1IjoiYW1hcnV3dSIsImEiOiJjbHc4aHdjaTIyZzYzMmlxdXFiMTV6N3dxIn0.SIuL5ZdI7cYQA48Q0TsGpQ';
var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v11',
    center: [-70.65801129916083, -33.44696738306632],
    zoom: 17
});


// Crear marcador 2
var marker1 = new mapboxgl.Marker()
    .setPopup(new mapboxgl.Popup().setHTML("<h3>Achoclonados</h3>")) // Contenido HTML del marcador
    .setLngLat([-70.65807298993697, -33.44681575671561]) // Coordenadas del marcador 2 (Longitud, Latitud)
    .addTo(map); // Agregar el marcador al mapa

// Crear marcador 2
var marker2 = new mapboxgl.Marker()
    .setPopup(new mapboxgl.Popup().setHTML("<h3>Relativo</h3>")) // Contenido HTML del marcador
    .setLngLat([-70.65355994534544, -33.44724370910515]) // Coordenadas del marcador 2 (Longitud, Latitud)
    .addTo(map); // Agregar el marcador al mapa


 // Script para prellenar datos al abrir el modal de editar producto
 $(document).ready(function() {
    $('.btn-editar-producto').click(function() {
        var productoId = $(this).data('id');
        var nombre = $(this).data('nombre');
        var precio = $(this).data('precio');

        $('#producto_id').val(productoId);
        $('#id_nombre').val(nombre);
        $('#id_precio').val(precio);
    });
});

// Script para configurar el modal de eliminar producto
$(document).ready(function() {
    $('.btn-eliminar-producto').click(function() {
        var productoId = $(this).data('id');
        var formAction = '{% url "eliminar_producto" 0 %}'.replace('0', productoId);
        $('#formEliminarProducto').attr('action', formAction);
    });
});