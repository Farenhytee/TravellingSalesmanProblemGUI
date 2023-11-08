import pygame
import random
from points import Point

width, height = 600, 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
gray = (75,75,75)

pygame.init()
pygame.display.set_caption("Travelling Salesman Problem")
screen = pygame.display.set_mode((width, height))

points = []

offset_screen = 50
smallest_path = []
record_distance = 0
number_of_points = 15

for i in range(number_of_points):
    x = random.randint(offset_screen, width-offset_screen)
    y = random.randint(offset_screen, height-offset_screen)

    point = Point(x,y)
    points.append(point)

def shuffle(a,b,c):
    temp = a[b]
    a[b] = a[c]
    a[c] = temp

def dist_calc(points_list):
    total = 0
    for n in range(len(points)-1):
        distance = ((points[n].x - points[n+1].x)**2 + (points[n].y - points[n+1].y)**2)**0.5
        total += distance
    return total

dist = dist_calc(points)

record_distance = dist

smallest_path = points.copy()

font = pygame.font.Font('OpenSans-Light.ttf', 32)

run = True
while run:
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for n in range(len(points)):
        pygame.draw.circle(screen, black, (points[n].x, points[n].y), 10)

    a = random.randint(0, len(points)-1)
    b = random.randint(0, len(points)-1)

    shuffle(points, a, b)

    dist = dist_calc(points)
    if dist < record_distance:
        record_distance = dist
        smallest_path = points.copy()

    for m in range(len(points)-1):
        pygame.draw.line(screen, gray, (points[m].x, points[m].y), (points[m+1].x, points[m+1].y), 2)

    for m in range(len(smallest_path)-1):
        pygame.draw.line(screen, red, (smallest_path[m].x, smallest_path[m].y), (smallest_path[m+1].x, smallest_path[m+1].y), 4)


    text2 = font.render("Shortest Path: ", 1, black)
    textRect2 = text2.get_rect()
    textRect2.center = (150, 550)
    screen.blit(text2, textRect2)

    text1 = font.render(str(round(record_distance, 3)), 1, black)
    textRect1 = text1.get_rect()
    textRect1.center = (350, 550)
    screen.blit(text1, textRect1)

    pygame.display.update()

pygame.quit()
    