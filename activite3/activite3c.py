# coding: utf-8

print("ACTIVITÉ 3c")

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

#img.show()

# Redimensionnement de l'image source en une image de taille moitié
imageVignette = img.resize((largeur // 2, hauteur // 2), Image.BICUBIC) # Division par 2 de la taille (// permet de ne récupérer que le quotient de la division)
largeurVignette,hauteurVignette= imageVignette.size

# Création des vignettes avec filtre de couleur
image1 = Image.new(imageVignette.mode,imageVignette.size) #jaune R255 V255 B0
image2 = Image.new(imageVignette.mode,imageVignette.size)
image3 = Image.new(imageVignette.mode,imageVignette.size)
image4 = Image.new(imageVignette.mode,imageVignette.size)

# boucle de traitement des pixels pour appliquer filtre couleur
for x in range(largeurVignette):
    for y in range(hauteurVignette):
        pixel = imageVignette.getpixel((x,y))
        # Filtre jaune : absorbe le bleu
        #p = (int(255*0.4 + pixel[0]*0.6), int(255*0.4 + pixel[1]*0.6), int(0*0.4 + pixel[2]*0.6))
        p = (int(pixel[0]), int(pixel[1]), int(0))
        image1.putpixel((x,y), p)
        # Filtre magenta : absorbe le vert
        #p = (int(255*0.4 + pixel[0]*0.6), int(0*0.4 + pixel[1]*0.6), int(255*0.4 + pixel[2]*0.6))
        p = (int(pixel[0]), int(0), int(pixel[2]))
        image2.putpixel((x,y), p)				
        # Filtre bleu : absorbe le rouge
        #p = (int(0*0.4 + pixel[0]*0.6), int(255*0.4 + pixel[1]*0.6), int(255*0.4 + pixel[2]*0.6))
        p = (int(0), int(pixel[1]), int(pixel[2]))
        image3.putpixel((x,y), p)
        # Filtre vert : absorbe le rouge et le bleu
        #p = (int(0*0.4 + pixel[0]*0.6), int(255*0.4 + pixel[1]*0.6), int(0*0.4 + pixel[2]*0.6))
        p = (int(0), int(pixel[1]), int(0))
        image4.putpixel((x,y), p)

# Création d'une image avec les 4 vignettes colorées
imageFinale = Image.new(img.mode,img.size)
imageFinale.paste(im=image1, box=(0, 0))
imageFinale.paste(im=image2, box=(largeurVignette, 0))
imageFinale.paste(im=image3, box=(0, largeurVignette))
imageFinale.paste(im=image4, box=(largeurVignette, largeurVignette))

# Affichage de l'image et enregistrement
imageFinale.show()
imageFinale.save("./images/" + nomImage + "-filtres-couleurs" + ext)

# Fermeture du fichier image
img.close()
