#!/usr/bin/node

const request = require('request');
const fs = require('fs');
if (!process.argv || process.argv.length < 4) {
  console.log('Missing arguments');
  process.exit(1);
}
request(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(process.argv[3], body, 'utf-8', function (err, result) {
      if (err) {
        console.log(err);
      }
    }
    );
  }
}
);
