
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import pygame
import math
import random
from tkinter import ttk
import wx

# Initialisation de Pygame
pygame.init()

def fctmenu():
    pygame.init()
    canevas = Canvas(fenetre, borderwidth=0, highlightthickness=0, width=800, height=600, bg="#322432")
    canevas.create_image(400, 300, image=fond_menu)
    bouton_quitter2 = Button(canevas, image=croix, borderwidth=0, highlightthickness=0, bg="#322432", command=canevas.destroy)
    bouton_quitter2.place(x=775, y=4)

    # Variables des paramètres
    visee_auto = BooleanVar(value=False)
    niveau_sonore = IntVar(value=100)
    pv = IntVar(value=100)
    tirs_par_joueur = IntVar(value=2)
    degats_par_tir = IntVar(value=10)
    niveau_selectionne = StringVar(value="Débutant")

    niveaux = ["Débutant", "Intermédiaire", "Avancé", "Expert"]

    # Fonction Toggle Visée
    def toggle_visee():
        if visee_auto.get():
            bouton_visee.config(text="Visée automatique : Activée")
        else:
            bouton_visee.config(text="Visée automatique : Désactivée")

    # Titre


    # Bouton Visée Automatique
    bouton_visee = Button(canevas, text="Visée automatique : Désactivée",command=lambda: [visee_auto.set(not visee_auto.get()), toggle_visee()], bg="#322432",fg="white")
    bouton_visee.place(x=300, y=80)

    # Liste déroulante Niveau
    Label(canevas, text="Niveau :", fg="white", bg="#322432").place(x=370, y=130)

    frame_menu = Frame(canevas, bg="#322432")
    frame_menu.place(x=340, y=160)

    menu_niveau = ttk.Combobox(frame_menu, values=niveaux, textvariable=niveau_selectionne, state="readonly")
    menu_niveau.pack()

    # Fonction pour créer des sliders
    def ajouter_slider(label, var, min_val, max_val, pos_y):
        Label(canevas, text=label, fg="white", bg="#322432").place(x=340, y=pos_y)
        Scale(canevas, from_=min_val, to=max_val, orient="horizontal", variable=var, length=300,
        troughcolor="#553B6A", fg="white", bg="#322432").place(x=250, y=pos_y + 30)

    ajouter_slider("Niveau Sonore", niveau_sonore, 0, 100, 200)
    ajouter_slider("Points de Vie", pv, 10, 1000, 280)
    ajouter_slider("Nombre de tirs par joueur", tirs_par_joueur, 1, 10, 360)
    ajouter_slider("Dégâts par tir", degats_par_tir, 10, 100, 440)

    # Bouton OK
    Button(canevas, text="OK", command=canevas.destroy,bg="#322432", fg="white").place(x=380, y=520)

    canevas.pack(pady=40)

def quitter():
    if messagebox.askokcancel("Quitter", "Voulez-vous vraiment quitter ?"):
        fenetre.quit()

