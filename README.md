# 🧠 Asistente Inteligente para Interpretación de Errores Fiscales

Este proyecto implementa un asistente inteligente que interpreta errores fiscales frecuentes en sistemas ERP, generando respuestas claras y empáticas para el usuario final. Utiliza Gemini API para generar explicaciones dinámicas basadas en prompts contextuales.

---

## 🚀 Objetivo

Diseñar un prototipo funcional que:
- Reciba un código o descripción de error fiscal
- Genere un prompt dinámico y efectivo
- Obtenga una respuesta explicativa desde Gemini
- Brinde asistencia inmediata al usuario

---

## 🛠️ Tecnologías utilizadas

- Python 3.11
- Gemini API (via `google.generativeai`)
- VSCode + entorno virtual (`venv`)
- Manejo de `.env` para proteger credenciales
- Estructura modular por archivos

---

## 📁 Estructura del proyecto

- main.py (script ptincipal para pruebas y simulaciones)
- interaccion.py (lógica de procesamiento del mensaje del usuario)
- errores.py (base de datos de errores frecuentes, códigos, descripciones y organismos)
- gemini_client.py (cliente para interactuar con Gemini API)
- .env (API Key protegida)
- README.md (Documentación del proyecto)


---

## 🔒 Buenas prácticas de repositorio
Se implementó un archivo .gitignore para mantener el repositorio limpio y seguro. Este archivo excluye:
- Entornos virtuales (venv/)
- Credenciales y configuraciones (.env, *.ini, *.cfg)
- Archivos compilados de Python (__pycache__/, *.pyc)
- Logs y archivos temporales (*.log, *.tmp)
- Configuraciones locales de VSCode (.vscode/)
- Archivos de sistema (.DS_Store, Thumbs.db)
Esto garantiza que el repositorio sea portable, seguro y profesional, facilitando su mantenimiento y colaboración.

---

## ⚙️ Instalación

1. Clonar el repositorio
2. Crear entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
3. Instalar dependencias:
   -- pip install -r requirements.txt
4. Crear archivo .env con API Key:
   -- GEMINI_API_KEY=tu_clave_aqui


## 🧪 Ejemplo de uso

# Mensaje del usuario
Me apareció el error 10010 al intentar enviar la factura. ¿Qué significa?

# Respuesta generada
Gracias por tu consulta. El error 10010 indica que el CUIT ingresado para el receptor de la factura no es válido según los registros de AFIP. Esto puede deberse a un error de tipeo, un CUIT inexistente o inhabilitado para operar.

Te sugerimos verificar que el número de CUIT esté correctamente ingresado y que corresponda a una persona o empresa habilitada. Si el dato es correcto y el error persiste, podés consultar el estado del CUIT en la web de AFIP o contactar a tu área administrativa para confirmar la información.

## 🧠 Lógica del flujo

1. El usuario escribe un mensaje con un código de error.
2. interacción.py detecta el código y busca su descripción en errores.py
3. Se genera un prompt contextual para Gemini.
4. gemini_client.py envía el prompt y recibe la respuesta.
5. Se devuelve una explicación clara y profesional al usuario.

## 📌 Personalización

Es posible adaptarlo fácilmente:
- El estilo de respuesta (más tecnico, informal, visual)
- La base de errores (errores.py)
- El motor de IA (si se desean probar otros modelos)

## 🧪 Pruebas sugeridas

. Mensajes con errores conocidos (10010, 20005, etc.)
.Mensajes sin código (validar respuesta de fallback)
. Mensajes con múltiples códigos (extender lógica si se desea)

## 📈 Escalabilidad

Este proyecto puede evolucionar hacia:
- API REST para integración con frontend ERP
- Interfaz web para testing de errores
- Asistente embebido en sistemas administrativos

## ✍️ Reflexión final

Este prototipo demuestra cómo el diseño de prompts efectivos puede mejorar la experiencia del usuario en entornos fiscales complejos. La modularidad del código permite escalar el asistente a otros dominios (ERP, soporte técnico, contabilidad) y su integración con Gemini abre posibilidades para respuestas cada vez más precisas y empáticas.

