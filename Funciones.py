import subprocess
import os
import random

def limpiar_consola():
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run(comando, shell=True)

def esperar_enter() -> None:
	input("Ingresá ENTER para continuar....")

def validar_usuario_y_contrasenia(usuario: str, contrasenia:str) -> bool:
     if len(usuario) < 4 or len(contrasenia) < 8:
          validacion = True
     else:
          validacion = False
     return validacion

def transferir_dinero(vector: list, monto: float) -> None:
     vector[3] -= monto

def cargar_dinero(vector: list, monto: float) -> None:
     vector[3] += monto



      

      


      