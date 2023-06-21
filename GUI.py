# I left out any overly self explanatory variables here

"""
Author: Lucien No
Date Modified: June 18th, 2023.
Description: This file (theamth.py) holds the custom made trig/log functions that are used in the math


**** CLASS ****
calculatorGUI-  class representing a calculator GUI.

    **** Primary variables: ****
    - window: The main Tkinter window object.
    - entry: The Entry widget for displaying and inputting the expression.
    - output: The Label widget for displaying the result of the calculation.
    - graphCanvas: The Canvas widget for drawing the graph.

 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

    *** Functions/Methods: ***
    ** Function 1 **
    - __init__(self, window): Initializes the calculator GUI.
      * Variable *
      window = The main TKinter object.

 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

    ** Function 2 **
    - createWidgets(self): Creates all the widgets for the calculator GUI.
      * Variables * 
      entry = Entry widget for displaying and inputting whats in the entry ifeld.
      output = Output widget for displaying the result of the input/expression.
      graphCanvas = The canvas widget for drawing the graph.

 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

    ** Function 3 **
    - buttonClick(self, button): Handles button click events.
      * Variables * 
      button = The button clicked.

  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
     
    ** Function 4 **
    - clearInputOutput(self): Clears the input and output fields.

 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    
    ** Function 5 **
    - drawGraph(self): Draws the graph based on the expression.

 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    
    ** Function 6 **
    - drawGraphLines(self, x, y, xMin, xMax, yMin, yMax): Draws the lines for the graph.
      * Variables *
      x = List of x coords of graph points.
      y = List of y coords of graph points.
      xMin = Minimum value of x axis.
      xMax = Maximum value of x axis.
      yMin = Minimum value of y axis.
      yMax = Maximum value of y axis.

 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    
    ** Function 7 **
    - clearGraphLines(self): Clears the lines of the graph.

 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    
    ** Function 8 **
    - drawHardcodedGraph(self): Draws the hardcoded graph.

* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *


"""


import tkinter as tk
from ttwidgets import TTButton
from RPN import calculateRPN


