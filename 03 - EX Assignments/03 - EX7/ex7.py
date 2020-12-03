import tkinter
from tkinter import messagebox
class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title = "Hello World Application"
        self.main_window.geometry('300x100')
        self.label = tkinter.Label(self.main_window, text = "Hello World!")
        self.label.grid(row=0,column=1)
        self.button = tkinter.Button(self.main_window, text="Press Me", command=self.myButtonCommand)
        self.button.grid(row=1,column=2)
        self.quit_button = tkinter.Button(self.main_window, text='Quit App', command=self.main_window.destroy)
        self.quit_button.grid(row=1,column=0, padx=(10,10))
        self.counter = 0
        tkinter.mainloop()

    def myButtonCommand(self):
        self.counter += 1
        self.messagebox = tkinter.messagebox.showinfo(title='Hello', 
        message= f'You have pressed the button {self.counter} times')
       

my_gui = MyGUI()
