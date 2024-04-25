#!/usr/bin/node
let indx = 0;
exports.logMe = function (item) {
  console.log(indx, ':', item);
  indx = indx + 1;
};
