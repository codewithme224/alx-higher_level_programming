#!/usr/bin/node
const argument = process.argv.slice(2);
if (argument.length <= 1) {
  console.log(0);
} else {
  argument.sort(function (a, b) { return a - b; });
  console.log(argument[argument.length - 2]);
}
