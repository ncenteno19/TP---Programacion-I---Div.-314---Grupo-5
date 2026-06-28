from Funciones import *
import random
from Prints import *

def iniciar_sesion(cliente: dict, empresa: dict, admin: dict, 
                   mensaje_error_long: str = "❌Error. Caracteres insuficientes"
                   ,mensaje_error_val: str = "❌Error. Los datos ingresados no son válidos.") -> dict:
    while True:
        usuario = input("Ingrese su Usuario: ")
        contrasenia = input("Ingrese su Contraseña: ")

        if validar_usuario_y_contrasenia(usuario,contrasenia):
            print(mensaje_error_long)
        else:
            if usuario == cliente["usuario"] and contrasenia == cliente["contraseña"]:
                return cliente
            if usuario == empresa["usuario"] and contrasenia == empresa["contraseña"]:
                return empresa
            if usuario == admin["usuario"] and contrasenia == admin["contraseña"]:
                return admin
            else:
                print(mensaje_error_val)
                iniciar_sesion

# PRIMERA FUCION DE INGRESAR_ENTERO CORREGIDA AL FINAL

#def ingresar_entero(mensaje: str = "Qué desea realizar?: ", 
#                    mensaje_error: str = "❌Dato inválido. Intente nuevamente") -> int:
#    """
#    Solicita al usuario el ingreso de un número entero positivo y valida
#    que la cadena ingresada represente un número entero válido.
#
#    Args:
#        mensaje (str): Texto que se muestra al usuario para solicitar el ingreso del número.
#        mensaje_error (str): Texto que se muestra cuando el dato ingresado no es válido.
#
#    Returns:
#        int: Número entero válido ingresado por el usuario.
#    """
#
#    numero = input(mensaje)

#    while validar_cadena_entero(numero) == False:
#        print(mensaje_error)
#        numero = input(mensaje)

#    numero = int(numero)
#    return numero

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
    
def ingresar_monto(vector: dict, monto_min: float = 350, monto_max: float = 2800000,
                   mensaje: str = "Ingrese el monto a Transferir: $ ",
                   mensaje_error1: str = "❌ Monto Supera su Saldo. Intente nuevamente",
                   mensaje_error2: str = "❌ El monto debe ser entre $350,00 y $2.800.000") -> float:
      
    while True:
        monto = float(ingresar_carga(mensaje))
       
        if monto > vector["saldo"]:
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
        
# Funcion que soluciona problema de ingreso de numeros
     
def ingresar_entero(mensaje: str = "Qué desea realizar?: ", mensaje_error: str = "❌ Error. Ingrese un número mayor a cero") -> int: 
    numero = input(mensaje)

    while validar_cadena_entero(numero) == False:
        print(mensaje_error)
        numero = input(mensaje)

    numero = float(numero)
    return numero

# Funciones para poder agregar un usuario 

def crear_usuario(usuarios: list) -> dict | None:
    limpiar_consola()
    print("══════════ ➕ CREAR USUARIO ══════════\n")

    tipo = ingresar_rol()
    cbu = generar_cbu_unico(usuarios)

    if tipo == "Cliente":
        nuevo_usuario = ingresar_datos_cliente(usuarios, cbu)
    else:
        nuevo_usuario = ingresar_datos_empresa(usuarios, cbu)

    ver_resumen_nuevo_usuario(nuevo_usuario)
    if confirmar_operacion():
        limpiar_consola()
        return nuevo_usuario
    else:
        print("\n⚠️  Operación cancelada. El usuario no fue registrado.")
        esperar_enter()
        limpiar_consola()
        return None


def ingresar_rol(mensaje: str = "Ingrese el rol (1. Cliente / 2. Empresa): ",
                 mensaje_error: str = "❌ Opción inválida. Ingrese 1 o 2") -> str:
    while True:
        print("Seleccione el tipo de usuario:")
        print("  1️⃣  Cliente")
        print("  2️⃣  Empresa")
        opcion = input(mensaje).strip()
        if opcion == "1":
            return "Cliente"
        elif opcion == "2":
            return "Empresa"
        print(mensaje_error)


def generar_cbu_unico(usuarios: list) -> str:
    
    cbus_existentes = []
    cbu_existe = True

    for u in usuarios:
        if "cbu" in u:
            cbus_existentes.append(u["cbu"])
    
    while cbu_existe:
        
        cbu = ""
        for _ in range(22):
            cbu += str(random.randint(0, 9))

        cbu_existe = False
        for cbu_registrado in cbus_existentes:
            if cbu == cbu_registrado:
                cbu_existe = True
                break

    return cbu


def ingresar_usuario_unico(usuarios: list,
                            mensaje: str = "Ingrese nombre de usuario: ",
                            mensaje_error_formato: str = "❌ Usuario inválido. Debe tener al menos 4 caracteres",
                            mensaje_error_duplicado: str = "❌ Ese nombre de usuario ya existe. Intente nuevamente") -> str:
    while True:
        usuario = input(mensaje).strip()

        if len(usuario) < 4:
            print(mensaje_error_formato)
            continue

        usuario_existe = False
        for u in usuarios:
            if u["usuario"] == usuario:
                usuario_existe = True
                break

        if not usuario_existe:
            return usuario
        print(mensaje_error_duplicado)

