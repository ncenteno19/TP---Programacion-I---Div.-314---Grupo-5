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

def ver_datos_cliente(vector: dict, mensaje_error: str = "❌ Verificar datos. Saldo negativo") -> None:

    if vector["saldo"] < 0:
        print(mensaje_error)
    else:
        limpiar_consola()
        print("══════════ 📋 DATOS DEL CLIENTE 📋 ══════════")
        print(f"💰 Saldo actual     : ${vector['saldo']:.2f}")
        print(f"👤 Nombre           : {vector['nombre']}")
        print(f"👤 Apellido         : {vector['apellido']}")
        print(f"📧 Mail             : {vector['mail']}")
        print(f"🪪 DNI               : {vector['dni']}")
        print(f"🎂 Edad             : {vector['edad']} años")
        print(f"📅 Año de alta      : {vector['año_alta']}")
        print(f"🔐 Token de sesión  : {random.randint(100000, 999999)}")

        print("════════════════════════════════════════════")

        print("")
        esperar_enter()
        limpiar_consola()

def ver_datos_empresa(vector: dict, mensaje_error: str = "❌ Verificar datos. Saldo negativo") -> None:
        
    if vector["saldo"] < 0:
        print(mensaje_error)
    else:
        limpiar_consola()
        print("══════════ 🏢 DATOS DE LA EMPRESA 🏢 ══════════")

        print(f"💰 Saldo actual        : ${vector['saldo']:.2f}")
        print(f"🏢 Razón social        : {vector['razon_social']}")
        print(f"🧾 CUIT                : {vector['cuit']}")
        print(f"📧 Mail                : {vector['mail']}")
        print(f"👥 Empleados           : {vector['empleados']}")
        print(f"📈 Facturación mensual : ${vector['capital']:.2f}")

        print("════════════════════════════════════════════")

        print("")
        esperar_enter()
        limpiar_consola()


def ver_inicio_transferencia(vector: dict, titulo: str) -> None:
    limpiar_consola()
    print(f"══════════ 💸 {titulo} 💸 ══════════")
    print(f"💰 Saldo actual     : ${vector['saldo']:.2f}")
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

def ver_inicio_carga(vector: dict, titulo: str) -> None:
    limpiar_consola()
    
    print(f"═════════ 💳 {titulo} 💳 ═════════")
    print(f"💰 Saldo actual     : ${vector['saldo']:.2f}")
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

# Prints de los usuarios añadidos como administrador

def ver_resumen_nuevo_usuario(vector: dict) -> None:
    limpiar_consola()
    print("══════════ 📋 RESUMEN DEL NUEVO USUARIO 📋 ══════════\n")

    if vector["tipo"] == "Cliente":
        print(f"👤 Tipo             : {vector['tipo']}")
        print(f"🔑 Usuario          : {vector['usuario']}")
        print(f"👤 Nombre           : {vector['nombre']}")
        print(f"👤 Apellido         : {vector['apellido']}")
        print(f"📧 Mail             : {vector['mail']}")
        print(f"🪪 DNI              : {vector['dni']}")
        print(f"🎂 Edad             : {vector['edad']} años")
        print(f"📅 Año de alta      : {vector['año_alta']}")
        print(f"🏷️  Alias            : {vector['alias']}")
        print(f"🏦 CBU              : {vector['cbu']}")
        print(f"💰 Saldo inicial    : ${vector['saldo']:.2f}")
    else:
        print(f"🏢 Tipo             : {vector['tipo']}")
        print(f"🔑 Usuario          : {vector['usuario']}")
        print(f"🏢 Razón social     : {vector['razon_social']}")
        print(f"🧾 CUIT             : {vector['cuit']}")
        print(f"📧 Mail             : {vector['mail']}")
        print(f"👥 Empleados        : {vector['empleados']}")
        print(f"📈 Facturación      : ${vector['capital']:.2f}")
        print(f"🏷️  Alias            : {vector['alias']}")
        print(f"🏦 CBU              : {vector['cbu']}")
        print(f"💰 Saldo inicial    : ${vector['saldo']:.2f}")

    print("\n════════════════════════════════════════════════════")

    esperar_enter()
    limpiar_consola()

def ver_informacion_del_sistema() -> str:
    limpiar_consola()
    
    print("══════════ 🖥️  INFORMACIÓN DEL SISTEMA 🖥️  ══════════\n")
    print("--------------------------------------------")
    print("╔══════════════════════════════════════════╗")
    print("║       👥 INTEGRANTES DEL GRUPO           ║")
    print("╠══════════════════════════════════════════╣")
    print("║      • Centeno, Nicolás Alejandro        ║")
    print("║      • Drago, Franco Nicolás             ║")
    print("║      • Ruecco, Agustín Nicolás           ║")
    print("╚══════════════════════════════════════════╝")
    print("--------------------------------------------")
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