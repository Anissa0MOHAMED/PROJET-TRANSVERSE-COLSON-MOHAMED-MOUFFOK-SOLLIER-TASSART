from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import pygame
import math
import random
from tkinter import ttk
import wx
import pygame.transform

def jeu ():
    import pygame
    import math
    import random
    import pygame.transform

    # Initialisation de Pygame
    pygame.init()

    # Configuration de la fenêtre
    WIDTH, HEIGHT = 1920, 1080
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Moteur physique")

    # texte
    big_font = pygame.font.SysFont('Arial', 40)
    small_font = pygame.font.SysFont('Arial', 20)

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
    # Constantes physiques
    G = 10
    tir_vitesse = 10
    # vitesse initiale des balles
    vx = 10
    vy = 0
    vab = 10
    vcd = 0
    # score initiale
    score1 = 5
    score2 = 5

    # Coordonnées de référence pour la génération des planètes via touche t
    ref_x1, ref_y1 = 300, 300
    ref_x2, ref_y2 = 1600, 300

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

    # couleur des planetes
    colors = [
        (255, 0, 0),  # Rouge
        (0, 255, 0),  # Vert
        (0, 0, 255),  # Bleu
        (255, 255, 0),  # Jaune
        (0, 255, 255),  # Cyan
        (255, 0, 255),  # Magenta
        (128, 0, 0),  # Marron
        (128, 128, 0),  # Olive
        (0, 128, 0),  # Vert foncé
        (128, 0, 128),  # Violet
        (0, 128, 128),  # Bleu-vert
        (0, 0, 128),  # Bleu marine
        (255, 165, 0),  # Orange
        (255, 192, 203),  # Rose
        (75, 0, 130),  # Indigo
        (139, 69, 19),  # Brun
        (255, 215, 0),  # Or
        (192, 192, 192),  # Argent
        (169, 169, 169),  # Gris foncé
        (0, 255, 127)  # Vert printemps
    ]
    # Distance minimale entre une planète et les vaisseaux
    DISTANCE_MINIMALE_VAISSEAUX = 200

    # Génération des planètes
    pla = random.randint(6, 10)  # Nombre de planètes
    for i in range(pla):
        while True:
            x = random.randint(0, WIDTH)
            y = random.randint(0, HEIGHT)
            pv = random.randint(3, 5)
            masse = random.randint(250, 1500)
            color = random.choice(colors)
            image = random.choice(planet_images)
            resized_image = resize_planet_image(image, masse)
            new_planet = {"x": x, "y": y, "masse": masse, "color": color, 'pv': pv, 'image': resized_image}

            # Vérifier la distance avec toutes les planètes existantes et les vaisseaux
            if all(distance(new_planet, p) > ((p["masse"] / 10 + new_planet["masse"] / 10) + 30) for p in planetes) and \
                    math.sqrt((x - 200) ** 2 + (y - 200) ** 2) > DISTANCE_MINIMALE_VAISSEAUX and \
                    math.sqrt((x - 1660) ** 2 + (y - 200) ** 2) > DISTANCE_MINIMALE_VAISSEAUX:
                planetes.append(new_planet)
                break  # Sort de la boucle une fois une planète valide trouvée

    # Liste des projectiles
    projectiles = []
    explosions = []
    # coordonnées d'apparition du point bleu
    x = 200
    y = 200

    ab = 1660
    cd = 200
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
            elif joueur_actuel == 1:
                if carburant1 > 0:
                    if keys[pygame.K_UP]:
                        if keys[pygame.K_r]:
                            ab += speed * math.cos(math.radians(angle2)) * 2
                            cd -= speed * math.sin(math.radians(angle2)) * 2
                            carburant1 -= 0.5
                        else:
                            ab += speed * math.cos(math.radians(angle2))
                            cd -= speed * math.sin(math.radians(angle2))
                            carburant1 -= 0.1
                if keys[pygame.K_DOWN]:
                    ab -= speed * math.cos(math.radians(angle2))
                    cd += speed * math.sin(math.radians(angle2))
                    carburant1 -= 0.1
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
                    pla = random.randint(6, 10)  # Nombre de nouvelles planètes
                    for i in range(pla):
                        while True:
                            gen_x = random.randint(0, WIDTH)
                            gen_y = random.randint(0, HEIGHT)
                            pv = random.randint(3, 5)
                            masse = random.randint(250, 1500)
                            color = random.choice(colors)
                            image = random.choice(planet_images)
                            resized_image = resize_planet_image(image, masse)
                            new_planet = {"x": gen_x, "y": gen_y, "masse": masse, "color": color, 'pv': pv,
                                          'image': resized_image}

                            # Vérifier la distance avec toutes les planètes existantes et les points de référence
                            if all(distance(new_planet, p) > ((p["masse"] / 10 + new_planet["masse"] / 10) + 30) for p
                                   in
                                   planetes) and \
                                    math.sqrt(
                                        (gen_x - ref_x1) ** 2 + (gen_y - ref_y1) ** 2) > DISTANCE_MINIMALE_VAISSEAUX and \
                                    math.sqrt(
                                        (gen_x - ref_x2) ** 2 + (gen_y - ref_y2) ** 2) > DISTANCE_MINIMALE_VAISSEAUX:
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

        dessiner_jauge_carburant(screen, 200, 50, 200, 30, carburant0)
        dessiner_jauge_carburant(screen, 1500, 50, 200, 30, carburant1)

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
                    score1 -= 1
                    planetes.clear()  # Supprime toutes les anciennes planètes
                    pla = random.randint(6, 10)  # Nombre de nouvelles planètes
                    for i in range(pla):
                        while True:
                            gen_x = random.randint(0, WIDTH)
                            gen_y = random.randint(0, HEIGHT)
                            pv = random.randint(3, 5)
                            masse = random.randint(250, 1500)
                            color = random.choice(colors)
                            image = random.choice(planet_images)
                            resized_image = resize_planet_image(image, masse)
                            new_planet = {"x": gen_x, "y": gen_y, "masse": masse, "color": color, 'pv': pv,
                                          'image': resized_image}

                            # Vérifier la distance avec toutes les planètes existantes et les points de référence
                            if all(distance(new_planet, p) > ((p["masse"] / 10 + new_planet["masse"] / 10) + 30) for p
                                   in
                                   planetes) and \
                                    math.sqrt(
                                        (gen_x - ref_x1) ** 2 + (gen_y - ref_y1) ** 2) > DISTANCE_MINIMALE_VAISSEAUX and \
                                    math.sqrt(
                                        (gen_x - ref_x2) ** 2 + (gen_y - ref_y2) ** 2) > DISTANCE_MINIMALE_VAISSEAUX:
                                planetes.append(new_planet)
                                break  # Ajoute la nouvelle planète et quitte la boucle
                    if score1 == 0:
                        pygame.quit()
                    projectiles.remove(proj)
                elif proj["color"] == BLUE and collision_vaisseau(proj, ab, cd):
                    pygame.mixer.Sound.play(explosion_sound)  # Explosion du vaisseau rouge
                    explosions.append({"x": proj["x"], "y": proj["y"], "frame": 0})
                    score2 -= 1
                    planetes.clear()  # Supprime toutes les anciennes planètes
                    pla = random.randint(6, 10)  # Nombre de nouvelles planètes
                    for i in range(pla):
                        while True:
                            gen_x = random.randint(0, WIDTH)
                            gen_y = random.randint(0, HEIGHT)
                            pv = random.randint(3, 5)
                            masse = random.randint(250, 1500)
                            color = random.choice(colors)
                            image = random.choice(planet_images)
                            resized_image = resize_planet_image(image, masse)
                            new_planet = {"x": gen_x, "y": gen_y, "masse": masse, "color": color, 'pv': pv,
                                          'image': resized_image}

                            # Vérifier la distance avec toutes les planètes existantes et les points de référence
                            if all(distance(new_planet, p) > ((p["masse"] / 10 + new_planet["masse"] / 10) + 30) for p
                                   in
                                   planetes) and \
                                    math.sqrt(
                                        (gen_x - ref_x1) ** 2 + (gen_y - ref_y1) ** 2) > DISTANCE_MINIMALE_VAISSEAUX and \
                                    math.sqrt(
                                        (gen_x - ref_x2) ** 2 + (gen_y - ref_y2) ** 2) > DISTANCE_MINIMALE_VAISSEAUX:
                                planetes.append(new_planet)
                                break  # Ajoute la nouvelle planète et quitte la boucle
                    if score2 == 0:
                        pygame.quit()
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
            txt = big_font.render(f'Vitesse: {round(vx, 2)} | Angle: {round(angle, 1) % 360}°', True, WHITE)
            screen.blit(txt, (200, 75))
        elif joueur_actuel == 1:
            txt = big_font.render(f'Vitesse: {round(vx, 2)} | Angle: {round(angle2 - 180, 1) % 360}°', True, WHITE)
            screen.blit(txt, (1350, 75))
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

        txt2 = big_font.render(f'{score1} | {score2}', True, WHITE)
        screen.blit(txt2, (960, 75))
        # Mettre à jour l'affichage
        pygame.display.flip()
        clock.tick(60)

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


