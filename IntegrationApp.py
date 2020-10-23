# FINDS BOTH DEFINITE AND INDEFINITE INTEGRALS

from tkinter import *
from sympy import *

from Eqn_mod import *


class Integration_Screen:
    def __init__(self, root, prev_screen):

        self.root = root
        
        self.__n_integ = 1
        ''' for how many times you want to integrate, not implemented yet'''

        # Main Frame
        self.__main_frame = Frame(self.root) 
        self.__main_frame.pack()

        # Top Frame, used for the whole eqn entry part
        self.__top_frame = Frame(self.__main_frame)
        self.__top_frame.pack(pady = 4)

        # Frame for the integral sign
        self.__sign_frame = Frame(self.__top_frame)
        self.__sign_frame.pack(side = "left")
        # Frame for an eqn entry
        self.__enter_frame = Frame(self.__top_frame)
        self.__enter_frame.pack(side = "left")

        # Frame for displaying the answer
        self.__eqn_frame = Frame(self.__main_frame)
        self.__eqn_frame.pack()

        self.__butt_frame = Frame(self.__main_frame)
        self.__butt_frame.pack()

        # Integral sign, Integral of f(x) from a to b
        self.__b_entry = Entry(self.__sign_frame, width = 2) # b is upper bound
        self.__b_entry.pack()

        self.__integral_sign = Label(self.__sign_frame, text = "∫", \
                                     font = ("Courier New", 40)) # Sign
        self.__integral_sign.pack()

        self.__a_entry = Entry(self.__sign_frame, width = 2) # a is lower bound
        self.__a_entry.pack()

        self.__d = Label(self.__enter_frame, text = "d") # For the dx at the end
        self.__var_ent = Entry(self.__enter_frame, width = 1) # Allows for entry of variable to integrate to
        self.__var_ent.insert(0, "x")

        self.__var_ent.pack(side = "right", padx = 0)
        self.__d.pack(side = "right", padx = 0)
        
        
        # Equation input 
        self.__equ_entry = Entry(self.__enter_frame)
        self.__equ_entry.insert(0, "0")
        self.__equ_entry.pack(padx = 2)

        # Calculate Button
        self.__calc_button = Button(self.__butt_frame, text = "Calculate", \
                                    command = self.calculate)
        self.__calc_button.pack(pady = 20)
        
        # Equation Output
        self.__label =  Label(self.__eqn_frame, text = "",\
                              font = ("Courier New", 14))
        self.__label.pack()

        # Back Button

        self.__back = Button(self.__butt_frame, text = "back", command = \
                         lambda: self.root.switch_screen(type(prev_screen), prev_screen.prev_screen))
        self.__back.pack()
        
        

    def calculate(self): # Calculates integral
        var = self.__var_ent.get() # Gets the variable 

       
        vari = Symbol(var) # Makes it a sympy symbol
        
        # Gets the limits of integration (a,b)
        limits = self.get_limits_of_integration()   # Another method in class       
        
        try: # Gets the eqn and parses it
            
            ans = self.__equ_entry.get()
            ans = get_parsed(ans)

        except: # If it fails, sets output to ERROR
            self.__label.configure(text = "ERROR")
            return ()


        if limits: # If the limits exist, takes definite integral

            try: # Attempts to take definite integral
                for i in range(self.__n_integ):
                    ans = Integral(ans,(vari, limits['a'], limits['b']))
                    ans = ans.doit()
            except: # Makes the label ERROR if exception occurs
                self.__label.configure(text = "ERROR")
                return ()
                
        else:

            try: # Attempts to take indefinite integral
                for i in range(self.__n_integ):
                    ans = Integral(ans, vari)
                    ans = ans.doit()
            except: # Makes the label ERROR if exception occurs
                self.__label.configure(text = "ERROR")
                return ()
                    
        ans = pretty(ans, use_unicode = True)
        self.__label.configure(text = ans) # Configures the label

        
            

    def get_limits_of_integration(self): # Gets the limit (a and b)
        a = self.__a_entry.get()
        b = self.__b_entry.get()

        limits = dict()

        if a=="" or b=="": # If no entry for 1, returns False
            return False
        limits["a"] = a
        limits["b"] = b

        return limits # Otherwise returns whats in them


    def update(self): # Update method
        self.root.after(100, self.root.update)

    def destroy(self): # Destroy method
        self.__main_frame.destroy()
