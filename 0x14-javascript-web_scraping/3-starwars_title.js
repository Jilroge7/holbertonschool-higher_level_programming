#!/usr/bin/node
const request = require('request');
const reqUrl = 'https://swapi-api.hbtn.io/api/films/';
const id = process.argv[2];
request(reqUrl + id, function (error, result, body) {
  console.log(JSON.parse(body).title);
  if (error) {
  }
});
