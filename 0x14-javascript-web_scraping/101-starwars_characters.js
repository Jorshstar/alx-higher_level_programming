#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

const apiUrl = 'https://swapi-api.hbtn.io/api/films/' + movieId + '/';
const characters = [];

function getCharacterName(characterUrl) {
  return new Promise((resolve, reject) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const character = JSON.parse(body);
        resolve(character.name);
      }
    });
  });
}

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const movie = JSON.parse(body);
    const promises = movie.characters.map((characterUrl) => {
      return getCharacterName(characterUrl);
    });
    Promise.all(promises)
      .then((names) => {
        console.log(names.join('\n'));
      })
      .catch((error) => {
        console.error(error);
      });
  }
});
