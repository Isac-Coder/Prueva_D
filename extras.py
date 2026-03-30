import os, random, time

def cargar():
    print("Cargando", end="")
    for _ in range(3):
        time.sleep(random.uniform(0.1, 0.4))
        print(".", end="", flush=True)

def saliendo():
    print("Saliendo", end="")
    for _ in range(3):
        time.sleep(random.uniform(0.1, 0.4))
        print(".", end="", flush=True)        

def Limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')