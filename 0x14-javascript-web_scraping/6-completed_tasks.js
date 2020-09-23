#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, result, body) {
  console.log(JSON.parse(body));
  if (error) {
  }
});
