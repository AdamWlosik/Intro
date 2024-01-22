import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))  # rozmiary okna 300x300
screen.fill("white")  # kolor
pygame.display.set_caption("Drawing shapes on surface")  # tytuł

pygame.draw.line(screen, 'black', (0, 0), (300, 300), 5)
# rysowanie linii(miejsce rysowania, kolor, koordynaty początkowe, koordynaty końcowe, szerokość)
pygame.draw.lines(screen, 'orange', False, [(100, 100), (200, 100), (100, 200)], 4)
# rysowanie kilku linii(miejsce rysowania, kolor, boolen czy ostatni punkt ma być połączony z pierwszym
# żeby zamknąć kształt, krotki z koordynatami punktów, szerokość
pygame.draw.rect(screen, 'red', (50, 50, 100, 100), 7)  # rysowanie kwadratu (miejsce rysowania, kolor,
# punkty graniczne lewa góra, prawa góra, lewy dól, prawy dół, szerokość)
pygame.draw.circle(screen, 'green', (200, 150), 50, 3)
# rysowanie okręgu (-||-, koordynaty środka, promień, szerkość lini)
pygame.draw.ellipse(screen, 'yellow', (300, 100, 100, 50), 4)
pygame.draw.polygon(screen, 'blue', ((250, 75), (300, 25), (300, 75)), 0)
# tworzenie kształtu z dwolonych punktów poprzez ich koordynaty, ustawienie szerokości na 0 wypełnia kolorem
done = True

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # event naciśnięcie przycisku, równe funkcji wbudowanej kończącej gre
            done = False

    pygame.display.flip()  # renderowanie gty na ekran
