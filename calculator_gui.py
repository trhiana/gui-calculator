"""
Name: Rhiana Thelemaque
Project Name: calculator_gui.py
This is a GUI calculator designed using tkinter. 
Designed following a tutorial.
"""

from tkinter import *

expression = " "

def press(number):
    global expression

    expression += str(number)
    equation.set(expression)


#evaluate the final expression
def equalPress():
    try:
        global expression
        total = str(eval(expression)) #evaluate expression and convert to string
        equation.set(total)
        expression = " "
    except:
        equation.set("Error") #if error is generated
        expression = " "

#to clear the entry textbox 
def clear(): 
    global expression
    expression = " "
    equation.set(" ")


if __name__ == "__main__":
    calc = Tk()
    calc.configure(background = "black") #background color
    calc.title("CALCULATOR")
    calc.geometry("270x150") #configuration of GUI window
    
    equation = StringVar() #create an instance of a variable class
    text_field = Entry(calc, textvariable = equation) #textbox for the expression
    text_field.grid(columnspan = 4, ipadx = 70) #grid for placing the key widgets

    equation.set(" ")

    #creating the buttons on the window
    buttonOne = Button(calc, text = " 1 ", fg = "black", bg = "grey", 
                            command = lambda: press(1), height = 1, width = 7)
    buttonOne.grid(row = 2, column = 0)

    buttonTwo = Button(calc, text = " 2 ", fg = "black", bg = "grey", 
                            command = lambda: press(2), height = 1, width = 7)
    buttonTwo.grid(row = 2, column = 1)

    buttonThree = Button(calc, text = " 3 ", fg = "black", bg = "grey", 
                            command = lambda: press(3), height = 1, width = 7)
    buttonThree.grid(row = 2, column = 2)

    buttonFour = Button(calc, text = " 4 ", fg = "black", bg = "grey", 
                            command = lambda: press(4), height = 1, width = 7)
    buttonFour.grid(row = 3, column = 0)

    buttonFive = Button(calc, text = " 5 ", fg = "black", bg = "grey", 
                            command = lambda: press(5), height = 1, width = 7)
    buttonFive.grid(row = 3, column = 1)

    buttonSix = Button(calc, text = " 6 ", fg = "black", bg = "grey", 
                            command = lambda: press(6), height = 1, width = 7)
    buttonSix.grid(row = 3, column = 2)

    buttonSeven = Button(calc, text = " 7 ", fg = "black", bg = "grey", 
                            command = lambda: press(7), height = 1, width = 7)
    buttonSeven.grid(row = 4, column = 0)

    buttonEight = Button(calc, text = " 8 ", fg = "black", bg = "grey", 
                            command = lambda: press(8), height = 1, width = 7)
    buttonEight.grid(row = 4, column = 1)

    buttonNine = Button(calc, text = " 9 ", fg = "black", bg = "grey", 
                            command = lambda: press(9), height = 1, width = 7)
    buttonNine.grid(row = 4, column = 2)

    buttonZero = Button(calc, text = " 0 ", fg = "black", bg = "grey", 
                            command = lambda: press(0), height = 1, width = 7)
    buttonZero.grid(row = 5, column = 0)

    plusSign = Button(calc, text = " + ", fg = "black", bg = "grey", 
                            command = lambda: press("+"), height = 1, width = 7)
    plusSign.grid(row = 2, column = 3)

    minusSign = Button(calc, text = " - ", fg = "black", bg = "grey", 
                            command = lambda: press("-"), height = 1, width = 7)
    minusSign.grid(row = 3, column = 3)

    divideSign = Button(calc, text = " / ", fg = "black", bg = "grey", 
                            command = lambda: press("/"), height = 1, width = 7)
    divideSign.grid(row = 4, column = 3)

    multiplySign = Button(calc, text = " * ", fg = "black", bg = "grey", 
                            command = lambda: press("*"), height = 1, width = 7)
    multiplySign.grid(row = 5, column = 3)

    equalSign = Button(calc, text = " = ", fg = "black", bg = "grey", 
                            command = equalPress, height = 1, width = 7)
    equalSign.grid(row = 5, column = 2)

    clear = Button(calc, text = " C ", fg = "black", bg = "grey", 
                            command = clear, height = 1, width = 7)
    clear.grid(row = 5, column = 1)

    decimal = Button(calc, text = " . ", fg = "black", bg = "grey",
                            command = lambda: press("."), height = 1, width = 7)
    decimal.grid(row = 6, column = 0)

    calc.mainloop() #start GUI
