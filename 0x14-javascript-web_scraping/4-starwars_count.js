#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('API URL is required');
  process.exit(1);
}

let count = 0;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error(`Unexpected status code: ${response.statusCode}`);
    process.exit(1);
  }

  const movies = JSON.parse(body).results;

  for (let movie of movies) {
    if (movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      count++;
    }
  }

  console.log(count);
});
