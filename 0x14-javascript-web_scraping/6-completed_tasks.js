#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, result, body) {
  if (error) return;
  const doList = JSON.parse(body);
  const dct = {};
  for (let ct = 0; ct < doList.length; ct++) {
    if (dct[doList[ct].userId] === undefined) {
      if (doList[ct].completed === true) {
        dct[doList[ct].userId] = 1;
      }
    } else {
      if (doList[ct].completed === true) {
        dct[doList[ct].userId] += 1;
      }
    }
  }
  console.log(dct);
});
