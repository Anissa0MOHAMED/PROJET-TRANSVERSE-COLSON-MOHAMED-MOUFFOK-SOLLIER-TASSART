import pygame
import   math
import random

import pygame.transform

# Initialisation de Pygame
pygame.init()

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
tir_vitesse = 10
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
        if all(distance(new_planet, p) > (p["masse"] / 10 + new_planet["masse"] / 10) for p in planetes):
            planetes.append(new_planet)
            break  # Sort de la boucle while quand une planète valide est trouvée

# Liste des projectiles
projectiles = []

#coordonnées d'apparition du point bleu
x=200
y=200

object_image = pygame.image.load('vaisseau.png')
object_image = pygame.transform.scale(object_image, (50, 50))

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

preview_enabled = True
# Boucle principale
clock = pygame.time.Clock()
running = True
vy=1
last_move_time = pygame.time.get_ticks()
angle = 0
speed = 5
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
            if distance({"x": temp_x, "y": temp_y}, planete) < planete["masse"] / 10:
                return points  # Arrête la simulation si la trajectoire touche une planète
        if temp_x < 0 or temp_x > WIDTH or temp_y < 0 or temp_y > HEIGHT:
            break
        points.append((int(temp_x), int(temp_y)))
    return points

while running:
    keys = pygame.key.get_pressed()
    moved = False

    if 70<y<1013 and 650>x>199:
        if keys[pygame.K_UP]:
            x += speed * math.cos(math.radians(angle))
            y -= speed * math.sin(math.radians(angle))
            moved = True
        if keys[pygame.K_DOWN]:
            x -= speed * math.cos(math.radians(angle))
            y += speed * math.sin(math.radians(angle))
            moved = True
    else:
        if y<=70:
            while(y<=70):
                y+=1
                moved = True
        if y>=1013:
            while(y>=1013):
                y-=1
                moved = True
        if x<=199:
            while(x<=199):
                x+=1
                moved = True
        if x>=650:
            while(x>=650):
                x-=1
                moved = True
    if keys[pygame.K_RIGHT]:
        angle -= 1
        moved = True
    if keys[pygame.K_LEFT]:
        angle += 1
        moved = True
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
            if event.key == pygame.K_SPACE:
                vX = vx * math.sin(math.radians(angle) - 80)
                vy = tir_vitesse * math.cos(math.radians(angle) - 80)
                projectiles.append({"x": x+25, "y": y+25, "vx": vX, "vy": vy})
            if event.key == pygame.K_a:
                running = False
                pygame.quit()
            if event.key == pygame.K_q:
                angle+=1
            if event.key == pygame.K_d:
                angle-=1
            if event.key == pygame.K_e:
                preview_enabled = not preview_enabled
            if event.key == pygame.K_s and vx > 5:
                vx -= 1
            if event.key == pygame.K_z and vx <15:
                vx += 1
            if event.key == pygame.K_z and vx < 15:
                vx += 1

    # Effacer l'écran
    screen.fill(DARK_BLUE)  # Fond bleu foncé (galaxie)

    # Dessin des étoiles
    for star in stars:
        pygame.draw.circle(screen, YELLOW, star, 1)  # Petits points jaunes


    # Dessiner les planètes
    for planete in planetes:
        pygame.draw.circle(screen, planete["color"], (planete["x"], planete["y"]), planete["masse"]/10)

    # Dessiner la position initiale du projectile en bleu
    rotated_image = pygame.transform.rotate(object_image, angle)
    new_rect = rotated_image.get_rect(center=object_image.get_rect(topleft=(x, y)).center)
    screen.blit(rotated_image, new_rect.topleft)


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
        pygame.draw.circle(screen, GREEN, ((proj["x"]), (proj["y"])), 5)

    #affiche puissance du tir
    txt = big_font.render(f'Vitesse: {round(vx, 2)} | Angle: {round(angle,1)%360}°', True, WHITE)
    screen.blit(txt, (200, 75))

    if show_preview and preview_enabled:
        trajectory = simulate_trajectory(x, y, angle, vx)
        for point in trajectory:
            pygame.draw.circle(screen, WHITE, point, 2)

    # Mettre à jour l'affichage
    pygame.display.flip()
    clock.tick(60)
