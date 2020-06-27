mymap = L.map('mapid').setView([43.8908662,-79.45511119999999], 13);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoiZGFuaWVscTk4NyIsImEiOiJja2J5MHVib2wwZzVrMnlwa3ZvcXFuZnpnIn0.0vmp6qcttBGbXK8QWXcfbw', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoiZGFuaWVscTk4NyIsImEiOiJja2J5MHVib2wwZzVrMnlwa3ZvcXFuZnpnIn0.0vmp6qcttBGbXK8QWXcfbw'
}).addTo(mymap);