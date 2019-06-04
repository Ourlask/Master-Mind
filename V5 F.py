#Import divers
from random import *
import time
from tkinter import*
import pygame
from pygame.locals import *
import time

#Valeurs et liste du code
points=[]
manche=0
partie= True
global go
go=False
clr_j=[]

pygame.init()

#Partie musique et son
pygame.mixer.music.load("son.wav")
pygame.mixer.music.play()

victoire = pygame.mixer.Sound("victoire.wav")
victoire.set_volume(1)

defaite = pygame.mixer.Sound("defaite.wav")
defaite.set_volume(0.5)

#Couleurs de référence pour nous aider dans le codage
couleurs=["Blanc","Rose","Vert","Rouge","Orange","Argent","Jaune","Bleu"]
couleurs_ordinateur=[0, 1, 2, 3, 4, 5, 6, 7]

#Positions initiales des billes
global x
x=134
global X
X=425
y=600

#Défition pour le temps
def intervalle():
    espace=fin-debut
    espace=int(espace)
    print("Tu as pris",espace,"secondes pour trouver la réponse !")
def intervalle_perdu():
    espace=fin-debut
    espace=int(espace)
    print("Tu as pris",espace,"secondes pour faire tes 10 tentatives !")


#Commandes boutons
def blanc():
    clr_j.append(0)
    bille_blanc = Bg.create_oval(x-26,y-26,x+26,y+26,width=1.5,fill="#FFFFFF")
    global x
    x+=72
    return x
def rose():
    clr_j.append(1)
    bille_rose = Bg.create_oval(x-26,y-26,x+26,y+26,width=1.5,fill="#EF1CC1")
    global x
    x+=72
    return x
def vert():
    clr_j.append(2)
    bille_vert = Bg.create_oval(x-26,y-26,x+26,y+26,width=1.5,fill="#28E10A")
    global x
    x+=72
    return x
def rouge():
    clr_j.append(3)
    bille_rouge = Bg.create_oval(x-26,y-26,x+26,y+26,width=1.5,fill="#FD0000")
    global x
    x+=72
    return x
def orange():
    clr_j.append(4)
    bille_orange = Bg.create_oval(x-26,y-26,x+26,y+26,width=1.5,fill="#FF5C00")
    global x
    x+=72
    return x
def argent():
    clr_j.append(5)
    bille_argent = Bg.create_oval(x-26,y-26,x+26,y+26,width=1.5,fill="#717171")
    global x
    x+=72
    return x
def jaune():
    clr_j.append(6)
    bille_jaune = Bg.create_oval(x-26,y-26,x+26,y+26,width=1.5,fill="#FAFF00")
    global x
    x+=72
    return x
def bleu():
    clr_j.append(7)
    bille_bleu = Bg.create_oval(x-26,y-26,x+26,y+26,width=1.5,fill="#0029FF")
    global x
    x+=72
    return x

#Transformation du go=False en go=True
def GO():
    global go
    go=True
    return go

#Bouton quitter
def quitter():
    fenetre.destroy()
    pygame.mixer.music.stop()


#Petites billes Noir et Blanches
def petit_noir():
    bille_petite_noir = Bg.create_oval(X-7,y-7,X+7,y+7,width=1.5,fill="#000000")
    global X
    X+=25
    return X
def petit_blanc():
    bille_petite_blanche = Bg.create_oval(X-7,y-7,X+7,y+7,width=1,fill="#FFFFFF")
    global X
    X+=25
    return X
def petit_vide():
    global X
    X+=25
    return X


#Création de fenêtre
fenetre=Tk()
fenetre.title("Mastermind ISN")

#Ficher background
img= PhotoImage(file='F:/ISN/Framemastermind2.png')

#Fichers boutons couleurs
b_blanc2= PhotoImage(file='F:/ISN/Couleurs/Blanc.png')
b_rose2= PhotoImage(file='F:/ISN/Couleurs/Rose.png')
b_vert2= PhotoImage(file='F:/ISN/Couleurs/Vert.png')
b_rouge2= PhotoImage(file='F:/ISN/Couleurs/Rouge.png')
b_orange2= PhotoImage(file='F:/ISN/Couleurs/Orange.png')
b_argent2= PhotoImage(file='F:/ISN/Couleurs/Argent.png')
b_jaune2= PhotoImage(file='F:/ISN/Couleurs/Jaune.png')
b_bleu2= PhotoImage(file='F:/ISN/Couleurs/Bleu.png')
b_valider= PhotoImage(file='F:/ISN/Valider.png')
quitter2= PhotoImage(file='F:/ISN/Quitter.png')

