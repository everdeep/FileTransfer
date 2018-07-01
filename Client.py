from tkinter import *
import FileFrame

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (FileFrame,):
            page_name = F.__name__
            frame = F.Application(master=container, controller=self)
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

    size = (800, 500)
    x = (root.winfo_screenwidth() - size[0]) / 2
    y = (root.winfo_screenheight() - size[1]) / 2
    root.geometry("%dx%d+%d+%d" % (size + (x, y)))

    # This seems to draw the window frame immediately, so only call deiconify()
    # after setting correct window position
    root.deiconify()
    root.lift()

    app = Application(master=root)
    app.master.title("File Transfer Application")
    # Start the program
    app.mainloop()
    root.destroy()
