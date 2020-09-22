#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId;
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const info = JSON.parse(body);
  for (const character of info.characters) {
    request(character, function (error, response, body) {
      const info = JSON.parse(body);
      if (error) {
        console.log(error);
      } else {
        console.log(info.name);
      }
    });
  }
});
