import folium
import webbrowser

# Create a map centered at New York City
m = folium.Map(location=[+8.92416, -67.42929], zoom_start=7)

# Add OpenStreetMap layer (Default Street View)
folium.TileLayer('OpenStreetMap', name='OpenStreetMap').add_to(m)

# Add CartoDB Positron (Light Street View)
#folium.TileLayer(
#    tiles='https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png',
#    attr='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a #href="https://carto.com/attributions">CARTO</a>',
#    name='CartoDB Positron'
#).add_to(m)

# Add Terrain layer (using OpenTopoMap as an alternative)
folium.TileLayer(
    tiles='https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png',
    attr='Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)',
    name='Terrain (OpenTopoMap)'
).add_to(m)

# Add Satellite layer
folium.TileLayer(
    tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
    attr='Esri',
    name='Satellite'
).add_to(m)

# Add Hybrid layer (Satellite with labels)
folium.TileLayer(
    tiles='https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}',
    attr='Google',
    name='Google Hybrid'
).add_to(m)
 
####################################
#####   # Cucuta, San Cristobal , Tovar, Niquitao, Barinas, San Carlos, Tinaquillo, Valencia, Maracay, Caracas
####
locations = [
    [
        (7.89391, -72.50782),   (7.76694, -72.225), ],
    [
        (7.76694, -72.225), (8.33015, -71.75277),  ],
    [
        (8.33015, -71.75277), (9.1130556, -70.4008333),    ],
 [ 
         (9.1130556, -70.4008333), (8.62261, -70.20749),    ],
    [
         (8.62261, -70.20749), (9.66415, -68.58659),     ],
    [
        (9.66415, -68.58659), (9.91861, -68.30472),      ], 
    [
         (9.91861, -68.30472), (10.16202, -68.00765),    ],
    [
         (10.16202, -68.00765), (10.23535, -67.59113),    ],
    [
       (10.23535, -67.59113), (10.48801, -66.87919) 
    ],
   
]
 
  
######
folium.PolyLine(
    locations=locations,
    color="red",
    weight=3,
    opacity=1,
    smooth_factor=80,
).add_to(m)
##########################################################
#####   # Niquitao, Horcones, Barquisimeto, San Carlos 
####          10.0647, -69.35703    10.0122, -69.4508
locations = [
    [
        (9.1130556, -70.4008333), (10.0122, -69.4508), ],
    [
        (10.0122, -69.4508), (10.0647, -69.35703), ],
    [
    (10.0647, -69.35703),  (9.66124, -68.58268), ],
     
]
########### 
folium.PolyLine(
    locations=locations,
    color="blue",
    weight=2,
    opacity=1,
    smooth_factor=80,
).add_to(m)
###########################
#####   #   Barinas, Mucurita
####
locations = [
     
    [
          (8.62261, -70.20749),
    (7.83333,  -68.8)
    ],
   
]
########### 
folium.PolyLine(
    locations=locations,
    color="yellow",
    weight=2,
    opacity=1,
    smooth_factor=80,
).add_to(m)
 
###############################
# Save the map
m.save("map_with_route_lay.html")

# Automatically open the map in the default web browser
webbrowser.open("map_with_route_lay.html")