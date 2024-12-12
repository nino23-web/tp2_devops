import subprocess

# Exemple de vulnérabilité : injection de commande
def execute_command(user_input):
    command = f"echo {user_input}"
    subprocess.run(command, shell=True)  # Utiliser 'shell=True' est dangereux

# Exemple de code non sécurisé
password = "1234"  # Mot de passe codé en dur (non sécurisé)

if __name__ == "__main__":
    user_input = input("Entrez une commande : ")
    execute_command(user_input)
