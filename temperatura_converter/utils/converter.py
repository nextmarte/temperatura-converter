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
