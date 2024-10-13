import pygame

class Enemigo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ancho =  70
        self.alto = 70
        self.velocidad = 5
        self.color = "purple"
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        self.imagen = pygame.image.load("media/nave_enemiga.png")
        self.imagen = pygame.transform.scale(self.imagen, (self.ancho, self.alto))
        self.vida = 3


    def dibujar(self, ventana):
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        #pygame.draw.rect(ventana, self.color, self.rect)
        ventana.blit(self.imagen, (self.x, self.y))
    
    def movimiento(self):
        self.y += self.velocidad
        