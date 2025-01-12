import pyttsx3
import speech_recognition as sr
import pywhatkit
import webbrowser
import datetime
import wikipedia
import requests


# escuchar microfono y devolver el audio como texto
def transformar_audio_en_texto():

  # almacenar recognizer en variable
  r = sr.Recognizer()

  # configurar el microfono
  with sr.Microphone() as origen:

    # tiempo de espera
    r.pause_threshold = 0.8

    # informar que comenzo la grabacion
    print("Ya puedes comenzar a hablar!!🎙")

    # guardar lo que escuche como audio
    audio = r.listen(origen)

    try:
      # buscar en google
      pedido = r.recognize_google(audio, language="es-pa")

      # prueba de que pudo ingresar
      print("Has dicho: " + pedido)
      return pedido
    
    except sr.UnknownValueError:
      print("Ups, no entendi")
      return "Sigo esperando"
    
    except sr.RequestError:
      print("Ups, no hay servicio")
      return "Sigo esperando"
    
    except:
      print("Ups, algo ha salido mal")
      return "Sigo esperando"


# funcion para que el asistente pueda ser escuchado
def hablar(mensaje):

  # encender el motor de pyttsx3
  engine = pyttsx3.init()
  
  # pronunciar mensaje
  engine.say(mensaje)

  # correr y esperar
  engine.runAndWait()


# informar el dia de la semana
def pedir_dia():

  # crear variable con datos de hoy
  dia = datetime.date.today()
  print(dia)

  # crear variable para el dia de semana
  dia_semana = dia.weekday()
  print(dia_semana)

  # diccionario con nombre de dias
  calendario = {
    0 : 'Lunes',
    1 : 'Martes',
    2 : 'Miércoles',
    3 : 'Jueves',
    4 : 'Viernes',
    5 : 'Sábado',
    6 : 'Domingo'}

  # decir el dia de la semana
  hablar(f'Hoy es {calendario[dia_semana]}')
 

# informar que hora es
def pedir_hora():
  
  # crear una variable con datos de la hora
  hora = datetime.datetime.now()
  hora = f'En este momento son las {hora.hour} y {hora.minute} '

  # decir la hora
  hablar(hora)


def obtener_clima(ciudad):
    # Tu API Key de OpenWeatherMap
    api_key = "TU_API_KEY_AQUÍ"
    
    # URL base de la API
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&lang=es&units=metric"
    
    try:
        # Hacer la solicitud a la API
        respuesta = requests.get(url)
        datos = respuesta.json()
        
        if datos["cod"] == 200:
            # Extraer información del clima
            descripcion = datos["weather"][0]["description"]
            temperatura = datos["main"]["temp"]
            humedad = datos["main"]["humidity"]
            return f"En {ciudad} el clima es {descripcion}, con una temperatura de {temperatura}°C y una humedad del {humedad}%."
        else:
            return f"No pude encontrar información del clima para {ciudad}. ¿Podrías verificar el nombre de la ciudad?"
    except Exception as e:
        return "Hubo un error al obtener el clima. Por favor, intenta nuevamente más tarde."


# funcion saludo inicial
def saludo_inicial():

  # crear variable con datos de hora
  hora = datetime.datetime.now()
  if hora.hour < 6 or hora.hour > 20:
    momento = 'Buenas noches'
  elif 6 <= hora.hour < 13:
    momento = 'Buen día'
  else:
    momento = 'Buenas tardes'
  
  # decir el saludo
  hablar(f'{momento}, Soy Yelena, tu asistente personal. Por favor, dime en que te puedo ayudar')


# funcion central del asistente
def pedir_cosas():

  # activar saludo inicial
  saludo_inicial()
  comenzar = True

  while comenzar:
    # activar el micro y guardar el pedido en un string
    pedido = transformar_audio_en_texto().lower()

    # Funcionalidades
    if 'abrir youtube' in pedido:
      hablar('Con gusto, Estoy abriendo youtube')
      webbrowser.open('https://www.youtube.com/')
      continue

    elif 'abrir el navegador' in pedido:
      hablar("Abriendo el navegador")
      webbrowser.open('https://www.google.com')
      continue

    elif 'qué día es hoy' in pedido:
      pedir_dia()
      continue

    elif 'qué hora es' in pedido:
      pedir_hora()
      continue

    elif 'clima' in pedido:
      hablar('¿Para qué ciudad quieres conocer el clima?')
      ciudad = transformar_audio_en_texto().lower()
      clima = obtener_clima(ciudad)
      hablar(clima)
      continue

    elif 'buscar en wikipedia' in pedido:
      hablar('Buscando eso en wikipedia')
      pedido = pedido.replace('wikipedia', '')
      wikipedia.set_lang('es')
      resultado = wikipedia.summary(pedido, sentences=1)
      hablar('Wikipedia dice lo siguiente:')
      hablar(resultado)
      continue

    elif 'buscar en internet' in pedido:
      hablar(f"Buscando en internet sobre {pedido}")
      pedido = pedido.replace('busca en internet', '')
      pywhatkit.search(pedido)
      hablar('Esto es lo que he encontrado')
      continue

    elif 'reproduce' in pedido:
      hablar('Buena idea, ya comienzo a reproducirlo')
      pywhatkit.playonyt(pedido)
      continue

    elif 'captura de pantalla' in pedido:
      hablar("Realizando una captura de la pantalla")
      pywhatkit.take_screenshot(file_name="captura_pantalla", delay= 2)
      continue

    elif 'abrir whatsapp' in pedido:
      hablar("Abriendo Whatsapp")
      pywhatkit.open_web()
      continue
    
    elif 'adiós' in pedido:
      hablar("Me voy a descansar, cualquier cosa me avisas")
      break


pedir_cosas()