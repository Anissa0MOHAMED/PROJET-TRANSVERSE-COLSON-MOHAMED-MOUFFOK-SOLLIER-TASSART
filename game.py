from tkinter import *
from tkinter import messagebox
from tkinter import font
from PIL import Image, ImageTk
import pygame
import math
import random
from tkinter import ttk
import os
import ctypes
import pygame.transform


pygame.init()
pseudos = []
def lancement_pseudo(): #Fonction qui lance une page qui permet de récupérer les noms

    pygame.init() # initialise pygame
    info = pygame.display.Info() #récupérer les informations sur la taille de l'ecran de l'utilisateur
    WIDTH, HEIGHT = info.current_w, info.current_h #variables de largeur et de hauteur permettant d'adapter l'affichage à chaque utilisateur

    # Création de la fenêtre pygame des pseudos
    fenetre = pygame.display.set_mode((WIDTH, HEIGHT))  #ajuste la taille de la fenetre à celle de l'utilisateur
    pygame.display.set_caption("pseudo") #donne un titre à la page

    # Chargement des images de fond
    fond1 = pygame.transform.scale(pygame.image.load('pseudo2.png'), (WIDTH, HEIGHT)) #fond pour demande de pseudo du joueur 1
    fond2 = pygame.transform.scale(pygame.image.load('pseudo1.png'), (WIDTH, HEIGHT)) #fond pour demande de pseudo du joueur 2

    # Bouton ok
    bouton_valider = pygame.image.load("ok.png").convert_alpha() #
    rect_bouton = bouton_valider.get_rect(topleft=(600, 500)) #recupere la portion de l'ecran associée au bouton ok pour permetre d'interagir avec

    # Zone de saisie du pseudo rectangle blanc
    input_box = pygame.Rect(525, 400, 300, 50)
    font = pygame.font.Font(None, 36)
    texte = '' #initialise la variable texte qui sert à récupérer les pseudos

    joueur_num = 1 # variable de test (pour l'affichage des pages et pour la position du pseudo dans la liste)


    while True:
        # Affiche le fond selon le joueur
        fond = fond1 if joueur_num == 1 else fond2
        fenetre.blit(fond, (0, 0))

        # Affiche le bouton ok
        fenetre.blit(bouton_valider, rect_bouton)

        # Affiche la zone de saisie
        pygame.draw.rect(fenetre, (255, 255, 255), input_box, 2)
        texte_surface = font.render(texte, True, (255, 255, 255))
        fenetre.blit(texte_surface, (input_box.x + 10, input_box.y + 10))

        # Gestion des événements touches et clics
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None

            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_bouton.collidepoint(event.pos):
                    pseudos.append(texte)
                    texte = ''
                    if joueur_num == 1:
                        joueur_num = 2
                    else:
                        pygame.quit()
                        return pseudos

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pseudos.append(texte)
                    texte = ''
                    if joueur_num == 1:
                        joueur_num = 2
                    else:
                        pygame.quit()
                        return pseudos
                elif event.key == pygame.K_BACKSPACE:
                    texte = texte[:-1]
                else:
                    texte += event.unicode

        pygame.display.flip()


def gameover1():
    info = pygame.display.Info()
    WIDTH, HEIGHT = info.current_w, info.current_h
    image = pygame.image.load("victoire_joueur1.png")
    image = pygame.transform.scale(image, (WIDTH, HEIGHT))

    screen = pygame.display.get_surface()
    screen.blit(image, (0, 0))
    pygame.display.flip()
    pygame.time.delay(5000)
    pygame.quit()

def gameover2():
    info = pygame.display.Info()
    WIDTH, HEIGHT = info.current_w, info.current_h
    image = pygame.image.load("victoire_joueur2.png")
    image = pygame.transform.scale(image, (WIDTH, HEIGHT))
    screen = pygame.display.get_surface()
    screen.blit(image, (0, 0))
    pygame.display.flip()
    pygame.time.delay(5000)
    pygame.quit()


def lancement1():
    fenetre.withdraw()  # Cache la fenêtre Tkinter
    lancement_pseudo()
    Afficher_consignes(1)
    fenetre.deiconify()  # Réaffiche l'acceuil quand la fenetre de jeu se ferme
def lancement2():

    fenetre.withdraw()  # Cache la fenêtre Tkinter

    lancement_pseudo()
    Afficher_consignes(2)
    fenetre.deiconify()  # Réaffiche l'acceuil quand la fenetre de jeu se ferme
def lancement3():

    fenetre.withdraw()

    lancement_pseudo()
    Afficher_consignes(3)
    fenetre.deiconify()  # Réaffiche l'acceuil quand la fenetre de jeu se ferme

