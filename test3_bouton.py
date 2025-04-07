from tkinter import *
import pygame
import   math
import random





class RButton:
    def __init__(self, root, text=None, bg=None, bd=None, **arg):
        self.img1 = tkinter.PhotoImage("bouton_rond", data="""
        R0lGODlhQABAAPcAAHx+fMTCxKSipOTi5JSSlNTS1LSytPTy9IyKjMzKzKyq
        rOzq7JyanNza3Ly6vPz6/ISChMTGxKSmpOTm5JSWlNTW1LS2tPT29IyOjMzO
        zKyurOzu7JyenNze3Ly+vPz+/OkAKOUA5IEAEnwAAACuQACUAAFBAAB+AFYd
        QAC0AABBAAB+AIjMAuEEABINAAAAAHMgAQAAAAAAAAAAAKjSxOIEJBIIpQAA
        sRgBMO4AAJAAAHwCAHAAAAUAAJEAAHwAAP+eEP8CZ/8Aif8AAG0BDAUAAJEA
        AHwAAIXYAOfxAIESAHwAAABAMQAbMBZGMAAAIEggJQMAIAAAAAAAfqgaXESI
        5BdBEgB+AGgALGEAABYAAAAAAACsNwAEAAAMLwAAAH61MQBIAABCM8B+AAAU
        AAAAAAAApQAAsf8Brv8AlP8AQf8Afv8AzP8A1P8AQf8AfgAArAAABAAADAAA
        AACQDADjAAASAAAAAACAAADVABZBAAB+ALjMwOIEhxINUAAAANIgAOYAAIEA
        AHwAAGjSAGEEABYIAAAAAEoBB+MAAIEAAHwCACABAJsAAFAAAAAAAGjJAGGL
        AAFBFgB+AGmIAAAQAABHAAB+APQoAOE/ABIAAAAAAADQAADjAAASAAAAAPiF
        APcrABKDAAB8ABgAGO4AAJAAqXwAAHAAAAUAAJEAAHwAAP8AAP8AAP8AAP8A
        AG0pIwW3AJGSAHx8AEocI/QAAICpAHwAAAA0SABk6xaDEgB8AAD//wD//wD/
        /wD//2gAAGEAABYAAAAAAAC0/AHj5AASEgAAAAA01gBkWACDTAB8AFf43PT3
        5IASEnwAAOAYd+PuMBKQTwB8AGgAEGG35RaSEgB8AOj/NOL/ZBL/gwD/fMkc
        q4sA5UGpEn4AAIg02xBk/0eD/358fx/4iADk5QASEgAAAALnHABkAACDqQB8
        AMyINARkZA2DgwB8fBABHL0AAEUAqQAAAIAxKOMAPxIwAAAAAIScAOPxABIS
        AAAAAIIAnQwA/0IAR3cAACwAAAAAQABAAAAI/wA/CBxIsKDBgwgTKlzIsKFD
        gxceNnxAsaLFixgzUrzAsWPFCw8kDgy5EeQDkBxPolypsmXKlx1hXnS48UEH
        CwooMCDAgIJOCjx99gz6k+jQnkWR9lRgYYDJkAk/DlAgIMICZlizat3KtatX
        rAsiCNDgtCJClQkoFMgqsu3ArBkoZDgA8uDJAwk4bGDmtm9BZgcYzK078m4D
        Cgf4+l0skNkGCg3oUhR4d4GCDIoZM2ZWQMECyZQvLMggIbPmzQIyfCZ5YcME
        AwFMn/bLLIKBCRtMHljQQcDV2ZqZTRDQYfWFAwMqUJANvC8zBhUWbDi5YUAB
        Bsybt2VGoUKH3AcmdP+Im127xOcJih+oXsEDdvOLuQfIMGBD9QwBlsOnzcBD
        hfrsuVfefgzJR599A+CnH4Hb9fcfgu29x6BIBgKYYH4DTojQc/5ZGGGGGhpU
        IYIKghgiQRw+GKCEJxZIwXwWlthiQyl6KOCMLsJIIoY4LlQjhDf2mNCI9/Eo
        5IYO2sjikX+9eGCRCzL5V5JALillY07GaOSVb1G5ookzEnlhlFx+8OOXZb6V
        5Y5kcnlmckGmKaaMaZrpJZxWXjnnlmW++WGdZq5ZXQEetKmnlxPgl6eUYhJq
        KKOI0imnoNbF2ScFHQJJwW99TsBAAAVYWEAAHEQAZoi1cQDqAAeEV0EACpT/
        JqcACgRQAW6uNWCbYKcyyEwGDBgQwa2tTlBBAhYIQMFejC5AgQAWJNDABK3y
        loEDEjCgV6/aOcYBAwp4kIF6rVkXgAEc8IQZVifCBRQHGqya23HGIpsTBgSU
        OsFX/PbrVVjpYsCABA4kQCxHu11ogAQUIOAwATpBLDFQFE9sccUYS0wAxD5h
        4DACFEggbAHk3jVBA/gtTIHHEADg8sswxyzzzDQDAAEECGAQsgHiTisZResN
        gLIHBijwLQEYePzx0kw37fTSSjuMr7ZMzfcgYZUZi58DGsTKwbdgayt22GSP
        bXbYY3MggQIaONDzAJ8R9kFlQheQQAAOWGCAARrwdt23Bn8H7vfggBMueOEG
        WOBBAAkU0EB9oBGUdXIFZJBABAEEsPjmmnfO+eeeh/55BBEk0Ph/E8Q9meQq
        bbDABAN00EADFRRQ++2254777rr3jrvjFTTQwQCpz7u6QRut5/oEzA/g/PPQ
        Ry/99NIz//oGrZpUUEAAOw==""")

        style = ttk.Style()
        style.element_create("RButton", "image", "bouton_rond", border=16, sticky="nsew")
        style.layout("RButton", [("RButton", {"sticky": "nsew"})])
        self.frame = tkinter.Frame(root)
        self.btn = ttk.Button(self.frame, text="Test", style="RButton", **arg)
        txt = tkinter.Text(self.frame, height=1, width=len(text) if text else 3,
                           borderwidth=0, takefocus=0, cursor='arrow')
        txt.grid(in_=self.btn, padx=30, pady=20)
        txt.insert(0.0, text if text else "   ")
        self.btn.grab_set()

    def grid(self, row=None, column=None, **arg):
        self.frame.grid(row=row, column=column, **arg)
        self.btn.grid()



