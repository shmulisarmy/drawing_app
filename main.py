import pygame

pygame.init()

winsize = 1000
pen_size = 15
window = pygame.display.set_mode((winsize, winsize))
speed = 5
window.fill((0, 0, 0))
run = True
drawing = False
color = (0,255,0)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_c]:
        window.fill((0,0,0))

    switch_colors_by_key = {
        'g': (0, 255, 0),
        'r': (255, 0, 0),
        'p': (0, 0, 255),
        'o': (255, 0, 130),
        'e': (0, 0, 0)
    }
    if keys[pygame.K_g]:
        color = switch_colors_by_key['g']
    if keys[pygame.K_r]:
        color = switch_colors_by_key['r']
    if keys[pygame.K_p]:
        color = switch_colors_by_key['p']
    if keys[pygame.K_o]:
        color = switch_colors_by_key['o']
    if keys[pygame.K_e]:
        color = switch_colors_by_key['e']
        
    if keys[pygame.K_UP]:
        pen_size += .4
    if keys[pygame.K_DOWN] and pen_size > 0:
        pen_size -= .4
    if keys[pygame.K_s]:
        drawing_surface = pygame.Surface((winsize, winsize))
        drawing_surface.blit(window, (0, 0))
        pygame.image.save(drawing_surface, "drawing.png")

    if drawing:
        posx, posy = pygame.mouse.get_pos()
        pygame.draw.circle(window, color, (posx, posy), pen_size*3 if color == (0,0,0) else pen_size)
    
    pygame.display.update()