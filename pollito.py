from tkinter import *
import random

# ------------------
# VARIABLES GLOBALES
# ------------------
BASE = 480
ALTURA = 480

x_pollito = 225
y_pollito = 430

puntos = 0
vidas = 3

carros = []

# -------------------
# FUNCIONES
# -------------------

def crear_carros():
    global carros
    carros = []
    
    lista_carriles = [80, 130, 180, 260, 310, 360]
    colores_disponibles = ["yellow", "blue", "red", "orange", "purple", "cyan"]
    
    for i in range(len(lista_carriles)):
        pos_y = lista_carriles[i]
        
        if i % 2 == 0:
            vel = 4
        else:
            vel = -4
            
        color_carro1 = random.choice(colores_disponibles)
        color_carro2 = random.choice(colores_disponibles)
        
        carro1 = [random.randint(0, 150), pos_y, vel, 50, 25, color_carro1]
        carro2 = [random.randint(250, 380), pos_y, vel, 50, 25, color_carro2]
        
        carros.append(carro1)
        carros.append(carro2)


def mover_arriba(event=None):
    global y_pollito, puntos
    if y_pollito > 10:
        y_pollito = y_pollito - 20
        
    if y_pollito <= 50:
        puntos = puntos + 100
        reiniciar_posicion()
        
    dibujar()


def mover_abajo(event=None):
    global y_pollito
    if y_pollito < ALTURA - 40:
        y_pollito = y_pollito + 20
    dibujar()


def mover_izquierda(event=None):
    global x_pollito
    if x_pollito > 10:
        x_pollito = x_pollito - 20
    dibujar()


def mover_derecha(event=None):
    global x_pollito
    if x_pollito < BASE - 30:
        x_pollito = x_pollito + 20
    dibujar()


def reiniciar_posicion():
    global x_pollito, y_pollito
    x_pollito = 225
    y_pollito = 430


def mover_carros_y_colisiones():
    global vidas, puntos
    
    for car in carros:
        car[0] = car[0] + car[2]
        
        if car[2] > 0 and car[0] > BASE:
            car[0] = -car[3]
            
        if car[2] < 0 and car[0] < -car[3]:
            car[0] = BASE
            
        x_carro = car[0]
        y_carro = car[1]
        ancho_carro = car[3]
        alto_carro = car[4]
        
        if (x_pollito < x_carro + ancho_carro and
            x_pollito + 25 > x_carro and
            y_pollito < y_carro + alto_carro and
            y_pollito + 25 > y_carro):
            
            vidas = vidas - 1
            reiniciar_posicion()
            
            if vidas <= 0:
                puntos = 0
                vidas = 3

    dibujar()
    ventana.after(30, mover_carros_y_colisiones)


def dibujar():
    c.delete("all")
    
    # 1. ESCENARIO
    c.create_rectangle(0, 0, BASE, 60, fill="green")
    c.create_rectangle(0, 215, BASE, 250, fill="green")
    c.create_rectangle(0, 410, BASE, ALTURA, fill="green")
    
    c.create_rectangle(0, 60, BASE, 215, fill="gray")
    c.create_rectangle(0, 250, BASE, 410, fill="gray")
    
    for x in range(0, BASE, 40):
        c.create_line(x, 110, x + 20, 110, fill="white")
        c.create_line(x, 160, x + 20, 160, fill="white")
        c.create_line(x, 300, x + 20, 300, fill="white")
        c.create_line(x, 355, x + 20, 355, fill="white")

    # 2. CARROS 
    for car in carros:
        x = car[0]
        y = car[1]
        ancho = car[3]
        alto = car[4]
        color = car[5]
        
        c.create_rectangle(x, y + 3, x + ancho, y + alto - 3, fill=color, outline="black")
        c.create_rectangle(x + 10, y + 6, x + ancho - 10, y + alto - 6, fill="lightblue", outline="black")
        c.create_rectangle(x + 5, y, x + 15, y + 3, fill="black")
        c.create_rectangle(x + ancho - 15, y, x + ancho - 5, y + 3, fill="black")
        c.create_rectangle(x + 5, y + alto - 3, x + 15, y + alto, fill="black")
        c.create_rectangle(x + ancho - 15, y + alto - 3, x + ancho - 5, y + alto, fill="black")

    # 3. POLLITO 
    c.create_oval(x_pollito, y_pollito + 8, x_pollito + 20, y_pollito + 24, fill="yellow", outline="black")
    c.create_oval(x_pollito + 10, y_pollito, x_pollito + 24, y_pollito + 14, fill="yellow", outline="black")
    c.create_oval(x_pollito + 18, y_pollito + 3, x_pollito + 22, y_pollito + 7, fill="black")
    c.create_polygon(x_pollito + 22, y_pollito + 6, x_pollito + 28, y_pollito + 9, x_pollito + 22, y_pollito + 12, fill="red", outline="black")

    # 4. PUNTAJE
    c.create_text(60, 30, text="Puntos: " + str(puntos), fill="white", font=("Arial", 11, "bold"))
    c.create_text(420, 30, text="Vidas: " + str(vidas), fill="white", font=("Arial", 11, "bold"))


# -----------------
# VENTANA PRINCIPAL
# -----------------
ventana = Tk()
ventana.title("Juego Pollito - Versión 2")
ventana.geometry("500x620")
ventana.config(bg="white")
ventana.resizable(False, False)

# Canvas del juego
frame_graficacion = Frame(ventana, bg="green", width=490, height=490)
frame_graficacion.place(x=5, y=5)

c = Canvas(frame_graficacion, width=BASE, height=ALTURA, bg="black")
c.place(x=5, y=5)

# Teclas
ventana.bind("<KeyPress-Right>", mover_derecha)
ventana.bind("<KeyPress-Left>", mover_izquierda)
ventana.bind("<KeyPress-Up>", mover_arriba)
ventana.bind("<KeyPress-Down>", mover_abajo)

# Panel inferior de controles
frame_controles = Frame(ventana, bg="green", width=490, height=110)
frame_controles.place(x=5, y=500)

# Botones de flechas compactos
bt_up = Button(frame_controles, text="▲", command=mover_arriba, width=3)
bt_up.place(x=225, y=10)

bt_left = Button(frame_controles, text="◄", command=mover_izquierda, width=3)
bt_left.place(x=185, y=40)

bt_right = Button(frame_controles, text="►", command=mover_derecha, width=3)
bt_right.place(x=265, y=40)

bt_down = Button(frame_controles, text="▼", command=mover_abajo, width=3)
bt_down.place(x=225, y=70)

# Inicio del programa
crear_carros()
mover_carros_y_colisiones()

ventana.mainloop()