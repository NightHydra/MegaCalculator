# SOLVES SYSTEMS OF EQUATIONS

from tkinter import *
from sympy import *
from Eqn_mod import *

class equation_line(Frame): # Only used in Systems_Frame, lines for inputting eqns
    def __init__(self, frame):
        Frame.__init__(self, frame)

        # Row/Col org.
        self.rowconfigure(0, weight = 1)
        self.columnconfigure(0, weight = 10)
        self.columnconfigure(1, weight = 1)
        self.columnconfigure(2, weight = 10)

        # Left side of the eqn
        self.__leftVar = StringVar() 
        self.__left = Entry(self, textvariable = self.__leftVar)
        self.__left.grid(column = 0, row = 0, sticky = 'we')
        #Equals sign
        self.__equal_sign = Label(self, text = "=")
        self.__equal_sign.grid(column = 1, row = 0)
        # Right side of the eqn
        self.__rightVar = StringVar()
        self.__right = Entry(self, textvariable = self.__rightVar)
        self.__right.grid(column = 2, row = 0, sticky = 'we')

    def get_eqn(self): # Reutns the equation in the entry box
        return [self.__leftVar.get(), self.__rightVar.get()]
               


class Equation_Screen(): # Screen Solving Systems of Equations
    def __init__(self, root, prev_screen):

        self.root = root

        self.__main_frame = Frame(self.root)
        self.__main_frame.pack(fill = BOTH)

        # Frames
        self.__ent_frame = Frame(self.__main_frame)
        self.__ans_frame = Frame(self.__main_frame)
        self.__butt_frame = Frame(self.__main_frame)

        self.__ent_frame.pack(fill = X)
        self.__ans_frame.pack(fill = X)
        self.__butt_frame.pack(fill = X)
        

        # Equation entries
        self.__eqn_lines = []
        self.add_entry(2)

        # Labels

        
        self.__ans_lab = Label(self.__ans_frame, text = "", font = \
                               ("Courier New", 14) )
        self.__ans_lab.pack()
        
        # Buttons
        self.__back = Button(self.__butt_frame, text = "back", command = \
                             lambda: self.root.switch_screen(type(prev_screen),\
                                  prev_screen.prev_screen))
        self.__calculate = Button(self.__butt_frame, text = "Solve", command = \
                                  self.solve)
        # Button to allow user to add an eqn entry
        self.__add_button = Button(self.__butt_frame, text = "Add Equation", \
                                   command = lambda: self.add_entry(1))
        # Button to allow user to delete an eqn entry
        self.__del_button = Button(self.__butt_frame, text = "Remove Equation", \
                                   command = lambda: self.del_entry(1))

        # Button Packing
        self.__calculate.pack(pady = 10) # Spacing

        self.__add_button.pack()
        self.__del_button.pack()
        
        self.__back.pack(pady = 10)
        


    def add_entry(self, amnt): # Adds n(param amnt) eqn entries, used in a button

        for i in range (amnt):
            self.__eqn_lines.append(equation_line(self.__ent_frame))
            self.__eqn_lines[-1].pack(fill = X)

    def del_entry(self, amnt): # Deletes n(param amnt) eqn entries, used in a button
        for i in range (amnt):
            self.__eqn_lines[-1].destroy()
            del self.__eqn_lines[-1]

    def solve(self): # Solves the systems

        # Getting all lines
        lines = []

        for line in self.__eqn_lines:
            lines.append(line.get_eqn())

        # Assumes any box not filled in is 0
        for line in lines:
            if line[0] == "":
                line[0] = "0"
            if line[1] == "":
                line[1] = "0"
                
            try:
                # Parses all lines
                line[0] = get_parsed(line[0])
                line[1] = get_parsed(line[1])
                

            except:
                # If 1 eqn is not valid, just returns an error
                self.__ans_lab.configure(text = "ERROR")
                return()

        system = []
        for line in lines:
            # Makes a sympy equation for each eqn, uses left + right sides
            system.append( Eq(line[0], line[1]) )
        
        ans = solve(tuple(system)) # Solves the system using sympy solve function
        if ans == []: # Puts not solution instead of "" if theres no answer
            self.__ans_lab.configure(text = "No Solution")
        else: # Otherwise puts the answer in a label using pretty
            self.__ans_lab.configure(text = pretty(ans, use_unicode = True))
        
        
    def update(self): # Update function
        self.root.after(100, self.root.update)

    def destroy(self): # Destroy function
        self.__main_frame.destroy()
        
        
        
