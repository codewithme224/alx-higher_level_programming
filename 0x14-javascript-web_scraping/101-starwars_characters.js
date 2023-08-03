#!/usr/bin/node

const request = require('request');
if (!process.argv || process.argv.length < 3) {
  console.log('Missing arguments');
  process.exit(1);
}
request('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const characters = JSON.parse(body).characters;
    printNames(characters, 0);
  }
}
);

function printNames (characters, index) {
  if (index >= characters.length) {
    return;
  }
  request(characters[index], function (err, response, body) {
    if (err) {
      console.log(err);
    } else {
      console.log(JSON.parse(body).name);
      printNames(characters, index + 1);
    }
  }
  );
}
