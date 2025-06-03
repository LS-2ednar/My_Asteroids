from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
    
    def draw(self,screen):
        pygame.draw.circle(screen,"white", self.position ,self.radius,width=2)

    def update(self,dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius < ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20.0,50.0)
        vec1 = self.velocity.rotate(random_angle)
        vec2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        child_1_asteroid = Asteroid(self.position.x,self.position.y,new_radius)
        child_2_asteroid = Asteroid(self.position.x,self.position.y,new_radius)
        child_1_asteroid.velocity = vec1*1.2
        child_2_asteroid.velocity = vec2*1.2

        