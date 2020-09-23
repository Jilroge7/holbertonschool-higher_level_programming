#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];
request(url, function (error, result, body) {
  fs.writeFile(file, body, (error) => {
    if (error) {
    }
  });
  if (error) {
  }
});
