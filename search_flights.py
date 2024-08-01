def buscar_vuelos(origen, destino, fecha_salida, fecha_regreso):
    # Simulación de búsqueda de vuelos
    vuelos = [
        {"origen": "SCL", "destino": "JFK", "fecha_salida": "2024-08-01", 
"precio": 500},
        {"origen": "SCL", "destino": "JFK", "fecha_salida": "2024-08-01", 
"precio": 550}
    ]
    resultados = [vuelo for vuelo in vuelos if vuelo["origen"] == origen 
and vuelo["destino"] == destino and vuelo["fecha_salida"] == fecha_salida]
    return resultados

# Ejemplo de uso
if __name__ == "__main__":
    vuelos_encontrados = buscar_vuelos("SCL", "JFK", "2024-08-01", None)
    print(vuelos_encontrados)