import pygame
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


def jeu():
    import pygame
    import math
    import random

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
    GREEN = (0, 255, 0)
    YELLOW = (255, 255, 0)
    BLUE = (0, 0, 255)
    DARK_BLUE = (10, 10, 50)
    WHITE = (255, 255, 255)

    # Constantes physiques
    G = 10

    # vitesse initiale des balles
    vx = 10
    vy = 0

    # Liste des planètes (coordonnées et masses)
    planetes = []

    # permet de mesurer la distance entre 2 planetes
    def distance(p1, p2):
        return math.sqrt((p1["x"] - p2["x"]) ** 2 + (p1["y"] - p2["y"]) ** 2)

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
    pla = random.randint(2, 4)  # permet de définir l'intervale de planéte généré
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

    # coordonnées d'apparition du point bleu
    x = 200
    y = 200

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
        if keys[pygame.K_DOWN]:  # modifie les coordonées du point bleu
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

            # if event.type == pygame.KEYDOWN:
            # if event.key == pygame.K_SPACE:
            # Création d'un nouveau projectile
            # projectiles.append({"x": x, "y": y, "vx": vx, "vy": vy})

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
            pygame.draw.circle(screen, planete["color"], (planete["x"], planete["y"]), planete["masse"] / 10)

        # Dessiner la position initiale du projectile en bleu
        pygame.draw.circle(screen, BLUE, (x, y), 10)

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
                    collide += 1
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
            pygame.draw.circle(screen, GREEN, ((proj["x"]), (proj["y"])), 10)

        # affiche puissance du tir
        txt = big_font.render(('Vx: ' + str(round(vx, 2)) + 'Vy: ' + str(round(vy, 2))), True, WHITE)
        screen.blit(txt, (200, 75))

        # Mettre à jour l'affichage
        pygame.display.flip()
        clock.tick(60)
    """
    fenetre = Tk()
    fenetre.resizable(True, True)
    fenetre.size()


    fenetre.attributes('-fullscreen', True)

    logo = PhotoImage(file="astro_war.png")
    acceuil= PhotoImage(file="acceuil1.png")
    exit= PhotoImage(file="exit.png")



    Label_acceuil = Label(fenetre, image=acceuil)
    Label_acceuil.place(relwidth=1, relheight=1)



    bouton_quitter = Button(fenetre, width= 30, height=10, borderwidth=0, highlightthickness=0, command=fenetre.quit)
    bouton_quitter.place(x=100,y=100)

    bouton =Button(fenetre, command=fenetre.quit)
    bouton.pack()

    canvas = Canvas(fenetre, width= 200, height=100, highlightthickness=0)
    canvas.place(x=100,y=100)
    canvas.create_image(100, 50, image=exit, anchor=CENTER)


    fenetre.mainloop()

    """





fenetre = Tk()

def quitter():
    if messagebox.askokcancel("Quitter", "Voulez-vous vraiment quitter ?"):
        fenetre.quit()











fenetre.resizable(True, True)
fenetre.size()


fenetre.attributes('-fullscreen', True)

logo = PhotoImage(file="astro_war.png")

acceuil_temp = Image.open("fond_ecran.png")
taille_ecran =(1537,870)
acceuil_nvl_taille = acceuil_temp.resize(taille_ecran , Image.Resampling.LANCZOS)
acceuil =ImageTk.PhotoImage(acceuil_nvl_taille)
#exit= PhotoImage(file="exit.png")

play_temp = Image.open("play_final.png")
exit_temp = Image.open("exit_final.png")
taillebt = (125, 100)

exit_nvl_taille = exit_temp.resize(taillebt, Image.Resampling.LANCZOS)
play_nvl_taille = play_temp.resize(taillebt, Image.Resampling.LANCZOS)

exit =ImageTk.PhotoImage(exit_nvl_taille)
play=ImageTk.PhotoImage(play_nvl_taille)




Label_acceuil = Label(fenetre, image=acceuil)
Label_acceuil.place(relwidth=1, relheight=1)





#canvas = Canvas(fenetre, width= 200, height=100, highlightthickness=0)
#canvas.create_image(100, 50, image=exit, anchor=CENTER)

#bouton_quitter = Button(canvas, width= 30, height=10, borderwidth=0, highlightthickness=0, command=fenetre.quit)
#bouton_quitter.place(x=50000,y=100)

#canvas.place(x=500,y=100)

bouton_quitter = Button(fenetre, image=exit, borderwidth=0, highlightthickness=0,bg="#322432", command=quitter)

bouton_quitter.place(x=600, y=550)
bouton_jouer = RButton(fenetre,image=play,borderwidth=0, highlightthickness=0,bg="#322432", command=jeu)
bouton_jouer.place(x=800, y=550)

fenetre.mainloop()

