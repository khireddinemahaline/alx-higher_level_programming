#!/usr/bin/node
const fs = require('fs');

function writeTofile (filePath, txt) {
  fs.writeFile(filePath, txt, 'utf-8', (error) => {
    if (error) {
      console.log('fiald to store text');
    } else {
      console.log('text stored successfly');
    }
  });
}

const filePath = process.argv[2];
const txt = process.argv[3];

writeTofile(filePath, txt);
