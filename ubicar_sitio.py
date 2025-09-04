import folium
from geopy.geocoders import Nominatim
import sys
import webbrowser


def obtener_coordenadas(poblacion):
    """Obtiene las coordenadas de una población usando Nominatim (OpenStreetMap)"""
    geolocalizador = Nominatim(user_agent="mapa_poblacion")
    ubicacion = geolocalizador.geocode(poblacion)
    
    if ubicacion:
        return ubicacion.latitude, ubicacion.longitude
    else:
        raise ValueError(f"No se encontró la población: {poblacion}")

def crear_mapa(poblacion, latitud, longitud):
    """Crea un mapa de Folium con un marcador en la ubicación especificada"""
    # Crear mapa centrado en las coordenadas
    mapa = folium.Map(location=[latitud, longitud], zoom_start=12)
    
    # Añadir marcador
    folium.Marker(
        location=[latitud, longitud],
        popup=f"<b>{poblacion}</b>",
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(mapa)
    
    # Guardar mapa como HTML
    nombre_archivo = f"{poblacion.replace(' ', '_')}_mapa.html"
    mapa.save(nombre_archivo)
    webbrowser.open(nombre_archivo)
    return nombre_archivo

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python mapa_poblacion.py <nombre_poblacion>")
        sys.exit(1)
    
    poblacion = sys.argv[1]
    
    try:
        # Obtener coordenadas
        lat, lon = obtener_coordenadas(poblacion)
        print(f"Coordenadas encontradas: Latitud {lat}, Longitud {lon}")
        
        # Crear mapa
        archivo_html = crear_mapa(poblacion, lat, lon)
        print(f"Mapa generado: {archivo_html}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)