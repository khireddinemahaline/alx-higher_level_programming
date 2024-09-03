#!/usr/bin/node

async function statusCode (url) {
  const request = new Request(url);
  const response = await fetch(request);

  const object = await response.text();

  if (object === 'OK') {
    console.log('code: 200');
  } else {
    console.log('code: 404');
  }
}

const url = process.argv[2];
statusCode(url);
