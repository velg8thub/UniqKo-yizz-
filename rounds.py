import tkinter as tk
from tkinter import messagebox

class Game:
    def __init__(self, rounds):
        self.rounds = rounds

    def adjust_rounds(self, change):
        new_rounds = self.rounds + change
        if new_rounds > 0:
            self.rounds = new_rounds
            return True
        else:
            return False

    def get_rounds(self):
        return self.rounds


class GameUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Round Adjuster")

        self.game = Game(5)  # Initialize with 5 rounds

        self.rounds_label = tk.Label(master, text=f"Rounds: {self.game.get_rounds()}")
        self.rounds_label.pack(pady=10)

        # Subtract button from our UI
        self.subtract_button = tk.Button(master, text="Subtract Round", command=self.subtract_round)
        self.subtract_button.pack(side=tk.LEFT, padx=20)

        # Add button from our UI
        self.add_button = tk.Button(master, text="Add Round", command=self.add_round)
        self.add_button.pack(side=tk.RIGHT, padx=20)

    def subtract_round(self):
        self.update_rounds(-1)

    def add_round(self):
        self.update_rounds(1)

    def update_rounds(self, change):
        if self.game.adjust_rounds(change):
            self.rounds_label.config(text=f"Rounds: {self.game.get_rounds()}")
        else:
            messagebox.showwarning("Warning", "Number of rounds must be positive.")

    def on_closing(self):
        self.master.destroy()

# Create the main window
root = tk.Tk()
game_ui = GameUI(root)
root.protocol("WM_DELETE_WINDOW", game_ui.on_closing)  # Handle window close event
root.mainloop()
