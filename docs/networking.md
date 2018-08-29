# Networking

Networking

## Classes

httpHost - Host HTTP connection </br>
tcpClient - Host TCP Client connection </br>
tcpServer - Host TCP server connection

## httpServer

`httpServer(host = '0.0.0.0', port = '8000')` - Creates HTTP connection </br>
`httpServer.start()` - Starts HTTP host connection

## tcpClient

`tcpClient(host = '0.0.0.0', port = '10000')` - Create TCP client </br>
`tcpClient.conntect()` - Attempts to connect to host </br>
`tcpCleint.send(data)` - Sends data to host (max of 99 characters). Data must be a string. </br>
`tcpClient.recv()` - Returns data received from server </br>
`tcpClient.stop()` - Stops TCP connection

## tcpServer

`tcpServer(host = '0.0.0.0', port = '10000')` - Create TCP host </br>
`tcpServer.listen()` - Listens for client connection </br>
`tcpServer.send(data)` - Sends data to client (max of 99 characters) </br>
`tcpServer.recv()` - Returns data received from client </br>
`tcpServer.stop()` - Stops TCP connection

## Example

httpServer:

```python
from bsmLib import httpServer

s = httpServer()
s.start()
```

tcpClient:

```python
from bsmLib import tcpClient

t = tcpClient()
t.connect()

while(1):
    print(c.recv())
```

tcpServer:

```python
from bsmLib import tcpServer

t = tcpServer()
t.listen()

x = 1
while(1):
    t.send(str(x))
    x += 1
```
