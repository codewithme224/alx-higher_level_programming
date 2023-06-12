#!/usr/bin/node
const myNum = process.argv.slice(2);
if (isNaN(myNum[0])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(myNum[0]));
}
