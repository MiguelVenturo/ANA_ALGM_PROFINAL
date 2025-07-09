def corte_varilla_dp(longitud, precios):
    """
    Resuelve el problema de corte de varillas usando programación dinámica.
    Utiliza programación dinámica bottom-up para evitar recálculos.
    
    Args:
        longitud: Longitud de la varilla
        precios: Lista de precios para cada longitud [1, 2, ..., n]
    
    Returns:
        Beneficio máximo obtenible
    """
    # Tabla DP donde dp[i] = beneficio máximo para longitud i
    dp = [0] * (longitud + 1)
    
    # Llenar la tabla de abajo hacia arriba
    for i in range(1, longitud + 1):
        max_val = -1
        for j in range(1, i + 1):
            max_val = max(max_val, precios[j-1] + dp[i-j])
        dp[i] = max_val
    
    return dp[longitud]

def corte_varilla_dp_con_solucion(longitud, precios):
    """
    Versión que también retorna los cortes realizados.
    """
    # Tabla DP
    dp = [0] * (longitud + 1)
    
    # Llenar la tabla DP
    for i in range(1, longitud + 1):
        max_val = -1
        for j in range(1, i + 1):
            max_val = max(max_val, precios[j-1] + dp[i-j])
        dp[i] = max_val
    
    # Reconstruir la solución
    cortes = []
    n = longitud
    while n > 0:
        for i in range(1, n + 1):
            if precios[i-1] + dp[n-i] == dp[n]:
                cortes.append(i)
                n = n - i
                break
    
    return dp[longitud], cortes

def corte_varilla_dp_optimizado(longitud, precios):
    """
    Versión optimizada con análisis de complejidad mejorado.
    """
    dp = [0] * (longitud + 1)
    cortes = [0] * (longitud + 1)  # Para reconstruir la solución
    
    for i in range(1, longitud + 1):
        max_val = -1
        mejor_corte = 0
        
        for j in range(1, i + 1):
            valor = precios[j-1] + dp[i-j]
            if valor > max_val:
                max_val = valor
                mejor_corte = j
        
        dp[i] = max_val
        cortes[i] = mejor_corte
    
    # Reconstruir solución usando la tabla de cortes
    solucion = []
    n = longitud
    while n > 0:
        solucion.append(cortes[n])
        n = n - cortes[n]
    
    return dp[longitud], solucion

# Ejemplo de uso y comparación
if __name__ == "__main__":
    # Datos de prueba
    precios = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    longitud = 10
    
    print("=== ALGORITMO DE PROGRAMACIÓN DINÁMICA ===")
    beneficio_max = corte_varilla_dp(longitud, precios)
    
    print(f"Longitud de la varilla: {longitud}")
    print(f"Precios: {precios}")
    print(f"Beneficio máximo: {beneficio_max}")
    
    # Versión con solución detallada
    beneficio, cortes = corte_varilla_dp_con_solucion(longitud, precios)
    
    print(f"Cortes realizados: {cortes}")
    print(f"Suma de cortes: {sum(cortes)}")
    
    # Versión optimizada
    print("\n=== VERSIÓN OPTIMIZADA ===")
    beneficio_opt, solucion_opt = corte_varilla_dp_optimizado(longitud, precios)
    print(f"Beneficio máximo (optimizado): {beneficio_opt}")
    print(f"Solución optimizada: {solucion_opt}")