import pygame


def startGame(gameDisplay, save, player, clock):
    '''runs the main game'''
    done = False
    player.rect.x = 0
    player.rect.y = 576
    player_list = pygame.sprite.Group()
    player_list.add(player)
    steps = 5 # pixels to move per step
    while not done:
        gameDisplay.fill((0, 0, 0))
        player_list.draw(gameDisplay)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pause_game = __import__('littlelight').pause_game
            done = pause_game(gameDisplay)
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.control(-steps, 0)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.control(steps, 0)
        if not (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and not (keys[pygame.K_LEFT] or keys[pygame.K_a]):
            player.control(0, 0)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
                    print('jump')
        # if event.type == pygame.KEYUP:
            # if event.key == pygame.K_LEFT or event.key == ord('a'):
                # player.control(0, 0)
            # if event.key == pygame.K_RIGHT or event.key == ord('d'):
                # player.control(0, 0)
        player.update()
        pygame.display.flip()
        clock.tick(20)
    return done