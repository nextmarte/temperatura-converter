"""Funções de conversão de unidades de temperatura."""


def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Converte temperatura de Celsius para Fahrenheit.

    Fórmula: F = (C × 9/5) + 32

    Args:
        celsius: Temperatura em graus Celsius

    Returns:
        Temperatura convertida em Fahrenheit
    """
    return (celsius * 9/5) + 32


def celsius_to_kelvin(celsius: float) -> float:
    """
    Converte temperatura de Celsius para Kelvin.

    Fórmula: K = C + 273.15

    Args:
        celsius: Temperatura em graus Celsius

    Returns:
        Temperatura convertida em Kelvin
    """
    return celsius + 273.15


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """
    Converte temperatura de Fahrenheit para Celsius.

    Fórmula: C = (F - 32) × 5/9

    Args:
        fahrenheit: Temperatura em graus Fahrenheit

    Returns:
        Temperatura convertida em Celsius
    """
    return (fahrenheit - 32) * 5/9


def fahrenheit_to_kelvin(fahrenheit: float) -> float:
    """
    Converte temperatura de Fahrenheit para Kelvin.

    Fórmula: K = (F - 32) × 5/9 + 273.15

    Args:
        fahrenheit: Temperatura em graus Fahrenheit

    Returns:
        Temperatura convertida em Kelvin
    """
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)


def kelvin_to_celsius(kelvin: float) -> float:
    """
    Converte temperatura de Kelvin para Celsius.

    Fórmula: C = K - 273.15

    Args:
        kelvin: Temperatura em Kelvin

    Returns:
        Temperatura convertida em Celsius

    Raises:
        ValueError: Se o valor for menor que 0 (zero absoluto)
    """
    if kelvin < 0:
        raise ValueError(
            "Temperatura em Kelvin não pode ser negativa (zero absoluto = 0 K)")
    return kelvin - 273.15


def kelvin_to_fahrenheit(kelvin: float) -> float:
    """
    Converte temperatura de Kelvin para Fahrenheit.

    Fórmula: F = (K - 273.15) × 9/5 + 32

    Args:
        kelvin: Temperatura em Kelvin

    Returns:
        Temperatura convertida em Fahrenheit

    Raises:
        ValueError: Se o valor for menor que 0 (zero absoluto)
    """
    if kelvin < 0:
        raise ValueError(
            "Temperatura em Kelvin não pode ser negativa (zero absoluto = 0 K)")
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)
