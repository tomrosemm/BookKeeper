import customtkinter as ctk
import tkinter as tk

# Basic parameters and initializations
# Supported modes : Light, Dark, System
ctk.set_appearance_mode("System")

# Supported themes : green, dark-blue, blue
ctk.set_default_color_theme("green")

# App Class
class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.attributes('-fullscreen', True)  # Make the window fullscreen
        self.bind("<Escape>", lambda event: self.destroy())  # Bind Escape key to close the window

        # Create a frame covering the entire window and set its background color
        self.bg_frame = tk.Frame(self, bg="#008e00")
        self.bg_frame.place(relwidth=1, relheight=1)

        # Center coordinates
        center_x = self.winfo_screenwidth() // 2
        center_y = self.winfo_screenheight() // 2

        # Name Label
        self.nameLabel = ctk.CTkLabel(self.bg_frame, text="Name")
        self.nameLabel.place(x=center_x - 150, y=center_y - 200)

        # Name Entry Field
        self.nameEntry = ctk.CTkEntry(self.bg_frame, placeholder_text="Teja")
        self.nameEntry.place(x=center_x - 50, y=center_y - 200)

        # Age Label
        self.ageLabel = ctk.CTkLabel(self.bg_frame, text="Age")
        self.ageLabel.place(x=center_x - 150, y=center_y - 150)

        # Age Entry Field
        self.ageEntry = ctk.CTkEntry(self.bg_frame, placeholder_text="18")
        self.ageEntry.place(x=center_x - 50, y=center_y - 150)

        # Gender Label
        self.genderLabel = ctk.CTkLabel(self.bg_frame, text="Gender")
        self.genderLabel.place(x=center_x - 150, y=center_y - 100)

        # Gender Radio Buttons
        self.genderVar = tk.StringVar(value="Prefer not to say")

        self.maleRadioButton = ctk.CTkRadioButton(self.bg_frame, text="Male", variable=self.genderVar, value="He is")
        self.maleRadioButton.place(x=center_x - 50, y=center_y - 100)

        self.femaleRadioButton = ctk.CTkRadioButton(self.bg_frame, text="Female", variable=self.genderVar, value="She is")
        self.femaleRadioButton.place(x=center_x + 50, y=center_y - 100)

        self.noneRadioButton = ctk.CTkRadioButton(self.bg_frame, text="Prefer not to say", variable=self.genderVar, value="They are")
        self.noneRadioButton.place(x=center_x + 150, y=center_y - 100)

        # Choice Label
        self.choiceLabel = ctk.CTkLabel(self.bg_frame, text="Choice")
        self.choiceLabel.place(x=center_x - 150, y=center_y - 50)

        # Choice Check boxes
        self.checkboxVar = tk.StringVar(value="Choice 1")

        self.choice1 = ctk.CTkCheckBox(self.bg_frame, text="choice 1", variable=self.checkboxVar, onvalue="choice1", offvalue="c1")
        self.choice1.place(x=center_x - 50, y=center_y - 50)

        self.choice2 = ctk.CTkCheckBox(self.bg_frame, text="choice 2", variable=self.checkboxVar, onvalue="choice2", offvalue="c2")
        self.choice2.place(x=center_x + 50, y=center_y - 50)

        # Occupation Label
        self.occupationLabel = ctk.CTkLabel(self.bg_frame, text="Occupation")
        self.occupationLabel.place(x=center_x - 150, y=center_y)

        # Occupation combo box
        self.occupationOptionMenu = ctk.CTkOptionMenu(self.bg_frame, values=["Student", "Working Professional"])
        self.occupationOptionMenu.place(x=center_x - 50, y=center_y)

        # Generate Button
        self.generateResultsButton = ctk.CTkButton(self.bg_frame, text="Generate Results")
        self.generateResultsButton.place(x=center_x - 50, y=center_y + 50)

        # Text Box
        self.displayBox = ctk.CTkTextbox(self.bg_frame, width=200, height=100)
        self.displayBox.place(x=center_x - 100, y=center_y + 100)


if __name__ == "__main__":
    app = App()
    app.mainloop()
