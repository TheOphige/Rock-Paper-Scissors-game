import tkinter as tk               
from tkinter import font  as tkfont
 
 
class PageOne(tk.Frame):
 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
         
        button_2 = tk.Button(self, text="Go to Start Page",
                           command=lambda: controller.show_frame("StartPage"))
        button_2.pack(padx=20, pady=20)
 
        button_3 = tk.Button(self, text="Go to Page Two",
                           command=lambda: controller.show_frame("PageTwo"))
        button_3.pack(padx=20, pady=20)
 
 
 
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()