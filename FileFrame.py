import time
import command
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

class Application(Frame):
    def __init__(self, master, controller):
        Frame.__init__(self, master)
        self._controller = controller
        self._command = command.CommandCenter()
        self.file_browsing_widgets()
        self.server_widgets()
        self.word = "it works"

    def file_browsing_widgets(self):
        # File browsing frame
        self.file_frame = LabelFrame(self, text="File browser", height=500, width=550)
        self.file_frame.grid(row=0, column=0, columnspan=2, sticky=W + N)
        self.file_frame.grid_propagate(0)

        self.listbox = Listbox(self.file_frame, bg='grey', width=60, height=20, selectmode=MULTIPLE)
        self.listbox.grid(row=0, column=0, columnspan=2, sticky=W + E)

        self.label_path = Label(self.file_frame, text='Enter the directory you want to save to below.')
        self.label_path.grid(row=1, column=0, columnspan=2, sticky=W)

        self.textbox = Text(self.file_frame, height=1, width=60, bg='grey')
        self.textbox.grid(row=2, column=0, columnspan=2, sticky=W + E + N + S)

        self.button_browse = Button(self.file_frame, text='Browse', command=lambda : self._command.execute('3', self))
        self.button_browse.grid(row=3, column=0, sticky=W + E + N + S)

        self.button_transfer_files = Button(self.file_frame, text='Transfer Files', command=lambda : self._command.execute('4', self))
        self.button_transfer_files.grid(row=3, column=1, sticky=W + E + N + S)

        self.button_remove_files = Button(self.file_frame, text='Remove Selected', command=lambda : self._command.execute('5', self))
        self.button_remove_files.grid(row=4, column=0, sticky=W + E + N + S)

        self.button_quit = Button(self.file_frame, text='Quit', command=self.quit)
        self.button_quit.grid(row=4, column=1, sticky=W + E + N + S)

    def server_widgets(self):
        # Server widgets
        self.server_frame = LabelFrame(self, text="Server Details", height=200, width=250)
        self.server_frame.grid(row=0, column=2, sticky=W + N)
        self.server_frame.grid_propagate(0)

        self.host_label = Label(self.server_frame, text='Host:')
        self.host_label.grid(row=0, column=2, sticky=W + N)
        self.host = Text(self.server_frame, height=1, width=34, bg='grey')
        self.host.insert(INSERT, 'localhost')
        self.host.grid(row=1, column=2, sticky=W + N + E)

        self.port_label = Label(self.server_frame, text='Port:')
        self.port_label.grid(row=2, column=2, sticky=W + N)
        self.port = Text(self.server_frame, height=1, width=34, bg='grey')
        self.port.insert(INSERT, '10025')
        self.port.grid(row=3, column=2, sticky=W + N + E)

        self.note = Text(self.server_frame, height=3, width=34, wrap=WORD, state=NORMAL)
        self.note.insert(INSERT, 'Note:\nMake sure to port forward the port on your router.')
        self.note['state'] = DISABLED
        self.note.grid(row=4, column=2)
