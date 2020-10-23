# FINDS EQN OF A NON INPLICIT DERIVITIVE

from tkinter import *
from sympy import *
from math import e

from Eqn_mod import *


class Derivative_Screen:
    def __init__(self, root, prev_screen):

        # Sets up its own root object
        self.root = root
        
        # Which Derivative to find, not actually used, var for future updates
        self.__n_deriv = 1

        # Frames

        self.__main_frame = Frame(root) # Main frame for the screen
        self.__main_frame.pack()

        # Top frame, the equation input part goes in this
        self.__top_frame = Frame(self.__main_frame)
        self.__top_frame.pack(pady = 10)
        # Part that has dy/dx, allows user to change variable x
        self.__dydx_frame = Frame(self.__top_frame)
        self.__dydx_frame.pack(side = "left")
        # Equation entry
        self.__eqn_frame = Frame(self.__top_frame)
        self.__eqn_frame.pack(side ="left")
        # Where the answer is put
        self.__ans_frame = Frame(self.__main_frame)
        self.__ans_frame.pack()
        # Where all buttons are placed
        self.__butt_frame = Frame(self.__main_frame)
        self.__butt_frame.pack()

        # Differentiation sign (auto set to dy/dx)

        self.__sign_top = Frame(self.__dydx_frame)
        self.__sign_mid = Frame(self.__dydx_frame)
        self.__sign_bot = Frame(self.__dydx_frame)

        self.__sign_top.pack()
        self.__sign_mid.pack()
        self.__sign_bot.pack()
        
        self.__d1_lab = Label(self.__sign_top, text = "d")
        self.__d2_lab = Label(self.__sign_bot, text = "d")

        self.__dependant_label = Label(self.__sign_top, text = "y")
        
        self.__independant_ent = Entry(self.__sign_bot, width = 1)
        self.__independant_ent.insert(0, "x")
        
        self.__over_lab = Label(self.__sign_mid, text = "-------")

        self.__d1_lab.pack(side = "left")
        self.__dependant_label.pack(side = "left")

        self.__over_lab.pack()

        self.__d2_lab.pack(side = "left")
        self.__independant_ent.pack(side = "left")

        # Entry for the equation to differentiate
        
        self.__equ_entry = Entry(self.__eqn_frame)
        self.__equ_entry.insert(0, "0") # Auto sets the eqn to 0
        self.__equ_entry.pack()

        # Label for the answer
        self.__yprime_lab = Label(self.__ans_frame, text = "y' =",\
                                 font = ("Courier New", 14))
        self.__yprime_lab.pack(side = "left")


        self.__ans_label =  Label(self.__ans_frame, text = "",\
                              font = ("Courier New", 14))
        self.__ans_label.pack(side = "left")

        # Buttons

        self.__back = Button(self.__butt_frame, text = "back",\
                        command = lambda: self.root.switch_screen(\
                            type(prev_screen), prev_screen.prev_screen) )
        self.__back.pack()
        
        

    def update(self): # Constantly updating function

        # Gets variable of taking y with respect to
        var = self.__independant_ent.get() 


        # Makes symbol object for variable with which y is being taken w.r.t
        var = Symbol(var)


        # Tries to parse equation
        try:
            
            ans = self.__equ_entry.get()
        
            ans = get_parsed(ans)
                
            
            for i in range(self.__n_deriv): # Takes derivitive n times
                ''' needs to be updated in future to take past 1st deriv '''
                ans = Derivative(ans, var)
                ans = ans.doit()
                

            ans = pretty(ans, use_unicode = True)
            
            self.__ans_label.configure(text = ans)

        # When fails, sets ans to Error 

        except:
            self.__ans_label.configure(text = "Error")

        self.root.after(100, self.root.update)

    # Mandatory destroy function
    
    def destroy(self):
        self.__main_frame.destroy()
        

        







        

        
        


    
