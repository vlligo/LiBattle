def main():
    import pygame

    pygame.init()
    w = 640
    h = 480
    screen = pygame.display.set_mode((w, h))
    pygame.display.set_caption("First level")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()
