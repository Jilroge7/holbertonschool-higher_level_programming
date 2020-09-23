#!/usr/bin/node
const request = require('request');
const reqUrl = process.argv[2];
request(reqUrl, function (error, result, body) {
  if (error) return;
  const allFilms = JSON.parse(body).results;
  let chrcount = 0;
  for (let ct = 0; ct < allFilms.length; ct++) {
    for (let chr = 0; chr < allFilms[ct].characters.length; chr++) {
      if (allFilms[ct].characters[chr].includes('18')) {
        chrcount++;
      }
    }
  }
  console.log(chrcount);
});
