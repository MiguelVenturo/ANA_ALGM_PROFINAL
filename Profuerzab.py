def corte_varilla_fuerza_bruta(longitud, precios):
    """
    Resuelve el problema de corte de varillas usando fuerza bruta.
    Explora todas las posibles combinaciones de cortes recursivamente.
    
    Args:
        longitud: Longitud de la varilla
        precios: Lista de precios para cada longitud [1, 2, ..., n]
    
    Returns:
        Beneficio máximo obtenible
    """
    if longitud == 0:
        return 0
    
    max_valor = -1
    
    # Probar todos los posibles primeros cortes
    for i in range(1, longitud + 1):
        valor = precios[i-1] + corte_varilla_fuerza_bruta(longitud - i, precios)
        max_valor = max(max_valor, valor)
    
    return max_valor

def corte_varilla_fuerza_bruta_con_solucion(longitud, precios):
    """
    Versión que también retorna los cortes realizados.
    """
    def resolver(n, cortes_actuales):
        if n == 0:
            return 0, cortes_actuales.copy()
        
        max_valor = -1
        mejor_cortes = []
        
        for i in range(1, n + 1):
            nuevos_cortes = cortes_actuales + [i]
            valor, cortes_resultado = resolver(n - i, nuevos_cortes)
            valor_total = precios[i-1] + valor
            
            if valor_total > max_valor:
                max_valor = valor_total
                mejor_cortes = cortes_resultado
        
        return max_valor, mejor_cortes
    
    return resolver(longitud, [])

# Ejemplo de uso
if __name__ == "__main__":
    # Datos de prueba: precios para longitudes 1, 2, 3, 4, 5
    precios = [1, 5, 8, 9, 10]
    longitud = 5
    
    print("=== ALGORITMO DE FUERZA BRUTA ===")
    beneficio_max = corte_varilla_fuerza_bruta(longitud, precios)
    
    print(f"Longitud de la varilla: {longitud}")
    print(f"Precios: {precios}")
    print(f"Beneficio máximo: {beneficio_max}")
    
    # Versión con solución detallada
    beneficio, cortes = corte_varilla_fuerza_bruta_con_solucion(longitud, precios)
    
    print(f"Cortes realizados: {cortes}")
    print(f"Verificación - Suma de cortes: {sum(cortes)}")