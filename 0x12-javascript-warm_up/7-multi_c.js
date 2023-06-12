#!/usr/bin/node
const x = process.argv.slice(2);
if (isNaN(x[0])) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x[0]; i++) {
    console.log('C is fun');
  }
}
