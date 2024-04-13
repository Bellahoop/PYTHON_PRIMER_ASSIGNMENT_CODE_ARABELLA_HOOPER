import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle

class PalindromeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PALINDROME CHECKER")
        self.geometry("500x300")
        self.configure(bg="#FFC0CB")
        self.entry = None
        self.create_widgets()

    def create_widgets(self):
        self.create_labels()
        self.create_entry_and_button()
        self.create_result_label()

    def create_labels(self):
        labels_data = [
            ("WELCOME TO THE PALINDROME CHECKER!", "#2d3674", 16, "bold"),
            ("A palindrome is a word, phrase, or sequence that reads the same backwards as forwards", None, 12, ""),
            ("Please enter a word or phrase you would like to check:", "#ffffff", 14, "bold"),
            ("Examples of palindromes: Madam, level, Was it a cat I saw", None, 10, "")
        ]
        for text, fg, font_size, font_style in labels_data:
            self.create_label(text, fg, font_size, font_style)

    def create_label(self, text, fg, font_size, font_style):
        font = ("Arial", font_size, font_style)
        bg_color = "#d95e99" if text.startswith("Please enter") else "#FFC0CB"
        label = tk.Label(self, text=text, fg=fg, bg=bg_color, font=font)
        label.pack(pady=(10, 0))

    def create_entry_and_button(self):
        self.create_entry()
        self.create_button()

    def create_entry(self):
        self.entry = tk.Entry(self, bg="#e0e0e0")
        self.entry.pack(pady=10, padx=10, ipady=3, fill=tk.X)

    def create_button(self):
        style = ThemedStyle(self)
        style.configure("TButton", foreground="#d95e99", font=("Arial", 16, "bold"))
        button = ttk.Button(self, text="CHECK", command=self.check_palindrome, style="TButton")
        button.pack(pady=5, ipadx=10)

    def create_result_label(self):
        self.result_label = tk.Label(self, bg="#FFC0CB", font=("Arial", 16, "bold"))
        self.result_label.pack(pady=10)

    def clean_word(self, word):
        return ''.join(char.lower() for char in word if char.isalnum())

    def is_palindrome(self, word):
        word = self.clean_word(word)
        return word == word[::-1]

    def check_palindrome(self):
        if self.entry:
            word = self.entry.get().lower()
            clean_word = self.clean_word(word)
            reversed_word = self.is_palindrome(word)
            self.result_label.config(text=f"Input: {clean_word} \n{word} {'is' if reversed_word else 'is not'} a palindrome", fg="#008000" if reversed_word else "#d40000")

if __name__ == "__main__":
    app = PalindromeApp()
    app.mainloop()