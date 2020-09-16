#!/usr/bin/node
add();
function add (a, b) {
  const first = parseInt(process.argv[2]);
  const second = parseInt(process.argv[3]);
  if (second) {
    console.log(first + second);
  } else {
    console.log('NaN');
  }
}
add(process.argv[2], process.argv[3]);
