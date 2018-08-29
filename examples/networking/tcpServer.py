from bsmLib import tcpServer

t = tcpServer()
t.listen()

x = 1
while(1):
    t.send(str(x))
    x += 1
