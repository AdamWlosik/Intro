import pygame

# ustawienia screena gry oraz pętli obsługującej grę

pygame.init()
screen = pygame.display.set_mode((300, 300))  # rozmiary okna 300x300
screen.fill("white")  # kolor
pygame.display.set_caption("My first pygame")  # tytuł

done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # event naciśnięcie przycisku, równe funkcji wbudowanej kończącej gre
            done = False

    pygame.display.flip()  # renderowanie gry na ekran
