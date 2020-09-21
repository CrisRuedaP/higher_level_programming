#!/usr/bin/node
const Square = require('./5-square.js');
class SquareChildren extends Square {
  charPrint (c) {
    if (c === undefined) {
      this.print(c);
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log('c'.repeat(this.width));
      }
    }
  }
}

module.exports = SquareChildren;
