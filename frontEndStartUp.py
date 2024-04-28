import tkinter as tk
import config
from tkinter import filedialog
from setup import condor, format_csv_value, technopop, marathon, jongara, strip_unique_isbns


def button1_click(window):
    bookAndCopyInitiaize()



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


def bookAndCopyInitiaize():
    return


def main():
    # Create the main window
    root = tk.Tk()
    root.title("Initial Setup")

    # Create and configure the frame
    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack()

    # Create a label
    label = tk.Label(frame, text="DO IN ORDER; CLOSE WHEN DONE", font=("Arial", 16))
    label.pack()

    # Create Button 1
    button1 = tk.Button(frame, text="1: Books", width=10, command=lambda: button1_click(root))
    button1.pack(side=tk.LEFT, padx=5)

    # Create Button 2
    button2 = tk.Button(frame, text="2: Students", width=10, command=lambda: button2_click(root))
    button2.pack(side=tk.LEFT, padx=5)

    # Create a Close button
    close_button = tk.Button(frame, text="Close", width=10, command=root.destroy)
    close_button.pack()

    # Run the main event loop
    root.mainloop()


if __name__ == "__main__":
    main()
