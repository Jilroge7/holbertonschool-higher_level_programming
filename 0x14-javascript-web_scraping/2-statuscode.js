#!/usr/bin/node
const request = require('request');
const requestUrl = process.argv[2];
request(requestUrl, function (error, result, body) {
  console.log('code: ' + result.statusCode);
  if (error) {
  }
});
