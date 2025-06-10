import pytest
from area_triangulo import calcular_area_triangulo

def test_area_triangulo_base_5_altura_7():
    """
    Validar el resultado cuando la base sea 5 y la altura sea 7.
    Área esperada: (5 * 7) / 2 = 17.5
    """
    resultado = calcular_area_triangulo(5, 7)
    assert resultado == 17.5

def test_base_negativa():
    """
    Validar que no se acepten valores negativos para la base.
    """
    with pytest.raises(ValueError, match="La base no puede ser negativa"):
        calcular_area_triangulo(-5, 7)

def test_altura_negativa():
    """
    Validar que no se acepten valores negativos para la altura.
    """
    with pytest.raises(ValueError, match="La altura no puede ser negativa"):
        calcular_area_triangulo(5, -7)

def test_base_cero():
    """
    Validar que la base no sea cero.
    """
    with pytest.raises(ValueError, match="La base no puede ser cero"):
        calcular_area_triangulo(0, 7)