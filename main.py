from fastapi.responses import HTMLResponse
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List

app = FastAPI()

# This HTTP endpoint returns an html file that contains JavaScript code to open a WebSocket connection
@app.get("/")
async def get():
    with open("index.html", "r") as f:
        return HTMLResponse(content=f.read())

class ConnectionManager:
    def __init__(self):
        # Keeps a list of currently connected WebSocket clients
        # Every browser tab = one WebSocket connection
        self.active_connections: List[WebSocket] = []

    # Accept & store a new connection
    async def connect(self, websocket: WebSocket):
        await websocket.accept() # Accept the WebSocket connection 
        self.active_connections.append(websocket) # Store the connection

    # When a client leaves, remove it from the list
    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    # Send a message to a specific client, Useful for private messages (not used here, but good design)
    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        # Sends the same message to all, this is what makes it a chat
        for connection in self.active_connections:
            await connection.send_text(message)

# This single instance is shared by all connections and Holds the global chat state
# If you created this inside the endpoint, every user would get a new chat room ❌
manager = ConnectionManager()
    
#WebSocket endpoint
@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):

    # Handshake happens, Client is added to active connections
    await manager.connect(websocket)

    try:
        # WebSocket is event-driven, not request-response. So we use an infinite loop to keep the connection alive
        while True:
            # Wait for a message from the client
            data = await websocket.receive_text()
            # Broadcast it to everyone
            await manager.broadcast(f"Client #{client_id} says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat")