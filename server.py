from TCP import *
import time
import socket

PORT = 10025

class Server(object):
    """ The Receiver class """
    def __init__(self):
        self._sock = None
        self._server = None
        self._status = False

    def __connect(self, host):
        server_address = (host, PORT)
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.connect(server_address)


    def __disconnect(self):
        self._sock.shutdown(socket.SHUT_RDWR)
        self._sock.close()


    def start_server(self, args):
        print('started server')
        host = args[0]
        server_address = (host, PORT)
        # Create the server, binding to localhost on port 10025
        self._server = ThreadedTCPServer(server_address, TCPHandler)
        # Start a thread with the server -- that thread will then start one
        # more thread for each request
        server_thread = threading.Thread(target=self._server.serve_forever)
        # Exit the server thread when the main thread terminates
        server_thread.daemon = True
        server_thread.start()
        self._status = True
        print("Server loop running in thread:", server_thread.name)


    def stop_server(self, args):
        print('stopping server')
        if self._status:
            self.server.shutdown()
            self.server.server_close()
            self._status = False
            print('Server stopped.')


    def send_data(self, args):
        print('sending data')
        if len(args) != 3:
            print('Invalid number of arguments')
            return

        host = args[0]
        load_path = args[1]
        save_path = args[2]
        if save_path[-1] != '/':
            save_path += '/'
        try:
            # Establish connection
            self.__connect(host)

            # Read in data
            data = open(load_path, 'rb').read()
            name = load_path.split('/')[-1]

            # Send the filename
            self._sock.sendall(name.encode('utf-8'))
            time.sleep(0.1)
            # Send the path to copy to
            self._sock.sendall(save_path.encode('utf-8'))
            time.sleep(0.1)
            # Send the file
            self._sock.sendall(data)
            time.sleep(0.1)

            # Close connection
            self.__disconnect()
            print('file sent')
        except Exception as e:
            print('Error:', e)
