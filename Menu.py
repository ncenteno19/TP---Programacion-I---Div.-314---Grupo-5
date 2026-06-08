from Inputs import *
from Funciones import *
from Prints import *

"""
#Hasta ahora con listas 
# Posicion : 0 usuario - 1 contraseña - 2 Tipo de Usuario - 
#            3 Saldo en Cuenta - 4 Nombre - 5 Apellido -
#            6 mail - 7 dni - 8 edad - 9 Año de alta 

"""


def iniciar_billetera() -> None:

    mostrar_encabezado()

# SOLO PARA PRUEBA CON USUARIO CORTOS - MODIFICAR FUNCION iniciar_sesion EN INPUTS

    # cliente = ["c.ronaldo", "balondeoro7", "Cliente", 10000.00,"Cristiano", "Rolando","c.ronaldo@gmail.com","33123456",39, 2026]
    # empresa = ["b","b","Empresa", 10000000000000.00, "NIKE S.A.", "20-46546544-1","nikeoficial@gmail.com",500, 1212121.11 ]
    # admin = ["admingalperin","mercado1234","Administrador"]

    cliente = ["a", "a", "Cliente", 1000.00, "Cristiano", "Rolando","c.ronaldo@gmail.com","33123456",39, 2026]
    empresa = ["b","b","Empresa", 10000000000000.00, "NIKE S.A.", "20-46546544-1","nikeoficial@gmail.com",500, 1212121.11 ]
    admin = ["c","c","Administrador"]
 
    usuario = iniciar_sesion(cliente,empresa,admin)

    limpiar_consola() 

    opcion = -1
    match usuario[2]:
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
                    limpiar_consola()
                    print("══════════ ➕ CREAR USUARIO ➕ ══════════")
                    nuevo_usuario = ingresar_nombre_usuario()
                    nueva_contrasenia = ingresar_contrasenia_nueva()
                    nuevo_rol = ingresar_rol()
                    if nuevo_rol == "cliente":
                        nuevo_vector = ingresar_datos_nuevo_cliente(nuevo_usuario, nueva_contrasenia)
                    else:
                        nuevo_vector = ingresar_datos_nueva_empresa(nuevo_usuario, nueva_contrasenia)
                    ver_crear_usuario(nuevo_vector)

                if opcion == 2:
                    limpiar_consola()
                    print("══════════ ❌ BORRAR USUARIO ❌ ══════════")
                    nombre_a_borrar = ingresar_nombre_usuario("Ingrese el usuario a eliminar (mínimo 4 caracteres): ")
                    ver_borrar_usuario(nombre_a_borrar)

                if opcion == 3:
                    ver_informacion_sistema()

                if opcion == 0:
                    mostrar_saludo()
 

def mostrar_menu_cliente(vector: list)-> None:
    # print("{:^30}".format("***💰 MENU PRINCIPAL 💰***"))
    print("*** MENU CLIENTE ***") 
    print(f"USUARIO: {vector[0]}")
    print(f"TIPO: {vector[2]}")
    print(f"SALDO ACTUAL: $ {vector[3]:.2f}")

    print("""
         1️⃣ 🧾 Ver datos
         2️⃣ 💸 Transferir dinero
         3️⃣ 💳 Cargar saldo
         0️⃣ 🚪 Salir
        """)
    
def mostrar_menu_empresa(vector: list)-> None:
    # print("{:^30}".format("***💰 MENU PRINCIPAL 💰***"))
    print("*** MENU EMPRESA ***") 
    print(f"USUARIO: {vector[0]}")
    print(f"TIPO: {vector[2]}")
    print(f"SALDO ACTUAL: $ {vector[3]:.2f}")
    
    print("""
         1️⃣ 🧾 Ver datos
         2️⃣ 💰 Recibir Dinero
         3️⃣ 💸 Liquidar Sueldo
         0️⃣ 🚪 Salir
        """)
      
def mostrar_menu_admin(vector: list)-> None:
    # print("{:^30}".format("***💰 MENU PRINCIPAL 💰***"))
    print("*** MENU ADMIN ***") 
    print(f"USUARIO: {vector[0]}")
    print(f"TIPO: {vector[2]}") 
    
    print("""
         1️⃣ ➕ Crear usuario
         2️⃣ ❌ Borrar usuario
         3️⃣ 🖥️  Ver Información de Sistema
         0️⃣ 🚪 Salir
        """)