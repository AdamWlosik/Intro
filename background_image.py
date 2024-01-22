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

is_jump = False  # zmienna do skakania
jump_count = 10

background_image = pygame.image.load("OOP/images/bg.jpeg")  # przypisanie tła z pliku do zmiennej
background_image = pygame.transform.scale(background_image, (w_width, w_height))  # skalowanie zmiennej do rozmiarów okna

done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # event naciśnięcie przycisku, równe funkcji wbudowanej kończącej gre
            done = False
    keys = pygame.key.get_pressed()  # przechwycenie naciśnięcia klawiatury
    if keys[pygame.K_LEFT] and x > 0:
        x -= vel
    if keys[pygame.K_RIGHT] and x < w_width - width:
        x += vel
    if not is_jump:  # if zapobiegajcy drugiemy skokowi gdy obiekt w czase skoku
        if keys[pygame.K_UP] and y > 0:  # sprawdznie czy keys to konkretyny klawisz y >0 pilnuje wyjeżdżania poza plansze
            y -= vel
        if keys[pygame.K_DOWN] and y < w_height - height:
            y += vel
        if keys[pygame.K_SPACE]:  # sprawdza naciśnięcie spacji i zmienia zmiennna skakanie
            is_jump = True
    else:
        if is_jump:
            if jump_count >= -10: # warunek, że skok kończy się po przejściu 10 klatek w dół, powrocie do pozycji start
                neg = 1  # zmienna do określenia kierunku skoku
                if jump_count < 0:  # spradzenie czy obiekt przeleciał 10 klatek i zmiana kierunku
                    neg = -1
                y -= (jump_count ** 2) * neg * 0.5  # formuła skacząca zmienia położenie obiektu na y
                jump_count -= 1  # ruch o 1 klatkę
            else:
                jump_count = 10
                is_jump = False
    screen.blit(background_image, (0, 0))  # ustawienie zmiennej jako tła i jej koordynaty
    pygame.draw.rect(screen, 'black', (x, y, width, height))
    clock.tick(60)  # ustawienie 60 fps do wcześniej stworzonej zmiennej
    pygame.display.flip()  # renderowanie gry na ekran
