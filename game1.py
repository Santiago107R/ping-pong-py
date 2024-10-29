import sys
import random
import pygame

pygame.init()
pygame.mixer.init()

ANCHO = 1280
ALTO = 720

FUENTE = pygame.font.SysFont("consolas", int(ANCHO/20))

pantalla = (pygame.display.set_mode((ANCHO, ALTO)))

pygame.display.set_caption("Ping Pong")

reloj = pygame.time.Clock()

#paletas

jugador = pygame.Rect(ANCHO-110, ALTO/2-50, 10, 100)
oponente = pygame.Rect(110, ALTO/2-50, 10, 100)

jugador_nom = "papu"
oponente_nom = "pepa"
#puntos
jugador_puntos = 0
oponente_puntos = 0

#pelotita

pelota = pygame.Rect(ANCHO/2-10, ALTO/2-10, 20, 20)
x_velo = 1
y_velo = 1

#barra
barra = pygame.Rect(ANCHO/2, 0, 2, ALTO)

#sonido
pong = pygame.mixer.Sound("pingpong.mp3")
victory = pygame.mixer.Sound("victory.mp3")

run = True
victoria = False

while run:
    tecla_presionada = pygame.key.get_pressed()
    
    if tecla_presionada[pygame.K_UP]:
        if jugador.top > 0:
            jugador.top -= 2
    if tecla_presionada[pygame.K_DOWN]:
        if jugador.bottom < ALTO:
            jugador.bottom += 2
            
    if tecla_presionada[pygame.K_w]:
        if oponente.top > 0:
            oponente.top -= 2
    if tecla_presionada[pygame.K_s]:
        if oponente.bottom < ALTO:
            oponente.bottom += 2
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            # run = False
    
    #logica de la pelota
    if pelota.y >= ALTO:
        y_velo = -1
    if pelota.y <= 0:
        y_velo = 1
    if pelota.x <= 0:
        jugador_puntos += 1
        pelota.center = (ANCHO/2, ALTO/2)
        x_velo = random.choice([1, -1])
        y_velo = random.choice([1, -1])
    if pelota.x >= ANCHO:
        oponente_puntos += 1
        pelota.center = (ANCHO/2, ALTO/2)
        x_velo = random.choice([1, -1])
        y_velo = random.choice([1, -1])
    #logica jugador y oponente
    if jugador.x - pelota.width <= pelota.x <= jugador.x and pelota.y in range(jugador.top-pelota.width, jugador.bottom+pelota.width):
        x_velo = -1
        pong.play()
    if oponente.x - pelota.width <= pelota.x <= oponente.x and pelota.y in range(oponente.top-pelota.width, oponente.bottom+pelota.width):
        x_velo = 1
        pong.play()
        
    
    #velocidad de la pelota
    pelota.x += x_velo * 2
    pelota.y += y_velo * 2
    
    #oponente IA
    if event == pygame.K_i:
        if oponente.y < pelota.y:
            oponente.top += 1
        if oponente.bottom > pelota.y:
            oponente.bottom -= 1
    
    
    #putuaciones
    jugador_puntos_texto = FUENTE.render(str(jugador_puntos), True, "white")
    oponente_puntos_texto = FUENTE.render(str(oponente_puntos), True, "white")
    
    pantalla.fill("black")
    
    #rectangulos de paleta
    pygame.draw.rect(pantalla, "white", jugador)
    pygame.draw.rect(pantalla, "white", oponente)
    #pelota pos
    pygame.draw.circle(pantalla, "white", pelota.center, 10)
    #puntuacion en pantalla
    pantalla.blit(jugador_puntos_texto, (ANCHO/2+140, 50))
    pantalla.blit(oponente_puntos_texto, (ANCHO/2-140, 50))
    #barra
    pygame.draw.rect(pantalla, "white", barra)
    pygame.display.update()
    reloj.tick(300) 
          
    if jugador_puntos == 10:
      victoria = True
      while victoria:
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 pygame.quit()
                 sys.exit()
                
         pantalla.fill("black")
         vic_texto = FUENTE.render(f"Victoria", True, "yellow")
         vic_jugador = FUENTE.render(f"para {jugador_nom}", True, "white")
         pantalla.blit(vic_texto, (ANCHO/2-150, ALTO/2-70))
         pantalla.blit(vic_jugador, (ANCHO/2-160, ALTO/2+-30))
         victory.play(-1)
         if event.type == pygame.MOUSEBUTTONDOWN:
             run = True
             victoria = False
             victory.stop()
             jugador_puntos = 0
             oponente_puntos = 0
         pygame.display.update()
    if oponente_puntos == 10:
      victoria = True
      while victoria:
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 pygame.quit()
                 sys.exit()
                
         pantalla.fill("black")
         vic_texto = FUENTE.render(f"Victoria", True, "yellow")
         vic_oponente = FUENTE.render(f"para {oponente_nom}", True, "white")
         pantalla.blit(vic_texto, (ANCHO/2-150, ALTO/2-70))
         pantalla.blit(vic_oponente, (ANCHO/2-160, ALTO/2+-30))
         victory.play(-1)
         
         if event.type == pygame.MOUSEBUTTONDOWN:
             run = True
             victoria = False
             victory.stop()
             jugador_puntos = 0
             oponente_puntos = 0
         pygame.display.update()