#Background
Bg=Canvas(fenetre,width=550, height=650)
Bg.pack(padx=0,pady=0)
fond=Bg.create_image(0,0,anchor=NW,image=img)

#Bouton
b_blanc = Button(fenetre,image=b_blanc2,command=blanc)
b_blanc.pack(side=LEFT)
b_rose = Button(fenetre,image=b_rose2,command=rose)
b_rose.pack(side=LEFT)
b_vert = Button(fenetre,image=b_vert2,command=vert)
b_vert.pack(side=LEFT)
b_rouge = Button(fenetre,image=b_rouge2,command=rouge)
b_rouge.pack(side=LEFT)
b_orange = Button(fenetre,image=b_orange2,command=orange)
b_orange.pack(side=LEFT)
b_argent = Button(fenetre,image=b_argent2,command=argent)
b_argent.pack(side=LEFT)
b_jaune = Button(fenetre,image=b_jaune2,command=jaune)
b_jaune.pack(side=LEFT)
b_bleu = Button(fenetre,image=b_bleu2,command=bleu)
b_bleu.pack(side=LEFT)
#Quitter
Quitter = Button(fenetre,image=quitter2,command=quitter)
Quitter.place(anchor=NW)
Quitter.pack()
#Valider : go=True
Valider = Button(fenetre,image=b_valider,command=GO)
Valider.pack(side=LEFT)

#Ordinateur choisit les 4 valeurs aléatoires
clr=[]
for i in range(4):
    clr.append(randint(0,7))

#Démarage du chronomètre
debut=time.time()

#Solution pour TESTER le programme
print("Code à trouver",clr)

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#Joueur
while partie:
    fenetre.update()
    while go:
        print("Un petit cercle blanc veut dire que la couleur mais n'a pas la bonne position et le cercle noir veut dire que la position et la couleur est bonne.")
        fenetre.update()
        manche +=1

    #Points
        for position in range(4):
            if clr_j[position] not in clr:
                points.append(0)
            elif clr_j[position]==clr[position]:
                points.append(2)
            else:
                points.append(1)

    #Impression des points et du tour
        print(clr_j)
        print(points)
    #Elimination des valeurs de clr_j
        clr_j.clear()

        for petites_billes in range(4):
            if points[petites_billes]==0:
                petit_vide()
                fenetre.update()
            elif points[petites_billes]==1:
                petit_blanc()
                fenetre.update()
            elif points[petites_billes]==2:
                petit_noir()
                fenetre.update()

    #Changement de la valeur de y en fonction de la manche
        if manche==1:
            y=540
        elif manche==2:
            y=480
        elif manche==3:
            y=420
        elif manche==4:
            y=360
        elif manche==5:
            y=300
        elif manche==6:
            y=240
        elif manche==7:
            y=180
        elif manche==8:
            y=120
        elif manche==9:
            y=60

        #Reprise des valeurs initiales de x et X
        x=134
        X=425

        fenetre.update()

    #Si tu as gagné
        if points == [ 2, 2, 2, 2] :
            if manche == 1:
                fin = time.time()
                intervalle()
                print ("Du premier coups ! Comment as-tu fais ??")
                partie = False
                go=False
                pygame.mixer.music.stop()
                victoire.play()


            else:
                fin = time.time()
                intervalle()
                print ("Bien joué tu fais ça en " + str(manche) + " manches.")
                partie = False
                go=False
                pygame.mixer.music.stop()
                victoire.play()



    #Permet de stoper la boucle
        if manche >=1 and manche <10 and points !=[ 2, 2, 2, 2] :
            print ("Manche suivante : ")
            go=False
            points.clear()
        elif manche >= 10:
            print ("Mince ! Tu n'as pas trouvé, les bonnes couleurs étaient: " + str(clr))
            partie=False
            pygame.mixer.music.stop()
            defaite.play()
            fin = time.time()
            intervalle_perdu()


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
