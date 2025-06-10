def calcular_area_triangulo(base, altura):
    # Validar que la base no sea cero
    if base == 0:
        raise ValueError("La base no puede ser cero")
    
    # Validar que no se acepten valores negativos
    if base < 0:
        raise ValueError("La base no puede ser negativa")
    
    if altura < 0:
        raise ValueError("La altura no puede ser negativa")
    
    # Calcular el área: (base * altura) / 2
    area = (base * altura) / 2
    return area