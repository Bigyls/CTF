#Puzzle Bubble
#100 points : flag

import pygame
import random

# Initialisation de Pygame
pygame.init()

# Définition des constantes
screen_width = 640
screen_height = 480
bubble_radius = 20
num_bubbles = 20
bubble_speed = 5
bubble_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)]
ball_radius = 10
ball_speed = 10
launcher_height = 20
black = (0, 0, 0)
white = (255, 255, 255)

# Création de la classe pour les bulles
class Bubble:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), bubble_radius)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

# Création de la classe pour la balle
class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.circle(screen, white, (self.x, self.y), ball_radius)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

# Création de la classe pour le lanceur de balle
class Launcher:
    def __init__(self):
        self.x = screen_width // 2
        self.y = screen_height - launcher_height

    def draw(self):
        pygame.draw.rect(screen, white, (self.x - 50, self.y, 100, launcher_height))

    def move_left(self):
        self.x -= 10

    def move_right(self):
        self.x += 10

# Création de la fonction pour initialiser les bulles sur l'écran
def init_bubbles():
    global bubbles

    # Initialisation de la liste des bulles
    bubbles = []

    # Positionnement des bulles sur l'écran
    for i in range(num_bubbles):
        x = random.randint(bubble_radius, screen_width - bubble_radius)
        y = random.randint(bubble_radius, screen_height // 2)
        color = random.choice(bubble_colors)
        bubble = Bubble(x, y, color)
        bubbles.append(bubble)

# Fonction pour dessiner les bulles sur l'écran
def draw_bubbles():
    for bubble in bubbles:
        bubble.draw()

# Fonction pour déplacer les bulles sur l'écran
def move_bubbles():
    for bubble in bubbles:
        bubble.move(0, bubble_speed)

# Fonction pour vérifier si la balle a touché une bulle
def check_collision():
    global score

    for bubble in bubbles:
        distance = ((bubble.x - ball.x) ** 2 + (bubble.y - ball.y) ** 2) ** 0.5

        if distance <= bubble_radius + ball_radius:
            # Suppression de la bulle touchée de la liste des bulles
            bubbles.remove(bubble)
            # Incrémentation du score
            score += 10
            
# Fonction pour dessiner le score sur l'écran
def draw_score():
    font = pygame.font.SysFont(None, 25)
    score_text = font.render("Score: " + str(score), True, white)
    screen.blit(score_text, (10, 10))

# Initialisation de la fenêtre du jeu
screen = pygame.display.set_mode((screen_width, screen_height))

# Initialisation du score
score = 0

# Initialisation des objets du jeu
init_bubbles()
ball = Ball(screen_width // 2, screen_height - launcher_height - ball_radius)
launcher = Launcher()

# Boucle principale du jeu
running = True
while running:
    # NHM2I
    # Gestion des événements 
    # {bulles}
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                launcher.move_left()
            elif event.key == pygame.K_RIGHT:
                launcher.move_right()
            elif event.key == pygame.K_SPACE:
                ball.move(0, -ball_speed)

    # Effacement de l'écran
    screen.fill(black)

    # Dessin des objets du jeu
    draw_bubbles()
    ball.draw()
    launcher.draw()
    draw_score()

    # Déplacement des objets du jeu
    move_bubbles()

    # Vérification des collisions
    check_collision()

    # Mise à jour de l'écran
    pygame.display.flip()

# Fermeture de Pygame
pygame.quit()
