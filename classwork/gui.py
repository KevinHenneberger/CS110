import tkinter

class MyGUI:

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Building a GUI')

        self.label = tkinter.Label(self.main_window, text="This is a label.")
        self.label.pack(side="right")

        self.button = tkinter.Button(self.main_window, text="This is a button.", command=self.changeLabel)
        self.button.pack()

        tkinter.mainloop()

    def changeLabel(self):
        self.label.config(text="You changed the label.")

def main():
    MyGUI()

main()