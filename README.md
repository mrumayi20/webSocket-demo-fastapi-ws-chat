# webSocket demo : fastapi-ws-chat

I build a server that manages multiple active connections and broadcasts any incoming message to everyone currently "plugged in."

## Theory about web sockets

What is web socket? <br>
-> WebSocket is a persistent connection between a client and a server. i.e. once the connection between client and server is established then they can send data to each other anytime. The server doesn't have to wait for a client's request to send data and the client doesn't have to wait for a new connection to send data to server. <br>

WebSockets are generally used to build real time systems like trading apps and messaging apps. <br>

How HTTP Work?<br>
-> So client sends a request to server (we establish a TCP connection) and then server sends response to the client(TCP connection close). In this way one request response cycle is completed. <br>

Now when client wants to ask something again, we establish this request and response cycle again. HTTP is a unidirectional, half duples(either client or server can send dtaa at a time) and stateless protocol. <br>

How web sockets work?<br>
->Web Sockets are a way to create bidirectional, stateful, fullduplex connection, Imagine it as a phone call, where client and server can talk anytime once the connection is established. <br>

To establish a web socket connection, first a client sends a an HTTP handshake request with an upgrade header(meaning client tells sever that now we are talking over HTTP but let's upgrade to WebSocket). And if server agrees then it replies with status code 101 which stands for switching protocol response. as soon as we get this response, handshake is complete, and we establish websocket connection. Now client and server will talk through the this new connection everytime they wanna communicate. <br>

## File Structure

├── main.py # The FastAPI logic <br>
├── index.html # The chat interface <br>

## How to run

run below command to run the application

```
uvicorn main:app --reload
```

## Reference

1. https://www.youtube.com/watch?v=favi7avxIag&t=443s
2. https://www.youtube.com/watch?v=ADVsjLHevtY
