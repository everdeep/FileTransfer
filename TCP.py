import os
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

        try:
            # Receiving the name of the file
            filename = self.request.recv(1024).decode('utf-8')
            # Receiving the directory to write the file to
            directory = self.request.recv(1024).decode('utf-8')

            if not os.path.exists(directory):
                os.makedirs(directory)

            # Receiving the file itself
            length = 0
            with open(directory + filename, 'wb') as f:
                while True:
                    self.data = self.request.recv(4096)
                    length += len(self.data)
                    if not self.data:
                        break
                    f.write(self.data)
                print('Wrote %s bytes to %s%s' % (length, directory, filename))
        except BrokenPipeError as e:
            print('! Error handling request from %s.' % self.client_address[0])
            print('! [ exception caught on line 46 of TCP.py ]')
            self.request.sendall('Server: There was an processing your file')

        print('Thread %s finished receiving from %s.' % (cur_thread.name, self.client_address[0]))
