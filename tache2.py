import randimport random

class Game:
    def _init_(self):
        self.target_number = random.randint(1, 100)
        self.attempts = 0
        self.guess = None

    def check_guess(self, guess):
        self.attempts += 1
        self.guess = guess
        if guess < self.target_number:
            return "C'est plus grand!"
        elif guess > self.target_number:
            return "C'est plus petit!"
        else:
            return f"Félicitations ! Vous avez deviné le nombre {self.target_number} en {self.attempts} essais."