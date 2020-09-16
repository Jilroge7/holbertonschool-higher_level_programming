#!/usr/bin/node
const number = parseInt(process.argv[2]);
let row;
let column;
if (isNaN(number) === true) {
  console.log('Missing size');
} else {
  for (row = 1; row <= number; row++) {
    for (column = 1; column <= number; column++) {
      process.stdout.write('X');
    }
    console.log('');
  }
}
