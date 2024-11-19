def kt_guess(game, guess):
    if len(guess) != 1 or not guess.isalpha(): # Megfelelő input vizsgálata->szám / 1-nél több betű nem lehet
        return False
    return game.kt_check_guess(guess)
