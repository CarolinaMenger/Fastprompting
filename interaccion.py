from gemini_client import generar_respuesta
from errores import errores_frecuentes
import re

def procesar_mensaje_usuario(mensaje: str) -> str:
    # Buscar código de error en el mensaje (ej: "error 10010")
    coincidencias = re.findall(r"\b\d{5}\b", mensaje)
    if not coincidencias:
        return "No se detectó ningún código de error en el mensaje del usuario."

    codigo = coincidencias[0]
    error = next((e for e in errores_frecuentes if e["codigo"] == codigo), None)
    if not error:
        return f"Se detectó el código {codigo}, pero no está definido en la lista de errores frecuentes."

    # Generar prompt para Gemini
    prompt = (
        f"Un usuario del ERP escribió: '{mensaje}'. Este mensaje incluye el error '{codigo}', "
        f"que corresponde a: '{error['descripcion']}' según el organismo '{error['organismo']}'. "
        f"Generá una respuesta clara, profesional y empática que le explique al usuario qué significa este error "
        f"y qué pasos puede seguir para resolverlo."
    )

    # Obtener respuesta del asistente
    respuesta = generar_respuesta(prompt)
    return respuesta