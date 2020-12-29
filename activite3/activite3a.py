# coding: utf-8

print("ACTIVITÉ 3a")

# PIL est une bibliothèque de traitement d'image
import PIL;
print("PIL version ", PIL.__version__)

# on importe le module Image de la bibliothèque PIL
from PIL import Image

import numpy as np
import random as rd

import tkinter as tk # en python 3
from tkinter import filedialog

ecran = tk.Tk()
ecran.withdraw()

# choisir un fichier image
fichierImage =  filedialog.askopenfilename(initialdir = "./images/",title = "Choisir un fichier image",filetypes = (("fichiers png","*.png"), ("fichiers jpeg","*.jpg"),("fichiers jpeg","*.jpeg"),("all files","*.*")))
if not fichierImage:
    exit()

import os
fichier = os.path.basename(fichierImage)
path = os.path.dirname(fichierImage)
nomImage = os.path.splitext(fichier)[0] # "felix-le-chat"     # mode P
ext = os.path.splitext(fichier)[1] # ".png"

# Une image de felix le chat !
img = Image.open(path + "/" + nomImage + ext);

# Affiche les informations sur l'image
print(img.format, img.size, img.mode)
print("Fichier :", img.filename)
print("L =", img.width, "x H =", img.height)
largeur, hauteur = img.size # Récupération de la largeur et hauteur de l'image

imgNG = img.convert('L') # conversion en niveaux de gris
imgNG.show()

# image -> tableau numpy (matrice)
matriceImageNG = np.array(imgNG)
lignes, colonnes = matriceImageNG.shape
print(lignes, "x", colonnes)
print(matriceImageNG.ndim, "dimensions")
print("")

# Affiche les pixels en noir (0) ou blanc (1)
#print(matriceImageNG)
for i in range(0,lignes):
    for j in range(0,colonnes):
        if(matriceImageNG[i,j] > 128):
            print(repr(1).rjust(1), end=' ')
        else:
            print(repr(0).rjust(1), end=' ')
        # ou :
        #print(repr(matriceImageNG[i,j]).rjust(3), end=' ')
    print("")
print("")

# transposée de l'image imgNG avec numpy
#matriceTransposeImageNG = matriceImageNG.transpose()
#print(matriceTransposeImageNG)

# transposée de l'image imgNG à la main
matriceTransposeImageNG = matriceImageNG.copy()
for i in range(0,lignes):
    for j in range(0,colonnes):
       matriceTransposeImageNG[j][i] = matriceImageNG[i][j]

# Affiche les pixels noir (0) ou blanc (1)
#print(matriceTransposeImageNG)
for i in range(0,lignes):
    for j in range(0,colonnes):
        if(matriceTransposeImageNG[i,j] > 128):
            print(repr(1).rjust(1), end=' ')
        else:
            print(repr(0).rjust(1), end=' ')
    print("")
print("")

# tableau numpy (matrice) -> image
imageNG = Image.fromarray(matriceTransposeImageNG, 'L')
imageNG.show()

imageNG.save(path + "/" + nomImage + "-transpose" + ext);

# Autres : image aléatoire
#matriceAleatoire = np.array([[rd.randrange(256) for k in range(100)] for i in range(100)])
#imageAleatoire = Image.fromarray(matriceAleatoire, 'L')
#imageAleatoire.show()

# Fermeture des fichiers
img.close()
imageNG.close()