def jeu_intermediaire():

    # Initialisation de Pygame
    pygame.init()

    # Captation de la résolution de l'écran afin d'adapter le jeu à toutes les résolutions
    root = Tk()
    screen_width = root.winfo_screenwidth() #capte la largeur de l'écran
    screen_height = root.winfo_screenheight() #capte la hauteur de l'écran
    root.destroy()
    # Configuration de la fenêtre
    WIDTH, HEIGHT = screen_width, screen_height
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Moteur physique")
    font_size = round(0.024 * WIDTH)
    # texte
    big_font = pygame.font.SysFont('Arial', font_size)
    small_font = pygame.font.SysFont('Arial', font_size)

    # Génération des étoiles
    NUM_STARS = 2000  # Nombre d'étoiles
    stars = [(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(NUM_STARS)]

    # Couleurs
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    BLUE = (0, 0, 255)
    DARK_BLUE = (10, 10, 50)
    WHITE = (255, 255, 255)
    # Couleur Planetes
    planet_images = [
        pygame.image.load('planete_1.png'),
        pygame.image.load('planete_2.png'),
        pygame.image.load('planete_3.png'),
        pygame.image.load('planete_4.png')
    ]

    planet_abimee = [
        pygame.image.load('planete_1_2.png'),
        pygame.image.load('planete_2_2.png'),
        pygame.image.load('planete_3_2.png'),
        pygame.image.load('planete_4_2.png')
    ]


    # Constantes physiques
    G = 10
    tir_vitesse = 10
    # vitesse initiale des balles
    vx = 10
    vy = 0
    vab = 10
    vcd = 0
    # score initiale
    score1 = 0
    score2 = 0

    # Coordonnées de référence pour la génération des planètes via touche t
    ref_x1, ref_y1 = 0.2*WIDTH,  0.2 * HEIGHT
    ref_x2, ref_y2 = 0.8*WIDTH, 0.2 * HEIGHT

    # carburant pour les vaisseaux
    carburant0 = 100
    carburant1 = 100

    # Liste des planètes (coordonnées et masses)
    planetes = []

    # permet de mesurer la distance entre 2 planetes
    def distance(p1, p2):
        return math.sqrt((p1["x"] - p2["x"]) ** 2 + (p1["y"] - p2["y"]) ** 2)

    # Permet de redimensionner les images des planetes

    def resize_planet_image(image, masse):
        size = int(masse / 4)
        return pygame.transform.scale(image, (size, size))

    # coordonnées d'apparition du vaisseau 1 puis 2
    x = 0.04 * WIDTH
    y = 0.04 * HEIGHT

    ab = 0.8 * WIDTH
    cd = 0.2 * HEIGHT

    # Distance minimale entre une planète et les vaisseaux
    # Distance minimale entre une planète et les vaisseaux
    DISTANCE_MINIMALE_VAISSEAUX = 100  # Ajustez cette valeur selon vos besoins

    # Génération des planètes
    pla = random.randint(6, 8)  # Nombre de planètes
    for i in range(pla):
        while True:
            gen_x = random.randint(0, WIDTH)
            gen_y = random.randint(0, HEIGHT)
            pv = 6
            masse = random.randint(250, 1500)
            i = random.randint(0, len(planet_images) - 1)
            image = resize_planet_image(planet_images[i], masse)
            image_abimee = resize_planet_image(planet_abimee[i], masse)

            new_planet = {"x": gen_x, "y": gen_y, "masse": masse, "pv": pv, "compteur": 0, "image": image,
                          "image_abimee": image_abimee}

            # Vérifier la distance avec toutes les planètes existantes
            if all(distance(new_planet, p) > ((p["masse"] / 10 + new_planet["masse"] / 10) + 30) for p in planetes) and \
                    math.sqrt((gen_x - x) ** 2 + (gen_y - y) ** 2) > DISTANCE_MINIMALE_VAISSEAUX and \
                    math.sqrt((gen_x - ab) ** 2 + (gen_y - cd) ** 2) > DISTANCE_MINIMALE_VAISSEAUX:
                planetes.append(new_planet)
                break  # Ajoute la nouvelle planète et quitte la boucle
    # Liste des projectiles
    projectiles = []
    explosions = []

    object_image = pygame.image.load('vaisseau.png')
    object_image = pygame.transform.scale(object_image, (50, 50))
    missile_bleu = pygame.image.load('missile bleu.png')
    missile_bleu = pygame.transform.scale(missile_bleu, (44, 44))
    missile_rouge = pygame.image.load('missile rouge.png')
    missile_rouge = pygame.transform.scale(missile_rouge, (44, 44))

    explosion_frames = [pygame.image.load(f'explosion/frame_{i}.png') for i in range(6)]
    explosion_sound = pygame.mixer.Sound("1917.mp3")
    explosion_sound.set_volume(0.2)  # Réglez le volume à 20% du volume maximal
    missile_sound = pygame.mixer.Sound("missile.mp3")
    musique = pygame.mixer.Sound("04. Hacking Malfunction (Battle).mp3")
    musique.play(-1)

    # Calcul des forces gravitationnelles
    def calculeNewton(proj, planete):
        dx = planete["x"] - proj["x"]
        dy = planete["y"] - proj["y"]
        distance_carre = dx ** 2 + dy ** 2

        force_magnitude = G * planete["masse"] / distance_carre
        distance = math.sqrt(distance_carre)
        return [force_magnitude * dx / distance, force_magnitude * dy / distance]

    # Détection de collision entre missiles et vaisseaux
    def collision_vaisseau(proj, vaisseau_x, vaisseau_y):
        distance_proj_vaisseau = math.sqrt((proj["x"] - (vaisseau_x + 25)) ** 2 + (proj["y"] - (vaisseau_y + 25)) ** 2)
        return distance_proj_vaisseau < 30  # Rayon de collision

    preview_enabled = True
    # Boucle principale
    clock = pygame.time.Clock()
    running = True
    joueur_actuel = 0
    vy = 1
    vcd = 1
    last_move_time = pygame.time.get_ticks()
    angle = 0
    angle2 = 180
    speed = 2
    show_preview = False

    def simulate_trajectory(x, y, angle, vx):
        points = []
        ship_center_x = x + 25
        ship_center_y = y + 25
        temp_vx = vx * math.sin(math.radians(angle) - 80)
        temp_vy = tir_vitesse * math.cos(math.radians(angle) - 80)
        temp_x, temp_y = ship_center_x, ship_center_y
        for _ in range(50):
            accel_x, accel_y = 0, 0
            for planete in planetes:
                force = calculeNewton({"x": temp_x, "y": temp_y}, planete)
                accel_x += force[0]
                accel_y += force[1]
            temp_vx += accel_x
            temp_vy += accel_y
            temp_x += temp_vx
            temp_y += temp_vy
            for planete in planetes:
                if distance({"x": temp_x, "y": temp_y}, planete) < (planete["masse"] / 10):
                    return points  # Arrête la simulation si la trajectoire touche une planète
            if temp_x < 0 or temp_x > WIDTH or temp_y < 0 or temp_y > HEIGHT:
                break
            points.append((int(temp_x), int(temp_y)))
        return points

    while running:
        keys = pygame.key.get_pressed()
        moved = False
        if not projectiles:
            if joueur_actuel == 0:
                if carburant0 > 0:
                    if keys[pygame.K_UP]:
                        if keys[pygame.K_r]:
                            x += speed * math.cos(math.radians(angle)) * 2
                            y -= speed * math.sin(math.radians(angle)) * 2
                            carburant0 -= 0.5
                        else:
                            x += speed * math.cos(math.radians(angle))
                            y -= speed * math.sin(math.radians(angle))
                            carburant0 -= 0.1
                    if keys[pygame.K_DOWN]:
                        x -= speed * math.cos(math.radians(angle))
                        y += speed * math.sin(math.radians(angle))
                        carburant0 -= 0.1
                if keys[pygame.K_RIGHT]:
                    angle -= 1
                if keys[pygame.K_LEFT]:
                    angle += 1
                if moved:
                    last_move_time = pygame.time.get_ticks()
                    show_preview = False
                elif pygame.time.get_ticks() - last_move_time > 200:
                    show_preview = True

            if joueur_actuel == 1:
                if carburant1 > 0:
                    if keys[pygame.K_UP]:
                        if keys[pygame.K_r]:
                            ab += speed * math.cos(math.radians(angle2)) * 2
                            cd -= speed * math.sin(math.radians(angle2)) * 2
                            carburant1 -= 0.5
                            moved = True
                        else:
                            ab += speed * math.cos(math.radians(angle2))
                            cd -= speed * math.sin(math.radians(angle2))
                            carburant1 -= 0.1
                            moved = True
                if keys[pygame.K_DOWN]:
                    ab -= speed * math.cos(math.radians(angle2))
                    cd += speed * math.sin(math.radians(angle2))
                    carburant1 -= 0.1
                    moved = True
                if keys[pygame.K_RIGHT]:
                    angle2 -= 1
                if keys[pygame.K_LEFT]:
                    angle2 += 1
        if moved:
            last_move_time = pygame.time.get_ticks()
            show_preview = False
        elif pygame.time.get_ticks() - last_move_time > 200:
            show_preview = True

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    planetes.clear()  # Supprime toutes les anciennes planètes
                    # Distance minimale entre une planète et les vaisseaux
                    DISTANCE_MINIMALE_VAISSEAUX = 100  # Ajustez cette valeur selon vos besoins

                    # Génération des planètes
                    pla = random.randint(4, 6)  # Nombre de planètes
                    for i in range(pla):
                        while True:
                            gen_x = random.randint(0, WIDTH)
                            gen_y = random.randint(0, HEIGHT)
                            pv = 6
                            masse = random.randint(250, 1500)
                            i = random.randint(0, len(planet_images) - 1)
                            image = resize_planet_image(planet_images[i], masse)
                            image_abimee = resize_planet_image(planet_abimee[i], masse)

                            new_planet = {"x": gen_x, "y": gen_y, "masse": masse, "pv": pv, "compteur": 0,
                                          "image": image, "image_abimee": image_abimee}

                            # Vérifier la distance avec toutes les planètes existantes
                            if all(distance(new_planet, p) > ((p["masse"] / 10 + new_planet["masse"] / 10) + 30) for p
                                   in planetes) and \
                                    math.sqrt((gen_x - x) ** 2 + (gen_y - y) ** 2) > DISTANCE_MINIMALE_VAISSEAUX and \
                                    math.sqrt((gen_x - ab) ** 2 + (gen_y - cd) ** 2) > DISTANCE_MINIMALE_VAISSEAUX:
                                planetes.append(new_planet)
                                break  # Ajoute la nouvelle planète et quitte la boucle
                if event.key == pygame.K_SPACE:
                    if joueur_actuel == 0:
                        vX = vx * math.sin(math.radians(angle) - 80)
                        vy = tir_vitesse * math.cos(math.radians(angle) - 80)
                        projectiles.append({"x": x + 25, "y": y + 25, "vx": vX, "vy": vy, "color": BLUE})
                        pygame.mixer.Sound.play(missile_sound)
                        if keys[pygame.K_f]:
                            projectiles.append({"x": x + 25, "y": y + 25, "vx": vX, "vy": vy + 0.5, "color": BLUE})
                            pygame.mixer.Sound.play(missile_sound)
                            projectiles.append({"x": x + 25, "y": y + 25, "vx": vX, "vy": vy - 0.5, "color": BLUE})
                            pygame.mixer.Sound.play(missile_sound)
                        if keys[pygame.K_g]:
                            projectiles.append({"x": x + 25, "y": y + 25, "vx": vX, "vy": vy + 0.5, "color": BLUE})
                            pygame.mixer.Sound.play(missile_sound)
                            projectiles.append({"x": x + 25, "y": y + 25, "vx": vX, "vy": vy - 0.5, "color": BLUE})
                            pygame.mixer.Sound.play(missile_sound)
                            projectiles.append({"x": x + 25, "y": y + 25, "vx": vX, "vy": vy + 1, "color": BLUE})
                            pygame.mixer.Sound.play(missile_sound)
                            projectiles.append({"x": x + 25, "y": y + 25, "vx": vX, "vy": vy - 1, "color": BLUE})
                            pygame.mixer.Sound.play(missile_sound)
                        joueur_actuel = 1
                        carburant0 = min(carburant0 + 5, 100)
                    elif joueur_actuel == 1:
                        vab = vx * math.sin(math.radians(angle2) - 80)
                        vcd = tir_vitesse * math.cos(math.radians(angle2) - 80)
                        projectiles.append({"x": ab + 25, "y": cd + 25, "vx": vab, "vy": vcd, "color": RED})
                        pygame.mixer.Sound.play(missile_sound)
                        if keys[pygame.K_f]:
                            projectiles.append({"x": ab + 25, "y": cd + 25, "vx": vab, "vy": vcd - 0.5, "color": RED})
                            pygame.mixer.Sound.play(missile_sound)
                            projectiles.append({"x": ab + 25, "y": cd + 25, "vx": vab, "vy": vcd + 0.5, "color": RED})
                            pygame.mixer.Sound.play(missile_sound)
                        if keys[pygame.K_g]:
                            projectiles.append({"x": ab + 25, "y": cd + 25, "vx": vab, "vy": vcd + 1, "color": RED})
                            pygame.mixer.Sound.play(missile_sound)
                            projectiles.append({"x": ab + 25, "y": cd + 25, "vx": vab, "vy": vcd - 1, "color": RED})
                            pygame.mixer.Sound.play(missile_sound)
                            projectiles.append({"x": ab + 25, "y": cd + 25, "vx": vab, "vy": vcd + 0.5, "color": RED})
                            pygame.mixer.Sound.play(missile_sound)
                            projectiles.append({"x": ab + 25, "y": cd + 25, "vx": vab, "vy": vcd - 0.5, "color": RED})
                            pygame.mixer.Sound.play(missile_sound)
                        joueur_actuel = 0
                        carburant1 = min(carburant1 + 5, 100)
                if event.key == pygame.K_a:
                    running = False
                    pygame.quit()
                if event.key == pygame.K_q:
                    if joueur_actuel == 0:
                        angle += 1
                    else:
                        angle2 += 1
                if event.key == pygame.K_d:
                    if joueur_actuel == 0:
                        angle -= 1
                    else:
                        angle2 -= 1
                if event.key == pygame.K_e:
                    preview_enabled = not preview_enabled
                if event.key == pygame.K_s and vx > 5:
                    vx -= 1
                if event.key == pygame.K_z and vx < 15:
                    vx += 1

        # Effacer l'écran
        screen.fill(DARK_BLUE)  # Fond bleu foncé (galaxie)

        # Dessin des étoiles
        for star in stars:
            pygame.draw.circle(screen, YELLOW, star, 1)  # Petits points jaunes

        def dessiner_jauge_carburant(screen, x, y, largeur, hauteur, carburant):
            # Calculer la largeur de la jauge en fonction du carburant restant
            carburant_largeur = (carburant / 100) * largeur
            # Dessiner le fond de la jauge (rouge)
            pygame.draw.rect(screen, RED, (x, y, largeur, hauteur))
            # Dessiner la jauge de carburant (bleue)
            pygame.draw.rect(screen, BLUE, (x, y, carburant_largeur, hauteur))
            # Dessiner la bordure de la jauge (noir)
            pygame.draw.rect(screen, BLACK, (x, y, largeur, hauteur), 2)

        dessiner_jauge_carburant(screen, 0.01 * WIDTH, 0.04 * HEIGHT, 0.2 * WIDTH, 0.04 * HEIGHT, carburant0)
        dessiner_jauge_carburant(screen, WIDTH - 0.21 * WIDTH, 0.04 * HEIGHT, 0.2 * WIDTH, 0.04 * HEIGHT, carburant1)

        # Dessiner les planètes
        for planete in planetes:
            image_rect = planete["image"].get_rect(center=(planete["x"], planete["y"]))
            screen.blit(planete["image"], image_rect.topleft)

        # Dessiner la position initiale du projectile en bleu
        rotated_image = pygame.transform.rotate(object_image, angle)
        new_rect = rotated_image.get_rect(center=object_image.get_rect(topleft=(x, y)).center)
        screen.blit(rotated_image, new_rect.topleft)

        rotated_image = pygame.transform.rotate(object_image, angle2)
        new_rect = rotated_image.get_rect(center=object_image.get_rect(topleft=(ab, cd)).center)
        screen.blit(rotated_image, new_rect.topleft)

        # Mettre à jour et dessiner les projectiles
        for proj in projectiles:
            accel_x, accel_y = 0, 0
            collide = 0
            for planete in planetes:  # permet de calculer pour chaque planete l'acceleration de la balle
                force = calculeNewton(proj, planete)
                accel_x += force[0]
                accel_y += force[1]
                collided = (math.sqrt((proj["x"] - planete["x"]) ** 2 + (proj["y"] - planete["y"]) ** 2) <= planete[
                    "masse"] / 10)  # permet de calculer pour chaque planete les colisions avec les balles
                if collided and collide == 0:
                    planete['pv'] -= 1
                    if planete["pv"] == 3:
                        planete["image"] = planete["image_abimee"]
                    if planete['pv'] <= 0:
                        planetes.remove(planete)
                    collide += 1
                    pygame.mixer.Sound.play(explosion_sound)
                    explosions.append({"x": proj["x"], "y": proj["y"], "frame": 0})
                    projectiles.remove(proj)
            off_screen = (proj["x"] < 0 or proj["x"] > WIDTH or proj["y"] < 0 or proj[
                "y"] > HEIGHT)  # verif si la balle est dans l'écran
            if off_screen:
                projectiles.remove(proj)  # suprime la balle si elle est hors de l'écran
            # Mise à jour des vitesses et positions
            proj["vx"] += accel_x
            proj["vy"] += accel_y
            proj["x"] += proj["vx"]
            proj["y"] += proj["vy"]

            # Dessiner le projectile
            angle_proj = math.degrees(math.atan2(proj["vy"], proj["vx"]))
            if proj["color"] == BLUE:
                rotated_missile = pygame.transform.rotate(missile_bleu, -angle_proj - 90)
            else:
                rotated_missile = pygame.transform.rotate(missile_rouge, -angle_proj - 90)
            new_rect = rotated_missile.get_rect(center=(proj["x"], proj["y"]))
            screen.blit(rotated_missile, new_rect.topleft)

            # Vérifier les collisions des projectiles avec les vaisseaux
            for proj in projectiles[:]:  # Copie de la liste pour éviter les erreurs de suppression
                if proj["color"] == RED and collision_vaisseau(proj, x, y):
                    pygame.mixer.Sound.play(explosion_sound)  # Explosion du vaisseau bleu
                    explosions.append({"x": proj["x"], "y": proj["y"], "frame": 0})
                    score1 += 1
                    if score1 == 5:
                        gameover2()  # Afficher la fonction Game Over
                        pygame.display.flip()  # Met à jour l'écran pour montrer le résultat
                        pygame.time.wait(2000)  # Attendre 2 secondes avant de quitter (facultatif)
                        pygame.quit()  # Fermer proprement Pygame
                        return  # Quitte la boucle ou la fonction principale
                    projectiles.remove(proj)

                elif proj["color"] == BLUE and collision_vaisseau(proj, ab, cd):
                    pygame.mixer.Sound.play(explosion_sound)  # Explosion du vaisseau rouge
                    explosions.append({"x": proj["x"], "y": proj["y"], "frame": 0})
                    score2 += 1
                    if score2 == 5:
                        gameover1()  # Afficher la fonction Game Over
                        pygame.display.flip()  # Met à jour l'écran pour montrer le résultat
                        pygame.time.wait(2000)  # Attendre 2 secondes avant de quitter (facultatif)
                        pygame.quit()  # Fermer proprement Pygame
                        return  # Quitte la boucle ou la fonction principale
                    projectiles.remove(proj)

            # Affichage des explosions
        for explosion in explosions:
            frame_index = explosion["frame"] // 5
            if frame_index < len(explosion_frames):
                screen.blit(explosion_frames[frame_index], (explosion["x"] - 50, explosion["y"] - 50))
                explosion["frame"] += 1
            else:
                explosions.remove(explosion)

        # affiche puissance du tir
        if joueur_actuel == 0:
            # Affichage de la vitesse et de l'angle
            txt = big_font.render(f'Vitesse: {round(vx, 2)} | Angle: {round(angle, 1) % 360}°', True, WHITE)
            # Affichage du pseudo juste en dessous du texte de la jauge (ou de l'élément précédent)
            txt_pseudo = big_font.render(f' Player1: {pseudos[0]}', True, WHITE)
            screen.blit(txt_pseudo, (25, 120))  # Affichage du pseudo
            # Affichage du texte de la vitesse et de l'angle à sa place
            screen.blit(txt, (25, 85))
        elif joueur_actuel == 1:
            txt = big_font.render(f'Vitesse: {round(vx, 2)} | Angle: {round(angle2 - 180, 1) % 360}°', True, WHITE)
            screen.blit(txt, (WIDTH - 425, 85))
            txt_pseudo = big_font.render(f' Player2: {pseudos[1]}', True, WHITE)
            screen.blit(txt_pseudo, (WIDTH - 425, 120))  # Affichage du pseudo

        if joueur_actuel == 0:
            if show_preview and preview_enabled:
                trajectory = simulate_trajectory(x, y, angle, vx)
                for point in trajectory:
                    pygame.draw.circle(screen, WHITE, point, 2)
        elif joueur_actuel == 1:
            if show_preview and preview_enabled:
                trajectory = simulate_trajectory(ab, cd, angle2, vx)
                for point in trajectory:
                    pygame.draw.circle(screen, WHITE, point, 2)

        txt2 = big_font.render(f'{score2} | {score1}', True, WHITE)
        screen.blit(txt2, (0.4 * WIDTH, 0.04 * HEIGHT))
        # Mettre à jour l'affichage
        pygame.display.flip()
        clock.tick(60)
def jeu_debutant():

    # Initialisation de Pygame
    pygame.init()

    # Captation de la résolution de l'écran afin d'adapter le jeu à toutes les résolutions
    root = Tk()
    screen_width = root.winfo_screenwidth() #capte la largeur de l'écran
    screen_height = root.winfo_screenheight() #capte la hauteur de l'écran
    root.destroy()
    # Configuration de la fenêtre
    WIDTH, HEIGHT = screen_width, screen_height
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Moteur physique")
    font_size = round(0.024 * WIDTH)
    # texte
    big_font = pygame.font.SysFont('Arial', font_size)
    small_font = pygame.font.SysFont('Arial', font_size)

    # Génération des étoiles
    NUM_STARS = 2000  # Nombre d'étoiles
    stars = [(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(NUM_STARS)]

    # Couleurs
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    BLUE = (0, 0, 255)
    DARK_BLUE = (10, 10, 50)
    WHITE = (255, 255, 255)
    # Couleur Planetes
    planet_images = [
        pygame.image.load('planete_1.png'),
        pygame.image.load('planete_2.png'),
        pygame.image.load('planete_3.png'),
        pygame.image.load('planete_4.png')
    ]

    planet_abimee = [
        pygame.image.load('planete_1_2.png'),
        pygame.image.load('planete_2_2.png'),
        pygame.image.load('planete_3_2.png'),
        pygame.image.load('planete_4_2.png')
    ]


    # Constantes physiques
    G = 10
    tir_vitesse = 10
    # vitesse initiale des balles
    vx = 10
    vy = 0
    vab = 10
    vcd = 0
    # score initiale
    score1 = 0
    score2 = 0

    # Coordonnées de référence pour la génération des planètes via touche t
    ref_x1, ref_y1 = 0.2*WIDTH,  0.2 * HEIGHT
    ref_x2, ref_y2 = 0.8*WIDTH, 0.2 * HEIGHT

    # carburant pour les vaisseaux
    carburant0 = 100
    carburant1 = 100

    # Liste des planètes (coordonnées et masses)
    planetes = []

    # permet de mesurer la distance entre 2 planetes
    def distance(p1, p2):
        return math.sqrt((p1["x"] - p2["x"]) ** 2 + (p1["y"] - p2["y"]) ** 2)

    # Permet de redimensionner les images des planetes

    def resize_planet_image(image, masse):
        size = int(masse / 4)
        return pygame.transform.scale(image, (size, size))

    # coordonnées d'apparition du vaisseau 1 puis 2
    x = 0.04 * WIDTH
    y = 0.04 * HEIGHT

    ab = 0.8 * WIDTH
    cd = 0.2 * HEIGHT

    # Distance minimale entre une planète et les vaisseaux
    DISTANCE_MINIMALE_VAISSEAUX = 100  # Ajustez cette valeur selon vos besoins

    # Génération des planètes
    pla = random.randint(4,6)  # Nombre de planètes
    for i in range(pla):
        while True:
            gen_x = random.randint(0, WIDTH)
            gen_y = random.randint(0, HEIGHT)
            pv = 6
            masse = random.randint(250, 1500)
            i = random.randint(0, len(planet_images) - 1)
            image = resize_planet_image(planet_images[i], masse)
            image_abimee = resize_planet_image(planet_abimee[i], masse)

            new_planet = {"x": gen_x, "y": gen_y, "masse": masse, "pv": pv, "compteur": 0, "image": image,"image_abimee": image_abimee}

            # Vérifier la distance avec toutes les planètes existantes
            if all(distance(new_planet, p) > ((p["masse"] / 10 + new_planet["masse"] / 10) + 30) for p in planetes) and \
                    math.sqrt((gen_x - x) ** 2 + (gen_y - y) ** 2) > DISTANCE_MINIMALE_VAISSEAUX and \
                    math.sqrt((gen_x - ab) ** 2 + (gen_y - cd) ** 2) > DISTANCE_MINIMALE_VAISSEAUX:
                planetes.append(new_planet)
                break  # Ajoute la nouvelle planète et quitte la boucle
    # Liste des projectiles
    projectiles = []
    explosions = []

    object_image = pygame.image.load('vaisseau.png')
    object_image = pygame.transform.scale(object_image, (50, 50))
    missile_bleu = pygame.image.load('missile bleu.png')
    missile_bleu = pygame.transform.scale(missile_bleu, (44, 44))
    missile_rouge = pygame.image.load('missile rouge.png')
    missile_rouge = pygame.transform.scale(missile_rouge, (44, 44))

    explosion_frames = [pygame.image.load(f'explosion/frame_{i}.png') for i in range(6)]
    explosion_sound = pygame.mixer.Sound("1917.mp3")
    explosion_sound.set_volume(0.2)  # Réglez le volume à 20% du volume maximal
    missile_sound = pygame.mixer.Sound("missile.mp3")
    musique = pygame.mixer.Sound("04. Hacking Malfunction (Battle).mp3")
    musique.play(-1)

    # Calcul des forces gravitationnelles
    def calculeNewton(proj, planete):
        dx = planete["x"] - proj["x"]
        dy = planete["y"] - proj["y"]
        distance_carre = dx ** 2 + dy ** 2

        force_magnitude = G * planete["masse"] / distance_carre
        distance = math.sqrt(distance_carre)
        return [force_magnitude * dx / distance, force_magnitude * dy / distance]

    # Détection de collision entre missiles et vaisseaux
    def collision_vaisseau(proj, vaisseau_x, vaisseau_y):
        distance_proj_vaisseau = math.sqrt((proj["x"] - (vaisseau_x + 25)) ** 2 + (proj["y"] - (vaisseau_y + 25)) ** 2)
        return distance_proj_vaisseau < 30  # Rayon de collision

    preview_enabled = True
    # Boucle principale
    clock = pygame.time.Clock()
    running = True
    joueur_actuel = 0
    vy = 1
    vcd = 1
    last_move_time = pygame.time.get_ticks()
    angle = 0
    angle2 = 180
    speed = 2
    show_preview = False

    def simulate_trajectory(x, y, angle, vx):
        points = []
        ship_center_x = x + 25
        ship_center_y = y + 25
        temp_vx = vx * math.sin(math.radians(angle) - 80)
        temp_vy = tir_vitesse * math.cos(math.radians(angle) - 80)
        temp_x, temp_y = ship_center_x, ship_center_y
        for _ in range(50):
            accel_x, accel_y = 0, 0
            for planete in planetes:
                force = calculeNewton({"x": temp_x, "y": temp_y}, planete)
                accel_x += force[0]
                accel_y += force[1]
            temp_vx += accel_x
            temp_vy += accel_y
            temp_x += temp_vx
            temp_y += temp_vy
            for planete in planetes:
                if distance({"x": temp_x, "y": temp_y}, planete) < (planete["masse"] / 10):
                    return points  # Arrête la simulation si la trajectoire touche une planète
            if temp_x < 0 or temp_x > WIDTH or temp_y < 0 or temp_y > HEIGHT:
                break
            points.append((int(temp_x), int(temp_y)))
        return points

    while running:
        keys = pygame.key.get_pressed()
        moved = False
        if not projectiles:
            if joueur_actuel == 0:
                if carburant0 > 0:
                    if keys[pygame.K_UP]:
                        if keys[pygame.K_r]:
                            x += speed * math.cos(math.radians(angle)) * 2
                            y -= speed * math.sin(math.radians(angle)) * 2
                            carburant0 -= 0.5
                        else:
                            x += speed * math.cos(math.radians(angle))
                            y -= speed * math.sin(math.radians(angle))
                            carburant0 -= 0.1
                    if keys[pygame.K_DOWN]:
                        x -= speed * math.cos(math.radians(angle))
                        y += speed * math.sin(math.radians(angle))
                        carburant0 -= 0.1
                if keys[pygame.K_RIGHT]:
                    angle -= 1
                if keys[pygame.K_LEFT]:
                    angle += 1
                if moved:
                    last_move_time = pygame.time.get_ticks()
                    show_preview = False
                elif pygame.time.get_ticks() - last_move_time > 200:
                    show_preview = True

            if joueur_actuel == 1:
                if carburant1 > 0:
                    if keys[pygame.K_UP]:
                        if keys[pygame.K_r]:
                            ab += speed * math.cos(math.radians(angle2)) * 2
                            cd -= speed * math.sin(math.radians(angle2)) * 2
                            carburant1 -= 0.5
                            moved = True
                        else:
                            ab += speed * math.cos(math.radians(angle2))
                            cd -= speed * math.sin(math.radians(angle2))
                            carburant1 -= 0.1
                            moved = True
                if keys[pygame.K_DOWN]:
                    ab -= speed * math.cos(math.radians(angle2))
                    cd += speed * math.sin(math.radians(angle2))
                    carburant1 -= 0.1
                    moved = True
                if keys[pygame.K_RIGHT]:
                    angle2 -= 1
                if keys[pygame.K_LEFT]:
                    angle2 += 1
        if moved:
            last_move_time = pygame.time.get_ticks()
            show_preview = False
        elif pygame.time.get_ticks() - last_move_time > 200:
            show_preview = True

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    planetes.clear()  # Supprime toutes les anciennes planètes
                    # Distance minimale entre une planète et les vaisseaux
                    DISTANCE_MINIMALE_VAISSEAUX = 100  # Ajustez cette valeur selon vos besoins

                    # Génération des planètes
                    pla = random.randint(4, 6)  # Nombre de planètes
                    for i in range(pla):
                        while True:
                            gen_x = random.randint(0, WIDTH)
                            gen_y = random.randint(0, HEIGHT)
                            pv = 6
                            masse = random.randint(250, 1500)
                            i = random.randint(0, len(planet_images) - 1)
                            image = resize_planet_image(planet_images[i], masse)
                            image_abimee = resize_planet_image(planet_abimee[i], masse)

                            new_planet = {"x": gen_x, "y": gen_y, "masse": masse, "pv": pv, "compteur": 0,
                                          "image": image, "image_abimee": image_abimee}

                            # Vérifier la distance avec toutes les planètes existantes
                            if all(distance(new_planet, p) > ((p["masse"] / 10 + new_planet["masse"] / 10) + 30) for p
                                   in planetes) and \
                                    math.sqrt((gen_x - x) ** 2 + (gen_y - y) ** 2) > DISTANCE_MINIMALE_VAISSEAUX and \
                                    math.sqrt((gen_x - ab) ** 2 + (gen_y - cd) ** 2) > DISTANCE_MINIMALE_VAISSEAUX:
                                planetes.append(new_planet)
                                break  # Ajoute la nouvelle planète et quitte la boucle
                if event.key == pygame.K_SPACE:
                    if joueur_actuel == 0:
                        vX = vx * math.sin(math.radians(angle) - 80)
                        vy = tir_vitesse * math.cos(math.radians(angle) - 80)
                        projectiles.append({"x": x + 25, "y": y + 25, "vx": vX, "vy": vy, "color": BLUE})
                        pygame.mixer.Sound.play(missile_sound)
                        if keys[pygame.K_f]:
                            projectiles.append({"x": x + 25, "y": y + 25, "vx": vX, "vy": vy + 0.5, "color": BLUE})
                            pygame.mixer.Sound.play(missile_sound)
                            projectiles.append({"x": x + 25, "y": y + 25, "vx": vX, "vy": vy - 0.5, "color": BLUE})
                            pygame.mixer.Sound.play(missile_sound)
                        if keys[pygame.K_g]:
                            projectiles.append({"x": x + 25, "y": y + 25, "vx": vX, "vy": vy + 0.5, "color": BLUE})
                            pygame.mixer.Sound.play(missile_sound)
                            projectiles.append({"x": x + 25, "y": y + 25, "vx": vX, "vy": vy - 0.5, "color": BLUE})
                            pygame.mixer.Sound.play(missile_sound)
                            projectiles.append({"x": x + 25, "y": y + 25, "vx": vX, "vy": vy + 1, "color": BLUE})
                            pygame.mixer.Sound.play(missile_sound)
                            projectiles.append({"x": x + 25, "y": y + 25, "vx": vX, "vy": vy - 1, "color": BLUE})
                            pygame.mixer.Sound.play(missile_sound)
                        joueur_actuel = 1
                        carburant0 = min(carburant0 + 5, 100)
                    elif joueur_actuel == 1:
                        vab = vx * math.sin(math.radians(angle2) - 80)
                        vcd = tir_vitesse * math.cos(math.radians(angle2) - 80)
                        projectiles.append({"x": ab + 25, "y": cd + 25, "vx": vab, "vy": vcd, "color": RED})
                        pygame.mixer.Sound.play(missile_sound)
                        if keys[pygame.K_f]:
                            projectiles.append({"x": ab + 25, "y": cd + 25, "vx": vab, "vy": vcd - 0.5, "color": RED})
                            pygame.mixer.Sound.play(missile_sound)
                            projectiles.append({"x": ab + 25, "y": cd + 25, "vx": vab, "vy": vcd + 0.5, "color": RED})
                            pygame.mixer.Sound.play(missile_sound)
                        if keys[pygame.K_g]:
                            projectiles.append({"x": ab + 25, "y": cd + 25, "vx": vab, "vy": vcd + 1, "color": RED})
                            pygame.mixer.Sound.play(missile_sound)
                            projectiles.append({"x": ab + 25, "y": cd + 25, "vx": vab, "vy": vcd - 1, "color": RED})
                            pygame.mixer.Sound.play(missile_sound)
                            projectiles.append({"x": ab + 25, "y": cd + 25, "vx": vab, "vy": vcd + 0.5, "color": RED})
                            pygame.mixer.Sound.play(missile_sound)
                            projectiles.append({"x": ab + 25, "y": cd + 25, "vx": vab, "vy": vcd - 0.5, "color": RED})
                            pygame.mixer.Sound.play(missile_sound)
                        joueur_actuel = 0
                        carburant1 = min(carburant1 + 5, 100)
                if event.key == pygame.K_a:
                    running = False
                    pygame.quit()
                if event.key == pygame.K_q:
                    if joueur_actuel == 0:
                        angle += 1
                    else:
                        angle2 += 1
                if event.key == pygame.K_d:
                    if joueur_actuel == 0:
                        angle -= 1
                    else:
                        angle2 -= 1
                if event.key == pygame.K_e:
                    preview_enabled = not preview_enabled
                if event.key == pygame.K_s and vx > 5:
                    vx -= 1
                if event.key == pygame.K_z and vx < 15:
                    vx += 1

        # Effacer l'écran
        screen.fill(DARK_BLUE)  # Fond bleu foncé (galaxie)

        # Dessin des étoiles
        for star in stars:
            pygame.draw.circle(screen, YELLOW, star, 1)  # Petits points jaunes

        def dessiner_jauge_carburant(screen, x, y, largeur, hauteur, carburant):
            # Calculer la largeur de la jauge en fonction du carburant restant
            carburant_largeur = (carburant / 100) * largeur
            # Dessiner le fond de la jauge (rouge)
            pygame.draw.rect(screen, RED, (x, y, largeur, hauteur))
            # Dessiner la jauge de carburant (bleue)
            pygame.draw.rect(screen, BLUE, (x, y, carburant_largeur, hauteur))
            # Dessiner la bordure de la jauge (noir)
            pygame.draw.rect(screen, BLACK, (x, y, largeur, hauteur), 2)

        dessiner_jauge_carburant(screen, 0.01 * WIDTH, 0.04 * HEIGHT, 0.2 * WIDTH, 0.04 * HEIGHT, carburant0)
        dessiner_jauge_carburant(screen, WIDTH - 0.21 * WIDTH, 0.04 * HEIGHT, 0.2 * WIDTH, 0.04 * HEIGHT, carburant1)

        # Dessiner les planètes
        for planete in planetes:
            image_rect = planete["image"].get_rect(center=(planete["x"], planete["y"]))
            screen.blit(planete["image"], image_rect.topleft)

        # Dessiner la position initiale du projectile en bleu
        rotated_image = pygame.transform.rotate(object_image, angle)
        new_rect = rotated_image.get_rect(center=object_image.get_rect(topleft=(x, y)).center)
        screen.blit(rotated_image, new_rect.topleft)

        rotated_image = pygame.transform.rotate(object_image, angle2)
        new_rect = rotated_image.get_rect(center=object_image.get_rect(topleft=(ab, cd)).center)
        screen.blit(rotated_image, new_rect.topleft)

        # Mettre à jour et dessiner les projectiles
        for proj in projectiles:
            accel_x, accel_y = 0, 0
            collide = 0
            for planete in planetes:  # permet de calculer pour chaque planete l'acceleration de la balle
                force = calculeNewton(proj, planete)
                accel_x += force[0]
                accel_y += force[1]
                collided = (math.sqrt((proj["x"] - planete["x"]) ** 2 + (proj["y"] - planete["y"]) ** 2) <= planete[
                    "masse"] / 10)  # permet de calculer pour chaque planete les colisions avec les balles
                if collided and collide == 0:
                    planete['pv'] -= 1
                    if planete["pv"] == 3:
                        planete["image"] = planete["image_abimee"]
                    if planete['pv'] <= 0:
                        planetes.remove(planete)
                    collide += 1
                    pygame.mixer.Sound.play(explosion_sound)
                    explosions.append({"x": proj["x"], "y": proj["y"], "frame": 0})
                    projectiles.remove(proj)
            off_screen = (proj["x"] < 0 or proj["x"] > WIDTH or proj["y"] < 0 or proj[
                "y"] > HEIGHT)  # verif si la balle est dans l'écran
            if off_screen:
                projectiles.remove(proj)  # suprime la balle si elle est hors de l'écran
            # Mise à jour des vitesses et positions
            proj["vx"] += accel_x
            proj["vy"] += accel_y
            proj["x"] += proj["vx"]
            proj["y"] += proj["vy"]

            # Dessiner le projectile
            angle_proj = math.degrees(math.atan2(proj["vy"], proj["vx"]))
            if proj["color"] == BLUE:
                rotated_missile = pygame.transform.rotate(missile_bleu, -angle_proj - 90)
            else:
                rotated_missile = pygame.transform.rotate(missile_rouge, -angle_proj - 90)
            new_rect = rotated_missile.get_rect(center=(proj["x"], proj["y"]))
            screen.blit(rotated_missile, new_rect.topleft)

            # Vérifier les collisions des projectiles avec les vaisseaux
            for proj in projectiles[:]:  # Copie de la liste pour éviter les erreurs de suppression
                if proj["color"] == RED and collision_vaisseau(proj, x, y):
                    pygame.mixer.Sound.play(explosion_sound)  # Explosion du vaisseau bleu
                    explosions.append({"x": proj["x"], "y": proj["y"], "frame": 0})
                    score1 += 1
                    if score1 == 5:
                        gameover2()  # Afficher la fonction Game Over
                        pygame.display.flip()  # Met à jour l'écran pour montrer le résultat
                        pygame.time.wait(2000)  # Attendre 2 secondes avant de quitter (facultatif)
                        pygame.quit()  # Fermer proprement Pygame
                        return  # Quitte la boucle ou la fonction principale
                    projectiles.remove(proj)

                elif proj["color"] == BLUE and collision_vaisseau(proj, ab, cd):
                    pygame.mixer.Sound.play(explosion_sound)  # Explosion du vaisseau rouge
                    explosions.append({"x": proj["x"], "y": proj["y"], "frame": 0})
                    score2 += 1
                    if score2 == 5:
                        gameover1()  # Afficher la fonction Game Over
                        pygame.display.flip()  # Met à jour l'écran pour montrer le résultat
                        pygame.time.wait(2000)  # Attendre 2 secondes avant de quitter (facultatif)
                        pygame.quit()  # Fermer proprement Pygame
                        return  # Quitte la boucle ou la fonction principale
                    projectiles.remove(proj)

            # Affichage des explosions
        for explosion in explosions:
            frame_index = explosion["frame"] // 5
            if frame_index < len(explosion_frames):
                screen.blit(explosion_frames[frame_index], (explosion["x"] - 50, explosion["y"] - 50))
                explosion["frame"] += 1
            else:
                explosions.remove(explosion)

        # affiche puissance du tir
        if joueur_actuel == 0:
            # Affichage de la vitesse et de l'angle
            txt = big_font.render(f'Vitesse: {round(vx, 2)} | Angle: {round(angle, 1) % 360}°', True, WHITE)
            # Affichage du pseudo juste en dessous du texte de la jauge (ou de l'élément précédent)
            txt_pseudo = big_font.render(f' Player1: {pseudos[0]}', True, WHITE)
            screen.blit(txt_pseudo, (25, 120))  # Affichage du pseudo
            # Affichage du texte de la vitesse et de l'angle à sa place
            screen.blit(txt, (25, 85))
        elif joueur_actuel == 1:
            txt = big_font.render(f'Vitesse: {round(vx, 2)} | Angle: {round(angle2 - 180, 1) % 360}°', True, WHITE)
            screen.blit(txt, (WIDTH - 425, 85))
            txt_pseudo = big_font.render(f' Player2: {pseudos[1]}', True, WHITE)
            screen.blit(txt_pseudo, (WIDTH - 425, 120))  # Affichage du pseudo

        if joueur_actuel == 0:
            if show_preview and preview_enabled:
                trajectory = simulate_trajectory(x, y, angle, vx)
                for point in trajectory:
                    pygame.draw.circle(screen, WHITE, point, 2)
        elif joueur_actuel == 1:
            if show_preview and preview_enabled:
                trajectory = simulate_trajectory(ab, cd, angle2, vx)
                for point in trajectory:
                    pygame.draw.circle(screen, WHITE, point, 2)

        txt2 = big_font.render(f'{score2} | {score1}', True, WHITE)
        screen.blit(txt2, (0.4 * WIDTH, 0.04 * HEIGHT))
        # Mettre à jour l'affichage
        pygame.display.flip()
        clock.tick(60)
def jeu_avance():

    # Initialisation de Pygame
    pygame.init()

    # Captation de la résolution de l'écran afin d'adapter le jeu à toutes les résolutions
    root = Tk()
    screen_width = root.winfo_screenwidth() #capte la largeur de l'écran
    screen_height = root.winfo_screenheight() #capte la hauteur de l'écran
    root.destroy()
    # Configuration de la fenêtre
    WIDTH, HEIGHT = screen_width, screen_height
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Moteur physique")
    font_size = round(0.024 * WIDTH)
    # texte
    big_font = pygame.font.SysFont('Arial', font_size)
    small_font = pygame.font.SysFont('Arial', font_size)

    # Génération des étoiles
    NUM_STARS = 2000  # Nombre d'étoiles
    stars = [(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(NUM_STARS)]

    # Couleurs
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    BLUE = (0, 0, 255)
    DARK_BLUE = (10, 10, 50)
    WHITE = (255, 255, 255)
    # Couleur Planetes
    planet_images = [
        pygame.image.load('planete_1.png'),
        pygame.image.load('planete_2.png'),
        pygame.image.load('planete_3.png'),
        pygame.image.load('planete_4.png')
    ]

    planet_abimee = [
        pygame.image.load('planete_1_2.png'),
        pygame.image.load('planete_2_2.png'),
        pygame.image.load('planete_3_2.png'),
        pygame.image.load('planete_4_2.png')
    ]


    # Constantes physiques
    G = 10
    tir_vitesse = 10
    # vitesse initiale des balles
    vx = 10
    vy = 0
    vab = 10
    vcd = 0
    # score initiale
    score1 = 0
    score2 = 0

    # Coordonnées de référence pour la génération des planètes via touche t
    ref_x1, ref_y1 = 0.2*WIDTH,  0.2 * HEIGHT
    ref_x2, ref_y2 = 0.8*WIDTH, 0.2 * HEIGHT

    # carburant pour les vaisseaux
    carburant0 = 100
    carburant1 = 100

    # Liste des planètes (coordonnées et masses)
    planetes = []

    # permet de mesurer la distance entre 2 planetes
    def distance(p1, p2):
        return math.sqrt((p1["x"] - p2["x"]) ** 2 + (p1["y"] - p2["y"]) ** 2)

    # Permet de redimensionner les images des planetes

    def resize_planet_image(image, masse):
        size = int(masse / 4)
        return pygame.transform.scale(image, (size, size))

    # coordonnées d'apparition du vaisseau 1 puis 2
    x = 0.04 * WIDTH
    y = 0.04 * HEIGHT

    ab = 0.8 * WIDTH
    cd = 0.2 * HEIGHT

    # Distance minimale entre une planète et les vaisseaux
    DISTANCE_MINIMALE_VAISSEAUX = 100  # Ajustez cette valeur selon vos besoins

    # Génération des planètes
    pla = random.randint(8, 10)  # Nombre de planètes
    for i in range(pla):
        while True:
            gen_x = random.randint(0, WIDTH)
            gen_y = random.randint(0, HEIGHT)
            pv = 6
            masse = random.randint(250, 1500)
            i = random.randint(0, len(planet_images) - 1)
            image = resize_planet_image(planet_images[i], masse)
            image_abimee = resize_planet_image(planet_abimee[i], masse)

            new_planet = {"x": gen_x, "y": gen_y, "masse": masse, "pv": pv, "compteur": 0, "image": image,
                          "image_abimee": image_abimee}

            # Vérifier la distance avec toutes les planètes existantes
            if all(distance(new_planet, p) > ((p["masse"] / 10 + new_planet["masse"] / 10) + 30) for p in planetes) and \
                    math.sqrt((gen_x - x) ** 2 + (gen_y - y) ** 2) > DISTANCE_MINIMALE_VAISSEAUX and \
                    math.sqrt((gen_x - ab) ** 2 + (gen_y - cd) ** 2) > DISTANCE_MINIMALE_VAISSEAUX:
                planetes.append(new_planet)
                break  # Ajoute la nouvelle planète et quitte la boucle
    # Liste des projectiles
    projectiles = []
    explosions = []

    object_image = pygame.image.load('vaisseau.png')
    object_image = pygame.transform.scale(object_image, (50, 50))
    missile_bleu = pygame.image.load('missile bleu.png')
    missile_bleu = pygame.transform.scale(missile_bleu, (44, 44))
    missile_rouge = pygame.image.load('missile rouge.png')
    missile_rouge = pygame.transform.scale(missile_rouge, (44, 44))

    explosion_frames = [pygame.image.load(f'explosion/frame_{i}.png') for i in range(6)]
    explosion_sound = pygame.mixer.Sound("1917.mp3")
    explosion_sound.set_volume(0.2)  # Réglez le volume à 20% du volume maximal
    missile_sound = pygame.mixer.Sound("missile.mp3")
    musique = pygame.mixer.Sound("04. Hacking Malfunction (Battle).mp3")
    musique.play(-1)

    # Calcul des forces gravitationnelles
    def calculeNewton(proj, planete):
        dx = planete["x"] - proj["x"]
        dy = planete["y"] - proj["y"]
        distance_carre = dx ** 2 + dy ** 2

        force_magnitude = G * planete["masse"] / distance_carre
        distance = math.sqrt(distance_carre)
        return [force_magnitude * dx / distance, force_magnitude * dy / distance]

    # Détection de collision entre missiles et vaisseaux
    def collision_vaisseau(proj, vaisseau_x, vaisseau_y):
        distance_proj_vaisseau = math.sqrt((proj["x"] - (vaisseau_x + 25)) ** 2 + (proj["y"] - (vaisseau_y + 25)) ** 2)
        return distance_proj_vaisseau < 30  # Rayon de collision

    preview_enabled = True
    # Boucle principale
    clock = pygame.time.Clock()
    running = True
    joueur_actuel = 0
    vy = 1
    vcd = 1
    last_move_time = pygame.time.get_ticks()
    angle = 0
    angle2 = 180
    speed = 2
    show_preview = False

    def simulate_trajectory(x, y, angle, vx):
        points = []
        ship_center_x = x + 25
        ship_center_y = y + 25
        temp_vx = vx * math.sin(math.radians(angle) - 80)
        temp_vy = tir_vitesse * math.cos(math.radians(angle) - 80)
        temp_x, temp_y = ship_center_x, ship_center_y
        for _ in range(50):
            accel_x, accel_y = 0, 0
            for planete in planetes:
                force = calculeNewton({"x": temp_x, "y": temp_y}, planete)
                accel_x += force[0]
                accel_y += force[1]
            temp_vx += accel_x
            temp_vy += accel_y
            temp_x += temp_vx
            temp_y += temp_vy
            for planete in planetes:
                if distance({"x": temp_x, "y": temp_y}, planete) < (planete["masse"] / 10):
                    return points  # Arrête la simulation si la trajectoire touche une planète
            if temp_x < 0 or temp_x > WIDTH or temp_y < 0 or temp_y > HEIGHT:
                break
            points.append((int(temp_x), int(temp_y)))
        return points

    while running:
        keys = pygame.key.get_pressed()
        moved = False
        if not projectiles:
            if joueur_actuel == 0:
                if carburant0 > 0:
                    if keys[pygame.K_UP]:
                        if keys[pygame.K_r]:
                            x += speed * math.cos(math.radians(angle)) * 2
                            y -= speed * math.sin(math.radians(angle)) * 2
                            carburant0 -= 0.5
                        else:
                            x += speed * math.cos(math.radians(angle))
                            y -= speed * math.sin(math.radians(angle))
                            carburant0 -= 0.1
                    if keys[pygame.K_DOWN]:
                        x -= speed * math.cos(math.radians(angle))
                        y += speed * math.sin(math.radians(angle))
                        carburant0 -= 0.1
                if keys[pygame.K_RIGHT]:
                    angle -= 1
                if keys[pygame.K_LEFT]:
                    angle += 1
                if moved:
                    last_move_time = pygame.time.get_ticks()
                    show_preview = False
                elif pygame.time.get_ticks() - last_move_time > 200:
                    show_preview = True

            if joueur_actuel == 1:
                if carburant1 > 0:
                    if keys[pygame.K_UP]:
                        if keys[pygame.K_r]:
                            ab += speed * math.cos(math.radians(angle2)) * 2
                            cd -= speed * math.sin(math.radians(angle2)) * 2
                            carburant1 -= 0.5
                            moved = True
                        else:
                            ab += speed * math.cos(math.radians(angle2))
                            cd -= speed * math.sin(math.radians(angle2))
                            carburant1 -= 0.1
                            moved = True
                if keys[pygame.K_DOWN]:
                    ab -= speed * math.cos(math.radians(angle2))
                    cd += speed * math.sin(math.radians(angle2))
                    carburant1 -= 0.1
                    moved = True
                if keys[pygame.K_RIGHT]:
                    angle2 -= 1
                if keys[pygame.K_LEFT]:
                    angle2 += 1
        if moved:
            last_move_time = pygame.time.get_ticks()
            show_preview = False
        elif pygame.time.get_ticks() - last_move_time > 200:
            show_preview = True

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    planetes.clear()  # Supprime toutes les anciennes planètes
                    # Distance minimale entre une planète et les vaisseaux
                    DISTANCE_MINIMALE_VAISSEAUX = 100  # Ajustez cette valeur selon vos besoins

                    # Génération des planètes
                    pla = random.randint(8, 10)  # Nombre de planètes
                    for i in range(pla):
                        while True:
                            gen_x = random.randint(0, WIDTH)
                            gen_y = random.randint(0, HEIGHT)
                            pv = 6
                            masse = random.randint(250, 1500)
                            i = random.randint(0, len(planet_images) - 1)
                            image = resize_planet_image(planet_images[i], masse)
                            image_abimee = resize_planet_image(planet_abimee[i], masse)

                            new_planet = {"x": gen_x, "y": gen_y, "masse": masse, "pv": pv, "compteur": 0,
                                          "image": image, "image_abimee": image_abimee}

                            # Vérifier la distance avec toutes les planètes existantes
                            if all(distance(new_planet, p) > ((p["masse"] / 10 + new_planet["masse"] / 10) + 30) for p
                                   in planetes) and \
                                    math.sqrt((gen_x - x) ** 2 + (gen_y - y) ** 2) > DISTANCE_MINIMALE_VAISSEAUX and \
                                    math.sqrt((gen_x - ab) ** 2 + (gen_y - cd) ** 2) > DISTANCE_MINIMALE_VAISSEAUX:
                                planetes.append(new_planet)
                                break  # Ajoute la nouvelle planète et quitte la boucle
                if event.key == pygame.K_SPACE:
                    if joueur_actuel == 0:
                        vX = vx * math.sin(math.radians(angle) - 80)
                        vy = tir_vitesse * math.cos(math.radians(angle) - 80)
                        projectiles.append({"x": x + 25, "y": y + 25, "vx": vX, "vy": vy, "color": BLUE})
                        pygame.mixer.Sound.play(missile_sound)
                        if keys[pygame.K_f]:
                            projectiles.append({"x": x + 25, "y": y + 25, "vx": vX, "vy": vy + 0.5, "color": BLUE})
                            pygame.mixer.Sound.play(missile_sound)
                            projectiles.append({"x": x + 25, "y": y + 25, "vx": vX, "vy": vy - 0.5, "color": BLUE})
                            pygame.mixer.Sound.play(missile_sound)
                        if keys[pygame.K_g]:
                            projectiles.append({"x": x + 25, "y": y + 25, "vx": vX, "vy": vy + 0.5, "color": BLUE})
                            pygame.mixer.Sound.play(missile_sound)
                            projectiles.append({"x": x + 25, "y": y + 25, "vx": vX, "vy": vy - 0.5, "color": BLUE})
                            pygame.mixer.Sound.play(missile_sound)
                            projectiles.append({"x": x + 25, "y": y + 25, "vx": vX, "vy": vy + 1, "color": BLUE})
                            pygame.mixer.Sound.play(missile_sound)
                            projectiles.append({"x": x + 25, "y": y + 25, "vx": vX, "vy": vy - 1, "color": BLUE})
                            pygame.mixer.Sound.play(missile_sound)
                        joueur_actuel = 1
                        carburant0 = min(carburant0 + 5, 100)
                    elif joueur_actuel == 1:
                        vab = vx * math.sin(math.radians(angle2) - 80)
                        vcd = tir_vitesse * math.cos(math.radians(angle2) - 80)
                        projectiles.append({"x": ab + 25, "y": cd + 25, "vx": vab, "vy": vcd, "color": RED})
                        pygame.mixer.Sound.play(missile_sound)
                        if keys[pygame.K_f]:
                            projectiles.append({"x": ab + 25, "y": cd + 25, "vx": vab, "vy": vcd - 0.5, "color": RED})
                            pygame.mixer.Sound.play(missile_sound)
                            projectiles.append({"x": ab + 25, "y": cd + 25, "vx": vab, "vy": vcd + 0.5, "color": RED})
                            pygame.mixer.Sound.play(missile_sound)
                        if keys[pygame.K_g]:
                            projectiles.append({"x": ab + 25, "y": cd + 25, "vx": vab, "vy": vcd + 1, "color": RED})
                            pygame.mixer.Sound.play(missile_sound)
                            projectiles.append({"x": ab + 25, "y": cd + 25, "vx": vab, "vy": vcd - 1, "color": RED})
                            pygame.mixer.Sound.play(missile_sound)
                            projectiles.append({"x": ab + 25, "y": cd + 25, "vx": vab, "vy": vcd + 0.5, "color": RED})
                            pygame.mixer.Sound.play(missile_sound)
                            projectiles.append({"x": ab + 25, "y": cd + 25, "vx": vab, "vy": vcd - 0.5, "color": RED})
                            pygame.mixer.Sound.play(missile_sound)
                        joueur_actuel = 0
                        carburant1 = min(carburant1 + 5, 100)
                if event.key == pygame.K_a:
                    running = False
                    pygame.quit()
                if event.key == pygame.K_q:
                    if joueur_actuel == 0:
                        angle += 1
                    else:
                        angle2 += 1
                if event.key == pygame.K_d:
                    if joueur_actuel == 0:
                        angle -= 1
                    else:
                        angle2 -= 1
                if event.key == pygame.K_e:
                    preview_enabled = not preview_enabled
                if event.key == pygame.K_s and vx > 5:
                    vx -= 1
                if event.key == pygame.K_z and vx < 15:
                    vx += 1

        # Effacer l'écran
        screen.fill(DARK_BLUE)  # Fond bleu foncé (galaxie)

        # Dessin des étoiles
        for star in stars:
            pygame.draw.circle(screen, YELLOW, star, 1)  # Petits points jaunes

        def dessiner_jauge_carburant(screen, x, y, largeur, hauteur, carburant):
            # Calculer la largeur de la jauge en fonction du carburant restant
            carburant_largeur = (carburant / 100) * largeur
            # Dessiner le fond de la jauge (rouge)
            pygame.draw.rect(screen, RED, (x, y, largeur, hauteur))
            # Dessiner la jauge de carburant (bleue)
            pygame.draw.rect(screen, BLUE, (x, y, carburant_largeur, hauteur))
            # Dessiner la bordure de la jauge (noir)
            pygame.draw.rect(screen, BLACK, (x, y, largeur, hauteur), 2)

        dessiner_jauge_carburant(screen, 0.01 * WIDTH, 0.04 * HEIGHT, 0.2 * WIDTH, 0.04 * HEIGHT, carburant0)
        dessiner_jauge_carburant(screen, WIDTH - 0.21 * WIDTH, 0.04 * HEIGHT, 0.2 * WIDTH, 0.04 * HEIGHT, carburant1)

        # Dessiner les planètes
        for planete in planetes:
            image_rect = planete["image"].get_rect(center=(planete["x"], planete["y"]))
            screen.blit(planete["image"], image_rect.topleft)

        # Dessiner la position initiale du projectile en bleu
        rotated_image = pygame.transform.rotate(object_image, angle)
        new_rect = rotated_image.get_rect(center=object_image.get_rect(topleft=(x, y)).center)
        screen.blit(rotated_image, new_rect.topleft)

        rotated_image = pygame.transform.rotate(object_image, angle2)
        new_rect = rotated_image.get_rect(center=object_image.get_rect(topleft=(ab, cd)).center)
        screen.blit(rotated_image, new_rect.topleft)

        # Mettre à jour et dessiner les projectiles
        for proj in projectiles:
            accel_x, accel_y = 0, 0
            collide = 0
            for planete in planetes:  # permet de calculer pour chaque planete l'acceleration de la balle
                force = calculeNewton(proj, planete)
                accel_x += force[0]
                accel_y += force[1]
                collided = (math.sqrt((proj["x"] - planete["x"]) ** 2 + (proj["y"] - planete["y"]) ** 2) <= planete[
                    "masse"] / 10)  # permet de calculer pour chaque planete les colisions avec les balles
                if collided and collide == 0:
                    planete['pv'] -= 1
                    if planete["pv"] == 3:
                        planete["image"] = planete["image_abimee"]
                    if planete['pv'] <= 0:
                        planetes.remove(planete)
                    collide += 1
                    pygame.mixer.Sound.play(explosion_sound)
                    explosions.append({"x": proj["x"], "y": proj["y"], "frame": 0})
                    projectiles.remove(proj)
            off_screen = (proj["x"] < 0 or proj["x"] > WIDTH or proj["y"] < 0 or proj[
                "y"] > HEIGHT)  # verif si la balle est dans l'écran
            if off_screen:
                projectiles.remove(proj)  # suprime la balle si elle est hors de l'écran
            # Mise à jour des vitesses et positions
            proj["vx"] += accel_x
            proj["vy"] += accel_y
            proj["x"] += proj["vx"]
            proj["y"] += proj["vy"]

            # Dessiner le projectile
            angle_proj = math.degrees(math.atan2(proj["vy"], proj["vx"]))
            if proj["color"] == BLUE:
                rotated_missile = pygame.transform.rotate(missile_bleu, -angle_proj - 90)
            else:
                rotated_missile = pygame.transform.rotate(missile_rouge, -angle_proj - 90)
            new_rect = rotated_missile.get_rect(center=(proj["x"], proj["y"]))
            screen.blit(rotated_missile, new_rect.topleft)

            # Vérifier les collisions des projectiles avec les vaisseaux
            for proj in projectiles[:]:  # Copie de la liste pour éviter les erreurs de suppression
                if proj["color"] == RED and collision_vaisseau(proj, x, y):
                    pygame.mixer.Sound.play(explosion_sound)  # Explosion du vaisseau bleu
                    explosions.append({"x": proj["x"], "y": proj["y"], "frame": 0})
                    score1 += 1
                    if score1 == 5:
                        gameover2()  # Afficher la fonction Game Over
                        pygame.display.flip()  # Met à jour l'écran pour montrer le résultat
                        pygame.time.wait(2000)  # Attendre 2 secondes avant de quitter (facultatif)
                        pygame.quit()  # Fermer proprement Pygame
                        return  # Quitte la boucle ou la fonction principale
                    projectiles.remove(proj)
                    planetes.clear()  # Supprime toutes les anciennes planètes
                    # Distance minimale entre une planète et les vaisseaux
                    DISTANCE_MINIMALE_VAISSEAUX = 100  # Ajustez cette valeur selon vos besoins

                    # Génération des planètes
                    pla = random.randint(8, 10)  # Nombre de planètes
                    for i in range(pla):
                        while True:
                            gen_x = random.randint(0, WIDTH)
                            gen_y = random.randint(0, HEIGHT)
                            pv = 6
                            masse = random.randint(250, 1500)
                            i = random.randint(0, len(planet_images) - 1)
                            image = resize_planet_image(planet_images[i], masse)
                            image_abimee = resize_planet_image(planet_abimee[i], masse)

                            new_planet = {"x": gen_x, "y": gen_y, "masse": masse, "pv": pv, "compteur": 0,
                                          "image": image, "image_abimee": image_abimee}

                            # Vérifier la distance avec toutes les planètes existantes
                            if all(distance(new_planet, p) > ((p["masse"] / 10 + new_planet["masse"] / 10) + 30) for p
                                   in planetes) and \
                                    math.sqrt((gen_x - x) ** 2 + (gen_y - y) ** 2) > DISTANCE_MINIMALE_VAISSEAUX and \
                                    math.sqrt((gen_x - ab) ** 2 + (gen_y - cd) ** 2) > DISTANCE_MINIMALE_VAISSEAUX:
                                planetes.append(new_planet)
                                break  # Ajoute la nouvelle planète et quitte la boucle
                elif proj["color"] == BLUE and collision_vaisseau(proj, ab, cd):
                    pygame.mixer.Sound.play(explosion_sound)  # Explosion du vaisseau rouge
                    explosions.append({"x": proj["x"], "y": proj["y"], "frame": 0})
                    score2 += 1
                    if score2 == 5:
                        gameover1()  # Afficher la fonction Game Over
                        pygame.display.flip()  # Met à jour l'écran pour montrer le résultat
                        pygame.time.wait(2000)  # Attendre 2 secondes avant de quitter (facultatif)
                        pygame.quit()  # Fermer proprement Pygame
                        return  # Quitte la boucle ou la fonction principale
                    planetes.clear()  # Supprime toutes les anciennes planètes
                    # Distance minimale entre une planète et les vaisseaux
                    DISTANCE_MINIMALE_VAISSEAUX = 100  # Ajustez cette valeur selon vos besoins

                    # Génération des planètes
                    pla = random.randint(8, 10)  # Nombre de planètes
                    for i in range(pla):
                        while True:
                            gen_x = random.randint(0, WIDTH)
                            gen_y = random.randint(0, HEIGHT)
                            pv = 6
                            masse = random.randint(250, 1500)
                            i = random.randint(0, len(planet_images) - 1)
                            image = resize_planet_image(planet_images[i], masse)
                            image_abimee = resize_planet_image(planet_abimee[i], masse)

                            new_planet = {"x": gen_x, "y": gen_y, "masse": masse, "pv": pv, "compteur": 0,
                                          "image": image, "image_abimee": image_abimee}

                            # Vérifier la distance avec toutes les planètes existantes
                            if all(distance(new_planet, p) > ((p["masse"] / 10 + new_planet["masse"] / 10) + 30) for p
                                   in planetes) and \
                                    math.sqrt((gen_x - x) ** 2 + (gen_y - y) ** 2) > DISTANCE_MINIMALE_VAISSEAUX and \
                                    math.sqrt((gen_x - ab) ** 2 + (gen_y - cd) ** 2) > DISTANCE_MINIMALE_VAISSEAUX:
                                planetes.append(new_planet)
                                break  # Ajoute la nouvelle planète et quitte la boucle
                    projectiles.remove(proj)

            # Affichage des explosions
        for explosion in explosions:
            frame_index = explosion["frame"] // 5
            if frame_index < len(explosion_frames):
                screen.blit(explosion_frames[frame_index], (explosion["x"] - 50, explosion["y"] - 50))
                explosion["frame"] += 1
            else:
                explosions.remove(explosion)

        # affiche puissance du tir
        if joueur_actuel == 0:
            # Affichage de la vitesse et de l'angle
            txt = big_font.render(f'Vitesse: {round(vx, 2)} | Angle: {round(angle, 1) % 360}°', True, WHITE)
            # Affichage du pseudo juste en dessous du texte de la jauge (ou de l'élément précédent)
            txt_pseudo = big_font.render(f' Player1: {pseudos[0]}', True, WHITE)
            screen.blit(txt_pseudo, (25, 120))  # Affichage du pseudo
            # Affichage du texte de la vitesse et de l'angle à sa place
            screen.blit(txt, (25, 85))
        elif joueur_actuel == 1:
            txt = big_font.render(f'Vitesse: {round(vx, 2)} | Angle: {round(angle2 - 180, 1) % 360}°', True, WHITE)
            screen.blit(txt, (WIDTH - 425, 85))
            txt_pseudo = big_font.render(f' Player2: {pseudos[1]}', True, WHITE)
            screen.blit(txt_pseudo, (WIDTH - 425, 120))  # Affichage du pseudo

        if joueur_actuel == 0:
            if show_preview and preview_enabled:
                trajectory = simulate_trajectory(x, y, angle, vx)
                for point in trajectory:
                    pygame.draw.circle(screen, WHITE, point, 2)
        elif joueur_actuel == 1:
            if show_preview and preview_enabled:
                trajectory = simulate_trajectory(ab, cd, angle2, vx)
                for point in trajectory:
                    pygame.draw.circle(screen, WHITE, point, 2)

        txt2 = big_font.render(f'{score2} | {score1}', True, WHITE)
        screen.blit(txt2, (0.4 * WIDTH, 0.04 * HEIGHT))
        # Mettre à jour l'affichage
        pygame.display.flip()
        clock.tick(60)
def Afficher_consignes(niveau):
    pygame.init()  # Initialisation de Pygame

    # Récupère la taille de l'écran de l'utilisateur
    info = pygame.display.Info()
    largeur, hauteur = info.current_w, info.current_h

    # Crée une fenêtre redimensionnable
    fenetre = pygame.display.set_mode((largeur, hauteur), pygame.RESIZABLE)
    pygame.display.set_caption("Consignes")

    # Chargement et mise à l'échelle des images de fond
    fond1 = pygame.transform.scale(pygame.image.load("consigne1.png").convert(), (largeur, hauteur))
    fond2 = pygame.transform.scale(pygame.image.load("consigne2.png").convert(), (largeur, hauteur))

    # Chargement des boutons avec transparence
    bouton_ok = pygame.image.load("ok.png").convert_alpha()
    rect_ok = bouton_ok.get_rect(topleft=(600, 500))

    bouton_jouer = pygame.image.load("jouer.png").convert_alpha()
    rect_jouer = bouton_jouer.get_rect(topleft=(600, 500))

    affichage_etape = 1  # Étape 1 : affichage du premier fond
    en_cours = True

    while en_cours:
        fenetre.fill((0, 0, 0))  # Nettoie l'écran
        taille_fenetre = fenetre.get_size()

        # Affiche le bon fond et bouton selon l'étape
        if affichage_etape == 1:
            fond = fond1
            bouton = bouton_ok
            rect = rect_ok
        else:
            fond = fond2
            bouton = bouton_jouer
            rect = rect_jouer

        # Redimensionne si la fenêtre a changé de taille
        if taille_fenetre != fond.get_size():
            fond_affiche = pygame.transform.scale(fond, taille_fenetre)
        else:
            fond_affiche = fond

        # Affiche le fond et le bouton
        fenetre.blit(fond_affiche, (0, 0))
        fenetre.blit(bouton, rect)

        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                en_cours = False

            elif event.type == pygame.VIDEORESIZE:
                # Met à jour la fenêtre à la nouvelle taille
                fenetre = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if rect.collidepoint(event.pos):
                    if affichage_etape == 1:
                        affichage_etape = 2  # Passe à l'étape suivante
                    else:

                        if niveau == 1:
                            jeu_debutant()
                        if niveau == 2:
                            jeu_intermediaire()
                        if niveau == 3:
                            jeu_avance()

                        en_cours = False

        pygame.display.flip()  # Rafraîchit l'écran

    pygame.quit()  # Ferme proprement Pygame
def fctmenu():
    pygame.init()

    #Canevas qui contient la fenetre de menu
    canevas = Canvas(fenetre, borderwidth=0, highlightthickness=0, width=800, height=600, bg="#322432")
    canevas.create_image(400, 300, image=fond_menu)

    #boutons du menu

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
    visee=0
    # Fonction Toggle Visée
    def toggle_visee():
        if visee_auto.get():
            bouton_visee.config(text="Visée automatique : Activée")
        else:
            bouton_visee.config(text="Visée automatique : Désactivée")
            visee = 1

    # Titre


    # Bouton Visée Automatique
    bouton_visee = Button(canevas, text="Visée automatique : Désactivée",command=lambda: [visee_auto.set(not visee_auto.get()), toggle_visee()], bg="#322432",fg="white")
    bouton_visee.place(x=300, y=80)




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

    return
def quitter():
    if messagebox.askokcancel("Quitter", "Voulez-vous vraiment quitter ?"):
        fenetre.quit()


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
debutant = Image.open("debutant.png")
intermediaire = Image.open("intermediaire.png")
avance = Image.open("avance.png")



#taille des boutons
taillebt = (200, 100)
taille_icones =(20,20)
taillebt3=(150,75)

#modification de la taille des boutons
menu_nvl_taille = menu_temp.resize(taillebt , Image.Resampling.LANCZOS)
exit_nvl_taille = exit_temp.resize(taillebt, Image.Resampling.LANCZOS)
play_nvl_taille = play_temp.resize(taillebt)
croix_nvl_taille = croix_temp.resize(taille_icones)

debutant_nvl_taille = debutant.resize(taillebt3)
intermediaire_nvl_taille = intermediaire.resize(taillebt3, Image.Resampling.LANCZOS)
avance_nvl_taille = avance.resize(taillebt3)

#création de copies des images de taille différente
exit_nvl_taille.save("exit_nvl_taille.png")
play_nvl_taille.save("playn_nvltaille.png")
menu_nvl_taille.save("menu_nvl_taille.png")
croix_nvl_taille.save("croix_nvl_taille.png")

debutant_nvl_taille.save("debutant_nvl_taille.png")
intermediaire_nvl_taille.save("intermediaire_nvl_taille.png")
avance_nvl_taille.save("avance_nvl_taille.png")

# conversion des images pour permettre l'affichage
exit = ImageTk.PhotoImage(exit_nvl_taille)
play = ImageTk.PhotoImage(play_nvl_taille)
menu = ImageTk.PhotoImage(menu_nvl_taille)
croix = ImageTk.PhotoImage(croix_nvl_taille)

debutant = ImageTk.PhotoImage(debutant_nvl_taille)
intermediaire = ImageTk.PhotoImage(intermediaire_nvl_taille)
avance = ImageTk.PhotoImage(avance_nvl_taille)


Label_acceuil = Label(fenetre, image=acceuil)
Label_acceuil.place(relwidth=1, relheight=1)



#Bas de page
bouton_quitter = Button(fenetre, image=exit, borderwidth=0, highlightthickness=0,bg="#322432", command=quitter)
bouton_quitter.place(x=800, y = 762)


bouton_menu = Button (fenetre, image=menu,borderwidth=0,highlightthickness=0, bg="#322432", command=fctmenu)
bouton_menu.place(x=550, y = 762)

#Hauts de page


bouton_intermediaire = Button(fenetre,image=intermediaire,borderwidth=0, highlightthickness=0,bg="#322432", command= lancement1)
bouton_intermediaire.place(x=650, y=570)

bouton_avance = Button(fenetre,image=avance,borderwidth=0, highlightthickness=0,bg="#322432", command=lancement2)
bouton_avance.place(x=850, y=570)

bouton_debutant = Button(fenetre,image=debutant,borderwidth=0, highlightthickness=0,bg="#322432", command= lancement3)
bouton_debutant.place(x=450, y=570)




fenetre.mainloop()



