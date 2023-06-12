#!/usr/bin/node
const size = process.argv.slice(2);
if (isNaN(size[0])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size[0]; i++) {
    console.log('X'.repeat(size[0]));
  }
}
