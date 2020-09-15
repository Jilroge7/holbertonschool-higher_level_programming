#!/usr/bin/node
let arg1 = process.argv[2];
const arg2 = process.argv[3];
try {
  console.log(arg1.concat(' is ', arg2));
} catch (e) {
  arg1 = 'undefined';
  console.log(arg1.concat(' is ', arg2));
}
