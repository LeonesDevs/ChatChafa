#!/usr/bin/bash

sudo ufw allow 8080/tcp
sudo ufw allow 8765/tcp

#	Start HTTP server in background
python3 server.py &
HTTP_PID=$!

echo "HTTP Server started with PID $HTTP_PID"

cleanup(){
	echo
	echo "Stopping ChatChafa..."

	kill "$HTTP_PID" 2>/dev/null

	sudo ufw delete allow 8080/tcp
	sudo ufw delete allow 8765/tcp

	echo "ChatChafa stopped"
}

trap cleanup EXIT INT TERM

#	Start Websocket server in foreground
python3 websocket_server.py
