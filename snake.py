# Snake, classic arcade game.
import sys
from turtle import clear, update, ontimer, setup, hideturtle, tracer, listen, \
    done, onkey
from random import randrange, choice
from freegames import square, vector
from threading import Thread
from playsound import playsound


# Función para abrir archivo de música
def music_func():
    playsound('TusaDakiti.mp3')


# Definir función que llama audio
music = Thread(target=music_func)
music.daemon = True
# Iniciar musica
music.start()

# Definir posición incial de comida
food = vector(0, 0)
# Definir posición inicial de serpiente
snake = [vector(10, 0)]
# Definir dirección de movimiento inicial
aim = vector(0, 10)
# Definir colores posibles de serpiente y comida
colors = ["black", "green", "yellow", "pink", "blue"]
# Seleccionar color para serpiente
snakeColor = choice(colors)
foodColor = snakeColor
# Seleccionar color para comida distinto a serpiente
while(foodColor == snakeColor):
    foodColor = choice(colors)


# Función para cambiar dirección de serpiente
def change(x, y):
    # Se cambia dirección horizontal
    aim.x = x
    # Se cambia dirección vertical
    aim.y = y


# Determina si el parámetro se encuentra dentro de los límites
def inside(head):
    return -200 < head.x < 190 and -200 < head.y < 190


# Función para jugabilidad, mueve serpiente y determina si comió
def move():
    # Hace una copia de la cabeza de la serpiente
    head = snake[-1].copy()
    # Replica cabeza en la dirección en que se mueve
    head.move(aim)

    # Verifica si la cabeza se choca con el borde o con la misma serpiente
    if not inside(head) or head in snake:
        # Pinta cabeza en rojo si se chocó
        square(head.x, head.y, 9, 'red')
        # Refrescar pantalla
        update()
        # Termina juego finalizando Python para que thread de musica pare
        sys.exit()
        # Termina función y por lo tanto el juego
        return

    # Si no chocó con nada la cabeza ahora es la desplazada
    snake.append(head)

    # Verifica si serpiente chocó con comida
    if abs(head - food) < 15:
        # Imprime longitud de serpiente
        print('Snake:', len(snake))
        # Calcula nuevo recuadro de posición de comida dentro de límites
        food.x = randrange(-15, 14) * 10
        food.y = randrange(-15, 14) * 10
    else:
        # Si no comió no crece y por lo tanto elimina cola
        # al haberse desplazado un espacio la cabeza
        snake.pop(0)
        # Crear bandera para saber si se movió comida
        movedFood = False
        # Asegurar que se mueve comida con un ciclo
        while(not movedFood):
            # Crear numero para dirección aleatoria
            new_direction = randrange(1, 5)
            # Condicional si movimiento es a la derecha
            if new_direction == 1 and food.x + 10 <= 140:
                # Desplazar comida
                food.x += 10
                # Actualizar bandera
                movedFood = True
            # Condicional si movimiento es hacia abajo
            elif new_direction == 2 and food.y - 10 >= -150:
                food.y -= 10
                movedFood = True
            # Condicional si movimiento es a la izquierda
            elif new_direction == 3 and food.x - 10 >= -150:
                food.x -= 10
                movedFood = True
            # Condicional si movimiento es hacia arriba
            elif new_direction == 4 and food.y + 10 <= 140:
                food.y += 10
                movedFood = True

    # Elimina todo de la pantalla para recargarla con movimiento
    clear()

    # Ciclo para recorrer cada recuadro de longitud de la serpiente
    for body in snake:
        # Grafica cuadrado en posición de cada recuadro de serpiente
        # del color definido anteriormente de manera aleatoria
        square(body.x, body.y, 9, snakeColor)

    # Grafica cuadrado de comida en posición definida de
    # color definido de manera aleatoria anteriormente
    square(food.x, food.y, 9, foodColor)
    # Refrresca pantalla con dibujos nuevos
    update()
    # Función se autoinvoca cada 100 milisegundos
    ontimer(move, 100)


# Define tamaño y posición de pantalla desplegable
setup(420, 420, 370, 0)
# No mostrar tortuga con la que se grafica
hideturtle()
# Deshabilitar tracer para poder hacer Update
tracer(False)
# Se escucha llamados de teclas para cambiar entre colores
# y dibujar distintas figuras
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
# Llamar a las funciones y empezar juego
move()
done()
