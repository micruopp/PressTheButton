"use strict";

function Application() {

	this.name = "Untitled";

}

Application.prototype.log = function(message) {
	console.log("[Space " + this.name + "]: " + message);
};

Application.prototype.request = function(url, callback) {

	let self = this;

	let xhr = new XMLHttpRequest();

	let method = 'POST';
	let type = 'json';
	let request = JSON.stringify({});

	xhr.onreadystatechange = function() {
		if (xhr.readyState == 4 && xhr.status == 200) {

			let res = xhr.response;

			let count = res.count;
			callback(count);

		}
	}

	xhr.responseType = type;
	xhr.open(method, url);
	xhr.setRequestHeader('Content-type', 'application/json; charset=utf-8');

	xhr.send(request);

};
