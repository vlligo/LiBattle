def main():
    import pygame
    import time

    pygame.init()
    w = 640
    h = 480
    screen = pygame.display.set_mode((w, h))
    pygame.display.set_caption("First level")

    def display_text(a: str, down=0) -> None:
        font = pygame.font.SysFont(None, 66)
        img = font.render(a, True, "black")
        screen.blit(img, (w / 2 - img.get_rect().width / 2, h / 2 - img.get_rect().height / 2 + down))
        pygame.display.flip()

    running = True
    col = 0
    ans_col = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                ans_col = col
                running = False
        col += 1
        if col == 255:
            col = -255
        screen.fill(pygame.Color(abs(col), 255 - abs(col), 0))
        display_text("Press on the left mouse button,")
        display_text("when the screen is red", 30)
        time.sleep(0.0005)
        pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                running = False
        screen.fill(pygame.Color(abs(col), 255 - abs(col), 0))
        display_text("Your score: {}/100".format(int(100 * abs(ans_col) / 255)))
        pygame.display.flip()
    pygame.quit()