class calculatorGUI:
    def __init__(self, window):
        self.window = window
        self.window.title("Calculator")
        self.window.configure(bg='black')
        self.createWidgets()
        self.drawHardcodedGraph()

    def createWidgets(self):
        self.entry = tk.Entry(self.window, font=("Pixer", 20), bg='#060606', fg='red')
        self.entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="n")

        self.output = tk.Label(self.window, font=("Pixer", 20), bg='#060606', fg='red', width=20, anchor="e")
        self.output.grid(row=1, column=0, columnspan=5, padx=10, pady=10, sticky="ew")

        buttons = [

            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'sin', 'cos', 'tan', 'log',
            '(', ')', '[', ']',
            'x', '^', ':)', 'del'

        ]

        rows = 9
        cols = 4

        row = 2
        col = 0

        for button in buttons:
            if row == rows:
                break

            btn = TTButton(

                self.window,
                text=button,
                width=5,
                height=2,
                font=("Pixer", 19),
                fg='red',
                bg='#060606',
                command=lambda button=button: self.buttonClick(button)

            )

            btn.grid(row=row, column=col, padx=10, pady=10, sticky="ew")
            col += 1

            if col == cols:
                col = 0
                row += 1

        clrBtn = TTButton(

            self.window,
            text="CLR",
            width=5,
            height=2,
            font=("Pixer", 30),
            bg='black',
            fg='red',
            command=self.clearInputOutput

        )

        clrBtn.grid(row=0, column=cols-1, padx=5, pady=5, sticky="ne")

        graphBtn = TTButton(

            self.window,
            text="Graph",
            width=5,
            height=2,
            font=("Pixer", 30),
            bg='black',
            fg='red',
            command=self.drawGraph

        )

        graphBtn.grid(row=0, column=0, padx=5, pady=5, sticky="nw")

        self.graphCanvas = tk.Canvas(self.window, width=400, height=400, bg='black')
        self.graphCanvas.grid(row=row, column=0, columnspan=cols, padx=10, pady=10, sticky="ew")

        self.drawHardcodedGraph()

        for col in range(cols):
            self.window.grid_columnconfigure(col, weight=1)

        for row in range(rows):
            self.window.grid_rowconfigure(row, weight=1)

    def buttonClick(self, button):
        currentExpression = self.entry.get()

        print("Pressed:", button)
        print("Expression:", currentExpression)

        if button == "=":
            try:
                result = calculateRPN(currentExpression)
                self.output.config(text=result)

            except Exception as e:
                self.output.config(text="Invalid Expression!")
                print("Error:", e)

            print(result)

        elif button in ['sin', 'cos', 'tan', 'log', '^']:
            self.entry.insert(tk.END, button + "(")

        elif button == ":)":
            self.output.config(text="😊")
            self.entry.config(fg='red', bg='black')

        elif button == "del":
            self.entry.delete(len(currentExpression) - 1, tk.END)

        else:
            self.entry.insert(tk.END, button)

    def clearInputOutput(self):
        self.entry.delete(0, tk.END)
        self.output.config(text="")
        self.clearGraphLines()

    def drawGraph(self):
        expression = self.entry.get()
        self.clearGraphLines()
        self.drawHardcodedGraph()

        try:
            x = range(-10, 10)
            y = [calculateRPN(expression, {'x': val}) for val in x]

            xMin, xMax = min(x), max(x)
            yMin, yMax = min(y), max(y)

            if xMax == xMin:
                xMax += 1
                xMin -= 1

            if yMax == yMin:
                yMax += 1
                yMin -= 1

            self.drawGraphLines(list(x), y, xMin, xMax, yMin, yMax)
            
        except Exception as e:
            self.output.config(text="Invalid Expression!")
            print("Error:", e)

    def drawGraphLines(self, x, y, xMin, xMax, yMin, yMax):
        canvasWidth = self.graphCanvas.winfo_width()
        canvasHeight = self.graphCanvas.winfo_height()

        xScale = canvasWidth / (xMax - xMin)
        yScale = canvasHeight / (yMax - yMin)

        x0 = -xMin * xScale
        y0 = canvasHeight - (-yMin * yScale)

        self.graphCanvas.create_line(0, y0, canvasWidth, y0, fill="red")
        self.graphCanvas.create_line(x0, 0, x0, canvasHeight, fill="red")

        for val in x:
            scaledX = x0 + (val * xScale)
            tickHeight = 10
            self.graphCanvas.create_line(scaledX, y0, scaledX, y0 + tickHeight, fill="red")
            self.graphCanvas.create_text(scaledX, y0 + tickHeight + 5, text=str(val), fill="red")

        for val in y:
            scaledY = y0 - (val * yScale)
            tickWidth = 5
            self.graphCanvas.create_line(x0, scaledY, x0 - tickWidth, scaledY, fill="red")
            self.graphCanvas.create_text(x0 - tickWidth - 5, scaledY, text=str(val), fill="red")

    def clearGraphLines(self):
        self.graphCanvas.delete("all")

    def drawHardcodedGraph(self):
        self.clearGraphLines()

        canvasWidth = self.graphCanvas.winfo_width()
        canvasHeight = self.graphCanvas.winfo_height()

        xMin, xMax = -10, 10
        yMin, yMax = -10, 10

        xScale = canvasWidth / (xMax - xMin)
        yScale = canvasHeight / (yMax - yMin)

        x0 = -xMin * xScale
        y0 = canvasHeight - (-yMin * yScale)

        self.graphCanvas.create_line(0, y0, canvasWidth, y0, fill="red")
        self.graphCanvas.create_line(x0, 0, x0, canvasHeight, fill="red")

        for val in range(xMin, xMax + 1):
            scaledX = x0 + (val * xScale)
            tickHeight = 10
            self.graphCanvas.create_line(scaledX, y0, scaledX, y0 + tickHeight, fill="red")
            self.graphCanvas.create_text(scaledX, y0 + tickHeight + 5, text=str(val), fill="red")

        for val in range(yMin, yMax + 1):
            scaledY = y0 - (val * yScale)
            tickWidth = 5
            self.graphCanvas.create_line(x0, scaledY, x0 - tickWidth, scaledY, fill="red")
            self.graphCanvas.create_text(x0 - tickWidth - 5, scaledY, text=str(val), fill="red")
