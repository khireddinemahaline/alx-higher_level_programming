#!/usr/bin/node
exports.callMeMoby = function (n, app) {
  let i = 0;
  for (i; i < n; i++) {
    app();
  }
};
