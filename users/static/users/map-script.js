var map;
var location;
var service;
var losangeles = new google.maps.LatLng(34.0576,-118.2508);
var browserSupportFlag = new Boolean();
var markers = [];

function initialize() {
	// load map, load click listener
	mapOptions = {
		zoom:12,
	};

	var map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

	// Try W3C Geolocation
	if (navigator.geolocation) {
		browserSupportFlag = True;
		navigator.geolocation.getCurrentPosition(function(position) {
			location = new google.maps.LatLng(position.coords.latitude,position.coords.longitude);
			map.setCenter(location);
			addMarker(location);
		}, function() {
			browserSupportFlag = false;
			handleNoGeolocation(browserSupportFlag);
		});
	}

	google.maps.event.addListener(map, 'click', loadClick(event));
	
}

function loadClick(event) {
	// clear map if needed
	if (markers != []) {
		setAllMap(null);
	}
	// create new marker
	addMarker(event.latLng);
	// render marker on map
	setAllMap(map);
	// update form
	var name = getName(event.latLng)
	var form = '
		{% csrf_token %}
		<p><input id="id_name" maxlength="70" name="name" type="text" value="'
		+ name +'" readonly /></p>
		<p><select id="id_user" name="user" style="display:none">
		<option value="{{request.user.id}}" selected="selected">{{request.user}}</option>
		</select></p>
		<p><input id="id_longitude" name="longitude" step="0.0001" type="number" value="'
		+ event.latLng.lng() + '" readonly /></p>
		<p><input id="id_latitude" name="latitude" step="0.0001" type="number" value="'
		+ event.latLng.lat() + '"/></p>
		<p><textarea id="id_custDescription" maxlength="500" name="custDescription" readonly />
			</textarea></p>
		<p><input type=submit value="Save this place!">
	'
	$("#autoadd").html(form)
}


function addMarker(position) {
	// adds a new marker and pushes it to the array
	var marker = new google.maps.Marker({
		position: position,
		map: map,
	});
	markers.push(marker);
}

function setMapAll(map) {
	// sets all markers to specified map (null/map)
	for (var i=0; i <= markers.length; i++) {
		markers[i].setMap(map);
		infoWindows[i].setMap(map);
	};
}

function getName(position) {
	// initiates a place search from given position
	var topName;
	var service = new google.maps.places.PlacesService(map);
	var request = {
		location:position,
		radius:100,
		type: [
			amusement_park,aquarium,art_gallery,bakery,bar,beauty_salon,
			book_store,bowling_alley,bus_station,cafe,campground,casino,
			cemetery,city_hall,clothing_store,convenience_store,
			department_store,museum,night_club,park,parking,pet_store,
			restaurant,rv_park,school,shoe_store,shopping_mall,spa,
			stadium,store,subway_station,train_station,university,zoo,
			establishment,florist,food,gas_station,jewelery_store,library,
			lodging,movie_theater
		]
	};
	service.radarSearch(request,function(results, status){
		// radar search callback
		if (status === google.maps.places.PlacesServiceStatus.OK) {
		    var topName = results[0].name;
		} else if (status === google.maps.places.PlacesServiceStatus.ZERO_RESULTS) {
			var topName = "Unknown";
		} else {
			alert(status);
			return;
		}
	});
	return topName;
}

function handleNoGeolocation(errorFlag) {
		// display error alert about geolocation service and
		// sets default location to LA
		if (errorFlag === true) {
			alert("Geolocation service failed.");
		} else {
			alert("Your browser doesn't support geolocation.");
		}
		location = losangeles;
		map.setCenter(location);
	}

google.maps.event.addDomListener(window, 'load', initialize);