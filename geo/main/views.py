from django.shortcuts import render
import socket
import geocoder
import folium

def get_device_info():
    device_name = socket.gethostname()
    ip_address = geocoder.ip('me').ip
    location = geocoder.ip(ip_address)
    latitude, longitude = location.latlng

    return {
        'device_name': device_name,
        'latitude': latitude,
        'longitude': longitude,
    }

def location(request):
    
    device_info = get_device_info()

  
    my_map = folium.Map(location=[device_info['latitude'], device_info['longitude']], zoom_start=10)


    folium.Marker(location=[device_info['latitude'], device_info['longitude']],
                  popup=f"Device Name: {device_info['device_name']}").add_to(my_map)

    map_html_path = 'device_map.html'
    my_map.save(map_html_path)


    context = {
        'device_name': device_info['device_name'],
        'latitude': device_info['latitude'],
        'longitude': device_info['longitude'],
        'map_html_path': map_html_path,
    }


    return render(request, 'main/index.html', context)
