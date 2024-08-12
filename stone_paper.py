import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")
        
        self.user_score = 0
        self.computer_score = 0
        self.rounds = 0
        self.max_rounds = 5
        
        self.create_widgets()
    
    def create_widgets(self):
        # Create main frame
        main_frame = tk.Frame(self.root, padx=20, pady=20)
        main_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Game Instructions
        self.instructions = tk.Label(main_frame, text="Choose Rock, Paper, or Scissors:", font=("Helvetica", 14))
        self.instructions.pack(pady=10)
        
        # Buttons for user choice
        button_frame = tk.Frame(main_frame)
        button_frame.pack(pady=10)
        
        self.rock_button = tk.Button(button_frame, text="Rock", command=lambda: self.play("rock"))
        self.rock_button.pack(side=tk.LEFT, padx=5)
        
        self.paper_button = tk.Button(button_frame, text="Paper", command=lambda: self.play("paper"))
        self.paper_button.pack(side=tk.LEFT, padx=5)
        
        self.scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: self.play("scissors"))
        self.scissors_button.pack(side=tk.LEFT, padx=5)
        
        # Result Area
        self.result_frame = tk.Frame(main_frame)
        self.result_frame.pack(pady=10)
        
        self.user_choice_label = tk.Label(self.result_frame, text="", font=("Helvetica", 12))
        self.user_choice_label.pack()
        
        self.computer_choice_label = tk.Label(self.result_frame, text="", font=("Helvetica", 12))
        self.computer_choice_label.pack()
        
        self.result_label = tk.Label(self.result_frame, text="", font=("Helvetica", 12))
        self.result_label.pack()
        
        self.score_label = tk.Label(main_frame, text="User Score: 0 | Computer Score: 0", font=("Helvetica", 12))
        self.score_label.pack(pady=10)
        
        self.play_again_button = tk.Button(main_frame, text="Play Again", command=self.ask_play_again)
        self.play_again_button.pack(pady=10)
    
    def play(self, user_choice):
        if self.rounds < self.max_rounds:
            choices = ["rock", "paper", "scissors"]
            computer_choice = random.choice(choices)
            result = self.determine_winner(user_choice, computer_choice)
            
            self.rounds += 1
            self.update_scores(result)
            self.display_result(user_choice, computer_choice, result)
            
            if self.rounds == self.max_rounds:
                self.end_game()
        else:
            messagebox.showinfo("Game Over", "The game is over. Please reset to play again.")
    
    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "tie"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            return "win"
        else:
            return "lose"
    
    def update_scores(self, result):
        if result == "win":
            self.user_score += 1
        elif result == "lose":
            self.computer_score += 1
    
    def display_result(self, user_choice, computer_choice, result):
        self.user_choice_label.config(text=f"Your choice: {user_choice.capitalize()}")
        self.computer_choice_label.config(text=f"Computer's choice: {computer_choice.capitalize()}")
        
        if result == "tie":
            self.result_label.config(text="It's a tie!")
        elif result == "win":
            self.result_label.config(text="You win this round!")
        else:
            self.result_label.config(text="You lose this round!")
        
        self.score_label.config(text=f"User Score: {self.user_score} | Computer Score: {self.computer_score}")
    
    def end_game(self):
        final_result = "Game Over!\n"
        if self.user_score > self.computer_score:
            final_result += "You won the game!"
        elif self.user_score < self.computer_score:
            final_result += "Computer won the game!"
        else:
            final_result += "The game is a tie!"
        
        self.result_label.config(text=final_result)
        self.rock_button.config(state=tk.DISABLED)
        self.paper_button.config(state=tk.DISABLED)
        self.scissors_button.config(state=tk.DISABLED)
        
        self.ask_play_again()
    
    def ask_play_again(self):
        response = messagebox.askyesno("Play Again", "Do you want to play another round?")
        if response:
            self.reset_game()
        else:
            self.root.quit()
    
    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.rounds = 0
        
        self.user_choice_label.config(text="")
        self.computer_choice_label.config(text="")
        self.result_label.config(text="")
        self.score_label.config(text="User Score: 0 | Computer Score: 0")
        
        self.rock_button.config(state=tk.NORMAL)
        self.paper_button.config(state=tk.NORMAL)
        self.scissors_button.config(state=tk.NORMAL)

# Create the main window
root = tk.Tk()
app = RockPaperScissorsGame(root)
root.mainloop()
