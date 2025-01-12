# 📚 Asistente Virtual por Voz 🤖🎤

Este proyecto implementa un asistente personal controlado por voz utilizando 🐍 Python. Permite realizar tareas como abrir aplicaciones 🖥️, obtener información de Wikipedia 📚, reproducir música en YouTube 🎶, entre otras.

---

## ✅ Requisitos Previos

Asegúrese de tener instalados los siguientes componentes antes de ejecutar el programa:

### 🐍 Python:
- **Python 3.7 o superior**

### 📦 Librerías Python:
- `pyttsx3`: Convertir texto en voz 🗣️.
- `speech_recognition`: Reconocer comandos de voz 🎧.
- `pywhatkit`: Realizar búsquedas en internet 🌐, reproducir videos 🎥, etc.
- `wikipedia`: Obtener información de Wikipedia 📖.
- `webbrowser`: Abrir enlaces en el navegador 🌍.
- `requests`: Para hacer solicitudes a aplicaciones web 🌍.

Instale las dependencias con el siguiente comando:
```bash
pip install pyttsx3 SpeechRecognition pywhatkit wikipedia
```

✨ Funcionalidades
El asistente reconoce comandos de voz 🎙️ y puede realizar las siguientes tareas:

🖥️🌐 Abrir aplicaciones y sitios web:
"Abrir YouTube" 📺
"Abrir el navegador" 🌍

📅⏰ Informar fecha y hora:
"¿Qué día es hoy?"
"¿Qué horas son?"

🔍 Buscar información:
"Busca en Wikipedia [tema]" 📖
"Busca en internet [término]" 🌐

🎥🎶 Reproducir videos en YouTube:
"Reproduce [nombre del video]"

📸 Captura de pantalla:
"Captura de pantalla"

💬 Abrir WhatsApp Web:
"Abrir WhatsApp"

❌ Cerrar el asistente:
"Adiós"

▶️ Uso
Ejecute los siguientes comandos en su terminal:
```bash
>> pip install pyttsx3 SpeechRecognition pywhatkit wikipedia
>> cd proyecto_asistente
>> python asistente_virtual.py
```

▶ OJO!! Sí quieres usar la funcionalidad de ver el clima debes realizar un paso importante,
debes incluir tu API KEY, en la linea del codigo 100 del archivo (./asistente_virtual.py).

>> Si quieres saber tu API KEY ingresa a https://home.openweathermap.org/,
Luego debes registrarte y acceder a la seccion de API keys, luego copias la clave y la pegas en la seccion
donde indica (api_key = "TU_API_KEY_AQUÍ" ) en la linea 100.

📝 Notas
Asegúrese de tener un micrófono funcional 🎤.
Verifique que su sistema tenga acceso a internet 🌐 para búsquedas en Wikipedia 📚 o reproducción de videos en YouTube 🎥.
El idioma para la búsqueda en Google está configurado como es-pa. Puede cambiarlo según sus necesidades.

🚀 Mejoras Futuras
🌍 Agregar soporte para otros idiomas.
📆 Integración con servicios adicionales (calendarios, correos, etc.).
🎧 Mejorar la precisión en el reconocimiento de voz.

🤝 Contributions
¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar este proyecto, no dudes en abrir una solicitud de extracción o crear un issue en el repositorio.

¡Gracias por tu interés en este proyecto! 😊

## 📜 Licencia
Este proyecto está bajo la licencia MIT. Para más detalles, consulta el archivo [LICENSE](./LICENSE).
