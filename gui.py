import tkinter as tk
import random

class GuessGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")

        self.number = random.randint(1, 100)

        self.label = tk.Label(root, text="Guess a number (1-100)")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.result = tk.Label(root, text="")
        self.result.pack()

        self.button = tk.Button(root, text="Submit", command=self.check)
        self.button.pack()

        self.reset_btn = tk.Button(root, text="Reset", command=self.reset)
        self.reset_btn.pack()

    def check(self):
        guess = int(self.entry.get())

        if guess < self.number:
            self.result.config(text="Too Low!")
        elif guess > self.number:
            self.result.config(text="Too High!")
        else:
            self.result.config(text="Correct! 🎉")

    def reset(self):
        self.number = random.randint(1, 100)
        self.result.config(text="")
        self.entry.delete(0, tk.END)

root = tk.Tk()
game = GuessGame(root)
root.mainloop()