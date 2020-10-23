# SOLVE MATHEMATICAL LIMITS

from tkinter import *
from sympy import *

from Eqn_mod import *


class Limit_Screen:
    def __init__(self, root, prev_screen):

        self.root = root

        self.__main_frame = Frame(root)
        self.__main_frame.pack(fill = BOTH, expand = True)

        # Frame for Equation
        self.__eqn_frame = Frame(self.__main_frame)
        self.__eqn_frame.pack(side = "top", fill = X, pady = 10)
        # Parts to the answer frame
        # Limit notation symbol
        self.__lim_frame = Frame(self.__eqn_frame)
        self.__lim_frame.pack(side = "left")
        # Entry frame
        self.__ent_frame = Frame(self.__eqn_frame)
        self.__ent_frame.pack(side = "left", fill = X, expand = True, padx = 5)

        # Answer Frame
        self.__ans_frame = Frame(self.__main_frame)
        self.__ans_frame.pack(side = "top", pady = 10)
        
        # Button Frame
        self.__butt_frame = Frame(self.__main_frame)
        self.__butt_frame.pack(side = "top")


        # Widgets for Equation Frame
        # Limit symbol widgets
        self.__lim_frame.rowconfigure(0, weight = 2)
        self.__lim_frame.rowconfigure(1, weight = 3)


        self.__lim_frame.columnconfigure(0, weight = 1)
        self.__lim_frame.columnconfigure(1, weight = 1)
        self.__lim_frame.columnconfigure(2, weight = 1)
        self.__lim_frame.columnconfigure(3, weight = 1)

        # Top part
        self.__lim_lab = Label(self.__lim_frame, text = "lim", \
                               font = ("Courier New", 18))
        self.__lim_lab.grid(row = 0, column = 1, pady = 0,\
                            sticky = "n", rowspan = 2)

        # Bottom part
        self.__var = StringVar()
        self.__var.set("x") # x is the default variable
        self.__var_ent = Entry(self.__lim_frame, textvariable = self.__var,\
                               width = 1)
        self.__var_ent.grid(row = 1, column = 0, sticky = "s")

        self.__goes_to = Label(self.__lim_frame, text = "->")
        self.__goes_to.grid(row = 1, column = 1, sticky = "s")

        self.__appr_value = StringVar()
        self.__appr_value_ent = Entry(self.__lim_frame,\
                                      textvariable = self.__appr_value,\
                                      width = 4)
        self.__appr_value_ent.grid(row = 1, column =2, sticky = "s")

        self.__side = StringVar()
        self.__side_ent = Entry(self.__lim_frame, textvariable = self.__side,\
                                width = 1)
        self.__side_ent.grid(row = 1, column = 4, sticky = "n", pady = 10)
                                      
                    

        


        # Equation entry box
        self.__eqn = StringVar()
        self.__eqn_ent = Entry(self.__ent_frame, textvariable = self.__eqn)
        self.__eqn_ent.pack(side = "top", fill = X)

        # Answer Widget

        # This label just says Answer (It never changes)
        self.__info_lab = Label(self.__ans_frame, text = "Answer:", \
                                font = ("Courier New", 14) ) 
        self.__info_lab.pack(side = "left")

        # This one shows the answer
        self.__ans = StringVar()
        self.__ans_lab = Label(self.__ans_frame, textvariable = self.__ans,\
                               font = ("Courier New", 14))
        self.__ans_lab.pack(side = "left", fill = X)


        # Widgets for Button Frame
        self.__back = Button(self.__butt_frame, text = "back", \
                             command = lambda: self.root.switch_screen(\
                                 type(prev_screen), prev_screen.prev_screen))
        self.__back.pack()


    def update(self): # Update function has more here, it constantly solves the limit
        # No need for a calc button
        
        # Gets all important parts of the limit
        eqn = self.__eqn.get()
        var = self.__var.get()
        value = self.__appr_value.get()
        side = self.__side.get()
        
        # If one or more part (minus the side) is blank, sets the label to ""
        if eqn == "" or var == "" or value == "":
            self.__ans.set("")
            
        else: # If everything is ok so far, it tries to parse and solve the limit
            try:

                eqn = get_parsed(eqn)

                pos_side_lim = limit(eqn, var, value, dir = "+")
                neg_side_lim = limit(eqn, var, value, dir = "-")

                # Determing what side to take the limit from

                if side == "+": # Positive side
                    ans = pos_side_lim
                elif side == "-": # Negative Side
                    ans = neg_side_lim
                else: # Both sides
                    if pos_side_lim == neg_side_lim:
                      # Pos side and negative side must be the same for the 
                      # limit to exist
                        ans = pos_side_lim

                    else:
                        ans = "DNE"
                        

                ans = pretty(ans, use_unicode = True)

                self.__ans.set(ans)

            except: # If exception occurs, makes the label an error
                self.__ans.set("Error")

        self.root.after(100, self.root.update)


    def destroy(self): # Destroy method
        self.__main_frame.destroy()
            
        
