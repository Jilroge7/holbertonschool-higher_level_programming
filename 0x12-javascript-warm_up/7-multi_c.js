#!/usr/bin/node
const number = parseInt(process.argv[2]);
let count;
if (isNaN(number) === true) {
  console.log('Missing number of occurences');
} else {
  for (count = 0; count < number; count++) {
    console.log('C is fun');
  }
}
