# Standard Stuff for a calculator
from tkinter import *
from Eqn_mod import *
from sympy import *


class Calculator_Frame(Frame): # Inherits from the tkinter Frame class
    def __init__(self, root, frame):

        
        self.root = root # Makes its own copy of the root
        Frame.__init__(self, frame) # Initialization from the parent class
        
        # Used for the various modes value set to typing allows user to enter - 
        # stuff into textbox

        # Otherwise ranges from 0-(#lines-1) and highlights the line
        self.__mode = "typing"
        # Used for copy/pasting prior eqns, keeps track of how far back the user is
        self.__backtrack = 0

        # Select color to highlight lines
        self.__highlight_color = "cyan"
        # How many lines are on screen at a time, not actually used, it only works with 4 now, I need to figure out a better algorithm in the future
        self.__on_screen_lines = 4 # DO NOT change at the moment

        # Sets up the frame for showing past inputs
        self.__prev_line_frame = Frame(self) # Puts it in the frame
        self.__prev_line_frame.pack(expand = NO, fill = X)

        # Entry for the equation
        self.__eqn_ent = Entry(self)
        # Different functions for pressing keys
        self.__eqn_ent.bind("<Return>", self.Return_Event) # Calculates the input
        self.__eqn_ent.bind("<Up>", self.Up_Event) # Highlights 1 eqn up
        self.__eqn_ent.bind("<Down>", self.Down_Event) # Highlights 1 eqn down
        self.__eqn_ent.pack(fill  = X) # When screen expands, the entry does as well

        # Configuring the column
        self.__prev_line_frame.grid_columnconfigure(0, weight = 1)

        # Frame setup for the past equations
        self.__prev_line_labs = []
        self.__prev_line_vars = []
        self.__anchors = ["e", "w"]

        # Algorithm for placing the equations, does it like a calculator
        for l in range (self.__on_screen_lines//2):
            for i in range(2):
                self.__prev_line_vars.append(StringVar())
                # Font needs to be single spaced for pretty to work correctly
                self.__prev_line_labs.append( Label(self.__prev_line_frame\
                                            , textvariable = self.__prev_line_vars[2*l+i]\
                                            , font = ("Courier New", 12)))

                self.__prev_line_labs[i+2*l].grid( row = ( (self.__on_screen_lines)-3*l-i)\
                                                      , sticky = self.__anchors[i]+"s")
            if l != self.__on_screen_lines//2-1:
                # Line between each input and solved output
                lab = Label(self.__prev_line_frame, text = "-"*1000).grid(\
                    row = (self.__on_screen_lines-(3*l)-2))



        

        

    def update(self): # Update function

        # Updating Labels for the prior lines
        lines = self.root.get_prior_lines("pretty") # Get the pretty strings, more mathematically notated

        # Displays the past 2 input/outputs, can be scrolled up though
        for i in range(self.__on_screen_lines):
            self.__prev_line_vars[i].set(lines[-1-i-self.__backtrack])
            
            
        
    def calculate_line(self): # Calculates the line
        line = self.__eqn_ent.get() 
        self.__eqn_ent.delete(0, "end") # Deletes whats in the entry box

        # This allows for using the prior line in the current eqn, like entering +2 on a TI84
        try: # Just in case it comes across an error
            if line[0] in ["+", "*", "/"] or line[0]+line[1] == "-(":
                prev_line = self.root.get_prior_lines("strings")[-1]
                line = "("+prev_line+")"+line
        except: # Exception doesnt need to do anything here
            pass 

        # Saves the line
        self.root.add_line(line)

        try:
            ans = get_parsed(line) # Parses the line
        except:
            self.root.add_line("ERROR") # If it cant, it makes the answer "ERROR"
            return () # Stops trying to calculate

        try: # Trys to simplify
            ans = simplify(ans)
        except Exception as e: # If not a valid expressions, tells you why as the answer
            self.root.add_line(e)
            return ()

        # Whether an error occurs or not, it always saves something as an answer to the input
        self.root.add_line(ans)

    def Up_Event(self, event): # When the user presses the up key
        if self.__mode == "typing": # If you are typing, disables the entry box
            # LOCKS ENTRY WIDGET whilemoving up and down
            self.__eqn_ent.config(state = 'disabled')
            # Sets the mode and starts allowing user to look back through eqns
            self.__mode = 0 # mode is how far back you are going, mode 0 is the prior answer, 1 is the prior input
            self.__prev_line_labs[0].configure(bg = \
                                               self.__highlight_color)
        elif self.__mode < self.__on_screen_lines-1: # Moves up one mode if everything is on screen
            self.__prev_line_labs[self.__mode].configure(bg = "white")
            self.__mode += 1
            self.__prev_line_labs[self.__mode].configure(bg = \
                                                         self.__highlight_color)
        else: # If highlight is moved offscreen goes back two, puts a new input/answer on the screen
            self.__backtrack += 2

            self.__prev_line_labs[self.__mode].configure(bg = "white")
            self.__mode -= 1
            self.__prev_line_labs[self.__mode].configure(bg = \
                                                         self.__highlight_color)

    def Down_Event(self, event): # When the users presses the down key
        if self.__mode == "typing": # If the user isnt back any eqns, does nothing
            pass
        
        elif self.__mode == 0: # If at the bottom, it enables the entry widget again
            # Enables the entry widget again
            self.__eqn_ent.config(state = 'normal')
            # Sets the frame back to typing mode
            self.__mode = "typing"
            self.__prev_line_labs[0].configure(bg = "white")
                
        elif self.__backtrack == 0: # If not past mode 4, just takes mode-1
            self.__prev_line_labs[self.__mode].configure(bg = "white")
            self.__mode -= 1
            self.__prev_line_labs[self.__mode].configure(bg = \
                                                         self.__highlight_color)
            
        else: # If beyond mode 4, makes sure everythings on screen
            self.__prev_line_labs[self.__mode].configure(bg = "white")

            if self.__mode%2 == 0:
                self.__backtrack -= 2
                self.__mode += 1
            else:
                self.__mode -= 1
                
            self.__prev_line_labs[self.__mode].configure(bg = \
                                                         self.__highlight_color)

    def Return_Event(self, event): # When the user presses return
        if self.__mode == "typing": # If user is entering eqn, calculates the line
            self.calculate_line()
        else: # Mode is not set to typing, takes what is currently highlighted
            # Sets equation entry box back to normal
            self.__prev_line_labs[self.__mode].configure(bg = \
                                                         "white")   
            
            self.__eqn_ent.config(state = 'normal')

            self.__eqn_ent.insert("end",\

            # Locates whats highlighted
            self.root.get_prior_lines("strings")[-1-self.__mode-self.__backtrack])

            self.__mode = "typing"



    
                
        
        
            
