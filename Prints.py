import random
import time

from Funciones import esperar_enter, limpiar_consola


def mostrar_encabezado() -> None:
    # print("""===💰 Bienvenido a BV UTN 💰===
    # Una Billetera Virtual para gestionar tu dinero de forma simple.
    # Su objetivo es poder realizar transferencias de forma simple y dinámica""")
    limpiar_consola()
    ancho = 0
    print("===💰 Bienvenido a BV UTN 💰===".center(ancho))
    print("Una Billetera Virtual para gestionar tu dinero de forma simple.".center(ancho))
    print("Su objetivo es poder realizar transferencias de forma simple y dinámica".center(ancho))
    print("")

def ver_datos_cliente(vector: list, mensaje_error: str = "❌ Verificar datos. Saldo negativo") -> None:

    if vector[3] < 0:
        print(mensaje_error)
    else:
        limpiar_consola()
        print("══════════ 📋 DATOS DEL CLIENTE 📋 ══════════")
        print(f"💰 Saldo actual     : ${vector[3]:.2f}")
        print(f"👤 Nombre           : {vector[4]}")
        print(f"👤 Apellido         : {vector[5]}")
        print(f"📧 Mail             : {vector[6]}")
        print(f"🪪 DNI               : {vector[7]}")
        print(f"🎂 Edad             : {vector[8]} años")
        print(f"📅 Año de alta      : {vector[9]}")
        print(f"🔐 Token de sesión  : {random.randint(100000, 999999)}")

        print("════════════════════════════════════════════")

        print("")
        esperar_enter()
        limpiar_consola()

def ver_inicio_transferencia(vector: list, titulo: str) -> None:
    limpiar_consola()
    print(f"══════════ 💸 {titulo} 💸 ══════════")
    print(f"💰 Saldo actual     : ${vector[3]:.2f}")
    print("═══════════════════════════════════════")
    print("")
    
def ver_transferencia(alias: str, monto: float, titulo: str) -> None:
    limpiar_consola()

    print(f"═══════ 💸 {titulo} 💸 ═══════\n")

    print("⏳ Procesando transferencia...")
    time.sleep(1)

    print(f"➡️  Destinatario : {alias}")
    print(f"💰 Monto        : $ {monto:.2f}")
    time.sleep(1)

    print("\n✅ Transferencia realizada con éxito")
    print("════════════════════════════════════\n")

    esperar_enter()
    limpiar_consola()

def ver_inicio_carga(vector: list, titulo = str) -> None:
    limpiar_consola()
    
    print(f"═════════ 💳 {titulo} 💳 ═════════")
    print(f"💰 Saldo actual     : ${vector[3]:.2f}")
    print("═══════════════════════════════════════")
    print("")

def ver_carga_de_saldo(carga: float, titulo: str) -> None:
    limpiar_consola()

    print(f"═════════ 💳 {titulo} 💳 ═════════\n")

    print("⏳ Procesando carga...")
    time.sleep(1)

    print(f"💰 Monto ingresado: $ {carga:.2f}")
    time.sleep(1)

    print("\n✅ Se ingresó el dinero en su cuenta")
    print("════════════════════════════════════\n")

    esperar_enter()
    limpiar_consola()

def mostrar_saludo() -> None:
    limpiar_consola()

    print("👋 ¡Hasta luego! Nos vemos pronto.")

def ver_datos_empresa(vector: list, mensaje_error: str = "❌ Verificar datos. Saldo negativo") -> None:

    if vector[3] < 0:
        print(mensaje_error)
    else:
        limpiar_consola()
        print("══════════ 🏢 DATOS DE LA EMPRESA 🏢 ══════════")

        print(f"💰 Saldo actual        : ${vector[3]:.2f}")
        print(f"🏢 Razón social        : {vector[4]}")
        print(f"🧾 CUIT                : {vector[5]}")
        print(f"📧 Mail                : {vector[6]}")
        print(f"👥 Empleados           : {vector[7]}")
        print(f"📈 Facturación mensual : ${vector[8]:.2f}")

        print("════════════════════════════════════════════")

        print("")
        esperar_enter()
        limpiar_consola()

def ver_crear_usuario(vector: list) -> None:
    limpiar_consola()
    print("══════════ ➕ CREAR USUARIO ➕ ══════════\n")
    print("⏳ Creando usuario...")
    time.sleep(1)
    print(f"👤 Usuario : {vector[0]}")
    print(f"🔑 Rol     : {vector[2]}")
    time.sleep(1)
    print("\n✅ Usuario creado con éxito")
    print("════════════════════════════════════\n")
    esperar_enter()
    limpiar_consola()

def ver_borrar_usuario(nombre_usuario: str) -> None:
    limpiar_consola()
    print("══════════ ❌ BORRAR USUARIO ❌ ══════════\n")
    print("⏳ Procesando eliminación...")
    time.sleep(1)
    print(f"👤 Usuario : {nombre_usuario}")
    time.sleep(1)
    print(f"\n✅ El usuario '{nombre_usuario}' fue eliminado del sistema")
    print("════════════════════════════════════\n")
    esperar_enter()
    limpiar_consola()

def ver_informacion_sistema() -> None:
    limpiar_consola()
    print("══════════ 🖥️  INFORMACIÓN DEL SISTEMA 🖥️  ══════════\n")

    print("👥 INTEGRANTES:")
    print("")

    print("📋 DESCRIPCIÓN DEL SISTEMA:")
    print("   ¿Para qué sirve?")
    print("   BV UTN es una billetera virtual que permite gestionar")
    print("   dinero de forma digital, realizando transferencias,")
    print("   cobros y pagos de sueldos de manera simple y segura.")
    print("")
    print("   ¿Qué problema resuelve?")
    print("   Elimina la necesidad de manejar efectivo y simplifica")
    print("   las transacciones financieras entre personas y empresas,")
    print("   ofreciendo trazabilidad y control sobre cada movimiento.")
    print("")

    print("👥 TIPOS DE USUARIO:")
    print("   • Cliente       : persona física que gestiona su dinero personal")
    print("   • Empresa       : organización que recibe pagos y liquida sueldos")
    print("   • Administrador : gestiona usuarios y supervisa el sistema")
    print("")

    print("⭐ FUNCIONALIDADES EXTRAS:")
    print("   🧍 Cliente:")
    print("      → Cargar saldo desde cuenta bancaria externa")
    print("      → Ver token de sesión de seguridad generado aleatoriamente")
    print("      → Historial de movimientos recientes (próxima entrega)")
    print("   🏢 Empresa:")
    print("      → Recibir pagos con monto simulado aleatorio")
    print("      → Consultar facturación mensual en panel de datos")
    print("   🔐 Administrador:")
    print("      → Crear nuevos usuarios con rol y datos personalizados")
    print("      → Dar de baja usuarios del sistema con confirmación")
    print("")
    print("════════════════════════════════════════════════════")
    print("")
    esperar_enter()
    limpiar_consola()