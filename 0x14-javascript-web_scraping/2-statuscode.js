#!/usr/bin/node

const request = require('request');
if (!process.argv || process.argv.length < 3) {
  console.log('Missing arguments');
  process.exit(1);
}
request(process.argv[2], function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
}
);
