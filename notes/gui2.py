import tkinter

class MyGUI:

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Building a GUI')

        self.frame1 = tkinter.Frame(self.main_window)
        self.frame2 = tkinter.Frame(self.main_window)

        self.frame1.pack(side="top")
        self.frame2.pack(side="bottom")

        self.label = tkinter.Label(self.frame1, text="This is a label.")
        self.label.pack(side="right")

        self.button = tkinter.Button(self.frame2, text="This is a button.", command=self.changeLabel)
        self.button.pack(side="left")

        self.input = tkinter.Entry(self.frame2, width=15)
        self.input.pack()

        tkinter.mainloop()

    def changeLabel(self):
        self.label.config(text=self.input.get())

def main():
    MyGUI()

main()
