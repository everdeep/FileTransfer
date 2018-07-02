from tkinter import *
import FileFrame
import command
import socket
import urllib.request

class Application(Frame):
    """
    Main file. Handles multiple frames which are loaded onto this
    parent window. At the moment there is only one frame (FileFrame).
    """
    def __init__(self, master, local_ip, ext_ip):
        Frame.__init__(self, master)
        self.pack()

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # NOTE: to add more frames just make a new file and import it
        #       like how the FileFrame has been imported and append to
        #       the tuple
        self.frames = {}
        for F in (FileFrame,):
            page_name = F.__name__
            frame = F.Application(master=container, controller=self, local_ip=local_ip, ext_ip=ext_ip)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("FileFrame")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == '__main__':
    root = Tk()
    root.withdraw()
    # Update "requested size" from geometry manager
    root.update_idletasks()

    size = (570, 520)
    x = (root.winfo_screenwidth() - size[0]) / 2
    y = (root.winfo_screenheight() - size[1]) / 2
    root.geometry("%dx%d+%d+%d" % (size + (x, y)))

    # This seems to draw the window frame immediately, so only call deiconify()
    # after setting correct window position
    root.deiconify()
    root.lift()

    # NOTE: retrieving the IPs does slow down launch time a bit

    # get local address
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    local_ip = s.getsockname()[0]
    s.close()

    # get external address
    ext_ip = urllib.request.urlopen('https://v4.ident.me/').read().decode('utf8')

    _command = command.CommandCenter()
    _command.execute('00', local_ip)

    app = Application(master=root, local_ip=local_ip, ext_ip=ext_ip)
    app.master.title("File Transfer Application")
    # Start the program
    app.mainloop()
    root.destroy()
