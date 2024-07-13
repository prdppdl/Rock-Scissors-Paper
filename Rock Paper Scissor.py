
import os
import random
import tkinter as tk
from tkinter import filedialog, messagebox

# Class to track scores
class ScoreTracker:
    def __init__(self):
        self.user_scores = [0] * 5  # Array of user scores
        self.computer_scores = [0] * 5  # Array of computer scores

    def update_user_score(self, round, score):
        self.user_scores[round] = score

    def update_computer_score(self, round, score):
        self.computer_scores[round] = score

    def display_scores(self):
        return f"User Scores: {self.user_scores}\nComputer Scores: {self.computer_scores}"

# Player class with multiple instance variables
class Player:
    def __init__(self, name, age, score=0, level=1):
        self.name = name
        self.age = age
        self.score = score
        self.level = level

# Game class that uses a modular approach
class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors Game")

        self.player_move_label = tk.Label(root, text="Enter your move (ROCK, PAPER, or SCISSORS):")
        self.player_move_label.pack()

        self.player_move_entry = tk.Entry(root)
        self.player_move_entry.pack()

        self.submit_button = tk.Button(root, text="Submit", command=self.play)
        self.submit_button.pack()

        self.save_button = tk.Button(root, text="Save Result", command=self.save_result)
        self.save_button.pack()

        self.read_button = tk.Button(root, text="Read Result", command=self.read_result)
        self.read_button.pack()

        self.tracker = ScoreTracker()
        self.player = Player("Player1", 25)  # Example player instance

    def play(self):
        player_move = self.player_move_entry.get().upper()
        if player_move not in ["ROCK", "PAPER", "SCISSORS"]:
            messagebox.showerror("Error", "Invalid input. Please enter ROCK, PAPER, or SCISSORS.")
            return

        moves = ["ROCK", "PAPER", "SCISSORS"]
        computer_move = random.choice(moves)

        result = self.determine_winner(player_move, computer_move)
        messagebox.showinfo("Result", f"Computer's move: {computer_move}\nResult: {result}")

        # Update scores based on result
        if result == "Player wins":
            self.tracker.update_user_score(0, self.tracker.user_scores[0] + 1)
        elif result == "Computer wins":
            self.tracker.update_computer_score(0, self.tracker.computer_scores[0] + 1)

    def save_result(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            player_move = self.player_move_entry.get().upper()
            moves = ["ROCK", "PAPER", "SCISSORS"]
            computer_move = random.choice(moves)
            result = self.determine_winner(player_move, computer_move)

            with open(file_path, "w") as file:
                file.write(f"Player's move: {player_move}\n")
                file.write(f"Computer's move: {computer_move}\n")
                file.write(f"Result: {result}\n")
                file.write(self.tracker.display_scores())
            messagebox.showinfo("Save Result", "Result saved successfully.")

    def read_result(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                messagebox.showinfo("Read Result", file.read())

    def determine_winner(self, player_move, computer_move):
        if player_move == computer_move:
            return "Draw"
        elif (player_move == "ROCK" and computer_move == "SCISSORS") or \
             (player_move == "PAPER" and computer_move == "ROCK") or \
             (player_move == "SCISSORS" and computer_move == "PAPER"):
            return "Player wins"
        else:
            return "Computer wins"

# Example of class with multiple options for object construction
class GameResult:
    def __init__(self, player_choice, computer_choice, result, timestamp=None):
        self.player_choice = player_choice
        self.computer_choice = computer_choice
        self.result = result
        self.timestamp = timestamp if timestamp else self.get_current_time()

    def get_current_time(self):
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsGame(root)
    root.mainloop()
