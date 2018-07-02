import command
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

class Application(Frame):
    """
    Frame for transferring files.
    """
    def __init__(self, master, controller, local_ip, ext_ip):
        Frame.__init__(self, master)
        self._controller = controller
        self._command = command.CommandCenter()
        self.client_details()
        self.file_browsing_widgets()

        self.label_localip['text'] = local_ip
        self.label_externalip['text'] = ext_ip

    def client_details(self):
        self.client_frame = LabelFrame(self, text='Client Details', height=50, width=550)
        self.client_frame.grid(row=0, column=0, columnspan=6, sticky=W + N)
        self.client_frame.grid_propagate(0)

        self.label_local = Label(self.client_frame, text='Local: ', font=('Helvetica', 14, 'bold'))
        self.label_local.grid(row=0, column=0, columnspan=1, sticky=W)

        self.label_localip = Label(self.client_frame, text='')
        self.label_localip.grid(row=0, column=1, columnspan=1, sticky=W)

        self.label_external = Label(self.client_frame, text='External:', font=("Helvetica", 14, 'bold'))
        self.label_external.grid(row=0, column=2, columnspan=1, sticky=W)

        self.label_externalip = Label(self.client_frame, text='')
        self.label_externalip.grid(row=0, column=3, columnspan=1, sticky=W)

        self.label_dest = Label(self.client_frame, text='Destination IP:', font=("Helvetica", 14, 'bold'))
        self.label_dest.grid(row=0, column=4, columnspan=1, sticky=W+E)

        self.textbox_ip = Text(self.client_frame, height=1, width=16, bg='grey')
        self.textbox_ip.grid(row=0, column=5, columnspan=1, sticky=E + N + S)


    def file_browsing_widgets(self):
        # File browsing frame
        self.file_frame = LabelFrame(self, text='File browser', height=500, width=550)
        self.file_frame.grid(row=1, column=0, columnspan=2, sticky=W + N)
        self.file_frame.grid_propagate(0)

        self.listbox = Listbox(self.file_frame, bg='grey', width=60, height=20, selectmode=MULTIPLE)
        self.listbox.grid(row=1, column=0, columnspan=2, sticky=W + E)

        self.label_path = Label(self.file_frame, text='Enter the directory you want to save to below.')
        self.label_path.grid(row=2, column=0, columnspan=2, sticky=W)

        self.textbox = Text(self.file_frame, height=1, width=60, bg='grey')
        self.textbox.grid(row=3, column=0, columnspan=2, sticky=W + E + N + S)

        self.button_browse = Button(self.file_frame, text='Browse', command=lambda : self._command.execute('10', self))
        self.button_browse.grid(row=4, column=0, sticky=W + E + N + S)

        self.button_transfer_files = Button(self.file_frame, text='Transfer Files', command=lambda : self._command.execute('11', self))
        self.button_transfer_files.grid(row=4, column=1, sticky=W + E + N + S)

        self.button_remove_files = Button(self.file_frame, text='Remove Selected', command=lambda : self._command.execute('12', self))
        self.button_remove_files.grid(row=5, column=0, sticky=W + E + N + S)

        self.button_quit = Button(self.file_frame, text='Quit', command=self.__quit)
        self.button_quit.grid(row=5, column=1, sticky=W + E + N + S)


    def __quit(self):
        self._command.execute('01')
        self.quit()
