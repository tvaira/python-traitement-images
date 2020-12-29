# coding: utf-8

print("ACTIVITÉ 3d")

# PIL est une bibliothèque de traitement d'image
import PIL;
print("PIL version ", PIL.__version__)

# on importe le module Image de la bibliothèque PIL
from PIL import Image, ImageFilter

import numpy as np

# Lenna !
#nomImage = "lenna_10"
#ext = ".jpeg"

import tkinter as tk # en python 3
from tkinter import filedialog

ecran = tk.Tk()
ecran.withdraw()

# choisir un fichier image
fichierImage =  filedialog.askopenfilename(initialdir = "./images/",title = "Choisir un fichier image",filetypes = (("fichiers jpeg","*.jpg"),("fichiers jpeg","*.jpeg"),("fichiers png","*.png"),("all files","*.*")))
if not fichierImage:
    exit()

import os
fichier = os.path.basename(fichierImage)
path = os.path.dirname(fichierImage)
nomImage = os.path.splitext(fichier)[0] # "felix-le-chat"     # mode P
ext = os.path.splitext(fichier)[1] # ".png"

# Une image avec du bruit
img = Image.open(path + "/" + nomImage + ext);

# Affiche les informations sur l'image
print(img.format, img.size, img.mode)
print("Fichier :", img.filename)
print("L =", img.width, "x H =", img.height)
largeur, hauteur = img.size

imgNG = img.convert('L') # conversion en niveaux de gris
imgNG.show()

# image -> tableau numpy
matriceImageNG = np.array(imgNG)
lignes, colonnes = matriceImageNG.shape
print(lignes, "x", colonnes)
print(matriceImageNG.ndim, "dimensions")

if lignes != colonnes:
    exit()

# Principe : Filtre médian (3 x 3)
filtreMedianImageNG = matriceImageNG.copy()
matricePixels = np.zeros((9))

for i in range(colonnes-1):
    for j in range(lignes-1):
        if j > 0 and i > 0:
            matricePixels[0] = matriceImageNG[i-1][j-1]
            matricePixels[1] = matriceImageNG[i-1][j]
            matricePixels[2] = matriceImageNG[i-1][j+1]
            matricePixels[3] = matriceImageNG[i][j-1]
            matricePixels[4] = matriceImageNG[i][j]
            matricePixels[5] = matriceImageNG[i][j+1]
            matricePixels[6] = matriceImageNG[i+1][j-1]
            matricePixels[7] = matriceImageNG[i+1][j]
            matricePixels[8] = matriceImageNG[i+1][j+1]
            s = np.sort(matricePixels, axis=None)  
            filtreMedianImageNG[i][j] = s[4] # on prend la valeur médiane

filtreMedianNG = Image.fromarray(filtreMedianImageNG, 'L')
filtreMedianNG.show()
filtreMedianNG.save(path + "/" + nomImage + "-filtre-median" + ext);

# sinon avec le module ImageFilter (5 x 5)
im2 = imgNG.filter(ImageFilter.MedianFilter(5))
im2.show()

# Fermeture des fichiers
img.close()
filtreMedianNG.close()
