# coding: utf-8

# un commentaire !

# Python3 pour Windows : https://www.python.org/downloads/
# PIL (Python Imaging Library) (Pillow fork)
# Installation : pip install Pillow
# Documentation : https://pillow.readthedocs.io/en/stable/

print("ACTIVITÉ 1")

# PIL est une bibliothèque de traitement d'image
import PIL;
print("PIL version ", PIL.__version__)

# on importe le module Image de la bibliothèque PIL
# le module Image fournit une classe du même nom qui sera utilisée pour représenter une image.
from PIL import Image

# cf. https://fr.wikipedia.org/wiki/Lenna

#import Tkinter as tk # en python 2
import tkinter as tk # en python 3
from tkinter import filedialog

ecran = tk.Tk()
#print(ecran.winfo_screen()) # nom de l'écran

ecran.withdraw()

# choisir un fichier image
fichierImage =  filedialog.askopenfilename(initialdir = "./images/",title = "Choisir un fichier image",filetypes = (("fichiers jpeg","*.jpg"),("fichiers jpeg","*.jpeg"),("fichiers png","*.png"),("all files","*.*")))
#fichierImage = filedialog.askopenfilename()
if not fichierImage:
    exit()

# Image est une classe (c'est un type Image)
# img est un objet de la classe Image
# la création d'un objet se nomme l'instanciation
# open() est une fonction (méthode) de la classe Image qui permet de charger un fichier image
img = Image.open(fichierImage);

# format, size et mode sont des données (attributs) de la classe Image
print(img.format, img.size, img.mode)
# exemple : les modes courants sont "L" (luminance) pour les images en niveaux de gris, "RGB" pour les images en couleurs vraies et "CMYK" pour les images pour l'imprimerie (quadrichromie)
print("Fichier :", img.filename)

print("Calculez le nombre de pixels de cette image.")

# Affichage des dimensions de l'image
print("L =", img.width, "x H =", img.height)
# Calcul et Affichage du nombre de pixels de l'image
print("Nombre de pixels =", (img.width*img.height) , "pixels")

# Affichage de l'image
#img.show()

# resize() est une fonction (méthode) de la classe Image qui permet de modifier la taille d'une image et d'en obtenir une nouvelle
# im2 est un objet de la classe Image
im2 = img.resize((228,192))
# save() est une fonction (méthode) de la classe Image qui sauvegarder l'image dans un fichier (ici, l'extension précisera le format de l'image)
im2.save("./images/lena_228x192.png")
print(im2.format, im2.size, im2.mode)
print("Nombre de pixels =", "L =", im2.width, "x H =", im2.height, "=", (im2.width*im2.height) , "pixels")
#im2.show()

# size est un tuple (les tuples sont des séquences qu'on ne pourra plus modifier)
size = (144,96) # les parenthèses ne sont pas obligatoires
width, height = size
print(size, width, height)

im3 = img.resize(size)
im3.save("./images/lena_144x96.png")
print(im3.format, im3.size, im3.mode)
print("Nombre de pixels =", "L =", im3.width, "x H =", im3.height, "=", (im3.width*im3.height) , "pixels")
#im3.show()

print("Calculez la résolution de l’écran en pixels par centimètre, puis en ppp.")

# Résolution = Nombre de pixels en largeur / Largeur
w, h = ecran.winfo_screenwidth(), ecran.winfo_screenheight() 
print("Ecran = %s pixels x %s pixels" % (w, h))

# Taille de l'écran
print("Ecran = %s mm x %s mm" % (ecran.winfo_screenmmwidth(), ecran.winfo_screenmmheight()))
print("Ecran = %s cm x %s cm" % (ecran.winfo_screenmmwidth()/10, ecran.winfo_screenmmheight()/10))

# Résolution (en pixels par cm)
ppc_w = (w / (ecran.winfo_screenmmwidth()/10))
ppc_h = (h / (ecran.winfo_screenmmheight()/10))
print("Résolution = %.2f x %.2f pixels par cm" % (ppc_w, ppc_h))

