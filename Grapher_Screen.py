# GRAPHS EQUATIONS

from tkinter import *
from sympy import *
from sympy.plotting import plot
from copy import deepcopy

from Eqn_mod import *

class equation_line(Frame): # only in Graph_Screen
    def __init__(self,frame, eqn_num):

        # Object for each individual equation entry

        Frame.__init__(self, frame)

        # row/col configuration
        self.rowconfigure(0, weight = 1)
        self.columnconfigure(0, weight = 0)
        self.columnconfigure(1, weight = 1)


        self.__yFrame = Frame(self) # Row for frame of "y =" part of eqns
        self.__yFrame.grid(row = 0, column = 1,  sticky = "we")
        
        self.__yFrame.rowconfigure(0, weight = 1)
        self.__yFrame.columnconfigure(0, weight = 1)
        self.__yFrame.columnconfigure(1, weight = 100) # allows much more room for the entry

        self.__SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉") # Allows me to use subscripts

        self.__y_equals = "y"+str(eqn_num)+"=" # Text for beginning label (y = )

        # The Label Part
        self.__lab_part = Label(self.__yFrame, \
                                text = self.__y_equals.translate(self.__SUB))
        self.__lab_part.grid(column = 0, row = 0)

        # The Entry Part
        self.__eqn = StringVar()
        self.__ent_part = Entry(self.__yFrame, textvariable = self.__eqn)
        self.__ent_part.grid(column = 1, row = 0, sticky = "we")

        # xFrame stuff, pack only when switching to parametic eqns
        # Same thing as above but with x coordinates (for parametric eqns)

        self.__xFrame = Frame(self)

        self.__xFrame.rowconfigure(0, weight = 1)
        self.__xFrame.columnconfigure(0, weight = 1)
        self.__xFrame.columnconfigure(1, weight = 100)

        self.__x_equals = "x"+str(eqn_num)+"=" # Text for beginning label (x = )

        self.__Xlab_part = Label(self.__xFrame, \
                                text = self.__x_equals.translate(self.__SUB))
        self.__Xlab_part.grid(column = 0, row = 0)

        # The Entry Part
        self.__xeqn = StringVar()
        self.__xent_part = Entry(self.__xFrame, textvariable = self.__xeqn)
        self.__xent_part.grid(column = 1, row = 0, sticky = "we")
        
        


    def get_eqn(self, eqn_type): # Eqn type is 0 for linear and 1 for parametric
        if eqn_type == 0:

            ret = self.__eqn.get()
            if ret == "":
                return None
            else:
                return ret # if linear, returns an eqn

        if eqn_type == 1:

            ret0 = self.__xeqn.get()
            ret1 = self.__eqn.get()
            if ret0 == "" or ret1 == "":
                return None
            else:
                return (ret0, ret1) # returns an x eqn (ret0) and a y eqn, (ret1)
            

    def make_para_entries(self): # Makes the entries for linear graphing
        self.columnconfigure(0, weight = 1)
        self.__xFrame.grid(row = 0, column = 0, sticky = "we")
        

    def make_lin_entries(self): # Makes the entries for parametric graphing
        self.columnconfigure(0, weight = 0)
        self.__xFrame.grid_remove()
        
        
        



class Graph_Screen(): # Application for Graphing equations
    def __init__(self, root, prev_screen):

        self.root = root
        

        self.__main_frame = Frame(self.root)
        self.__main_frame.pack(fill = BOTH)

        # Local Varibales

        self.__entries_on_screen = 0

        # Frames

        # Definition of Top frame and bottom frame
        self.__top_frame = Frame(self.__main_frame)
        self.__bot_frame = Frame(self.__main_frame)
        self.__top_frame.pack(fill = X)
        self.__bot_frame.pack(fill = X)

        # frames in Top Frame
        self.__ent_frame = Frame(self.__top_frame)
        self.__ent_frame.pack(fill = X)

        # frames in bottom frame
        self.__butt_frame = Frame(self.__bot_frame)
        self.__butt_frame.pack(side = "left")

        self.__opt_frame = Frame(self.__bot_frame)
        self.__opt_frame.pack(side = "right")
        

        # Equation entries
        self.__eqn_lines = []
        self.add_entry(5)

        # Buttons
        self.__graph_butt = Button(self.__butt_frame, text = "graph", command = \
                                  self.graph)
        self.__back = Button(self.__butt_frame, text = "back", command=  \
                             lambda: self.root.switch_screen(type(prev_screen),\
                                                prev_screen.prev_screen))


        # Options
        self.__opt_frame.rowconfigure(0, weight = 1)
        self.__opt_frame.columnconfigure(0, weight = 1)
        self.__opt_frame.columnconfigure(1, weight = 1)
        self.__opt_frame.columnconfigure(2, weight = 1)
        

        self.__eqn_type_lab = Label(self.__opt_frame, text = "Equation Type:")
        self.__eqn_type_lab.grid(row = 0, column = 0)

        # Option for Linear vs Parametric
        self.__eqn_type = IntVar()
        
        self.__lin_opt = Radiobutton(self.__opt_frame, text = "Linear",\
                        variable = self.__eqn_type,\
                        value = 0, command = self.change_to_linear)
        self.__para_opt = Radiobutton(self.__opt_frame, text = "Parametric",\
                        variable = self.__eqn_type,\
                        value = 1, command = self.change_to_polar)


        
        self.__lin_opt.grid(row = 0, column = 1) # Default as linear
        self.__para_opt.grid(row = 0, column = 2) 
        
        self.__eqn_type.set(0)
        
        # Packing Buttons
        self.__graph_butt.pack()
        self.__back.pack()

    

    def add_entry(self, amnt): # Adds n entries, n in the param amnt

        for i in range(amnt):
            self.__eqn_lines.append(equation_line(self.__ent_frame, self.__entries_on_screen))
            self.__eqn_lines[-1].pack(fill = X)
            self.__entries_on_screen += 1 # Added last so it goes y0 y1 etc.
            

    def del_entry(self, amnt): # remove n entries, n in the param amnt

        for i in range(amnt):
            self.__eqn_lines[-1].destroy()
            del self.__eqn_lines[-1]
            self.__entries_on_screen -= 1

    def change_to_polar(self): # Method to assign to button that makes entries for polar eqns
        for line in self.__eqn_lines:
            line.make_para_entries() # Method from the equation line class

    def change_to_linear(self):# Method to assign to button that makes entries for linear eqns

        for line in self.__eqn_lines:
            line.make_lin_entries() # Method from the equation line class

    def graph(self):

        eqn_type = self.__eqn_type.get() # Gets whether linear or parametric
        
        eqns = [line.get_eqn(eqn_type) for line in self.__eqn_lines]

        while None in eqns: # Removes all parts the user did not type anything into
            eqns.remove(None)

        if eqn_type == 0: # Solving for linears eqns
            try:
                eqns = [get_parsed(eqn) for eqn in eqns] # Parses all eqns
            except:
                return()

            plot(*eqns, xlim = (-10,10), ylim = (-10, 10)) # Plots linear

        if eqn_type == 1: # Solving for parametric eqns
            try:
                eqns = [( get_parsed(parts[0]), get_parsed(parts[1]) )\
                        for parts in eqns] # Parses all parts for all eqns
            except:
                return()

            plot_parametric(*eqns, xlim = (-10,10), ylim = (-10, 10)) # Plots parametric
        

        
        

    def update(self): # Update method
        self.root.after(100, self.root.update)

    def destroy(self): # Destroy method
        self.__main_frame.destroy()
        
        

        

        
