import folium
import  pandas


data= pandas.read_csv("volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])

def color_producer(elevation):
    if elevation<1000:
       return "green"
    elif 1000 <= elevation  < 3000:
        return "orange"
    else:
        return "red"

map=folium.Map(location=[41 ,-112],zoom_start=6,tiles="Mapbox Bright")

fgv= folium.FeatureGroup(name="volcanoes")

for lt, ln, el in zip(lat, lon, elev):

    fgv.add_child(folium.Marker(location=[lt,ln], popup=str(el)+"m", icon=folium.Icon(color_producer(el))))


fgp= folium.FeatureGroup(name="population")
fgp.add_child(folium.GeoJson(data=open('world.json',encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']<1000000
else 'orange'if 1000000<=x['properties']['POP2005']<20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())

map.save("map.html")


