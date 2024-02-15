#!/usr/bin/node
// Import the request module
const request = require('request');

// Get the movie ID from the command-line arguments
const movieId = process.argv[2];

// Construct the URL for the API request
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

// Make a request to the Star Wars API to get the film data
request(url, function (error, response, body) {
  if (error) {
    // If there's an error, log it
    console.error('error:', error);
  } else {
    // Parse the response body to get the list of character URLs
    const characters = JSON.parse(body).characters;
    // Start printing character names, beginning with the first character
    printCharacters(characters, 0);
  }
});

// Function to print character names
function printCharacters (characters, i) {
  // Make a request to the Star Wars API to get a character's data
  request(characters[i], function (error, response, body) {
    if (error) {
      // If there's an error, log it
      console.error('error:', error);
    } else {
      // Print the character's name
      console.log(JSON.parse(body).name);
      // If there are more characters, print the next one
      if (i + 1 < characters.length) {
        printCharacters(characters, i + 1);
      }
    }
  });
}
