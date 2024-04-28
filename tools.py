from setup import samba, format_csv_value, condor
import tkinter as tk
import subprocess


def function1():
    script_path = 'updateBookDetails.py'
    subprocess.run(['python', script_path])


def function2():
    script_path = 'staleCupcakes.py'
    subprocess.run(['python', script_path])


def function3():
    print("Function 3 called")


def function4():
    print("Function 4 called")


def function5():
    print("Function 5 called")


def create_window():
    root = tk.Tk()
    root.geometry("500x450")  # Set the initial size of the window
    root.title("Tools")

    # Create a frame to hold buttons and labels
    frame = tk.Frame(root)
    frame.pack(side="left", fill="both", expand=True, padx=20, pady=20)  # Adding padding

    # Define button names, functions, and label texts
    button_info = [
        ("Samba", function1, "Add missing details to books in your library"),
        ("Stale Cupcakes", function2, "Set up your system for use for the first time")
        #("Button 3 Name", function3, "Label 3 Text"),
        #("Button 4 Name", function4, "Label 4 Text"),
        #("Button 5 Name", function5, "Label 5 Text"),
    ]

    # Create buttons and labels
    for i, (button_name, func, label_text) in enumerate(button_info):
        button = tk.Button(frame, text=button_name, width=15, height=3, command=func)  # Assign function to button
        button.grid(row=i, column=0, sticky="nsew", padx=10, pady=10)  # Adding padding
        label = tk.Label(frame, text=label_text, font=("Arial", 12))  # Set individual label text
        label.grid(row=i, column=1, sticky="w", padx=10, pady=10)  # Adding padding

    root.mainloop()


def main():
    create_window()


if __name__ == "__main__":
    main()