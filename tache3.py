import tkinter as tk
from tkinter import font
from tache2 import JeuDevinettes

class Interface:
    def init(self, root):
        self.root = root
        self.root.title("Jeu de Devinettes")
        self.root.geometry("400x400")
        self.root.configure(bg="#5c95ff")  # Bleu vif

        # Police personnalisée
        self.custom_font = font.Font(family="Helvetica", size=14)

        # Widgets de l'interface
        self.header_label = tk.Label(root, text="Bienvenue au Jeu de Devinettes!", bg="#5c95ff", font=font.Font(family="Helvetica", size=16, weight="bold"), fg="#ffffff")  # Blanc
        self.header_label.pack(pady=20)

        self.question_label = tk.Label(root, text="", wraplength=300, bg="#5c95ff", font=self.custom_font, fg="#ffffff")  # Blanc
        self.entry_reponse = tk.Entry(root, font=self.custom_font, width=30, bd=2, relief="groove", fg="#000000", bg="#ffffff")  # Blanc
        self.submit_button = tk.Button(root, text="Soumettre", command=self.submit_response, bg="#ff4081", font=self.custom_font, padx=10, pady=5, fg="#ffffff")  # Rose vif
        self.start_button = tk.Button(root, text="Démarrer le jeu", command=self.start_game, bg="#76ff03", font=self.custom_font, padx=10, pady=5, fg="#000000")  # Vert vif
        self.start_button.pack(pady=10)

        # Label pour afficher les essais restants
        self.essais_label = tk.Label(root, text="Essais restants : 3", bg="#5c95ff", font=self.custom_font, fg="#ffffff")  # Blanc

    def start_game(self):
        global jeu
        jeu = JeuDevinettes()
        self.start_button.pack_forget()  # Cache le bouton de démarrage
        self.header_label.pack_forget()  # Cache le label de bienvenue
        self.question_label.pack(pady=10)  # Affiche le label de question
        self.entry_reponse.pack(pady=10)  # Affiche le champ de réponse
        self.submit_button.pack(pady=10)  # Affiche le bouton de soumission
        self.essais_label.pack(pady=10)  # Affiche le label d'essais restants
        self.afficher_question()

    def afficher_question(self):
        question = jeu.afficher_question()
        self.question_label.config(text=question)
        self.entry_reponse.delete(0, tk.END)
        self.essais_label.config(text=f"Essais restants : {jeu.essais_restants}")

    def submit_response(self):
        reponse_utilisateur = self.entry_reponse.get()
        jeu.verifier_reponse(reponse_utilisateur)
        self.afficher_question()
        self.essais_label.config(text=f"Essais restants : {jeu.essais_restants}")
    # API_KEY = "hgfhghjhgbvcxccvcvc"
    # PASSXORD = "ghfhfgh"
