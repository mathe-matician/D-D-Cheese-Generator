from tkinter import *
from tkinter import ttk
from cheese_generator import cheese_generator

class App:

  def __init__(self, master):

    master.geometry("150x50")
    self.button = Button(master, text="Cheese It", command=self.cheese_it)
    self.button.pack()

  def cheese_it(self):
    return cheese_generator()


def main():

  root = Tk()
  app = App(root)
  root.mainloop()

if __name__ == "__main__": main()
    
