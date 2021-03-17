"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.

"""
# se importan las librerias a utilizar
from turtle import up, goto, down, begin_fill, forward, undo, \
    left, end_fill, setup, onscreenclick, listen, onkey, color, done
from freegames import vector


# funcion para el trazo de una linea recta
def line(start, end):
    "Draw line from start to end."
    # up() "levanta el lapiz"
    up()
    # se mueve a la posción del primer click
    goto(start.x, start.y)
    # down() "baja el lapiz" y comienza trazo
    down()
    # se mueve hasta la posición del segundo click
    goto(end.x, end.y)


# funcion trazo de cuadrado
def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    # Empieza relleno de forma
    begin_fill()
# 4 trazos
    for count in range(4):
        # largo = punto final de x - inicial en x
        forward(end.x - start.x)
        # para cada trazo, rota 90 grados hacia la izquierda
        left(90)
# fin del relleno
    end_fill()


# funcion trazo circulo
def circle(start, end):
    "Draw circle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    # establecer radio de acuerdo a los puntos
    radio = (end.x-start.x)/2
    # circunferencia de acuerdo al radio
    avanzar = 2*3.14159*radio/360
    # 359 trazos para graficar la circunferencia
    for count in range(359):
        # avanza de acuerdo al largo de circun
        forward(avanzar)
        left(1)
        # movimieto de x a y
    goto(start.x, start.y)
    end_fill()


# funcion trazo rectangulo
def rectangle(start, end):
    "Draw rectangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    # Ciclo para realizar 2 series de trazos
    for count in range(2):
        # Avanza rayando la distancia de ancho definida entre los dos clicks
        forward(end.x-start.x)
        left(90)
        # Avanza rayando la distancia de alto definida entre clicks
        forward(end.y-start.y)
        left(90)
    end_fill()


# funcion trazo triangulo
def triangle(start, end):
    "Draw triangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    # Ciclo para realizar los tres trazos de un triángulo equilatero
    for count in range(3):
        # Avanza la distancia definida pr los dos clicks
        forward(end.x - start.x)
        # Rota 120 grados al ser equilatero
        left(120)
    end_fill()


# recibe coordenadas de dos clicks
def tap(x, y):
    "Store starting point or draw shape."
    # al recibir un click, comienza a "guardar"
    start = state['start']
    # si es el primer click
    if start is None:
        # de acuerdo a los parametros de entrada
        # guarda info. en vectores
        state['start'] = vector(x, y)
    # Si es el segundo click
    else:
        # Obtiene figura a dibujar del estado shape
        shape = state['shape']
        # Guarda coordenadas del segundo click
        end = vector(x, y)
        # Llama a la función obtenida con ambas coordenadas de clicks
        shape(start, end)
        # Reinicia a estado inicial de iniciar dibujo
        state['start'] = None


# Crea diccionario de datos
def store(key, value):
    "Store value in state at key."
    state[key] = value


# Define estado inicial a rayar con líneas
state = {'start': None, 'shape': line}
# Define tamaño y posición de pantalla desplegable
setup(420, 420, 370, 0)
# Con cada click en la pantalla se llama a la función tap
onscreenclick(tap)
# Se escucha llamados de teclas para cambiar entre colores
# y dibujar distintas figuras
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
# nuevo_color
onkey(lambda: color('pink'), 'P')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
