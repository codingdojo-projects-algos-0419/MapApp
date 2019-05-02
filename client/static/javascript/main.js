document.addEventListener("DOMContentLoaded", function(event) {

    var map = L.map('map').setView([44.977753, -93.265015], 16);
    
    L.tileLayer('https://api.mapbox.com/styles/v1/mwiltzius/cjuucw1uo1qpo1frs2vldzv8r/tiles/256/{z}/{x}/{y}@2x?access_token={accessToken}', {
        maxZoom: 18,
        id: 'mapbox.streets',
        accessToken: 'pk.eyJ1IjoibXdpbHR6aXVzIiwiYSI6ImNqdXVjZTFjazBoYzY0M243OTZ1ZWx6YWMifQ.7iYMruXZbUR_2DWQpULrMg'
    }).addTo(map);

    // L.Routing.control({
    //     waypoints: [
    //         L.latLng(57.75, 11.94),
    //         L.latLng(57.6792,11.949)
    //     ]
    // }).addTo(map)

    startLat = 54.75
    startLong = 11.94

    L.Routing.control({
        // waypoints: [
        //             L.latLng(startLat, startLong),
        //             L.latLng(57.6792,11.949)
        //         ],
        // router: L.Routing.mapbox('pk.eyJ1IjoibXdpbHR6aXVzIiwiYSI6ImNqdXVjZTFjazBoYzY0M243OTZ1ZWx6YWMifQ.7iYMruXZbUR_2DWQpULrMg')
        geocoder: L.Control.Geocoder.nominatim()
    }).addTo(map);

    $('.leaflet-routing-geocoder:nth-child(2)').after('<p class="adder">Add to My Destinations</p>')

    $('.adder').on('click', function(){
        var destination = $(this).prev().children('input')
        destination.attr('name', 'destination')
        if (destination.val()) {
            
            $.ajax({
                url: '/add_destination',
                method: 'POST',
                data: destination.serialize()
            })

        }
    })

})