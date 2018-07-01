import socket
import threading
from socketserver import ThreadingMixIn, TCPServer, BaseRequestHandler

class ThreadedTCPServer(ThreadingMixIn, TCPServer):
    pass

class TCPHandler(BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    # Runs before handle
    def setup(self):
        pass

    def handle(self):
        """ Handler method, this is called after setup """
        # self.request is the TCP socket connected to the client
        cur_thread = threading.current_thread()
        print('Thread %s receiving from %s.' % (cur_thread.name, self.client_address[0]))
        # Determine what the client is sending
        self.data = self.request.recv(1024).decode().split(',')
        print('data:', self.data)
        self.command_menu(self.data[0])
        print('Thread %s finished receiving from %s.' % (cur_thread.name, self.client_address[0]))

    def command_menu(self, command):
        """ This handles receiving different requests from clients. """
        print(command)
