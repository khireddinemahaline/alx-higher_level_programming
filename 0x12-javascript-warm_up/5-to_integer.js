#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log(parseInt('My number:', process.argv[2]));
}
