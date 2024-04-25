#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let s = '';
      for (let j = 0; j < this.width; j++) {
        s += 'X';
      }
      console.log(s);
    }
  }

  rotate (ele) {
    this.ele = ele;
    this.ele = this.height;
    this.height = this.width;
    this.width = this.ele;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
};
