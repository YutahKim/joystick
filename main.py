import pygame
pygame.init()


class combos():
    def __init__(self):
        self.entrada= []
        self.mapeo={"a":0,"b":1,"c":2,"d":3,"arriba":11,"abajo":12,"izq":13,"der":14}

    def orden(self,c):
        if len(self.entrada)<5:
            self.entrada.append(c)
        else:
            self.entrada=[]
        print(self.entrada)



def main():
    pygame.display.set_caption('JoyStick Example')
    surface = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    running = True

    font = pygame.font.Font(None, 20)
    linesize = font.get_linesize()
    joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
    for joy in joysticks:
        joy.init()

    aux=0
    ant=0
    cont=0
    stat=""
    comb=combos()
    unpress=True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        surface.fill((0,0,0))
        position = [10, 10]


        for joy in joysticks:
            image = font.render('name: ' + joy.get_name(), 1, (0,200,0))
            surface.blit(image, position)
            position[1] += linesize

            image = font.render('button count: {0}'.format(joy.get_numbuttons()), 1, (0,200,0))
            surface.blit(image, position)
            position[1] += linesize

            image = font.render('Estado: {0}'.format(stat), 1, (0,200,0))
            surface.blit(image, position)
            position[1] += linesize

            for i in range(joy.get_numbuttons()):
                if joy.get_button(i):
                    if cont==0:
                        comb.orden(i)
                        cont=1
                        #unpress=False
                    if (ant==3 and i==1):
                        stat="Combo Completo"
                        ant=0
                    else :
                        ant=0
                        stat=""
                    if (i==3):
                        ant=i

                    image = font.render('{0}: push ant {1}'.format(i,ant), 1, (0,200,0))
                    surface.blit(image, position)
                    position[1] += linesize

        pygame.display.flip()
        clock.tick(20)

    pygame.quit()

main()
