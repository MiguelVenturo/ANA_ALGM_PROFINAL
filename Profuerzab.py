def corte_varilla_fuerza_bruta_con_solucion(longitud, precios):
    
    def resolver(n, cortes_actuales):
        if n == 0:
            return 0, cortes_actuales.copy()
        
        max_valor = -1
        mejor_cortes = []

        for i in range(1, n + 1):
            nuevos_cortes = cortes_actuales + [i]
            valor, cortes_resultado = resolver(n - i, nuevos_cortes)
            valor_total = precios[i - 1] + valor

            if valor_total > max_valor:
                max_valor = valor_total
                mejor_cortes = cortes_resultado
        
        return max_valor, mejor_cortes

    return resolver(longitud, [])


if __name__ == "__main__":
    print("=== FUERZA BRUTA - CORTE DE VARILLA ===")
    
    # Ingreso de datos
    longitud = int(input("Ingrese la longitud total de la varilla: "))
    print(f"Ingrese los precios para cada longitud de 1 hasta {longitud}:")
    
    precios = []
    for i in range(1, longitud + 1):
        precio = int(input(f"Precio para longitud {i}: "))
        precios.append(precio)
    
    # Calcular solución
    beneficio, cortes = corte_varilla_fuerza_bruta_con_solucion(longitud, precios)

    # Mostrar resultados
    print("\n=== RESULTADOS ===")
    print(f"Beneficio máximo: {beneficio}")
    print(f"Cortes a realizar: {cortes}")