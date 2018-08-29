# bsmLib/networking.py
# Basic Networking Objects

# MIT License
#
# Copyright (c) 2018 BSMRKRS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from platform import python_version
from socket import socket, AF_INET, SOCK_STREAM

if python_version() >= '3':
    import http.server as http
    import socketserver as socketServer
else:
    import SimpleHTTPServer as http
    import SocketServer as socketServer

ENCODE = 'utf-8' # Encoding

class httpServer:
    '''
    Basic Python HTTP Server
    '''

    def __init__(self, host = '0.0.0.0', port = 8000):
        '''
        Creates HTTP connection object
        '''
        self.host = host
        self.port = port
        self.server_address = (host, port)

    def start(self):
        '''
        Starts HTTP host connection
        '''
        handler = http.SimpleHTTPRequestHandler
        httpd = socketServer.TCPServer(self.server_address, handler)
        print("Hosting at http://%s:%d" % self.server_address)
        httpd.serve_forever()


class tcp:
    '''
    Basic TCP networking
    '''
    def __str__(c):
        '''
        Returns host and port
        '''
        host = c.host
        port = c.port
        s = "%s:%d" % (host, port)
        return s

    def send(self, s):
        '''
        Sends data (max of 99 characters)
        '''
        n = int('%02.0f' % len(s)) # Expected str len
        if n > 99:
            print("Error: Data longer than 99 characters")
            self.stop()
            exit()
        self.sock.sendto(str(n).encode(ENCODE), self.server_address) # Sends expected str len
        r = self.sock.recv(1).decode(ENCODE) # Asks if msg recvived
        if not int(r):
            print("Error: Failed to send expected len")
        self.sock.sendto(s.encode(ENCODE), self.server_address) # Send str
        r = self.sock.recv(1).decode(ENCODE) # Ask if msg recvived
        if not int(r):
            print("Error: Failed to send str")

    def recv(self):
        '''
        Returns data received
        '''
        size = self.sock.recv(2).decode(ENCODE) # Ask expected len
        self.sock.sendto('1'.encode(ENCODE), self.server_address) # Send msg recvived
        if size == '':
            return None
        size = int(size)
        s = self.sock.recv(size).decode(ENCODE) # Ask for msg
        while(len(s) != size): # If len != expect size, then ask again
            print("Error: Failed to recv full str... asking for msg again")
            s = self.sock.recv(size - len(s)).decode(ENCODE)
        self.sock.sendto('1'.encode(ENCODE), self.server_address) # Send msg recvived
        return s

    def stop(self):
        '''
        Stops TCP connection
        '''
        print("Closing connection")
        self.sock.close()


class tcpClient(tcp):
    '''
    Basic TCP Client Networking
    '''
    def __init__(self, host = '0.0.0.0', port = 10000):
        '''
        Create TCP client object
        '''
        self.host = host
        self.port = port
        self.server_address = (host, port)
        self.sock = socket(AF_INET, SOCK_STREAM)

    def connect(self):
        '''
        Attempts to connect to host
        '''
        try:
            self.sock.connect(self.server_address)
        except:
            print("Error: Failed to connect to %s:%d" % self.server_address)
            exit()


class tcpServer(tcp):
    '''
    Basic TCP Server Networking
    '''
    def __init__(self, host = '0.0.0.0', port = 10000):
        '''
        Create TCP host object
        '''
        self.host = host
        self.port = port
        self.server_address = (host, port)
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.bind(self.server_address)
        self.sock.listen(1)

    def listen(self):
        '''
        Listens for client connection
        '''
        self.sock, self.client_address = self.sock.accept()
