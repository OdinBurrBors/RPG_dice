from tkinter import *
import random

# Création de la fenêtre principale
fenetre = Tk()
fenetre.title("Lancement de dés")

# Fonction pour lancer le dé 10
def lance_de_10():
    resultat = random.randint(1, 10)
    message.configure(text=resultat)

# Fonction pour lancer le dé 20
def lance_de_20():
    resultat = random.randint(1, 20)
    message.configure(text=resultat)

# Fonction pour lancer le dé 100
def lance_de_100():
    resultat = random.randint(1, 100)
    message.configure(text=resultat)

# Création des boutons
bouton_de_10 = Button(fenetre, text="Lancer le dé 10", command=lance_de_10)
bouton_de_20 = Button(fenetre, text="Lancer le dé 20", command=lance_de_20)
bouton_de_100 = Button(fenetre, text="Lancer le dé 100", command=lance_de_100)

# Création du label pour afficher le résultat
message = Label(fenetre)

# Affichage des boutons et du label
bouton_de_10.pack()
bouton_de_20.pack()
bouton_de_100.pack()
message.pack()

fenetre.mainloop()