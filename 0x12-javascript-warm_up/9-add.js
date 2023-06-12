#!/usr/bin/node
function addAndParseArgs (a, b) {
  const parseArgToNumber = arg => Number(arg);
  const parsedArg1 = parseArgToNumber(a);
  const parsedArg2 = parseArgToNumber(b);
  return parsedArg1 + parsedArg2;
}

console.log(addAndParseArgs(process.argv[2], process.argv[3]));
