const WebSocket = require('ws');
const fs = require('fs');

var ws = new WebSocket('wss://gateway.discord.gg/?v=6&encoding=json');
const token = fs.readFileSync('token.txt', 'utf8').replace(/(\r\n|\r|\n)/g, '');

payload = {
  op: 2,
  d: {
    token: token,
    intents: 512,
    properties: {
      $os: 'linux',
      $browser: 'other',
      $device: 'pc',
    },
  },
};

ws.addEventListener('open', function open(x) {
  ws.send(JSON.stringify(payload));
});

ws.addEventListener('message', function incoming(data) {
  var x = data.data;
  var payload = JSON.parse(x);

  const { t, event, op, d } = payload;

  switch (op) {
    // OPCODE 10 GIVES the HEARTBEAT INTERVAL, SO YOU CAN KEEP THE CONNECTION ALIVE
    case 10:
      const { heartbeat_interval } = d;
      setInterval(() => {
        ws.send(JSON.stringify({ op: 2, d: null }));
      }, heartbeat_interval);

      break;
  }

  switch (t) {
    // IF MESSAGE IS CREATED, IT WILL LOG IN THE CONSOLE
    case 'MESSAGE_CREATE':
      console.log(d.author.username + ': ' + d.content);
  }
});
