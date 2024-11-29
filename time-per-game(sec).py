import tkinter as tk
from tkinter import messagebox

class GameUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Game Time Adjuster")

        self.time_per_game = 30  # Initialize to 30 seconds

        # Create the label
        self.time_label = tk.Label(master, text="Time per Game (sec)")
        self.time_label.pack(pady=10)

        # Create the display label
        self.time_display = tk.Label(master, text=f"Time per Game: {self.time_per_game} sec")
        self.time_display.pack(pady=10)

        # Create the subtract button
        self.subtract_button = tk.Button(master, text="-", command=self.subtract_time)
        self.subtract_button.pack(side=tk.LEFT, padx=20)

        # Create the add button
        self.add_button = tk.Button(master, text="+", command=self.add_time)
        self.add_button.pack(side=tk.RIGHT, padx=20)

    def subtract_time(self):
        if self.time_per_game > 0:
            self.time_per_game -= 1
            self.update_time_display()

    def add_time(self):
        self.time_per_game += 1
        self.update_time_display()

    def update_time_display(self):
        self.time_display.config(text=f"Time per Game: {self.time_per_game} sec")

# Create the main window
root = tk.Tk()
game_ui = GameUI(root)
root.mainloop()
