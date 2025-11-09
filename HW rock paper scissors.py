import tkinter as tk
from tkinter import messagebox
import random
window = tk.Tk()
window.title("Rock Paper Scissors Game")
window.geometry("400x400")
window.config(bg="#F0F8FF")
choices = ["Rock", "Paper", "Scissors"]
def play(user_choice):
    computer_choice = random.choice(choices)
    result = ""
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")
title_label = tk.Label(window, text="Rock Paper Scissors", font=("Arial", 18, "bold"), bg="#F0F8FF")
title_label.pack(pady=20)
result_label = tk.Label(window, text="", font=("Arial", 14), bg="#F0F8FF")
result_label.pack(pady=20)
button_frame = tk.Frame(window, bg="#F0F8FF")
button_frame.pack(pady=10)
rock_button = tk.Button(button_frame, text="Rock", width=12, font=("Arial", 12), command=lambda: play("Rock"))
rock_button.grid(row=0, column=0, padx=5)
paper_button = tk.Button(button_frame, text="Paper", width=12, font=("Arial", 12), command=lambda: play("Paper"))
paper_button.grid(row=0, column=1, padx=5)
scissors_button = tk.Button(button_frame, text="Scissors", width=12, font=("Arial", 12), command=lambda: play("Scissors"))
scissors_button.grid(row=0, column=2, padx=5)
exit_button = tk.Button(window, text="Exit", font=("Arial", 12), bg="red", fg="white", command=window.quit)
exit_button.pack(pady=20)
window.mainloop()