def jeu():
    # Configuration de la fenêtre
    WIDTH, HEIGHT = 1920, 1080
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Moteur physique")

    #texte
    big_font = pygame.font.SysFont('Arial', 40)
    small_font = pygame.font.SysFont('Arial', 20)

    # Génération des étoiles
    NUM_STARS = 2000  # Nombre d'étoiles
    stars = [(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(NUM_STARS)]

    # Couleurs
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    YELLOW = (255, 255, 0)
    BLUE = (0, 0, 255)
    DARK_BLUE = (10,10,50)
    WHITE = (255, 255, 255)

    # Constantes physiques
    G = 10

    # vitesse initiale des balles
    vx=10
    vy=0

    # Liste des planètes (coordonnées et masses)
    planetes = []

    #permet de mesurer la distance entre 2 planetes
    def distance(p1, p2):
        return math.sqrt((p1["x"] - p2["x"])**2 + (p1["y"] - p2["y"])**2)

    #couleur des planetes
    colors = [
        (255, 0, 0),      # Rouge
        (0, 255, 0),      # Vert
        (0, 0, 255),      # Bleu
        (255, 255, 0),    # Jaune
        (0, 255, 255),    # Cyan
        (255, 0, 255),    # Magenta
        (128, 0, 0),      # Marron
        (128, 128, 0),    # Olive
        (0, 128, 0),      # Vert foncé
        (128, 0, 128),    # Violet
        (0, 128, 128),    # Bleu-vert
        (0, 0, 128),      # Bleu marine
        (255, 165, 0),    # Orange
        (255, 192, 203),  # Rose
        (75, 0, 130),     # Indigo
        (139, 69, 19),    # Brun
        (255, 215, 0),    # Or
        (192, 192, 192),  # Argent
        (169, 169, 169),  # Gris foncé
        (0, 255, 127)     # Vert printemps
    ]
    pla = random.randint(2, 4) #permet de définir l'intervale de planéte généré
    for i in range(pla):
        while True:
            x = random.randint(300, 1620)
            y = random.randint(300, 780)
            masse = random.randint(250, 1500)
            color = random.choice(colors)
            new_planet = {"x": x, "y": y, "masse": masse, "color": color}

            # Vérifier la distance avec toutes les planètes existantes
            if all(distance(new_planet, p) > (p["masse"] / 10 + new_planet["masse"] / 10 + 40) for p in planetes):
                planetes.append(new_planet)
                break  # Sort de la boucle while quand une planète valide est trouvée

    # Liste des projectiles
    projectiles = []

    #coordonnées d'apparition du point bleu
    x=200
    y=200

    # Calcul des forces gravitationnelles
    def calculeNewton(proj, planete):
        dx = planete["x"] - proj["x"]
        dy = planete["y"] - proj["y"]
        distance_carre = dx ** 2 + dy ** 2
        if distance_carre < 1000:  # Évite des accélérations trop grandes si trop proche
            return [0, 0]
        force_magnitude = G * planete["masse"] / distance_carre
        distance = math.sqrt(distance_carre)
        return [force_magnitude * dx / distance, force_magnitude * dy / distance]


    # Boucle principale
    clock = pygame.time.Clock()
    running = True

    while running:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:                     #modifie les coordonées du point bleu
            y += 1
        if keys[pygame.K_UP]:
            y -= 1
        if keys[pygame.K_RIGHT]:
            x += 1
        if keys[pygame.K_LEFT]:
            x -= 1
        if keys[pygame.K_SPACE]:
            projectiles.append({"x": x, "y": y, "vx": vx, "vy": vy})
        if keys[pygame.K_s]:
            vy += 0.1
        if keys[pygame.K_z]:
            vy -= 0.1
        if keys[pygame.K_d]:
            vx += 0.1
        if keys[pygame.K_q]:
            vx -= 0.1


        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            #if event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_SPACE:
                    # Création d'un nouveau projectile
                    #projectiles.append({"x": x, "y": y, "vx": vx, "vy": vy})
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    running = False
                    pygame.quit()




        # Effacer l'écran
        screen.fill(DARK_BLUE)  # Fond bleu foncé (galaxie)

        # Dessin des étoiles
        for star in stars:
            pygame.draw.circle(screen, YELLOW, star, 1)  # Petits points jaunes


        # Dessiner les planètes
        for planete in planetes:
            pygame.draw.circle(screen, planete["color"], (planete["x"], planete["y"]), planete["masse"]/10)

        # Dessiner la position initiale du projectile en bleu
        pygame.draw.circle(screen, BLUE, (x, y), 10)

        # Mettre à jour et dessiner les projectiles
        for proj in projectiles:
            accel_x, accel_y = 0, 0
            collide=0
            for planete in planetes: #permet de calculer pour chaque planete l'acceleration de la balle
                force = calculeNewton(proj, planete)
                accel_x += force[0]
                accel_y += force[1]
                collided = (math.sqrt((proj["x"] - planete["x"]) ** 2 + (proj["y"] - planete["y"]) ** 2) <= planete["masse"]/10)  #permet de calculer pour chaque planete les colisions avec les balles
                if  collided and collide==0:
                    collide+=1
                    projectiles.remove(proj)
            off_screen = (proj["x"] < 0 or proj["x"] > WIDTH or proj["y"] < 0 or proj["y"] > HEIGHT) #verif si la balle est dans l'écran
            if off_screen:
                projectiles.remove(proj) #suprime la balle si elle est hors de l'écran
            # Mise à jour des vitesses et positions
            proj["vx"] += accel_x
            proj["vy"] += accel_y
            proj["x"] += proj["vx"]
            proj["y"] += proj["vy"]

            # Dessiner le projectile
            pygame.draw.circle(screen, GREEN, ((proj["x"]), (proj["y"])), 10)

        #affiche puissance du tir
        txt = big_font.render(('Vx: ' + str(round(vx, 2)) + 'Vy: ' + str(round(vy, 2))), True, WHITE)
        screen.blit(txt, (200, 75))


        # Mettre à jour l'affichage
        pygame.display.flip()
        clock.tick(60)


fenetre = Tk()
#permet l'expension de la page
fenetre.resizable(True, True)
fenetre.attributes('-fullscreen', True)

#images de fond
acceuil_temp = Image.open("fond_ecran.png")
fond_menu_temp= Image.open("fond_menu.png")

taille_ecran =(1537,870)
taille_menu = (800,600)

acceuil_nvl_taille = acceuil_temp.resize(taille_ecran , Image.Resampling.LANCZOS)
fond_menu_nvl_taille=fond_menu_temp.resize(taille_menu , Image.Resampling.LANCZOS)

acceuil = ImageTk.PhotoImage(acceuil_nvl_taille)
fond_menu = ImageTk.PhotoImage(fond_menu_nvl_taille)



#Images associées aux boutons

#ouverture des images
menu_temp = Image.open("menu.png")
play_temp = Image.open("play_final.png")
exit_temp = Image.open("quitter.png")
croix_temp = Image.open("croix.png")


#taille des boutons
taillebt = (200, 100)
taillebt2= (180, 76)
taille_icones =(20,20)

#modification de la taille des boutons
menu_nvl_taille = menu_temp.resize(taillebt , Image.Resampling.LANCZOS)
exit_nvl_taille = exit_temp.resize(taillebt2, Image.Resampling.LANCZOS)
play_nvl_taille = play_temp.resize(taillebt)
croix_nvl_taille = croix_temp.resize(taille_icones)

#création de copies des images de taille différente
exit_nvl_taille.save("exit_nvl_taille.png")
play_nvl_taille.save("playn_nvltaille.png")
menu_nvl_taille.save("menu_nvl_taille.png")
croix_nvl_taille.save("croix_nvl_taille.png")

# conversion des images pour permettre l'affichage
exit = ImageTk.PhotoImage(exit_nvl_taille)
play = ImageTk.PhotoImage(play_nvl_taille)
menu = ImageTk.PhotoImage(menu_nvl_taille)
croix = ImageTk.PhotoImage(croix_nvl_taille)




Label_acceuil = Label(fenetre, image=acceuil)
Label_acceuil.place(relwidth=1, relheight=1)



bouton_quitter = Button(fenetre, image=exit, borderwidth=0, highlightthickness=0,bg="#322432", command=quitter)
bouton_quitter.place(x=800, y = 770)



bouton_jouer = Button(fenetre,image=play,borderwidth=0, highlightthickness=0,bg="#322432", command=jeu)
bouton_jouer.place(x=650, y=550)

bouton_menu = Button (fenetre, image=menu,borderwidth=0,highlightthickness=0, bg="#322432", command=fctmenu)
bouton_menu.place(x=550, y = 750)

fenetre.mainloop()
