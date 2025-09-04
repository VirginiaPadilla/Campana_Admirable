import folium
import webbrowser

m = folium.Map(location=[10.48801, -66.87919],zoom_start=7)

#Localizar punto en el mapa  
#Definir un grupo de características 
grupo = folium.map.FeatureGroup()

#Ubicar un punto según su longitud y latitud
grupo.add_child(folium.features.CircleMarker([9.9656988, -68.2240014],radius = 5, color="blue", fill_color = "Red"))

#Añadir el punto en el mapa
m.add_child(grupo)#Añadir marcador y un texto al hacer click en este

folium.Marker([9.9656988, -68.2240014], popup="Taguanes").add_to(m)

##  Agua de Obispos
#Ubicar un punto según su longitud y latitud
grupo.add_child(folium.features.CircleMarker([9.704,-70.107],radius = 5, color="blue", fill_color = "Red"))

#Añadir el punto en el mapa
m.add_child(grupo)#Añadir marcador y un texto al hacer click en este

folium.Marker([9.704,-70.107], popup="Agua de Obispos").add_to(m)

##  Niquitao
#Ubicar un punto según su longitud y latitud
grupo.add_child(folium.features.CircleMarker([9.118333,-70.492778],radius = 5, color="blue", fill_color = "Red"))

#Añadir el punto en el mapa
m.add_child(grupo)#Añadir marcador y un texto al hacer click en este

folium.Marker([9.118333,-70.492778], popup="Niquitao").add_to(m)

##  Horcones
#Ubicar un punto según su longitud y latitud
grupo.add_child(folium.features.CircleMarker([10.012222222222, -69.450833333333],radius = 5, color="blue", fill_color = "Red"))

#Añadir el punto en el mapa
m.add_child(grupo)#Añadir marcador y un texto al hacer click en este

folium.Marker([10.012222222222, -69.450833333333], popup="Horcones").add_to(m)


##  Cucuta
#Ubicar un punto según su longitud y latitud
grupo.add_child(folium.features.CircleMarker([7.9075, -72.504722222222],radius = 5, color="blue", fill_color = "Red"))

#Añadir el punto en el mapa
m.add_child(grupo)#Añadir marcador y un texto al hacer click en este

folium.Marker([7.9075, -72.504722222222], popup="Cucuta").add_to(m)



m.save("batalla.html")
webbrowser.open("batalla.html")


 
