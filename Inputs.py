from Funciones import *


def iniciar_sesion(cliente: list, empresa: list, admin: list, 
                   mensaje_error_long: str = "❌Error. Caracteres insuficientes"
                   ,mensaje_error_val: str = "❌Error. Los datos ingresados no son válidos.") -> list:
    while True:
        usuario = input("Ingrese su Usuario: ")
        contrasenia = input("Ingrese su Contraseña: ")

        # if validar_usuario_y_contrasenia(usuario,contrasenia):
        #     print(mensaje_error_long)
        # else:
        #     if usuario == cliente[0] and contrasenia == cliente[1]:
        #         return cliente
        #     if usuario == empresa[0] and contrasenia == empresa[1]:
        #         return empresa
        #     if usuario == admin[0] and contrasenia == admin[1]:
        #         return admin
        #     print(mensaje_error_val)

 
        """SOLO PARA PRUEBA CON USUARIO CORTOS - MODIFICAR LISTAS DE TIPOS DE CLIENTES EN MENU"""

        if usuario == cliente[0] and contrasenia == cliente[1]:
            return cliente
        if usuario == empresa[0] and contrasenia == empresa[1]:
            return empresa
        if usuario == admin[0] and contrasenia == admin[1]:
            return admin
        print(mensaje_error_val)

def ingresar_entero(mensaje: str = "Qué desea realizar?: ", 
                    mensaje_error: str = "❌Dato inválido. Intente nuevamente") -> int:
    """
    Solicita al usuario el ingreso de un número entero positivo y valida
    que la cadena ingresada represente un número entero válido.

    Args:
        mensaje (str): Texto que se muestra al usuario para solicitar el ingreso del número.
        mensaje_error (str): Texto que se muestra cuando el dato ingresado no es válido.

    Returns:
        int: Número entero válido ingresado por el usuario.
    """

    numero = input(mensaje)

    while validar_cadena_entero(numero) == False:
        print(mensaje_error)
        numero = input(mensaje)

    numero = int(numero)
    return numero

def validar_cadena_entero(cadena: str) -> bool:
    """
    Verifica si una cadena representa un número entero válido.
    Utilizando código ASCII

    Args:
        cadena (str): Cadena a validar.

    Returns:
        bool: True si la cadena contiene solo dígitos, False en caso contrario.
    """
    if len(cadena) > 0:
        retorno = True
        for i in range(len(cadena)):
            caracter = cadena[i]
            caracter_ascii = ord(caracter)
            if caracter_ascii > 57 or caracter_ascii < 48:
                retorno = False
                break
    else:
        retorno = False

    return retorno

def ingresar_alias(mensaje: str = "Ingrese el Alias: ",
                   mensaje_error: str = "❌Alias Incorrecto. Intente nuevamente") -> str:
    while True:
         alias = input(mensaje).strip() #.strip agregado solo por recomendación de IA, la cual borra espacios en blanco
        
         if 8 <= len(alias) <= 16:
            return alias
         else:
             print(mensaje_error)
    
def ingresar_monto(vector: list, monto_min: float = 0, monto_max: float = 0,
                   mensaje: str = "Ingrese el monto a Transferir: $ ",
                   mensaje_error1: str = "❌ Monto Supera su Saldo. Intente nuevamente",
                   mensaje_error2: str = "❌ El monto debe ser entre $350.000 y $2.800.000") -> float:
      
    while True:
        monto = float(ingresar_carga(mensaje))
        if monto > vector[3]:
            print(mensaje_error1)
        elif monto < monto_min or monto > monto_max:
            print(mensaje_error2)

        else:
            return monto
     

def ingresar_carga(mensaje: str,
                   mensaje_error1: str = "❌ Monto debe ser Mayor a Cero. Intente nuevamente", 
                   mensaje_error2: str = "❌ Error. Ingrese un número mayor a cero") -> int:
     while True:
        carga = ingresar_entero(mensaje, mensaje_error2)
        if carga == 0:
            print(mensaje_error1)
        else:
            return carga
        
#funcion que soluciona problema de ingreso de numeros    
def ingresar_entero(mensaje: str = "Qué desea realizar?: ", mensaje_error: str = "❌ Error. Ingrese un número mayor a cero") -> int: 
    numero = input(mensaje)

    while validar_cadena_entero(numero) == False:
        print(mensaje_error)
        numero = input(mensaje)

    numero = float(numero)
    return numero

