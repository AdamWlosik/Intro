import pygame

# ustawienia screena gry oraz pętli obsługującej grę

pygame.init()
w_width = 500
w_height = 500
screen = pygame.display.set_mode((w_width, w_height))  # rozmiary okna 300x300
screen.fill("white")  # kolor
pygame.display.set_caption("My first pygame")  # tytuł

# creating object
x = 50
y = 380
width = 64
height = 64
vel = 5

clock = pygame.time.Clock()  # zmienna do regulowania fps

is_jump = False  # zmienna do skakania
jump_count = 5

background_image = pygame.image.load("OOP/images/bg.jpeg")  # przypisanie tła z pliku do zmiennej
background_image = pygame.transform.scale(background_image,
                                          (w_width, w_height))  # skalowanie zmiennej do rozmiarów okna

# charakter
left = False
right = False
walk_count = 0

walk_right = [pygame.image.load(f'soldier/{i}.png') for i in range(1, 10)]  # ładowanie po kolei wszystkich img z pliku
walk_left = [pygame.image.load(f'soldier/L{i}.png') for i in range(1, 10)]
char = pygame.image.load('soldier/standing.png')


def DrawInGameloop():
    screen.blit(background_image, (0, 0))  # ustawienie zmiennej jako tła i jej koordynaty
    clock.tick(25)  # ustawienie 60 fps do wcześniej stworzonej zmiennej

    global walk_count

    if walk_count + 1 >= 27: # podniesione z 9 do 27 ilosc obrazków bo niżej wyświetlamy 3 razy każdy
        walk_count = 0

    if left:
        screen.blit(walk_left[walk_count//3], (x, y)) #  //3 sprawia, że każdy z zołnierzy wyświetla sie 3 razy bardziej naturalny ruch
        walk_count += 1

    elif right:
        screen.blit(walk_right[walk_count//3], (x, y))
        walk_count += 1

    else:
        screen.blit(char, (x, y))

    pygame.display.flip()  # renderowanie gry na ekran


done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # event naciśnięcie przycisku, równe funkcji wbudowanej kończącej gre
            done = False

    keys = pygame.key.get_pressed()  # przechwycenie naciśnięcia klawiatury

    if keys[pygame.K_LEFT] and x > 0:
        x -= vel
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and x < w_width - width:
        x += vel
        left = False
        right = True

    else:
        left = False
        right = False
        walk_count = 0

    if not is_jump:  # if zapobiegajcy drugiemy skokowi gdy obiekt w czase skoku
        if keys[pygame.K_SPACE]:  # sprawdza naciśnięcie spacji i zmienia zmiennna skakanie
            is_jump = True
            right = False
            left = False
    else:
        if is_jump:
            if jump_count >= -5:  # warunek, że skok kończy się po przejściu 10 klatek w dół, powrocie do pozycji start
                neg = 1  # zmienna do określenia kierunku skoku
                if jump_count < 0:  # spradzenie czy obiekt przeleciał 10 klatek i zmiana kierunku
                    neg = -1
                y -= (jump_count ** 2) * neg * 0.5  # formuła skacząca zmienia położenie obiektu na y
                jump_count -= 1  # ruch o 1 klatkę
            else:
                jump_count = 5
                is_jump = False
    DrawInGameloop()
