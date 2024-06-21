#!/usr/bin/node
var list = require('./100-main.js').list;
console.log(list);
console.log(list.map((x, index) => x * index));