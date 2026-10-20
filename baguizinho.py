import os
os.system('cls || clear')

import turtle

t = turtle.Turtle()
t.speed(3)
t.pensize(2)

# Define a cor de preenchimento (ex: rosa claro)
t.fillcolor("blue")

# Inicia o preenchimento
t.begin_fill()

# --- Desenho da Base (Testículos) ---
# Lado esquerdo
t.penup()
t.goto(-40, 0)
t.pendown()
t.circle(40)

# Lado direito
t.penup()
t.goto(40, 0)
t.pendown()
t.circle(40)

# --- Desenho do Corpo ---
t.penup()
t.goto(-30, 60)
t.pendown()
t.setheading(90)
t.forward(150)
t.circle(-30, 180) # Topo (glande)
t.forward(150)

# Finaliza o preenchimento de toda a forma
t.end_fill()

# Detalhe extra: linha da glande
t.penup()
t.goto(-30, 180)
t.setheading(0)
t.pendown()
t.circle(-30, 180)

turtle.done()
