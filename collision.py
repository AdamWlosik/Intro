import pygame

# ustawienia screena gry oraz pętli obsługującej grę

pygame.init()
w_width = 500
w_height = 500
screen = pygame.display.set_mode((w_width, w_height))  # rozmiary okna 300x300
screen.fill("white")  # kolor
pygame.display.set_caption("My first pygame")  # tytuł

clock = pygame.time.Clock()  # zmienna do regulowania fps

background_image = pygame.image.load("images/bg.jpeg")  # przypisanie tła z pliku do zmiennej
background_image = pygame.transform.scale(background_image,
                                          (w_width, w_height))  # skalowanie zmiennej do rozmiarów okna
walk_right = [pygame.image.load(f'soldier/{i}.png') for i in range(1, 10)]  # ładowanie po kolei wszystkich img z pliku
walk_left = [pygame.image.load(f'soldier/L{i}.png') for i in range(1, 10)]
char = pygame.image.load('soldier/standing.png')
enemy_walk_left = [pygame.image.load(f'enemy/L{i}.png') for i in range(1, 10)]
enemy_walk_right = [pygame.image.load(f'enemy/R{i}.png') for i in range(1, 10)]


class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.is_jump = False  # zmienna do skakania
        self.jump_count = 5
        self.left = False
        self.right = False
        self.walk_count = 0  #  zmienna która podstawiamy pod nume obrazka
        self.standing = True # czy postać stoi
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, screen):
        if self.walk_count + 1 >= 27: # wczytujemy obrazki 3 razy więć 9(liczba obrazków) * 3
            self.walk_count = 0

        if not self.standing: # sprawdzenie czy postac stoi
            if self.left:
                screen.blit(walk_left[self.walk_count // 3], (self.x, self.y)) # wczytanie obrazków do ruchu postaci 3 razy żeby ruch wyglądał naturalniej
                self.walk_count += 1

            elif self.right:
                screen.blit(walk_right[self.walk_count // 3], (self.x, self.y))
                self.walk_count += 1

        else: # jeśli stoi
            if self.right:  # patrzy w prawo
                screen.blit(walk_right[0], (self.x, self.y))  # wczytujemy obrazek 0 - postać stoi
            else:  # patrz w lewo
                screen.blit(walk_left[0], (self.x, self.y))


class Projectile:

    def __init__(self, x, y, radius, color, direction):
        self.direction = direction
        self.y = y
        self.color = color
        self.radius = radius
        self.x = x
        self.vel = 8 * direction

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius) # rysowanie koła (pocisku)


class Enemy:
    def __init__(self, x, y, width, height, end):
        self.end = end
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.walk_count = 0  # zmienna która podstawiamy pod numer obrazka
        self.vel = 3
        self.path = [x, end]

    def draw(self, screen):
        self.move()
        if self.walk_count + 1 >= 27:
            self.walk_count = 0

        if self.vel > 0:  # sprawdzamy czy prędkość dodatnia ujemna i ładujemy odpowiednie grafiki
            screen.blit(enemy_walk_right[self.walk_count // 3], (self.x, self.y))
            self.walk_count += 1
        else:
            screen.blit(enemy_walk_left[self.walk_count // 3], (self.x, self.y))
            self.walk_count += 1

    def move(self):
        if self.vel > 0: #  sprawdzamy kierunek ruchu przez znak przy predości
            if self.x < self.path[1] - self.width: #  sprawdzamy czy pozycja przeciwnika - jego szerokość > od szerokości okna gry
                self.x += self.vel
            else: # jeśli wychodzimy poza ekran zmieniamy znak przy prędkości i restartujemy wczytywanie obrazków enemy
                self.vel = self.vel * - 1
                self.x += self.vel
                self.walk_count = 0
        else: # to samo co wyżej tylko dal ujemniej predkości czyli przeciwnego kierunku ruchu 
            if self.x > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * - 1
                self.x += self.vel
                self.walk_count = 0


def drawInGameLoop():
    screen.blit(background_image, (0, 0))  # ustawienie zmiennej jako tła i jej koordynaty
    clock.tick(25)  # ustawienie 25 fps do wcześniej stworzonej zmiennej
    soldier.draw(screen)
    enemy.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)  # rysowanie pocisków
    pygame.display.flip()  # renderowanie gry na ekran


soldier = Player(50, 435, 64, 64)
enemy = Enemy(30, w_height - 64, 64, 64, w_width)
shoot = 0
bullets = []

done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # event naciśnięcie przycisku, równe funkcji wbudowanej kończącej gre
            done = False

        if shoot > 0:
            shoot += 1
        if shoot > 10:
            shoot = 0  # dodanie opóźnienia w strzelaniu żeby pociski sie nie łączyły

    for bullet in bullets:
        if 500 > bullet.x > 0:  # sprawdzeie czy pociks w granicach okna
            bullet.x += bullet.vel  #  przesuwanie pocisku po osi x z prędkościa vel
        else:
            bullets.pop(bullets.index(bullet))  # usuwanie z listy pocików jak wyjdzie poza ekran

    keys = pygame.key.get_pressed()  # przechwycenie naciśnięcia klawiatury

    if keys[pygame.K_SPACE] and shoot == 0:
        if soldier.right:  # jeśli soldier patrzy w prawo kierunek pocisku dodatni
            direction = 1
        else:
            direction = -1

        if len(bullets) < 5: #  limit pocisków wystrzelonych na raz
            bullets.append(Projectile((soldier.x + (soldier.width + 70) // 2), (soldier.y + (soldier.height + 30) // 2),
                                      6, "red", direction))  # dodanie wystrzelonego pocisku do listy i jego koordynatów itd
        shoot = 1

    if keys[pygame.K_LEFT] and soldier.x > 0:
        soldier.x -= soldier.vel
        soldier.left = True
        soldier.right = False
        soldier.standing = False

    elif keys[pygame.K_RIGHT] and soldier.x < w_width - soldier.width:
        soldier.x += soldier.vel
        soldier.left = False
        soldier.right = True
        soldier.standing = False

    else:  # nie wciskamy przycisku ruchu postać stoi
        soldier.standing = True
        soldier.walk_count = 0

    if not soldier.is_jump:  # if zapobiegajcy drugiemy skokowi gdy obiekt w czase skoku
        if keys[pygame.K_UP]:  # sprawdza naciśnięcie spacji i zmienia zmiennna skakanie
            soldier.is_jump = True
            soldier.right = False
            soldier.left = False
    else:
        if soldier.is_jump:
            if soldier.jump_count >= -5:  # warunek, że skok kończy się po przejściu 10 klatek w dół, powrocie do pozycji start
                neg = 1  # zmienna do określenia kierunku skoku
                if soldier.jump_count < 0:  # spradzenie czy obiekt przeleciał 10 klatek i zmiana kierunku
                    neg = -1
                soldier.y -= (soldier.jump_count ** 2) * neg * 0.5  # formuła skacząca zmienia położenie obiektu na y
                soldier.jump_count -= 1  # ruch o 1 klatkę
            else:
                soldier.jump_count = 5
                soldier.is_jump = False
    drawInGameLoop()
