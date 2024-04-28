import tkinter as tk
from bookAndCopySetup import bookandcopyinitialize
from studentSetup import studentinitialize


def button1_click(window):
    bookandcopyinitialize()


def button2_click(window):
    studentinitialize()


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

    # Create another label
    label2 = tk.Label(frame, text="Need in Files folder: students.csv and list_of_isbn_mine.txt", font=("Arial", 12))
    label2.pack()

    # Create Button 1
    button1 = tk.Button(frame, text="1: Books", width=10, command=lambda: button1_click(root))
    button1.pack(side=tk.LEFT, padx=5, pady=10)

    # Create Button 2
    button2 = tk.Button(frame, text="2: Students", width=10, command=lambda: button2_click(root))
    button2.pack(side=tk.LEFT, padx=5, pady=10)

    # Create a Close button
    close_button = tk.Button(frame, text="Close", width=10, command=root.destroy)
    close_button.pack(pady=10)

    # Run the main event loop
    root.mainloop()


if __name__ == "__main__":
    main()
