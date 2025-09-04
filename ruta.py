import folium
from geopy.geocoders import Nominatim
import requests
import sys
import webbrowser

def obtener_coordenadas(poblacion):
    """Obtiene las coordenadas de una población usando Nominatim"""
    geolocalizador = Nominatim(user_agent="ruta_poblaciones")
    ubicacion = geolocalizador.geocode(poblacion)
    
    if ubicacion:
        return ubicacion.latitude, ubicacion.longitude
    else:
        raise ValueError(f"No se encontró la población: {poblacion}")

def obtener_ruta(punto_inicio, punto_fin):
    """Obtiene la ruta entre dos puntos usando el servicio OSRM"""
    url = f"http://router.project-osrm.org/route/v1/driving/{punto_inicio[1]},{punto_inicio[0]};{punto_fin[1]},{punto_fin[0]}?steps=true&geometries=geojson"
    
    try:
        respuesta = requests.get(url)
        datos = respuesta.json()
        return datos['routes'][0]['geometry']['coordinates']
    except Exception as e:
        raise RuntimeError(f"Error al obtener la ruta: {str(e)}")

def crear_mapa(poblacion1, poblacion2, coords1, coords2, ruta_coords):
    """Crea un mapa con las dos poblaciones y la ruta entre ellas"""
    # Calcular punto medio para centrar el mapa
    lat_media = (coords1[0] + coords2[0]) / 2
    lon_media = (coords1[1] + coords2[1]) / 2
    
    # Crear mapa
    mapa = folium.Map(location=[lat_media, lon_media], zoom_start=8)
    
    # Convertir coordenadas de la ruta al formato [lat, lon]
    ruta_formateada = [[coord[1], coord[0]] for coord in ruta_coords]
    
    # Añadir ruta
    folium.PolyLine(
        locations=ruta_formateada,
        color='blue',
        weight=5,
        opacity=0.7
    ).add_to(mapa)
    
    # Añadir marcadores
    folium.Marker(
        location=coords1,
        popup=f"<b>Origen:</b> {poblacion1}",
        icon=folium.Icon(color='green', icon='flag')
    ).add_to(mapa)
    
    folium.Marker(
        location=coords2,
        popup=f"<b>Destino:</b> {poblacion2}",
        icon=folium.Icon(color='red', icon='flag')
    ).add_to(mapa)
    
    # Guardar mapa
    nombre_archivo = f"Ruta_{poblacion1.replace(' ', '_')}_a_{poblacion2.replace(' ', '_')}.html"
    mapa.save(nombre_archivo)
    webbrowser.open(nombre_archivo)
    return nombre_archivo

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python ruta_poblaciones.py <poblacion_origen> <poblacion_destino>")
        sys.exit(1)
    
    poblacion1 = sys.argv[1]
    poblacion2 = sys.argv[2]
    
    try:
        print(f"Buscando coordenadas de {poblacion1}...")
        coords1 = obtener_coordenadas(poblacion1)
        print(f"Coordenadas encontradas: {coords1}")
        
        print(f"Buscando coordenadas de {poblacion2}...")
        coords2 = obtener_coordenadas(poblacion2)
        print(f"Coordenadas encontradas: {coords2}")
        
        print("Calculando ruta...")
        ruta_coords = obtener_ruta(coords1, coords2)
        print("Ruta obtenida")
        
        print("Generando mapa...")
        archivo_html = crear_mapa(poblacion1, poblacion2, coords1, coords2, ruta_coords)
        print(f"Mapa generado: {archivo_html}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)