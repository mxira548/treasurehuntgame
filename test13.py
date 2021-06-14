import time
def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)

        titleText = gameDisplay.blit(title, (170, 200))    # title is an image
        titleText.center = ((display_width / 2), (display_height / 2))

        # button(x, y, w, h, inactive, active, action=None)
        button(100, 350, 195, 80, startBtn, startBtn_hover, game_loop)
        button(300, 350, 195, 80, creditsBtn, creditsBtn_hover, #Your function)

        pygame.display.update()
        time.sleep(15)
def button(x, y, w, h, inactive, active, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        gameDisplay.blit(active, (x, y))
        if click[0] == 1 and action is not None:
            action()
    else:
        gameDisplay.blit(inactive, (x, y))
button(340, 560, 400, 200, randomBtn, randomBtn_hover, random_func)
