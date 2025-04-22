import pygame
import random

# Kitchen


# Bathroom


# Office1
office1 = pygame.image.load("office.png")

# Office2


# Cafe


# void -- Rare



class Floor:
    def __init__(self, display, type):
        self.type = type 
        self.display = display
        self.collisions = []

        match (self.type.lower()):
            case "kitchen":
                pass

            case "bathroom":
                pass
            
            case "office1":
                self.image = office1
                self.collisions.append(pygame.Rect(708, 232, 135, 83))
                self.collisions.append(pygame.Rect(916, 228, 135, 83))
                self.collisions.append(pygame.Rect(1124, 232, 135, 83))
                self.collisions.append(pygame.Rect(1328, 228, 235, 83))
                self.collisions.append(pygame.Rect(708, 376, 135, 83))
                self.collisions.append(pygame.Rect(920, 376, 135, 83))
                self.collisions.append(pygame.Rect(1132, 376, 135, 83))
                self.collisions.append(pygame.Rect(1336, 368, 135, 83))

            case "office2":
                pass

            case "cafe":
                pass

            case "void":
                pass

    def draw(self):
        self.display.blit(self.image, (0, 0))

        
