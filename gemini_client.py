import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")  # o "gemini-pro" si tenés acceso

response = model.generate_content("¿Qué es Fast Prompting?")
print(response.text)