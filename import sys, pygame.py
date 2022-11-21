import sys, pygame
pygame.init()

WHTE = (225,225,255)
janela=pygame.display.set_mode((800,400))

objeto1=pygame.Rect(400,200,100,100)
pygame.draw.rect(janela, WHITE, objeto1)

run=True
while run:
    pygame.display.uptade()