from tkinter import filedialog

def button1_click(window):
    # Open a file dialog for selecting a .txt file
    filepath = filedialog.askopenfilename(parent=window, filetypes=[("Text files", "*.txt")])
    if filepath:
        print("Selected .txt file:", filepath)

def button2_click(window):
    # Open a file dialog for selecting a .csv file
    filepath = filedialog.askopenfilename(parent=window, filetypes=[("CSV files", "*.csv")])
    if filepath:
        print("Selected .csv file:", filepath)

def button3_click():
    print("Button 3 clicked!")

def button4_click():
    print("Button 4 clicked!")

def button5_click():
    print("Button 5 clicked!")