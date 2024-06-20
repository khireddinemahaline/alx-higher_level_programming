#!/usr/bin/node
exports.addMeMaybe = function (number, theFunction) {
  number = theFunction(1 + number);
};
