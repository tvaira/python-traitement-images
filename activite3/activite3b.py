# coding: utf-8

print("ACTIVITÉ 3b")

# PIL est une bibliothèque de traitement d'image
import PIL;
print("PIL version ", PIL.__version__)

# on importe le module Image de la bibliothèque PIL
from PIL import Image

import numpy as np

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

# image -> tableau numpy
matriceImageNG = np.array(imgNG)
lignes, colonnes = matriceImageNG.shape
print(lignes, "x", colonnes)
print(matriceImageNG.ndim, "dimensions")

# Symétrie verticale
symetrieVerticaleImageNG = matriceImageNG.copy()
for x in range(0,colonnes):
    for y in range(0,lignes):
       symetrieVerticaleImageNG[x][lignes-y-1] = matriceImageNG[x][y]

imageVerticaleNG = Image.fromarray(symetrieVerticaleImageNG, 'L')
imageVerticaleNG.show()
imageVerticaleNG.save(path + "/" + nomImage + "-symetrie-verticale" + ext);

# tag::snippet-symetrie-rotation[] 
# Symétrie horizontale
symetrieHorizontaleImageNG = matriceImageNG.copy()
for x in range(0,colonnes):
    for y in range(0,lignes):
       symetrieHorizontaleImageNG[-x+colonnes-1][y] = matriceImageNG[x][y]

imageHorizontaleNG = Image.fromarray(symetrieHorizontaleImageNG, 'L')
imageHorizontaleNG.show()
imageHorizontaleNG.save(path + "/" + nomImage + "-symetrie-horizontale" + ext);

# Rotation
rotationImageNG = matriceImageNG.copy()
for x in range(0,colonnes):
    for y in range(0,lignes):
       rotationImageNG[colonnes-x-1][lignes-y-1] = matriceImageNG[x][y]

imageRotationNG = Image.fromarray(rotationImageNG, 'L')
imageRotationNG.show()
imageRotationNG.save(path + "/" + nomImage + "-rotation" + ext);
# end::snippet-symetrie-rotation[]

# Fermeture des fichiers
img.close()
imageHorizontaleNG.close()
imageVerticaleNG.close()
imageRotationNG.close()
