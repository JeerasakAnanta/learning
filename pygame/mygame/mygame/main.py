import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions and setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Neon Racer")
clock = pygame.time.Clock()

# Colors and fonts
BG_COLOR = (20, 20, 30)
PLAYER_COLOR = (0, 255, 255)  # Neon cyan for the player
OBSTACLE_COLOR = (255, 50, 50)
PICKUP_COLOR = (50, 255, 50)
ROAD_COLOR = (50, 50, 50)
FONT = pygame.font.Font(None, 36)

# Game Variables
player_pos = [WIDTH // 2, HEIGHT - 120]
player_speed = 7
obstacles = []
pickups = []
frame_count = 0
score = 0

# Road variables
road_y = 0
road_speed = 5
obstacle_spawn_rate = 30  # frames

def draw_road():
    global road_y
    road_y += road_speed
    if road_y >= HEIGHT:
        road_y = 0
    pygame.draw.rect(screen, ROAD_COLOR, (200, road_y, 400, HEIGHT))
    pygame.draw.rect(screen, ROAD_COLOR, (200, road_y - HEIGHT, 400, HEIGHT))

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def move_player():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 200:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < 540:
        player_pos[0] += player_speed

def spawn_objects():
    global frame_count
    frame_count += 1
    if frame_count % obstacle_spawn_rate == 0:
        x = random.randint(220, 580)
        obstacles.append([x, -50, random.randint(4, 7)])
    if random.randint(1, 200) == 1:
        x = random.randint(220, 580)
        pickups.append([x, -30])

def update_obstacles():
    for obstacle in obstacles[:]:
        obstacle[1] += obstacle[2]
        obs_rect = pygame.Rect(obstacle[0], obstacle[1], 40, 40)
        pygame.draw.rect(screen, OBSTACLE_COLOR, obs_rect)
        if obstacle[1] > HEIGHT:
            obstacles.remove(obstacle)

def update_pickups():
    for pickup in pickups[:]:
        pickup[1] += 3
        pick_rect = pygame.Rect(pickup[0] - 15, pickup[1] - 15, 30, 30)
        pygame.draw.ellipse(screen, PICKUP_COLOR, pick_rect)
        if pickup[1] > HEIGHT:
            pickups.remove(pickup)

def draw_player():
    player_rect = pygame.Rect(player_pos[0], player_pos[1], 60, 30)
    pygame.draw.rect(screen, PLAYER_COLOR, player_rect)
    return player_rect

def check_collisions(player_rect):
    global score
    for obstacle in obstacles:
        obs_rect = pygame.Rect(obstacle[0], obstacle[1], 40, 40)
        if player_rect.colliderect(obs_rect):
            print("Game Over!")
            return False
    for pickup in pickups[:]:
        pick_rect = pygame.Rect(pickup[0] - 15, pickup[1] - 15, 30, 30)
        if player_rect.colliderect(pick_rect):
            score += 100
            pickups.remove(pickup)
    return True

def update_score():
    global score
    score += 1
    score_text = FONT.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

def main():
    global running
    running = True
    while running:
        screen.fill(BG_COLOR)
        draw_road()
        running = handle_events()
        move_player()
        spawn_objects()
        update_obstacles()
        update_pickups()
        player_rect = draw_player()
        running = running and check_collisions(player_rect)
        update_score()
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    sys.exit()

# if __name__ == "__main__":
#     main()
