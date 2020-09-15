#!/usr/bin/node
if (process.argv.length === 2) {
  const statement = 'No Argument';
  console.log(statement);
} else if (process.argv.length === 3) {
  const statement = 'Argument found';
  console.log(statement);
} else {
  const statement = 'Arguments found';
  console.log(statement);
}
