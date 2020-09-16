#!/usr/bin/node
function factorial (a) {
  const num = Number(a);
  if (isNaN(num) === true | num === 1) {
    return 1;
  }
  return num * factorial(num - 1);
}
console.log(factorial(process.argv[2]));
