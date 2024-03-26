# Codigo para verisar el nivel de la bateria

import psutil

battery = psutil.sensors_battery()

percent = battery.percent
charging = battery.power_plugged
    
if charging:
    print(f"Batería: {percent}% (Cargando)")
else:
    print(f"Batería: {percent}% (No está cargando)")

