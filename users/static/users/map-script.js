var map;
var markers = [];

function initialize() {
	/*
	var center = new google.maps.LatLng(ParseFloat('{{location_list[0].latitude}}'),ParseFloat('{{location_list[0].latitude}}'));
	*/

	var center = new google.maps.LatLng(34.0594,-118.2459)
	console.log('var center set');

	/*var listLength = ParseInt('{{location_list|length}}');*/

	console.log('var listLength set');

	mapOptions = {
		zoom:12,
		center:center
	};

	var map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

	console.log('var map set');
	/*
	{% for location in location_list %}
		position = new google.maps.LatLng(ParseFloat('{{location.latitude}}'),ParseFloat('{{location.longitude}}'));

		addMarker(position);
	{% endfor %}

	console.log('location markers set');
	*/
}

function addMarker(position) {
	// adds a new marker and pushes it to the array
	var marker = new google.maps.Marker({
		position: position,
		map: map,
	});
	markers.push(marker);
}

google.maps.event.addDomListener(window, 'load', initialize);