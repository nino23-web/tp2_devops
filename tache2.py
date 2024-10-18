from tache1 import obtenir_questions
from tkinter import messagebox

class JeuDevinettes:
    def _init_(self):
        self.questions = obtenir_questions()
        self.bonne_reponse = 0
        self.index_question = 0
        self.essais_restants = 3  # Nombre d'essais restants

    def verifier_reponse(self, reponse_utilisateur):
        if self.index_question < len(self.questions):
            question = self.questions[self.index_question]
            if reponse_utilisateur.lower() == question['reponse'].lower():
                self.bonne_reponse += 1
                messagebox.showinfo("Résultat", "Bonne réponse !")
            else:
                messagebox.showinfo("Résultat", f"Mauvaise réponse ! La bonne réponse était : {question['reponse']}")
                self.essais_restants -= 1  # Décrementer le nombre d'essais restants

            if self.essais_restants <= 0:  # Vérifier si les essais sont épuisés
                self.afficher_score()
            else:
                self.index_question += 1
                self.afficher_question()
                self.mettre_a_jour_essais()
        else:
            self.afficher_score()

    def afficher_question(self):
        if self.index_question < len(self.questions):
            question = self.questions[self.index_question]['question']
            return question
        else:
            self.afficher_score()

    def afficher_score(self):
        score = (self.bonne_reponse / len(self.questions)) * 100
        messagebox.showinfo("Fin du jeu", f"Votre score est : {score:.2f}%")
        self.reset()

    def mettre_a_jour_essais(self):
        return self.essais_restants

    def reset(self):
        self.bonne_reponse = 0
        self.index_question = 0
        self.essais_restants = 3
        self.mettre_a_jour_essais()
        return self.afficher_question()
