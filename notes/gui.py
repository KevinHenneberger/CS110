"""
GUIs
- procedural programming
    - sequential
- object oriented programming
- GUI = graphical user interface
- screen or window and components
- mouse input and keyboard input
- event driven programming
     - based on current state
     - behaviors tied to specific event
- design pattern
- MVC = model view controller
- controller = keeps track of models and directs events
- models = data or state
- view = display
- controller interacts with views and model 
- view and model should be completely separate 
- main loop
    - in controller
    - infinite loop
    - loop
        - get events
            - check events
            - if (event 1)...
            - if (event 2)...
            - if (event 3)...
        - alter state
        - update view
"""

import tkinter

class MyGUI:

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Sample GUI')

        self.label1 = tkinter.Label(self.main_window, text="Hello")
        self.label1.pack(side="left")
        self.label2 = tkinter.Label(self.main_window, text="Hello")
        self.label2.pack(side="right")

        self.button1 = tkinter.Button(self.main_window, text="Exit", command=self.main_window.destroy)
        self.button1.pack()

        self.counter = 0
        self.button2 = tkinter.Button(self.main_window, text="Click", command=self.count)
        self.button2.pack()

        tkinter.mainloop()

    def count(self):
        self.counter += 1
        self.message = str(self.counter)
        self.label1.config(text=self.message)

def main():
    MyGUI()

main()
