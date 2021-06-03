import tkinter as tk



class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()
class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 1")
       label.pack(side="top", fill="both", expand=True)
class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 2")
       label.pack(side="top", fill="both", expand=True)
class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 3")
       label.pack(side="top", fill="both", expand=True)
       
class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Page 1", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Page 2", command=p2.lift)
        b3 = tk.Button(buttonframe, text="Page 3", command=p3.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

        p1.show()

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()





####################################################################################
import tkinter as tk

class SampleApp(tk.Tk):


    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        for frame in self.frames.values():
            frame.grid_remove()
        frame = self.frames[page_name]
        frame.grid()
        frame.winfo_toplevel().geometry("")

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page", font=100)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("PageTwo"))
        button1.pack()
        button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=100)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=100)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()




######################################################################################
from tkinter import *
from functools import partial
  
def raise_frame(frame):
    frame.tkraise()
  
main_win = Tk()
main_win.geometry('500x500')
main_win.title("Registration Form")
 
second_frame = Frame(main_win)
second_frame.place(x=0, y=0, width=500, height=500)
 
first_frame = Frame(main_win)
first_frame.place(x=0, y=0, width=500, height=500)
 
 
label_0 = Label(first_frame, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)
  
  
label_1 = Label(first_frame, text="FullName",width=20,font=("bold", 10))
label_1.place(x=80,y=130)
  
entry_1 = Entry(first_frame)
entry_1.place(x=240,y=130)
  
label_2 = Label(first_frame, text="Email",width=20,font=("bold", 10))
label_2.place(x=68,y=180)
  
entry_2 = Entry(first_frame)
entry_2.place(x=240,y=180)
  
