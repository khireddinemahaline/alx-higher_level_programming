#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  let i = 0;
  let j = 0;
  x = parseInt(process.argv[2]);
  while (i < x) {
    console.log('x'.repeat(x));
    i++;
  }  
}
