#Imports
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
BLOCK_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // BLOCK_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // BLOCK_SIZE
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake class
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.direction = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
        self.color = GREEN
        self.score = 0
        self.level = 1
        self.speed = 7

    def get_head_position(self):
        return self.positions[0]

    def turn(self, direction):
        if self.length > 1 and (direction[0] * -1, direction[1] * -1) == self.direction:
            return
        self.direction = direction

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * BLOCK_SIZE)) % SCREEN_WIDTH), (cur[1] + (y * BLOCK_SIZE)) % SCREEN_HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            return True
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.direction = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
        self.score = 0
        self.level = 1
        self.speed = 7

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, WHITE, r, 1)

# Food class
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()
        self.timer = 1000  # Timer in milliseconds
        self.time_remaining = self.timer

    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH - 1) * BLOCK_SIZE, random.randint(0, GRID_HEIGHT - 1) * BLOCK_SIZE)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(surface, self.color, r)

    def update(self, dt):
        self.time_remaining -= dt
        if self.time_remaining <= 0:
            self.randomize_position()
            self.time_remaining = self.timer

# Main function
def main():
    snake = Snake()
    food = Food()

    clock = pygame.time.Clock()
    game_over = False

    while not game_over:
        dt = clock.tick(60)  # Get delta time in milliseconds
        screen.fill((0, 0, 0))

        # Draw snake and food
        if snake.move():
            game_over = True
        snake.draw(screen)
        food.draw(screen)

        # Update and draw food timer
        food.update(dt)
        font = pygame.font.Font(None, 24)
        timer_text = font.render(f"Time until new food: {food.time_remaining / 1000:.1f}s", True, WHITE)
        screen.blit(timer_text, (10, 10))

        # Check for collisions
        if snake.get_head_position() == food.position:
            snake.length += 1
            snake.score += 1
            food.randomize_position()

        # Check for border collision
        if (snake.get_head_position()[0] < 0 or snake.get_head_position()[0] >= SCREEN_WIDTH or
                snake.get_head_position()[1] < 0 or snake.get_head_position()[1] >= SCREEN_HEIGHT):
            game_over = True

        # Display score and level
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {snake.score}", True, WHITE)
        level_text = font.render(f"Level: {snake.level}", True, WHITE)
        screen.blit(score_text, (10, 50))
        screen.blit(level_text, (10, 90))

        pygame.display.update()

        # Increase speed and level
        if snake.score >= 3 * snake.level:
            snake.speed += 1
            snake.level += 1

        # Cap the frame rate
        clock.tick(snake.speed)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                elif event.key == pygame.K_UP:
                    snake.turn((0, -1))
                elif event.key == pygame.K_DOWN:
                    snake.turn((0, 1))
                elif event.key == pygame.K_LEFT:
                    snake.turn((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    snake.turn((1, 0))

    # Game over message
    font = pygame.font.Font(None, 72)
    game_over_text = font.render("Game Over", True, WHITE)
    game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
    screen.blit(game_over_text, game_over_rect)
    pygame.display.flip()

    # Wait for a few seconds before restarting
    pygame.time.wait(2000)

    # Restart the game
    main()

# Run the game
if __name__ == "__main__":
    main()
