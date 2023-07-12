import pygame
from sys import exit

pygame.init()
screen_width = 300
screen_height = 215
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bubble Sort")
background_color = (0, 0, 0)  # black
bar_color = (0, 255, 0)  # green


def draw_bars(screen, background_color, bar_color, bar_width, bar_heights, screen_height):
    screen.fill(background_color)
    for i, height in enumerate(bar_heights):

        pygame.draw.rect(screen, bar_color, (i * bar_width, screen_height - height, bar_width, height))


def bubble_sort(arr):
    bar_width = screen_width / len(arr) # less 10 for padding
    bar_heights = arr
    for i in range(0, len(arr)):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                swap(arr, i, j)
                draw_bars(screen, background_color, bar_color, bar_width, bar_heights, screen_height)
                pygame.display.update()
                pygame.time.delay(100)


def visualization(arr):
    bar_width = screen_width / len(arr)  # less 10 for padding
    bar_heights = arr
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        bubble_sort(arr)
        draw_bars(screen, background_color, bar_color, bar_width, bar_heights, screen_height)
        pygame.display.update()


def swap(arr, idx1, idx2):
    temp = arr[idx1]
    arr[idx1] = arr[idx2]
    arr[idx2] = temp


if __name__ == '__main__':
    visualization([119, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 150, 200, 211, 188, 122, 41, 123, 55, 22])

