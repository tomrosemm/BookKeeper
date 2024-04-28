import tkinter as tk
from buttonClickStartup import button1_click, button2_click, button3_click, button4_click, button5_click

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Button Clicks")

    # Create and configure the frame
    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack()

    # Create a label
    label = tk.Label(frame, text="SETUP: DO IN NUMERICAL ORDER; CLOSE WHEN DONE", font=("Arial", 16))
    label.pack()

    # Create Button 1
    button1 = tk.Button(frame, text="1: Find isbn.txt", width=20, command=lambda: button1_click(root))
    button1.pack(side=tk.LEFT, padx=5)

    # Create Button 2
    button2 = tk.Button(frame, text="2: Find students.csv", width=20, command=lambda: button2_click(root))
    button2.pack(side=tk.LEFT, padx=5)

    # Create Button 3
    button3 = tk.Button(frame, text="3: Build Books Data", width=20, command=button3_click)
    button3.pack(side=tk.LEFT, padx=5)

    # Create Button 4
    button4 = tk.Button(frame, text="4: Build Copies", width=20, command=button4_click)
    button4.pack(side=tk.LEFT, padx=5)

    # Create Button 5
    button5 = tk.Button(frame, text="5: Parse students.csv", width=20, command=button5_click)
    button5.pack(side=tk.LEFT, padx=5)

    # Create a Close button
    close_button = tk.Button(frame, text="Close", width=10, command=root.destroy)
    close_button.pack()

    # Run the main event loop
    root.mainloop()


if __name__ == "__main__":
    main()