label_3 = Label(first_frame, text="Gender",width=20,font=("bold", 10))
label_3.place(x=70,y=230)
var = IntVar()
Radiobutton(first_frame, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
Radiobutton(first_frame, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)
  
label_4 = Label(first_frame, text="country",width=20,font=("bold", 10))
label_4.place(x=70,y=280)
  
list1 = ['Canada','India','UK','Nepal','Iceland','South Africa'];
c=StringVar()
droplist=OptionMenu(first_frame,c, *list1)
droplist.config(width=15)
c.set('select your country')
droplist.place(x=240,y=280)
  
label_4 = Label(first_frame, text="Programming",width=20,font=("bold", 10))
label_4.place(x=85,y=330)
var1 = IntVar()
Checkbutton(first_frame, text="java", variable=var1).place(x=235,y=330)
var2 = IntVar()
Checkbutton(first_frame, text="python", variable=var2).place(x=290,y=330)
  
Button(first_frame, text='Submit',width=20,bg='brown',fg='white', command=lambda:raise_frame(second_frame)).place(x=180,y=380)
 
label_8 = Label(second_frame, text="Welcome to page 2",width=20,font=("bold", 10))
label_8.place(x=70,y=230)
 
Button(second_frame, text="Switch back to page 1",width=20,bg='brown',fg='white', command=lambda:raise_frame(first_frame)).place(x=180,y=380)
 
main_win.mainloop()



##################################################################################################
import tkinter as tk

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # alternate ways to create the frames & append to frames dict: comment out one or the other

        for F in (StartPage, PLG):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # self.frames["StartPage"] = StartPage(parent=container, controller=self) 
        # self.frames["PLG"] = PLG(parent=container, controller=self)
        # self.frames["StartPage"].grid(row=0, column=0, sticky="nsew")
        # self.frames["PLG"].grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    # alternate version of show_frame: comment out one or the other

    def show_frame(self, page_name):
        for frame in self.frames.values():
            frame.grid_remove()
        frame = self.frames[page_name]
        frame.grid()

    # def show_frame(self, page_name):
        # frame = self.frames[page_name]
        # frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="start page")
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Page One", command=lambda: controller.show_frame("PLG"))
        button1.pack()        

        button2 = tk.Button(self, text="focus traversal demo only")
        button2.pack()
        button2.focus_set()

        button3 = tk.Button(self, text="another dummy button")
        button3.pack()

        lbl = tk.Label(self, text="tkraise messes up focus traversal\nwhich you can see by testing the two versions of show_frame.()\nUsing grid_remove instead of tkraise solves that,\nwhile preventing frames from being unable to resize to fit their own contents.")
        lbl.pack()

class PLG(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Enter something below; the two buttons clear what you type.")
        label.pack(side="top", fill="x", pady=10)
        self.wentry = tk.Entry(self)
        self.wentry.pack(pady = 10)
        self.text = tk.Text(self)
        self.text.pack(pady = 10)
        restart_button = tk.Button(self, text="Restart", command=self.restart)
        restart_button.pack()
        refresh_button = tk.Button(self, text="Refresh", command=self.refresh) 
        refresh_button.pack()  

    def restart(self):
        self.refresh()
        self.controller.show_frame("StartPage")

    def refresh(self):
        self.wentry.delete(0, "end")
        self.text.delete("1.0", "end")
        # set focus to any widget except a Text widget so focus doesn't get stuck in a Text widget when page hides
        self.wentry.focus_set()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()


################################################################################################
import tkinter as tk
from PageOne import PageOne
from PageTwo import PageTwo
 
 
class MainApp(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
 
         
        ###MENU FRAME
        left_frame = tk.Frame(root, borderwidth=1, bg= "white", relief="solid", highlightthickness=2)
        left_frame.pack(side="left", expand=False, fill="y")
        container = tk.Frame(left_frame, borderwidth=1, bg= "white", relief="solid")
        container.pack(expand=True, fill="both", padx=5, pady=5)
 
        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
 
            frame.grid(row=0, column=0, sticky="nsew")
 
        self.show_frame("StartPage")
 
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
 
class StartPage(tk.Frame):
 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
 
        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame("PageOne"))
 
        button1.pack(padx=20, pady=20)
 
        button2 = tk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("PageTwo"))
 
        button2.pack(padx=20, pady=20)
   
        
        ###TOP
        right_frame = tk.Frame(root, borderwidth=1, bg= "white", relief="solid", highlightthickness=2)
        right_frame.pack(side="right", expand=True, fill="both")
        top_box = tk.Frame(right_frame, borderwidth=1, bg= "white", relief="solid")
        top_box.pack(expand=True, fill="both", padx=10, pady=10)
        label_top = tk.Label(top_box, text="Title Logo", bg= "white")
        label_top.pack()
         
        ###BOTTOM
        bottom_box = tk.Frame(right_frame, borderwidth=1, bg= "white", relief="solid")
        bottom_box.pack(expand=True, fill="both", padx=10, pady=10)
        PageOne(bottom_box,controller)
        PageTwo(bottom_box, controller)

         
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1200x650")
    MainApp(root).pack(side="top", fill="both", expand=True)
    root.mainloop()


###############################################################################################
import tkinter as tk 
class MainApp(tk.Frame):    
  def __init__(self, parent, *args, **kwargs):        
    tk.Frame.__init__(self, parent, *args, **kwargs)        
    self.parent = parent                  
    ###MENU FRAME        
    left_frame = tk.Frame(root, borderwidth=1, bg= "white", relief="solid", highlightthickness=2)       
    left_frame.pack(side="left", expand=False, fill="y")        
    container = tk.Frame(left_frame, borderwidth=1, bg= "white", relief="solid")        
    container.pack(expand=True, fill="both", padx=5, pady=5)        
    btn_1 = tk.Button(container, text="Home")        
    btn_1.pack(padx=20, pady=20)        
    btn_2 = tk.Button(container, text="Page One")        
    btn_2.pack(padx=20,pady=20)                 
    ###TOP        
    right_frame = tk.Frame(root, borderwidth=1, bg= "white", relief="solid", highlightthickness=2)        
    right_frame.pack(side="right", expand=True, fill="both")        
    top_box = tk.Frame(right_frame, borderwidth=1, bg= "white", relief="solid")        
    top_box.pack(expand=True, fill="both", padx=10, pady=10)        
    label_top = tk.Label(top_box, text="Title Logo", bg= "white")        
    label_top.pack()                 
    ###BOTTOM        
    bottom_box = tk.Frame(right_frame, borderwidth=1, bg= "white", relief="solid")        
    bottom_box.pack(expand=True, fill="both", padx=10, pady=10)      


if __name__ == "__main__":    
  root = tk.Tk()    
  root.geometry("1200x650")    
  MainApp(root).pack(side="top", fill="both", expand=True)    
  root.mainloop()