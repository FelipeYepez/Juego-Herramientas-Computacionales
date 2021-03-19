"""Pacman, classic arcade game.

Exercises

1. Change the board.
2. Change the number of ghosts.
3. Change where pacman starts.
4. Make the ghosts faster/slower.
5. Make the ghosts smarter.

"""

from random import choice
from turtle import bgcolor, Turtle, clear, up, goto, dot, \
    update, ontimer, setup, hideturtle, tracer, listen, onkey, done
from freegames import floor, vector

state = {'score': 0}
path = Turtle(visible=False)
writer = Turtle(visible=False)
aim = vector(5, 0)
pacman = vector(-40, -80)
ghosts = [
    # vector donde se enuentra cada ghost
    # nos dice hacia donde se mueve cada ghost
    [vector(-180, 160), vector(5, 0)],
    [vector(-180, -160), vector(0, 5)],
    [vector(100, 160), vector(0, -5)],
    [vector(100, -160), vector(-5, 0)],
]
tiles = [
    #  en 1 habra recuadro, en 0 hay espacio vacio
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
    0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0,
    0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0,
    0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
    0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0,
    0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]


def square(x, y):
    "Draw square using path at (x, y)."
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()
    # elimina los puntos que pacman come
    for count in range(4):
        path.forward(20)
        path.left(90)
    path.end_fill()


def offset(point):
    "Return offset of point in tiles."
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index


#  moimiento en cada punto del tablero del juego
def valid(point):
    "Return True if point is valid in tiles."
    index = offset(point)

    if tiles[index] == 0:
        return False

    index = offset(point + 19)

    if tiles[index] == 0:
        return False
    return point.x % 20 == 0 or point.y % 20 == 0


# funcion para crear tablero de juego
def world():
    "Draw world using path."
    #  fondo negro, contorno azul
    bgcolor('black')
    path.color('blue')

    # parametros del ciclo = largo del tablero
    for index in range(len(tiles)):
        tile = tiles[index]

        if tile > 0:
            # centrar x y y en el cuadro del juego, es decir,
            # que no salgan de los bordes
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)
            # grosor y posicion de los puntos
            if tile == 1:
                path.up()
                # +10 cuasa que los puntos queden centrados
                # en cada recuadro
                path.goto(x + 10, y + 10)
                path.dot(2, 'white')


# establecer movimiento de pacman y ghosts
def move():
    "Move pacman and all ghosts."
    writer.undo()
    writer.write(state['score'])

    clear()

    if valid(pacman + aim):
        pacman.move(aim)

    index = offset(pacman)

    # aumeto del score de acuerdo a los puntos
    # obtenidos por pacman
    if tiles[index] == 1:
        tiles[index] = 2
        state['score'] += 1
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y)

    up()
    # ancho de pacman en recuadro
    goto(pacman.x + 10, pacman.y + 10)
    # grosor y color de pacman
    dot(20, 'yellow')

    for point, course in ghosts:
        # si pacman esta a la izquierda, ghost va a la derecha si puede
        if point.x < pacman.x and valid(point + vector(10, 0)):
            #  # 10 es velocidad de ghost
            course.x = 10
            course.y = 0
        # si pacman esta a la derecha, ghost va a izq si puede

        elif point.x > pacman.x and valid(point + vector(-10, 0)):
            course.x = -10
            course.y = 0
        # si pacman esta abajo, ghost va arriba si puede
        elif point.y < pacman.y and valid(point + vector(0, 10)):
            course.x = 0
            course.y = 10
        # si pacman esta arriba, ghost va abajo si puede

        elif point.y > pacman.y and valid(point + vector(0, -10)):
            course.x = 0
            course.y = -10
        # si pacman no esta cerca
        else:
            options = [
                # ghost va hacia donde pueda
                # num 10 es velocidad de ghost
                vector(10, 0),
                vector(-10, 0),
                vector(0, 10),
                vector(0, -10),
            ]
            # movimiento aleatorio
            plan = choice(options)
            course.x = plan.x
            course.y = plan.y
        # movimiento hacia un punto valido, es decir, 1
        if valid(point + course):
            point.move(course)

        up()
        # ancho de ghost en su posicion
        goto(point.x + 10, point.y + 10)
        # tamaño y color de ghosts
        dot(20, 'red')
    # refresh a la pantalla
    update()
    for point, course in ghosts:
        # distancia entre el radio de pacman y ghost
        if abs(pacman - point) < 20:
            return
    #  velocidad del juego
    ontimer(move, 100)


# funcion correspondencia de valores en vectores
def change(x, y):
    "Change pacman aim if valid."
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y


# tamaño de recuadro principal
setup(420, 420, 370, 0)

hideturtle()
tracer(False)
writer.goto(160, 160)
writer.color('white')
writer.write(state['score'])
listen()
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')
world()
move()
done()
