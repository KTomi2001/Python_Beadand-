import random

def kt_guess(game, guess):
    if len(guess) != 1 or not guess.isalpha():
        return False
    return game.kt_check_guess(guess)

class kt_Game:
    def __init__(self):
        self.words = ["alma", "banán", "citrom", "narancs"]
        self.word = random.choice(self.words)
        self.current_state = "_" * len(self.word)
        self.attempts = 0
        self.max_attempts = 10

    def kt_check_guess(self, guess):
        new_state = list(self.current_state)
        found = False
        for idx, char in enumerate(self.word):
            if char == guess:
                new_state[idx] = char
                found = True
        self.current_state = "".join(new_state)
        self.attempts += 1
        return found

    def is_game_over(self):
        return self.current_state == self.word or self.attempts >= self.max_attempts

