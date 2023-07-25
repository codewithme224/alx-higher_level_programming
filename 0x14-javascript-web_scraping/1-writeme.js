#!/usr/bin/node

const fs = require('fs');
if (!process.argv || process.argv.length < 3) {
  console.log('Missing arguments');
  process.exit(1);
}
fs.writeFile(process.argv[2], process.argv[3], 'utf-8', function (err, result) {
  if (err) {
    console.log(err);
  }
}
);
