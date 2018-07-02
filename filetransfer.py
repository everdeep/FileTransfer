import command
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
            host = obj.textbox_ip.get(1.0, END).strip()
            # Send file
            _command = command.CommandCenter()
            _command.execute('02', host, load_path, save_path)
        except Exception as e:
            messagebox.showinfo("Error", 'Please check your host details or ensure the destination client.')
            print('Error:', e)
            print('! [ exception caught on line 22 of filetransfer.py ]')


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
