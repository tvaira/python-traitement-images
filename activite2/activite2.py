# coding: utf-8

print("ACTIVITÉ 2")

# PIL est une bibliothèque de traitement d'image
import PIL;
print("PIL version ", PIL.__version__)

# on importe le module Image de la bibliothèque PIL
from PIL import Image

#"felix-the-cat-nb.png" -> mode RGB
#"felix-le-chat.png"    -> mode P

#import Tkinter as tk # en python 2
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

#imgNG = img.convert('L') # conversion en niveaux de gris
#imgNG.show()

# Affiche les informations sur l'image
print(img.format, img.size, img.mode)
print("Fichier :", img.filename)
print("L =", img.width, "x H =", img.height)
largeur, hauteur = img.size # Récupération de la largeur et hauteur de l'image
#print("L =", largeur, "x H =", hauteur)
print("Nombre de pixels =", (img.width*img.height) , "pixels")
#print("Nombre de pixels =", (largeur*hauteur) , "pixels")

# Création d'une nouvelle image de même type
nouvelleImage = Image.new(img.mode, img.size)

# Affiche les valeurs des pixels
if(img.width*img.height < 2000): # pour les petites images
    print("Affiche les valeurs des pixels de l'image d'origine")
    for x in range(largeur):
        for y in range(hauteur):
            # récupére les valeurs du pixel
            pixel = img.getpixel((x,y))
            if(isinstance(pixel, int)):
                gris = pixel
            elif(isinstance(pixel, tuple)):
                # calcul du poids de chaque composante du gris dans le pixel (CIE709)
                gris = int(0.2125 * pixel[0] + 0.7154 * pixel[1] + 0.0721 * pixel[2])
                # calcul la valeur de gris par moyenne des 3 canaux RVB
                #gris = int((1/3) * pixel[0] + (1/3) * pixel[1] + (1/3) * pixel[2])
                #gris = int(0.33 * pixel[0] + 0.33 * pixel[1] + 0.33 * pixel[2])
            print(repr(gris).rjust(3), end=' ')
        print("")

# Affiche les pixels en noir (0) ou blanc (1)
if(img.width*img.height < 2000): # pour les petites images
    print("Affiche les pixels en noir (0) ou blanc (1)")

for x in range(largeur):
    for y in range(hauteur):
        # récupére les valeurs du pixel
        pixel = img.getpixel((x,y))
        if(isinstance(pixel, int)):
            gris = pixel
        elif(isinstance(pixel, tuple)):
            # calcul du poids de chaque composante du gris dans le pixel (CIE709)
            gris = int(0.2125 * pixel[0] + 0.7154 * pixel[1] + 0.0721 * pixel[2])
            # calcul la valeur de gris par moyenne des 3 canaux RVB
            #gris = int((1/3) * pixel[0] + (1/3) * pixel[1] + (1/3) * pixel[2])
            #gris = int(0.33 * pixel[0] + 0.33 * pixel[1] + 0.33 * pixel[2])
        # un noir (0) ou un blanc (1) ?
        if(gris > 128):
            if(img.width*img.height < 2000):
                print(repr(1).rjust(1), end=' ') #print("1", end='')
            # un pixel blanc
            if(isinstance(pixel, int)):
                p = 255
            elif(isinstance(pixel, tuple)):
                p = (255,255,255) # RVB
        else:
            if(img.width*img.height < 2000):
                print(repr(0).rjust(1), end=' ') #print("0", end='')
            # un pixel noir
            if(isinstance(pixel, int)):
                p = 0
            elif(isinstance(pixel, tuple)):
                p = (0,0,0) # RVB
        # ajoute le pixel à la nouvelle image
        nouvelleImage.putpixel((x,y), p)
    if(img.width*img.height < 2000):
        print("")

# Affiche les valeurs des pixels
if(img.width*img.height < 2000): # pour les petites images
    print("Affiche les valeurs des pixels de la nouvelle image")
    for x in range(largeur):
        for y in range(hauteur):
            # récupére les valeurs du pixel
            pixel = nouvelleImage.getpixel((x,y))
            if(isinstance(pixel, int)):
                gris = pixel
            elif(isinstance(pixel, tuple)):
                # calcul du poids de chaque composante du gris dans le pixel (CIE709)
                gris = int(0.2125 * pixel[0] + 0.7154 * pixel[1] + 0.0721 * pixel[2])
                # calcul la valeur de gris par moyenne des 3 canaux RVB
                #gris = int((1/3) * pixel[0] + (1/3) * pixel[1] + (1/3) * pixel[2])
                #gris = int(0.33 * pixel[0] + 0.33 * pixel[1] + 0.33 * pixel[2])
            print(repr(gris).rjust(3), end=' ')
        print("")

# Enregistrement de la nouvelle image
nouvelleImage.save(path + "/" + nomImage + "-nouveau" + ext);

# Affichage de l'image
#img.show()
nouvelleImage.show()

# Fermeture des fichiers
img.close()
nouvelleImage.close()
