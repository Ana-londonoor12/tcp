from Procesador_dato import DatosMeteorologicos

archivo_ejemplo = "datos.txt"
datos = DatosMeteorologicos(archivo_ejemplo)
promedio_temp, promedio_hum, promedio_pres, promedio_vel_viento, direccion_predominante = datos.procesar_datos()

print("Temperatura promedio:", promedio_temp)
print("Humedad promedio:", promedio_hum)
print("Presión promedio:", promedio_pres)
print("Velocidad promedio del viento:", promedio_vel_viento)
print("Dirección predominante del viento:", direccion_predominante)