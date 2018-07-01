from multiprocessing import Process
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

class FileTransfer(object):
    """ The Receiver class """

    def __transfer(self, load_path, save_path, obj):
        """
        Each file transfer creates a new connection
        from the client to server since it was
        a lot easier than sending multiple files
        over one connection.
        """
        try:
            # grabs the host and port from the server details
            host = obj.host.get(1.0, END).strip()
            port = int(obj.port.get(1.0, END))
            # sock = connect_to_server(host, port)
            #self.__send_data(sock, load_path, save_path)
            # sock.close()
            print('sending file')
        except Exception as e:
            messagebox.showinfo("Error",
                                'Please check your host and port details or ensure the server is running.\n\nHost: '
                                '%s\nPort: %s\n '
                                % (host, port)
                                )
            print('Error:', e)


    @staticmethod
    def __send_data(sock, load_path, save_path):
        if save_path[-1] != '/':
            save_path += '/'
        try:
            pass
            # data = open(load_path, 'rb').read()
            # name = load_path.split('/')[-1]
            # print('Sending file', name)
            # # Server command
            # sock.sendall(b'1')
            # time.sleep(0.1)
            # # Send the filename
            # sock.sendall(name.encode('utf-8'))
            # time.sleep(0.1)
            # # Send the path to copy to
            # sock.sendall(save_path.encode('utf-8'))
            # time.sleep(0.1)
            # # Send the file
            # sock.sendall(data)
            # time.sleep(0.1)
        except Exception as e:
            print('Error:', e)


    def browse(self, args):
        """
        Allows user to select files from
        their computer and upload them to
        the program
        """
        print('browsing files')
        obj = args[0]
        names = filedialog.askopenfilenames(
            parent=obj,
            initialdir='~',
            title='Choose a file.'
        )
        for name in names:
            if name not in obj.listbox.get(0, END):
                obj.listbox.insert(END, name)

    def transfer(self, args):
        """
        User can either transfer all files
        or select a few files and transfer them
        """
        print('transfering files')
        obj = args[0]
        # fetch the directory in the textbox
        directory = obj.textbox.get(1.0, END).rstrip()
        # fetches all file directories listed in the box
        files = obj.listbox.get(0, END)
        if len(files) == 0:
            messagebox.showinfo("Alert", "Add some files to transfer first")
        elif len(directory) == 0:
            messagebox.showinfo("Alert", "Add a destination directory in textbox above")
        else:
            pids = []
            for file in files:
                p = Process(target=self.__transfer, args=(file, directory, obj))
                pids.append(p)
                p.start()

            for p in pids:
                p.join()


    def remove(self, args):
        """
        Allows user to select files from
        the listbox and remove them
        """
        print('removing files')
        # grabs all selected files, returns as tuple
        indices = args[0].listbox.curselection()
        if len(indices) == 0:
            messagebox.showinfo("Alert", "No files selected")
        else:
            # delete in reverse order
            for index in sorted(indices, reverse=True):
                args[0].listbox.delete(index)
