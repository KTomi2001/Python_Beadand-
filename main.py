import tkinter as tk
from game import kt_functions
from kt_functions import kt_guess

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("app")
        self.root.geometry("600x400")

        self.game = kt_functions.kt_Game()

        self.label = tk.Label(root, text="Tippelj egy betűt!")
        self.label.pack()

        self.current_state_label = tk.Label(root, text=self.game.current_state)
        self.current_state_label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.guess_button = tk.Button(root, text="Tippelek", command=self.make_guess)
        self.guess_button.pack()

        self.new_game_button = tk.Button(root, text="Új játék", command=self.start_new_game)
        self.new_game_button.pack()

        self.status_label = tk.Label(root, text="")
        self.status_label.pack()

    def make_guess(self):
        guess = self.entry.get()
        self.entry.delete(0, tk.END)

        if self.game.attempts >= 10:
            self.status_label.config(text="Elérte a maximum próbálkozást, kezdjen új játékot.")
            return

        if kt_guess(self.game, guess):
            self.label.config(text="Talált!")
        else:
            self.label.config(text="Nem talált.")

        self.current_state_label.config(text=self.game.current_state)
        self.status_label.config(text=f"Próbálkozások: {self.game.attempts}/10")

        if self.game.is_game_over():
            if self.game.current_state == self.game.word:
                self.status_label.config(text="Gratulálunk, kitalálta a szót!")
            else:
                self.status_label.config(text="Elérte a maximum próbálkozást, kezdjen új játékot.")

    def start_new_game(self):
        self.game = kt_functions.kt_Game()
        self.label.config(text="Tippelj egy betűt!")
        self.current_state_label.config(text=self.game.current_state)
        self.status_label.config(text="Próbálkozások: 0/10")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
