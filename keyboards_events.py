import pygame

# ustawienia screena gry oraz pętli obsługującej grę

pygame.init()
w_width = 500
w_height = 500
screen = pygame.display.set_mode((w_width, w_height))  # rozmiary okna 300x300
screen.fill("white")  # kolor
pygame.display.set_caption("My first pygame")  # tytuł

# creating object
x = 0
y = 0
width = 50
height = 50
vel = 5

clock = pygame.time.Clock()  # zmienna do regulowania fps
done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # event naciśnięcie przycisku, równe funkcji wbudowanej kończącej gre
            done = False
    keys = pygame.key.get_pressed()  # przechwycenie naciśnięcia klawiatury
    if keys[pygame.K_UP]:  # sprawdznie czy keys to konkretyny klawisz
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    screen.fill("white")
    pygame.draw.rect(screen, 'black', (x, y, width, height))
    clock.tick(60)  # ustawienie 60 fps do wcześniej stworzonej zmiennej
    pygame.display.flip()  # renderowanie gry na ekran
