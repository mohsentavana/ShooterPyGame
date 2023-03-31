  # t.me/MohsenLinux
  # https://github.com/mohsentavana
  # Enjoy for Free 
  
  # first import player.png & enemy.png & explosion.png & background.png 

import pygame
import random
import socket
import threading

# Initialize pygame
pygame.init()

# Set up the display
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Multiplayer Shooter Game")

# Set up the player
player_width = 50
player_height = 50
player_x = width // 2 - player_width // 2
player_y = height - player_height - 20
player_speed = 5
player_image = pygame.image.load("player.png").convert_alpha()

# Set up the enemy
enemy_width = 50
enemy_height = 50
enemy_x = random.randint(0, width - enemy_width)
enemy_y = -enemy_height
enemy_speed = 3
enemy_image = pygame.image.load("enemy.png").convert_alpha()

# Set up the bullet
bullet_width = 5
bullet_height = 10
bullet_x = player_x + player_width // 2 - bullet_width // 2
bullet_y = player_y - bullet_height
bullet_speed = 10
bullet_state = "ready"
bullet_image = pygame.Surface((bullet_width, bullet_height))
bullet_image.fill((255, 255, 255))

# Set up the score
score = 0
font = pygame.font.Font(None, 36)

# Load background image
background_image = pygame.image.load("background.png").convert()

# Load explosion image
explosion_image = pygame.image.load("explosion.png").convert_alpha()

# Set up the network
server_ip = "localhost" # Replace with the IP address of your server
server_port = 5555
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))
player_id = client_socket.recv(1024).decode()

# Game loop
def game_loop():
    global player_x, player_y, enemy_x, enemy_y, score, bullet_state
    running = True
    while running:
        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_x -= player_speed
                    client_socket.send(("move_left," + player_id + "," + str(player_x)).encode())
                elif event.key == pygame.K_RIGHT:
                    player_x += player_speed
                    client_socket.send(("move_right," + player_id + "," + str(player_x)).encode())
                elif event.key == pygame.K_SPACE and bullet_state == "ready":
                    bullet_x = player_x + player_width // 2 - bullet_width // 2
                    bullet_y = player_y - bullet_height
                    bullet_state = "fire"
                    client_socket.send(("fire_bullet," + player_id + "," + str(bullet_x)).encode())

        # Receive data from server
        data = client_socket.recv(1024).decode()
        if data:
            data = data.split(",")
            if data[0] == "player":
                player_id = data[1]
                player_x = int(data[2])
                player_y = int(data[3])
            elif data[0] == "enemy":
                enemy_x = int(data[1])
                enemy_y = int(data[2])
           
