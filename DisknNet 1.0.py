import tkinter as tk
from tkinter import messagebox
import os

def map_network_drive():
    # Récupérer l'URL saisie par l'utilisateur
    url = url_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    # Lettre du lecteur réseau à mapper
    drive_letter = drive_letter_entry.get().upper()

    if not url or not drive_letter:
        messagebox.showerror("Erreur", "L'URL et la lettre du lecteur sont obligatoires.")
        return

    # Commande pour mapper le lecteur réseau
    command = f'net use {drive_letter}: {url} /user:{username} {password}'

    try:
        result = os.system(command)
        if result == 0:
            messagebox.showinfo("Succès", f"Lecteur réseau {drive_letter}: mappé avec succès.")
        else:
            messagebox.showerror("Erreur", f"Échec de la connexion au lecteur réseau. Code d'erreur : {result}")
    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur est survenue : {str(e)}")

# Création de la fenêtre principale
root = tk.Tk()
root.title("DisknNet 1.0")
root.geometry("400x400")
root.config(bg="#f0f0f0")

# Ajout des widgets à la fenêtre
url_label = tk.Label(root, text="URL du lecteur réseau :", font=("Arial", 12), bg="#f0f0f0")
url_label.pack(pady=5)
url_entry = tk.Entry(root, font=("Arial", 12), width=40)
url_entry.pack(pady=5)

username_label = tk.Label(root, text="Nom d'utilisateur :", font=("Arial", 12), bg="#f0f0f0")
username_label.pack(pady=5)
username_entry = tk.Entry(root, font=("Arial", 12), width=40)
username_entry.pack(pady=5)

password_label = tk.Label(root, text="Mot de passe :", font=("Arial", 12), bg="#f0f0f0")
password_label.pack(pady=5)
password_entry = tk.Entry(root, font=("Arial", 12), show='*', width=40)
password_entry.pack(pady=5)

drive_letter_label = tk.Label(root, text="Lettre du lecteur (ex: Z) :", font=("Arial", 12), bg="#f0f0f0")
drive_letter_label.pack(pady=5)
drive_letter_entry = tk.Entry(root, font=("Arial", 12), width=5)
drive_letter_entry.pack(pady=5)

connect_button = tk.Button(root, text="Connecter", font=("Arial", 12), bg="#4CAF50", fg="#fff", command=map_network_drive)
connect_button.pack(pady=20)

# Exécution de la boucle principale
root.mainloop()
