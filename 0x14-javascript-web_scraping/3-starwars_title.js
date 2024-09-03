#!/usr/bin/node
const { error } = require('console');
const request = require('request')

function filmTitle (episodeId) {
  const url = `https://swapi-api.alx-tools.com/api/films/${episodeId}/`; // Construct the URL
  request(url, (error, Response, body)=> {
    if (error){
        console.log(error)
    } else {
        const data = JSON.parse(body);
        console.log(data.title);
    }
  })
}

const episodeId = process.argv[2];
filmTitle(episodeId);
