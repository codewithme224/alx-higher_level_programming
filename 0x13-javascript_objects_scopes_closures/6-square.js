#!/usr/bin/node
const SquareOld = require('./5-square');
class Square extends SquareOld {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    const row = c.repeat(this.width);
    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }
}
module.exports = Square;
