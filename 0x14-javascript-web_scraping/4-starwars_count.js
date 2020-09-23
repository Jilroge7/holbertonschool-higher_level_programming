#!/usr/bin/node
const request = require('request');
const reqUrl = 'https://swapi-api.hbtn.io/api/films';
request(reqUrl, function (error, result, body) {
  const allFilms = JSON.parse(body);
  const reg = new RegExp(allFilms, 'g');
  const character = reg.exec('/people/18/');
  let count;
  for (count = 0; count < character.length; count++) {
  }
  console.log(count);
  if (error) {
  }
});
