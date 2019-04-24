document.addEventListener("DOMContentLoaded", function(event) {

    var map = L.map('map').setView([44.977753, -93.265015], 16);
    
    L.tileLayer('https://api.mapbox.com/styles/v1/mwiltzius/cjuucw1uo1qpo1frs2vldzv8r/tiles/256/{z}/{x}/{y}@2x?access_token={accessToken}', {
        maxZoom: 18,
        id: 'mapbox.streets',
        accessToken: 'pk.eyJ1IjoibXdpbHR6aXVzIiwiYSI6ImNqdXVjZTFjazBoYzY0M243OTZ1ZWx6YWMifQ.7iYMruXZbUR_2DWQpULrMg'
    }).addTo(map);

})