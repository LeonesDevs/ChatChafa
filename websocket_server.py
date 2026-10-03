import asyncio
import websockets

clients = set()


async def handler(websocket):
    clients.add(websocket)

    print(f"Client connected ({len(clients)} online)")

    try:
        async for message in websocket:
            print(f"Received: {message}")

            for client in clients:
                await client.send(message)

    except websockets.exceptions.ConnectionClosed:
        pass

    finally:
        clients.remove(websocket)

        print(f"Client disconnected ({len(clients)} online)")


async def main():
    async with websockets.serve(
        handler,
        "0.0.0.0",
        8765
    ):
        print("ChatChafa WebSocket server running on port 8765")

        await asyncio.Future()


asyncio.run(main())