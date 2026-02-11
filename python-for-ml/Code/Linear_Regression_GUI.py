import tkinter as tk
import numpy as np

class SalaryPredictorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Depi R4 - Machine Learning Diploma")
        self.root.geometry("400x200")
        self.create_widget()
        
    def create_widget(self):
        header = tk.Label(self.root, text = "Depi", bg = "blue", fg = "white", font = ("Arial", 16))
        header.pack(fill=tk.X)

if __name__ == "__main__":
    root = tk.Tk()
    app = SalaryPredictorApp(root)
    root.mainloop()    