import tkinter as tk
import subprocess


def run_script1():
    script_path = 'frontEndStartUp.py'
    subprocess.run(['python', script_path])


def run_script2():
    script_path = 'tools.py'
    subprocess.run(['python', script_path])


def button1_clicked():
    run_script1()


def button2_clicked():
    run_script2()


def main():
    # Create the main window
    root = tk.Tk()
    root.title("Admin Tools")

    # Create the buttons
    button1 = tk.Button(root, text="Initial File Setup Pt 1", width=30, height=15, command=button1_clicked)
    button2 = tk.Button(root, text="Tools", width=30, height=15, command=button2_clicked)

    # Grid layout
    button1.grid(row=0, column=0, padx=75, pady=75)
    button2.grid(row=0, column=1, padx=75, pady=75)

    # Start the main event loop
    root.mainloop()


if __name__ == '__main__':
    main()
