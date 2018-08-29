from bsmLib import tcpClient

t = tcpClient()
t.connect()

while(1):
    print(t.recv())