# Résolution ppp (en pixels par pouce) ou ppi (pixel per inch)
ppi_w = (w / (ecran.winfo_screenmmwidth()/10)) * 2.54
ppi_h = (h / (ecran.winfo_screenmmheight()/10)) * 2.54
print("Résolution = %.2f x %.2f ppp (pixels par pouce)" % (ppi_w, ppi_h))

print("Calculez pour l'image Femme_288x192.png la taille exacte en centimètres qui doit s'afficher à l'écran de l'ordinateur.")

print("Taille : L =", im2.width, "pixels x H =", im2.height, "pixels")
print("Taille : L = %.2f" % (im2.width/ppc_w), "cm x H = %.2f" % (im2.height/ppc_h), "cm")

# Bonus :
depth = ecran.winfo_screendepth() # retourne le nombre de bits par pixel
print("Nombre de bits par pixel =", depth) # RGB 24 bits = R8 + G8 + B8

# cf. le format BMP (sans compression)
print("Taille : L =", (im2.width*depth), "bits x H =", (im2.height*depth), "bits", "=", ((im2.width*im2.height*depth)), "bits")
print("Taille : L =", (im2.width*depth), "bits x H =", (im2.height*depth), "bits", "=", ((im2.width*im2.height*depth))/8, "octets")
# https://fr.wikipedia.org/wiki/Préfixe_binaire
print("Taille :", (((im2.width*im2.height*depth))/8)/1024, " Kio (kibi)")
print("Taille :", (((im2.width*im2.height*depth))/8)/1000, " ko (kilo)")
#print("Taille :", (((im2.width*im2.height*depth))/8)/1024/1024, " Mio (mebi)")
#print("Taille :", (((im2.width*im2.height*depth))/8)/1000/1000, " Mo (mega)")

# Résultats :
# ACTIVITÉ 3
# PIL version  5.1.0
# JPEG (512, 512) RGB
# Fichier : ./images/lena.jpg
# 2. Calculez le nombre de pixels de cette image.
# L = 512 x H = 512
# Nombre de pixels = 262144 pixels
# None (228, 192) RGB
# Nombre de pixels = L = 228 x H = 192 = 43776 pixels
# (144, 96) 144 96
# None (144, 96) RGB
# Nombre de pixels = L = 144 x H = 96 = 13824 pixels
# 1. Calculez la résolution de l’écran en pixels par centimètre, puis en ppp.
# Ecran = 1920 pixels x 1080 pixels
# Ecran = 602 mm x 343 mm
# Ecran = 60.2 cm x 34.3 cm
# Résolution = 31.89 x 31.49 pixels par cm
# Résolution = 81.01 x 79.98 ppp (pixels par pouce)
# 7. Calculez pour l'image Femme_288x192.png la taille exacte en centimètres qui doit s'afficher à l'écran de l'ordinateur.
# Taille : L = 228 pixels x H = 192 pixels
# Taille : L = 7.15 cm x H = 6.10 cm
# Nombre de bits par pixel = 24
# Taille : L = 5472 bits x H = 4608 bits = 1050624 bits
# Taille : L = 5472 bits x H = 4608 bits = 131328.0 octets
# Taille : 128.25  Kio (kibi)
# Taille : 131.328  ko (kilo)

# Image au format RAW
# $ ls -l images/lena_228x192.data
# -rw-rw-r-- 1 tv tv 131328 nov.  24 09:23 images/lena_228x192.bmp

# $ ls -lh images/lena_228x192.data 
# -rw-rw-r-- 1 tv tv 129K nov.  24 09:23 images/lena_228x192.bmp

# $ ls -l --si images/lena_228x192.data 
# -rw-rw-r-- 1 tv tv 132k nov.  24 09:23 images/lena_228x192.bmp

