#!/usr/bin/node

const fs = require('fs');

function read (filePath) {
  fs.readFile(filePath, 'utf-8', (error, data) => {
    if (error) {
      console.log('Error: ', error);
    } else {
      console.log(data);
    }
  });
}

const filePath = process.argv[2];

if (!filePath) {
  console.log('Usage: node script.js <filePath>');
} else {
  read(filePath);
}
