#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = https://swapi.dev/api/films/${movieId}/;

request(url, function (error, response, body) {
if (error) {
console.log(error);
} else {
const characters = JSON.parse(body).characters;
characters.forEach((characterUrl) => {
request(characterUrl, function (error, response, body) {
if (error) {
console.log(error);
} else {
const name = JSON.parse(body).name;
console.log(name);
}
});
});
}
});
