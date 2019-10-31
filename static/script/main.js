"use strict";

window.onload = main;

function main() {

	let app = new Application();
	app.log("Hello, world!");

	let socket = io.connect('http://' + document.domain + ':' + location.port + '/');

	let button = document.querySelector('#the-button');
	button.addEventListener('click', function(e) {
		let url = '/';

		socket.emit('clicked', {});

		// app.request(url, function(res, err) {
		// 	let count = res;
		// 	updateCountLabel(count);
		// });
	});

	// button.addEventListener('touchstart', function(e) {
	// 	let label = document.querySelector('#count');
	// 	label.innerHTML = "TOUCHED";
	// });

	socket.on('connection', function(msg) {
		console.log("Socket connected.");
	});

	socket.on('count update', function(msg) {
		let count = msg['count'];
		updateCountLabel(count);
	});

	// Emit

	// Broadcast

}

function updateCountLabel(value) {
	let label = document.querySelector('#count');
	label.innerHTML = "" + value;
}