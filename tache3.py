import tkinter as tk
from tache2 import Game
from tache4 import get_user_guess, display_message

def setup_gui(game):
    window = tk.Tk()
    window.title("Jeu de Devinette")

    def on_submit():
        guess = get_user_guess(entry)
        message = game.check_guess(guess)
        display_message(label, message)

    label = tk.Label(window, text="Devinez le nombre entre 1 et 100")
    label.pack()

    entry = tk.Entry(window)
    entry.pack()

    submit_button = tk.Button(window, text="Soumettre", command=on_submit)
    submit_button.pack()

    window.mainloop()
