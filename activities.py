import pygame


pygame.init()
main_window = pygame.display.set_mode((2400,1602))
running = True
path = "D:/pic.jpg"

pygame.image.load(path).get_width()


def greyscale(img):
    for x in range(img.get_width()):
        for y in range(img.get_height()):
            colour = img.get_at((x,y))
            greyscale_value = (colour.r + colour.g + colour.b) / 3
            img.set_at((x,y), (greyscale_value, greyscale_value, greyscale_value))


def sepia_tone(picture):
    greyscale(picture)
    for x in range(picture.get_width()):
        for y in range(picture.get_height()):
            colour = picture.get_at((x,y))

            # tint shadows
            if colour.r < 63:
                colour.r = int(colour.r * 1.1)
                colour.b = int(colour.b * 0.9)

            # tint midtones
            if colour.r > 62 & colour.r < 192:
                colour.r = int(colour.r * 1.15) % 255
                colour.b = int(colour.b * 0.85)

            # tint highlights
            if colour.r > 191:
                colour.r = int(colour.r * 1.08) % 255

                if colour.r > 255:
                    colour.r = 255

                colour.b = int(colour.b * 0.93)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = False

    surf = pygame.image.load(path)

    sepia_tone(surf)

    main_window.fill((255,255,255))
    main_window.blit(surf, (0, 0))


    pygame.display.update()

pygame.quit()
