from interaccion import procesar_mensaje_usuario

if __name__ == "__main__":
    mensaje_usuario = "Me apareció el error 10010 al intentar enviar la factura. ¿Qué significa?"
    respuesta = procesar_mensaje_usuario(mensaje_usuario)
    print("💬 Respuesta del asistente:")
    print(respuesta)