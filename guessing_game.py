import random
import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("450x350")
root.config(bg="#ffffff")  # White background for a clean look
root.resizable(False, False)

# Generate the secret number
secret_number = random.randint(1, 100)
attempts = 0

# Function to handle guess submission
def check_guess():
    global attempts
    guess = entry_guess.get()

    # Check if the input is a valid number
    if not guess.isdigit():
        messagebox.showerror("Invalid Input", "Please enter a valid number.")
        entry_guess.delete(0, tk.END)  # Clear invalid input
        return

    guess = int(guess)
    attempts += 1

    # Provide feedback based on the guess
    if guess < secret_number:
        label_feedback.config(text=f"📉 Too low! Guess Again!", fg="#e63946")  # Red for too low
    elif guess > secret_number:
        label_feedback.config(text=f"📈 Too high! Guess Again!", fg="#e63946")  # Red for too high
    else:
        label_feedback.config(text=f"🎉 You guessed it in {attempts} attempts!", fg="#2a9d8f")  # Green for success
        # Disable further guesses once the correct number is guessed
        entry_guess.config(state='disabled')
        btn_guess.config(state='disabled')

    entry_guess.delete(0, tk.END)  # Clear input after each guess

# Function to reset the game
def reset_game():
    global secret_number, attempts
    # Generate a new secret number
    secret_number = random.randint(1, 100)
    attempts = 0
    label_feedback.config(text="Game reset! Start guessing again.", fg="#457b9d")  # Blue for reset message
    # Re-enable input and buttons
    entry_guess.config(state='normal')
    btn_guess.config(state='normal')
    entry_guess.delete(0, tk.END)  # Clear the guess input

# GUI Components
label_title = tk.Label(root, text="Number Guessing Game", font=("Helvetica", 22, "bold"), bg="#ffffff", fg="#1d3557")  # Dark blue title
label_title.pack(pady=20)

label_instruction = tk.Label(root, text="Guess a number between 1 and 100", font=("Helvetica", 14), bg="#ffffff", fg="#1d3557")  # Dark blue instruction
label_instruction.pack(pady=10)

entry_guess = tk.Entry(root, font=("Helvetica", 16), justify='center', bd=3)
entry_guess.pack(pady=10)

# Button with black text for better visibility
btn_guess = tk.Button(root, text="Submit Guess", command=check_guess, font=("Helvetica", 14), bg="#2a9d8f", fg="black", bd=2)  # Green button with black text
btn_guess.pack(pady=10)

label_feedback = tk.Label(root, text="Start guessing...", font=("Helvetica", 12), bg="#ffffff", fg="#457b9d")  # Blue feedback
label_feedback.pack(pady=20)

# Button with black text for better visibility
btn_reset = tk.Button(root, text="Reset Game", command=reset_game, font=("Helvetica", 12), bg="#e63946", fg="black", bd=2)  # Red reset button with black text
btn_reset.pack(pady=10)

# Start the GUI event loop
root.mainloop()
