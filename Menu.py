from Inputs import *
from Funciones import *
from Prints import *

"""
# Indices de listas previo a diccionarios
# Posicion : 0 usuario - 1 contraseña - 2 Tipo de Usuario - 
#            3 Saldo en Cuenta - 4 Nombre - 5 Apellido -
#            6 mail - 7 dni - 8 edad - 9 Año de alta 

"""


def iniciar_billetera() -> None:

    mostrar_encabezado()

# TIPOS DE CLIENTES EN VECTORES - USUARIOS CORTOS (previo a los diccionarios)

    # cliente = ["a", "a", "Cliente", 1000.00, "Cristiano", "Rolando","c.ronaldo@gmail.com","33123456",39, 2026]
    # empresa = ["b","b","Empresa", 10000000000000.00, "NIKE S.A.", "20-46546544-1","nikeoficial@gmail.com",500, 1212121.11 ]
    # admin = ["c","c","Administrador"]

# TIPOS DE CLIENTES EN DICCIONARIO - USUARIOS CORTOS

#    cliente = {
#        "usuario": "a",
#        "contraseña": "a",
#        "tipo": "Cliente",
#        "saldo": 1000.00,
#        "nombre": "Cristiano",
#        "apellido": "Rolando",
#        "mail": "c.ronaldo@gmail.com",
#        "dni": "33123456",
#        "edad": 39,
#        "año_alta": 2026
#    }

#    empresa = {
#        "usuario": "b",
#        "contraseña": "b",
#        "tipo": "Empresa",
#        "saldo": 10000000000000.00,
#        "razon_social": "NIKE S.A.",
#        "cuit": "20-46546544-1",
#        "mail": "nikeoficial@gmail.com",
#        "empleados": 500,
#        "capital": 1212121.11
#    }

#    admin = {
#        "usuario": "c",
#        "contraseña": "c",
#        "tipo": "Administrador"
#    }

# TIPOS DE CLIENTES EN DICCIONARIO - USUARIOS COMPLETOS

    cliente = {
        "usuario": "c.ronaldo",
        "contraseña": "balondeoro7",
        "tipo": "Cliente",
        "saldo": 1000.00,
        "nombre": "Cristiano",
        "apellido": "Rolando",
        "mail": "c.ronaldo@gmail.com",
        "dni": "33123456",
        "edad": 39,
        "año_alta": 2026,
        "alias": "cronaldo07",
        "cbu": "9876543210987654321098"
    }

    empresa = {
        "usuario": "nikeoficial",
        "contraseña": "chiquitapia",
        "tipo": "Empresa",
        "saldo": 10000000000000.00,
        "razon_social": "NIKE S.A.",
        "cuit": "20-46546544-1",
        "mail": "nikeoficial@gmail.com",
        "empleados": 500,
        "capital": 1212121.11,
        "alias": "nikeof",
        "cbu": "1234567890123456789012"
    }

    admin = {
        "usuario": "admingalperin",
        "contraseña": "mercado1234",
        "tipo": "Administrador"
    }
 
    usuarios = [cliente, empresa]

    usuario = iniciar_sesion(cliente, empresa, admin)

    limpiar_consola() 

    opcion = -1
    match usuario["tipo"]:
        case "Cliente":
            while opcion != 0:
                mostrar_menu_cliente(usuario)
                opcion = ingresar_entero()

                if opcion == 1:
                    ver_datos_cliente(cliente)
                if opcion == 2:
                    ver_inicio_transferencia(cliente, "TRANSFERIR")
                    alias = ingresar_alias()
                    monto = ingresar_monto(cliente)
                    transferir_dinero(cliente, monto)
                    ver_transferencia(alias, monto, "TRANSFERIR")
                if opcion == 3:
                    ver_inicio_carga(cliente, "CARGAR SALDO")
                    carga = ingresar_carga("Ingrese dinero en su cuenta: $ ")
                    cargar_dinero(cliente, carga)
                    ver_carga_de_saldo(carga, "CARGAR SALDO")
                if opcion == 0:
                    mostrar_saludo()

        case "Empresa":
            while opcion != 0:
                mostrar_menu_empresa(usuario)
                opcion = ingresar_entero()
            
                if opcion == 1:
                    ver_datos_empresa(empresa)
                if opcion == 2:
                    ver_inicio_carga(empresa, "RECIBIR DINERO")
                    carga = ingresar_carga("Cobrar pago: $ ")
                    cargar_dinero(empresa, carga)
                    ver_carga_de_saldo(carga, "RECIBIR DINERO")
                if opcion == 3:
                    ver_inicio_transferencia(empresa, "LIQUIDAR SUELDO")
                    alias = ingresar_alias()
                    monto = ingresar_monto(empresa, 350000, 2800000)
                    transferir_dinero(empresa, monto)
                    ver_transferencia(alias, monto, "LIQUIDAR SUELDO")
                

                if opcion == 0:
                    mostrar_saludo()


        case "Administrador":
             while opcion != 0:
                mostrar_menu_admin(usuario)
                opcion = ingresar_entero()
          
                if opcion == 1:
                    nuevo = crear_usuario(usuarios)
                    if nuevo is not None:
                        usuarios.append(nuevo)

                if opcion == 2:
                    borrar_usuario()

                if opcion == 3:
                    ver_informacion_del_sistema()        

                if opcion == 0:
                    mostrar_saludo()
 

def mostrar_menu_cliente(vector: dict)-> None:
    # print("{:^30}".format("***💰 MENU PRINCIPAL 💰***"))
    print("*** MENU CLIENTE ***") 
    print(f"USUARIO: {vector['usuario']}")
    print(f"TIPO: {vector['tipo']}")
    print(f"SALDO ACTUAL: $ {vector['saldo']:.2f}")

    print("""
         1️⃣ 🧾 Ver datos
         2️⃣ 💸 Transferir dinero
         3️⃣ 💳 Cargar saldo
         0️⃣ 🚪 Salir
        """)
    
def mostrar_menu_empresa(vector: dict)-> None:
    # print("{:^30}".format("***💰 MENU PRINCIPAL 💰***"))
    print("*** MENU EMPRESA ***") 
    print(f"USUARIO: {vector['usuario']}")
    print(f"TIPO: {vector['tipo']}")
    print(f"SALDO ACTUAL: $ {vector['saldo']:.2f}")
    
    print("""
         1️⃣ 🧾 Ver datos
         2️⃣ 💰 Recibir Dinero
         3️⃣ 💸 Liquidar Sueldo
         0️⃣ 🚪 Salir
        """)
      
def mostrar_menu_admin(vector: dict)-> None:
    # print("{:^30}".format("***💰 MENU PRINCIPAL 💰***"))
    print("*** MENU ADMIN ***") 
    print(f"USUARIO: {vector['usuario']}")
    print(f"TIPO: {vector['tipo']}") 
    
    print("""
         1️⃣ ➕ Crear usuario
         2️⃣ ❌ Borrar usuario
         3️⃣ 🖥️  Ver Información de Sistema
         0️⃣ 🚪 Salir
        """)
 