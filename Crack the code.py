import tkinter as tk
from tkinter import *
import tkinter.messagebox
LARGEFONT =("Arial", 10)
def countercalculate(code,text,e1,correctyes,correctno):
    for i in range(4):
                if code[i] == text[i]:
                    correctyes += 1
                elif code[i] in text:         
                    correctno += 1
    tkinter.messagebox.showinfo("Message",f"You got {correctyes+correctno}  numbers correct and {correctyes} in correct position")
    e1.delete(0, 'end')
    
def restartgame(e1,controller):
    e1.delete(0, 'end')
    Page3.counter1=0
    Page3.counter2=0
    Page3.codeplayer1=0
    Page3.codeplayer2=0
    controller.show_frame(StartPage)
    
def Gamelogic(e1,correctyes,correctno,controller,label):
    Guess=e1.get()
    if Page3.counter1>Page3.counter2:
        Page3.counter2=Page3.counter2+1
        if Guess==Page3.codeplayer1:
            tkinter.messagebox.showinfo("Message",f"You got it in {Page3.counter2} tries!")
            restartgame(e1,controller)
        else:
          countercalculate(Page3.codeplayer1,Guess,e1,correctyes,correctno)
          label.config(text="Now Player 1's turn\nEnter your 4 digit Guess") 
    else:
        Page3.counter1=Page3.counter1+1
        if Guess==Page3.codeplayer2:
            tkinter.messagebox.showinfo("Message",f"You got it in {Page3.counter1} tries!")
            restartgame(e1,controller)
        else:
          countercalculate(Page3.codeplayer2,Guess,e1,correctyes,correctno)
          label.config(text="Now Player 2's turn\nEnter your 4 digit Guess")

def checklength(e1,controller,label):
    code=e1.get()
    if Page3.codeplayer1==0:
            if len(code) == 4 and code.isdigit():tkinter.messagebox.showinfo("Message","Good!\nNow player 2's turn");e1.delete(0,4);Page3.codeplayer1=code;label.config(text="Now player 2's turn")
            else:tkinter.messagebox.showwarning("Warning", "Only 4 numbers are allowed!");e1.delete(0,'end')
    elif Page3.codeplayer2==0:
        if len(code) == 4 and code.isdigit():tkinter.messagebox.showinfo("Message","Well done!\nLets start cracking");e1.delete(0,4);Page3.codeplayer2=code;controller.show_frame(Page3);label.config(text="It is Player 1's turn\nEnter your 4 digit code")
        else:tkinter.messagebox.showwarning("Warning", "Only 4 numbers are allowed!");e1.delete(0,'end')          

def checkanswer(e1,correctyes,correctno,controller,label):
        text=e1.get()
        if len(text) == 4 and text.isdigit():Gamelogic(e1,correctyes,correctno,controller,label)
        else:
            tkinter.messagebox.showwarning("Warning", "Only 4 numbers are allowed!");e1.delete(0, 'end')

class tkinterApp(tk.Tk):	
	# __init__ function for class tkinterApp 
	def __init__(self, *args, **kwargs): 
		
		# __init__ function for class Tk
		tk.Tk.__init__(self, *args, **kwargs)
		
		# creating a container
		container = tk.Frame(self)
		container.pack(side = "top", fill = "both", expand = True) 
		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		# initializing frames to an empty array
		self.frames = {} 

		# iterating through a tuple consisting
		# of the different page layouts
		for F in (StartPage,Page2,Page3):

			frame = F(container, self)

			# initializing frame of that object from
			# startpage, page1, page2 respectively with 
			# for loop
			self.frames[F] = frame 

			frame.grid(row = 0, column = 0, sticky ="nsew")
			frame.configure(bg="#5A47A5")

		self.show_frame(StartPage)
	# to display the current frame passed as
	# parameter
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()    
        
# first window frame startpage

class StartPage(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)
		
		label = Label(self, text ="Welcome to the Crack The Code", font = LARGEFONT, bg="#5A47A5")
		
		label.grid(row = 1, column = 2) 

		buttontwoplayers = Button(self, text ="Start The Game",command = lambda : controller.show_frame(Page2),width=17,bg="#FF0101", activebackground="#FF0101")
	
		buttontwoplayers.grid(row = 2, column =2)


# third window frame page2
class Page2(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent);turn=True
  
		label = Label(self, text ="It is Player 1's turn\nEnter your 4 digit code", font = LARGEFONT, bg="#5A47A5")
		label.grid(row = 1, column = 1, padx = 10, pady = 10)
  
		e1 = Entry(self)
		e1.configure({"background": "#6F6F6F"})
		e1.grid(row=1,column=2)
  
		button1 = Button(self, text ="Done",bg="#CCA62C",command = lambda :checklength(e1,controller,label), activebackground="#CCA62C")
		button1.grid(row = 3, column = 3, padx = 10, pady = 10)	

class Page3(tk.Frame):
	codeplayer1=0
	codeplayer2=0
	counter1=0
	counter2=0
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
  
		label = Label(self, text ="It is Player 1's turn\nEnter your 4 digit Guess", font = LARGEFONT, bg="#5A47A5")
		label.grid(row = 1, column = 1, padx = 10, pady = 10)
  
		e1 = Entry(self)
		e1.configure({"background": "#6F6F6F"})
		e1.grid(row=1,column=2)
  
		correctyes=0
		correctno=0
  
		button1 = Button(self,text ="Done",bg="#CCA62C",command=lambda :checkanswer(e1,correctyes,correctno,controller,label), activebackground="#CCA62C")
		button2 = Button(self, text ="New Game",bg="#6D2061",command = lambda : restartgame(e1,controller), activebackground="#6D2061")

		button1.grid(row = 4, column = 3, padx = 10, pady = 10)
		button2.grid(row = 6, column = 3, padx = 10, pady = 10)
			

# Driver Code
app = tkinterApp()
app.title('Code Crack')
app.geometry('500x500')
app.resizable(width=False, height=False)
app.mainloop()