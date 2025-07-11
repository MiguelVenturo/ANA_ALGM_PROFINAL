def corte_varilla_dp_optimizado(longitud, precios):
    """
    EF-ANALISI Y PROG
    CalculaR el beneficio máximo y la lista de cortes óptimos para una varilla dada.
    
    Parámetros:
        longitud (int): Longitud total de la varilla.
        precios (list): Lista de precios por cada posible corte (1 hasta longitud).
    
    Retorna:
        tuple: Beneficio máximo y lista de cortes a realizar.
    """
    dp = [0] * (longitud + 1)
    cortes = [0] * (longitud + 1)  # Para reconstruir la solución
    
    for i in range(1, longitud + 1):
        max_val = -1
        mejor_corte = 0
        for j in range(1, i + 1):
            valor = precios[j - 1] + dp[i - j]
            if valor > max_val:
                max_val = valor
                mejor_corte = j
        dp[i] = max_val
        cortes[i] = mejor_corte
    
    # Reconstrucción de la solución
    solucion = []
    n = longitud
    while n > 0:
        solucion.append(cortes[n])
        n -= cortes[n]
    
    return dp[longitud], solucion


if __name__ == "__main__":
    print("=== PROBLEMA DE CORTE DE VARILLA ===")
    
    # Ingreso de datos
    longitud = int(input("Ingrese la longitud total de la varilla: "))
    print(f"Ingrese los precios para cada longitud de 1 hasta {longitud}:")
    
    precios = []
    for i in range(1, longitud + 1):
        precio = int(input(f"Precio para longitud {i}: "))
        precios.append(precio)
    
    # Cálculo usando DP optimizado
    beneficio, cortes = corte_varilla_dp_optimizado(longitud, precios)
    
    # Mostrar resultados
    print("\n=== RESULTADOS ===")
    print(f"Beneficio máximo: {beneficio}")
    print(f"Cortes a realizar: {cortes}")
    print(f"Suma de cortes: {sum(cortes)}")