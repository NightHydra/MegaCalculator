# Modules imports
from tkinter import *
# My file imports
from DerivativeApp import Derivative_Screen
from IntegrationApp import Integration_Screen
from Equation_Inputs import Equation_Screen
from Grapher_Screen import Graph_Screen
from Limits import Limit_Screen
from MatrixApp import Matrix_Screen

class Applications_Menu: # Screen for the application menu
    def __init__(self, root, prev_screen):

        # Gets the previous screen, in this case the main menu
        self.prev_screen = prev_screen
        # Has its own reference to root
        self.root = root

        # Sets the main frame for the application menu
        self.__main_frame = Frame(root)
        self.__main_frame.pack()

        # All of the buttons to go to various calculator esk. applications
        # All buttons call the roots switch screen method changing the screen
        # and gives the next screen a reference to this one.  Doing this will
        # make navigating various screens with back buttons easier
        
        self.__Derivative_button = Button(self.__main_frame, text = "Derivatives",\
            command = lambda: self.root.switch_screen(Derivative_Screen, self) )
        self.__Integration_button = Button(self.__main_frame, text = "Integration",\
            command = lambda: self.root.switch_screen(Integration_Screen, self))
        self.__Systems_button = Button(self.__main_frame, text = "Equation solver",\
            command = lambda: self.root.switch_screen(Equation_Screen, self))
        self.__Graph_button = Button(self.__main_frame, text = "Grapher",\
            command = lambda: self.root.switch_screen(Graph_Screen, self))
        self.__Limit_button = Button(self.__main_frame, text = "Limits",\
            command = lambda: self.root.switch_screen(Limit_Screen, self))
        self.__Matrix_button = Button(self.__main_frame, text = "Matrix Toolbox",\
            command = lambda: self.root.switch_screen(Matrix_Screen, self))

        # The back button
        self.__back_button = Button(self.__main_frame, text = "Back",\
            command = lambda: self.root.switch_screen(type(self.prev_screen)))

        # Put the application buttons in this order, Graphing, Solving Systems
        # Solving Limits, Solving Derivatives, and solving integrals
        self.__Graph_button.pack()
        self.__Systems_button.pack()
        self.__Limit_button.pack()
        self.__Derivative_button.pack()
        self.__Integration_button.pack()
        self.__Matrix_button.pack()
        
        # And finally the back button
        self.__back_button.pack(pady = 20)       

    def destroy(self): # Destroy method
        self.__main_frame.destroy()

    def update(self): # Update method
        self.root.after(100, self.root.update)
