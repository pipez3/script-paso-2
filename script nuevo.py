import requests

def calcular_distancia(ciudad_origen, ciudad_destino):
    api_key = 'tu_api_key_de_Google_Distance_Matrix'
    url = f'https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins={ciudad_origen}&destinations={ciudad_destino}&key={api_key}'
    response = requests.get(url)
    data = response.json()

    distancia = data['rows'][0]['elements'][0]['distance']['value'] / 1000  # Convertir a kilómetros
    duracion = data['rows'][0]['elements'][0]['duration']['value']  # En segundos

    return distancia, duracion

def calcular_combustible(distancia):
    rendimiento = 12  # Kilómetros por litro (ajusta esto según tu vehículo)
    litros = distancia / rendimiento
    return litros

def convertir_tiempo(segundos):
    horas = segundos // 3600
    segundos %= 3600
    minutos = segundos // 60
    segundos %= 60
    return horas, minutos, segundos

# Solicitar ciudades
ciudad_origen = input("Ciudad de Origen: ")
ciudad_destino = input("Ciudad de Destino: ")

# Calcular distancia y duración
distancia, duracion_segundos = calcular_distancia(ciudad_origen, ciudad_destino)
duracion_horas, duracion_minutos, duracion_segundos = convertir_tiempo(duracion_segundos)

# Calcular combustible requerido
combustible = calcular_combustible(distancia)

# Imprimir resultados
print(f"\nDistancia: {distancia:.3f} km")
print(f"Duración del viaje: {duracion_horas} horas, {duracion_minutos} minutos, {duracion_segundos} segundos")
print(f"Combustible requerido: {combustible:.3f} lts")

# Imprimir narrativa del viaje
print("\nNarrativa del viaje:")
print(f"Viajando desde {ciudad_origen} hasta {ciudad_destino}, recorreremos una distancia de {distancia:.3f} km.")
print(f"La duración estimada del viaje es de {duracion_horas} horas, {duracion_minutos} minutos, {duracion_segundos} segundos.")
print(f"Se necesitarán aproximadamente {combustible:.3f} litros de combustible.")

# Agregar salida de letra Q
print("\nQ")
