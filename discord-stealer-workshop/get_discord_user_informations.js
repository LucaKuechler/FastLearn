const fs = require('fs');

const API_ENDPOINT = 'https://discord.com/api/v9/users/@me';

const TOKEN = "<TOKEN>"

const headers = {
  Authorization: `${TOKEN}`,
  'Content-Type': 'application/json',
};

fetch(API_ENDPOINT, { method: 'GET', headers })
  .then((response) => {
    if (response.ok) {
      return response.json();
    } else {
      throw new Error(`Request failed with status: ${response.status}`);
    }
  })
  .then((data) => {
    console.log('User Info:', data);
  })
  .catch((error) => {
    console.error('Error:', error);
  });
