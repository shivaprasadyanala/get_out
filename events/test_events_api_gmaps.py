<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nearby Places</title>
    <style>
        #map { height: 500px; width: 100%; }
        #places-list { margin-top: 20px; }
    </style>
    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBw-y5vYKpbFjeYIOcahr_NgzHPDN4Oppk&libraries=places&callback=initMap" async defer></script>
</head>
<body>
    <h1>Nearby Restaurants & Activities in Cologne</h1>
    <div id="map"></div>

    <!-- Display the places in a list -->
    <div id="places-list"></div>

    <script>
        function initMap() {
            const cologneLatLng = { lat: 50.9375, lng: 6.9603 }; // Coordinates for Cologne, Germany
            const map = new google.maps.Map(document.getElementById("map"), {
                center: cologneLatLng,
                zoom: 14
            });

            // Fetch nearby places in Cologne (restaurants, tourist attractions)
            fetchNearbyPlaces(cologneLatLng);
        }

        // Fetch nearby places in Cologne and process the JSON data
        function fetchNearbyPlaces(location) {
            const apiKey = 'YOUR_API_KEY';  // Replace with your API key
            const radius = 1500; // 1.5 km radius
            const type = 'restaurant|tourist_attraction'; // Searching for restaurants and tourist attractions
            const url = https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=${location.lat},${location.lng}&radius=${radius}&type=${type}&key=${apiKey};

            // Fetch data from Google Places API
            fetch(url)
                .then(response => response.json())
                .then(data => {
                    if (data.status === 'OK') {
                        displayPlacesOnMap(data.results);
                        displayPlacesList(data.results);
                    } else {
                        console.error('Places API Error:', data.status);
                    }
                })
                .catch(error => console.error('Error fetching places:', error));
        }

        // Display places on the map
        function displayPlacesOnMap(places) {
            places.forEach(place => {
                new google.maps.Marker({
                    position: place.geometry.location,
                    map: map,
                    title: place.name
                });
            });
        }

        // Display places in a list (JSON format)
        function displayPlacesList(places) {
            const placesListContainer = document.getElementById('places-list');
            placesListContainer.innerHTML = '';  // Clear previous list

            const list = document.createElement('ul');
            places.forEach(place => {
                const listItem = document.createElement('li');
                listItem.innerHTML = <strong>${place.name}</strong><br/>${place.vicinity}<br/><br/>;
                list.appendChild(listItem);
            });

            placesListContainer.appendChild(list);
        }
    </script>
</body>
</html>