#!/usr/bin/node

const request = require('request');
if (!process.argv || process.argv.length < 3) {
  console.log('Missing arguments');
  process.exit(1);
}
request(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const results = JSON.parse(body);
    const completed = {};
    for (let i = 0; i < results.length; i++) {
      if (results[i].completed) {
        if (completed[results[i].userId]) {
          completed[results[i].userId]++;
        } else {
          completed[results[i].userId] = 1;
        }
      }
    }
    console.log(completed);
  }
}
);
