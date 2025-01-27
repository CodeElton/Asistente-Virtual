# Asistente Virtual por Voz

Este proyecto implementa un asistente personal controlado por voz utilizando 🐍 Python. Permite realizar tareas como abrir aplicaciones 🖥️, obtener información de Wikipedia 📚, reproducir música en YouTube 🎶, entre otras.

---

## ✅ Requisitos Previos

### 🐍 Python:
- Python 3.7 o superior.

### 📦 Librerías Python:
Asegúrese de instalar las siguientes dependencias antes de ejecutar el programa:

- `pyttsx3`: Convertir texto en voz 🗣️.
- `SpeechRecognition`: Reconocer comandos de voz 🎧.
- `pywhatkit`: Realizar búsquedas en internet 🌐, reproducir videos 🎥, etc.
- `wikipedia`: Obtener información de Wikipedia 📖.
- `webbrowser`: Abrir enlaces en el navegador 🌍.
- `requests`: Realizar solicitudes a aplicaciones web 🌍.

Instale todas las dependencias ejecutando el siguiente comando:

```bash
pip install -r requirements.txt
```

---

## ✨ Funcionalidades

El asistente reconoce comandos de voz 🎙️ y puede realizar las siguientes tareas:

### 🖥️🌐 Abrir aplicaciones y sitios web:
- **Ejemplo:**
  - "Abrir YouTube" 📺
  - "Abrir el navegador" 🌍

### 📅⏰ Informar fecha y hora:
- **Ejemplo:**
  - "¿Qué día es hoy?"
  - "¿Qué horas es?"

### 🔍 Buscar información:
- **Ejemplo:**
  - "Busca en Wikipedia [tema]" 📖
  - "Busca en internet [término]" 🌐

### 🎥🎶 Reproducir videos en YouTube:
- **Ejemplo:**
  - "Reproduce [nombre del video]"

### 💬 Abrir WhatsApp Web:
- **Ejemplo:**
  - "Abrir WhatsApp"

### ❌ Cerrar el asistente:
- **Ejemplo:**
  - "Adiós"

---

## ▶️ Uso

Ejecute los siguientes comandos en su terminal:

```bash
pip install -r requirements.txt
cd proyecto_asistente
python asistente_virtual.py
```

> **Nota:** Si desea utilizar la funcionalidad de consulta del clima, debe configurar su API KEY. Edite la línea 100 del archivo `asistente_virtual.py` e introduzca su clave API:

```python
api_key = "TU_API_KEY_AQUÍ"
```

Para obtener su API KEY:
1. Ingrese a [OpenWeatherMap](https://home.openweathermap.org/).
2. Regístrese y acceda a la sección "API keys".
3. Copie la clave y péguela en la sección indicada del código.

---

## 📝 Notas

- Asegúrese de tener un micrófono funcional 🎤.
- Verifique que su sistema tenga acceso a internet 🌐 para búsquedas en Wikipedia 📚 o reproducción de videos en YouTube 🎥.
- El idioma para la búsqueda en Google está configurado como `es-pa`. Puede modificarlo según sus necesidades.

---

## 🚀 Mejoras Futuras

- 🌍 Agregar soporte para otros idiomas.
- 📆 Integración con servicios adicionales (calendarios, correos, etc.).
- 🎧 Mejorar la precisión en el reconocimiento de voz.

---

## 🤝 Contributions

¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar este proyecto, no dudes en abrir una solicitud de extracción o crear un issue en el repositorio.

---

## 📜 Licencia

Este proyecto está bajo la licencia MIT. Para más detalles, consulta el archivo `LICENSE`.****
