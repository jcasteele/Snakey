import pygame
import sys
import random
from pygame.math import Vector2

class Dot:
    def __init__(self):
        self.rad = 10
        self.eaten = True
    
    def location(self):
        self.x = random.randint(0, board_x)
        self.y = random.randint(0, board_y)   
        self.locate = Vector2((self.x * cell), (self.y * cell))     
    
    def draw_dot(self):
        if self.eaten == True:
            self.location()
            pygame.draw.circle(screen, "green", self.locate, self.rad)
            
            self.eaten = False
            
        elif self.locate.x <= (0 + cell) or self.locate.x >= (800 - cell):
            self.location()
            pygame.draw.circle(screen, "green", self.locate, self.rad)
            
        elif self.locate.y <= (0 + cell) or self.locate.y >= (800 - cell):
            self.location()
            pygame.draw.circle(screen, "green", self.locate, self.rad)
            
        else:
            pygame.draw.circle(screen, "green", self.locate, self.rad)

class Snake:
    def __init__(self):
        self.body = [Vector2(board_x, board_y), Vector2((board_x * cell), (board_y * cell)), Vector2((board_x * (2 * cell)), (board_y * (2 * cell)))]
        self.rad = 10
        self.direction = Vector2(cell, 0)
        self.growing = False
        self.dead = False
    
    def draw_snake(self):
        if self.dead == False:
            for segment in self.body:
                pygame.draw.circle(screen, "red", segment, self.rad)
        
        if self.dead == True:
            for segment in self.body:
                pygame.draw.circle(screen, "black", segment, self.rad)
    
    def move_snake(self):
        if self.dead == True:
            None
        else:
            if self.growing == True:
                snake_copy = self.body[:]
                snake_copy.insert(0, snake_copy[0] + self.direction)   
                self.body = snake_copy[:]
                
                self.growing = False
            else:        
                snake_copy = self.body[:-1]
                snake_copy.insert(0, snake_copy[0] + self.direction)   
                self.body = snake_copy[:]
    
    def grow(self):
        self.growing = True
    
    def death(self):
        for segment in self.body[1:]:
            if self.body[0] == segment:            
                self.dead = True
        
        if self.body[0].x <= 0 or self.body[0].x >= 800:
            self.dead = True
        
        if self.body[0].y <= 0 or self.body[0].y >= 800:
            self.dead = True
        
class Main:
    def __init__(self):
        self.snake = Snake()
        self.dot = Dot()
        
    def update(self):
        self.snake.move_snake()
        self.eat()
        self.snake.death()
    
    def draw_game(self):
        self.dot.draw_dot()
        self.snake.draw_snake()
    
    def eat(self):
        if self.dot.locate == self.snake.body[0]:
            self.snake.grow()
            
            self.dot.eaten = True
            self.dot.draw_dot()
            
            for segment in self.snake.body[:]:
                if segment == self.dot.locate:
                    self.dot.eaten = True
                    self.dot.draw_dot()

pygame.init()

board_x = 40
board_y = 40
cell = 20

pygame.display.set_caption("Snakey")

screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()

update = pygame.USEREVENT
pygame.time.set_timer(update, 150)

game = Main()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == update:
            game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.snake.direction = Vector2(0, -cell)
            if event.key == pygame.K_DOWN:
                game.snake.direction = Vector2(0, cell)
            if event.key == pygame.K_LEFT:
                game.snake.direction = Vector2(-cell, 0)
            if event.key == pygame.K_RIGHT:
                game.snake.direction = Vector2(cell, 0)
                
    screen.fill("white")
    game.draw_game()

    pygame.display.update()
    clock.tick(60)