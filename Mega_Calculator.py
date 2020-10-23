# MAIN PROGRAM IN THE CALCULATOR

from tkinter import *
from sympy import *
from math import e
import pickle
from sympy.physics.units import degree

from Calculator_Frame import Calculator_Frame
from ApplicationsMenu import Applications_Menu



# The Mainscreen    
class Main_Screen:
    def __init__(self, root):
        # Sets up its own variable for the root
        self.root = root

        # Makes its frame in the root
        self.__main_frame = Frame(root)

        # Packs the mainframe, makes sure the frame fills and continues to fill
        # the whole root window
        self.__main_frame.pack(fill = BOTH)

        
        # Sets up the frame for the main part of the calculator
        self.__Calculator_Frame = Calculator_Frame(root, self.__main_frame)
        self.__Calculator_Frame.pack(fill = BOTH)

        # Application Button on the mainscreen, opens the application frame
        self.__applic_button = Button(self.__main_frame, text = "Applications",\
        command = lambda: self.root.switch_screen(Applications_Menu, self) )

        # Quit button, saves and exits the program
        self.__quit_button = Button(self.__main_frame, text = "Quit",\
                                    command = self.root.end_program)

        self.__quit_button.pack()

        self.__applic_button.pack()



    def update(self): # Manditory Update Function
        self.__Calculator_Frame.update()
        self.root.after(100, self.root.update)
        
    def destroy(self): # Manditory Destroy Function
        self.__main_frame.destroy()
    
        


class Root(Tk): # Class extention of tkinter.Tk(), Window of the program

    def __init__(self):
        Tk.__init__(self) # Tk() initialization function


        self.title("PI-84") # Renames the window

        self.__screen = Main_Screen(self) # sets a variable to a set of screens
        
        
        self.geometry("200x300") # Sets basic geometry
        
        # Storage for prior lines on the main calculator part, allows for
        # Pressing up key to highlight a past input
        self.__prior_lines = dict()

        try:
            self.__prior_lines = load("StringLines.dat")

        except:
            self.__prior_lines["pretty"] = ["", "", "", ""]
            self.__prior_lines["strings"] = ["", "", "", ""]
        

        self.after(100, self.update) # Starts the update functions
        self.mainloop() # Mainloop
        

    
        

    def switch_screen(self, replacement, *args): 

        # Switches the screen, destroys the current frame and packs a new one

        # So the screen stays the same size when switching frames
        curr_screen_size = self.get_size() 
        
        self.__screen.destroy() # Destoys the current frame, all screens have a destroy method

        # Sets the screen variable to the replacement one, also accepts arguments that might be needed
        self.__screen = replacement(self, *args) 
        
        # Second part so the screen size remains constant
        self.geometry(str(curr_screen_size[0])+"x"+str(curr_screen_size[1]))

    

    def get_prior_lines(self, type_): # Returns prior lines of a specific type
        return self.__prior_lines[type_]

    def add_line(self, line): # Saves the line, saves the normal version
        # and the pretty version.  Pretty is a sympy method
    
        self.__prior_lines["strings"].append(str(line))
        self.__prior_lines["pretty"].append(pretty(line, use_unicode = True))

    def get_size(self): # Method to get the current screen size
        width = self.winfo_width()
        height = self.winfo_height()

        return [width, height] # Returns 2d list, width followed by height


    def end_program(self): # Saves, and exits the GUI

        # Saving
        save("StringLines.dat", self.__prior_lines)
        

        # Destroys the main root
        self.destroy()

        
        
    def update(self): #Looping of the update function, called by screen classes
        
        (self.__screen.update())


def main(): # Main functions
    root = Root()


def save(file, info): # Saving function

    # Saving to File
    with open(file, "wb") as file:
        pickle.dump(info, file)


def load(file): # Loading function

    # Loading from file
    with open(file, "rb") as file:
        info = pickle.load(file)


    return info # Returns the dictionary

    

main() # Calling of the main function
    

        
