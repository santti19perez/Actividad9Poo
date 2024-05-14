from typing import Tuple

class DatosMeteorologicos:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo
        self.direcciones_viento = {
            "N": 0,
            "NNE": 22.5,
            "NE": 45,
            "ENE": 67.5,
            "E": 90,
            "ESE": 112.5,
            "SE": 135,
            "SSE": 157.5,
            "S": 180,
            "SSW": 202.5,
            "SW": 225,
            "WSW": 247.5,
            "W": 270,
            "WNW": 292.5,
            "NW": 315,
            "NNW": 337.5
        }

    def procesar_datos(self) -> Tuple[float, float, float, float, str]:
        with open(self.nombre_archivo, 'r') as f:
            lineas = f.readlines()

        temperatura_total = 0
        humedad_total = 0
        presion_total = 0
        viento_total = 0
        direcciones_total = 0
        conteo = 0

        for linea in lineas:
            if "Temperatura:" in linea:
                temperatura_total += float(linea.split(":")[1].strip())
            elif "Humedad:" in linea:
                humedad_total += float(linea.split(":")[1].strip())
            elif "Presión:" in linea:
                presion_total += float(linea.split(":")[1].strip())
            elif "Viento:" in linea:
                viento_total += float(linea.split(":")[1].split(",")[0].strip())
                direccion = linea.split(":")[1].split(",")[1].strip()
                direcciones_total += self.direcciones_viento[direccion]
                conteo += 1

        temperatura_promedio = temperatura_total / conteo
        humedad_promedio = humedad_total / conteo
        presion_promedio = presion_total / conteo
        viento_promedio = viento_total / conteo
        direccion_promedio = min(self.direcciones_viento.keys(), key=lambda k: abs(self.direcciones_viento[k] - (direcciones_total / conteo)))

        return temperatura_promedio, humedad_promedio, presion_promedio, viento_promedio, direccion_promedio
