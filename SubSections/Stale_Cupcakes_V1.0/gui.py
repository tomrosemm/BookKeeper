# import tkinter as tk
# from controller import Controller
#
# class GUI:
#     def __init__(self, root):
#         self.root = root
#         self.controller = Controller()
#
#         self.entry = tk.Entry(self.root)
#         self.entry.pack()
#
#         self.button = tk.Button(self.root, text="Process", command=self.process_data)
#         self.button.pack()
#
#     def process_data(self):
#         data = self.entry.get()
#         processed_data = self.controller.process_data_from_gui(data)
#         # Do something with the processed data, e.g., display it in a label
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = GUI(root)
#     root.mainloop()