def ingresar_dni_unico(usuarios: list,
                       mensaje: str = "Ingrese DNI sin puntos: ",
                       mensaje_error_duplicado: str = "❌ Ese DNI ya está registrado. Intente nuevamente",
                       mensaje_error_formato: str = "❌ DNI inválido. Debe contener exactamente 8 dígitos") -> str:
    while True:
        dni = input(mensaje).strip()
        dni_valido = True

        if len(dni) != 8:
            dni_valido = False
        else:
            for caracter in dni:
                if ord(caracter) < 48 or ord(caracter) > 57:
                    dni_valido = False
                    break

        if not dni_valido:
            print(mensaje_error_formato)
            continue

        dni_existe = False
        for u in usuarios:
            if u.get("dni") == dni:
                dni_existe = True
                break

        if not dni_existe:
            return dni
        print(mensaje_error_duplicado)


def ingresar_alias_unico(usuarios: list,
                          mensaje: str = "Ingrese alias (ej: perro.gato.casa): ",
                          mensaje_error_duplicado: str = "❌ Ese alias ya está registrado. Intente nuevamente",
                          mensaje_error_formato: str = "❌ Alias inválido. Debe tener entre 8 y 20 caracteres") -> str:
    while True:
        alias = input(mensaje).strip()

        if len(alias) < 8 or len(alias) > 20:
            print(mensaje_error_formato)
            continue

        alias_existe = False
        for u in usuarios:
            if u["alias"] == alias:
                alias_existe = True
                break

        if not alias_existe:
            return alias
        print(mensaje_error_duplicado)

def ingresar_contraseña(mensaje: str = "Ingrese una contraseña: ",
                         mensaje_error: str = "❌ La contraseña debe tener al menos 8 caracteres") -> str:
    while True:
        contraseña = input(mensaje).strip()
        if len(contraseña) >= 8:
            return contraseña
        print(mensaje_error)

def ingresar_cuit(usuarios: list,
                       mensaje: str = "Ingrese CUIT sin puntos ni guiones: ",
                       mensaje_error_duplicado: str = "❌ Ese CUIT ya está registrado. Intente nuevamente",
                       mensaje_error_formato: str = "❌ CUIT inválido. Debe contener exactamente 11 dígitos") -> str:
    while True:
        cuit = input(mensaje).strip()
        cuit_valido = True

        if len(cuit) != 11:
            cuit_valido = False
        else:
            for caracter in cuit:
                if ord(caracter) < 48 or ord(caracter) > 57:
                    cuit_valido = False
                    break

        if not cuit_valido:
            print(mensaje_error_formato)
            continue

        cuit_existe = False
        for u in usuarios:
            if u.get("cuit") == cuit:
                cuit_existe = True
                break

        if not cuit_existe:
            return cuit
        print(mensaje_error_duplicado)

def ingresar_datos_cliente(usuarios: list, cbu: str) -> dict:
    print("\n── Datos del Cliente ──")
    usuario   = ingresar_usuario_unico(usuarios)
    contraseña = ingresar_contraseña()
    nombre    = input("Ingrese nombre: ").strip()
    apellido  = input("Ingrese apellido: ").strip()
    mail      = input("Ingrese mail: ").strip()
    dni       = ingresar_dni_unico(usuarios)
    edad      = int(ingresar_entero("Ingrese edad: "))
    año_alta  = int(ingresar_entero("Ingrese año de alta: "))
    alias     = ingresar_alias_unico(usuarios)

    return {
        "usuario":   usuario,
        "contraseña": contraseña,
        "tipo":      "Cliente",
        "saldo":     0.00,
        "nombre":    nombre,
        "apellido":  apellido,
        "mail":      mail,
        "dni":       dni,
        "edad":      edad,
        "año_alta":  año_alta,
        "alias":     alias,
        "cbu":       cbu
    }


def ingresar_datos_empresa(usuarios: list, cbu: str) -> dict:
    print("\n── Datos de la Empresa ──")
    usuario      = ingresar_usuario_unico(usuarios)
    contraseña   = ingresar_contraseña()
    razon_social = input("Ingrese razón social: ").strip()
    cuit         = ingresar_cuit(usuarios)
    mail         = input("Ingrese mail: ").strip()
    empleados    = int(ingresar_entero("Ingrese cantidad de empleados: "))
    capital      = float(ingresar_carga("Ingrese facturación mensual: $ "))
    alias        = ingresar_alias_unico(usuarios)

    return {
        "usuario":      usuario,
        "contraseña":   contraseña,
        "tipo":         "Empresa",
        "saldo":        0.00,
        "razon_social": razon_social,
        "cuit":         cuit,
        "mail":         mail,
        "empleados":    empleados,
        "capital":      capital,
        "alias":        alias,
        "cbu":          cbu
    }


def confirmar_operacion(mensaje: str = "¿Confirmar registro? (si/no): ",
                         mensaje_error: str = "❌ Ingrese 's' para confirmar o 'n' para cancelar") -> bool:
    while True:
        respuesta = input(mensaje).strip().lower()
        if respuesta == "si":
            return True
        elif respuesta == "no":
            return False
        print(mensaje_error)

def borrar_usuario() -> None:
    limpiar_consola()
    print("══════════ ❌ BORRAR USUARIO ══════════\n")

    while True:
        usuario = input("Ingrese el nombre de usuario a borrar: ").strip()

        if len(usuario) >= 4:
            break
        print("❌ El nombre de usuario debe tener al menos 4 caracteres")

    print(f"\n⚠️  ¿Está seguro que desea borrar el usuario '{usuario}'?")
    if confirmar_operacion("confirmar operacion ? si/no: "):
        print(f"\n🗑️  Borrando usuario '{usuario}'...")
        time.sleep(1)
        print(f"✅ El usuario '{usuario}' fue eliminado correctamente")
        esperar_enter()
        limpiar_consola()
    else:
        print("\n⚠️  Operación cancelada. El usuario no fue eliminado.")
        esperar_enter()
        limpiar_consola()
    