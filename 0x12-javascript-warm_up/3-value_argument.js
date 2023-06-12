#!/usr/bin/node
const argument = process.argv[2];
const result = typeof argument === 'undefined' ? 'No argument' : argument;
console.log(result);
