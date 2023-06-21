"""

Author: Lucien No.
Description: Revermse polish notation graphing calculator that has a very broken graphing situation but correctly working everything else.
Date Last Modified: June 20th, 2023.

"""

import tkinter as tk
from GUI import *

if __name__ == "__main__":
    window = tk.Tk()
    calculator = calculatorGUI(window)
    window.mainloop()
