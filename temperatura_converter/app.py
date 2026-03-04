"""Interface Gradio para conversão de temperatura."""

import gradio as gr

from .utils.converter import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
)


def convert_temperature(
    unit: str, value: float
) -> tuple[str, str]:
    """
    Converte temperatura baseada na unidade de entrada selecionada.

    Args:
        unit: Unidade de entrada ('celsius', 'fahrenheit')
        value: Valor da temperatura a converter

    Returns:
        Tupla com (celsius, fahrenheit) como strings formatadas
    """
    if value is None:
        return "Erro", "Erro"

    try:
        if unit == "celsius":
            celsius = value
            fahrenheit = celsius_to_fahrenheit(celsius)
        elif unit == "fahrenheit":
            fahrenheit = value
            celsius = fahrenheit_to_celsius(fahrenheit)
        else:
            return "Erro", "Erro"

        return f"{celsius:.2f}", f"{fahrenheit:.2f}"
    except ValueError as e:
        error_msg = f"Erro: {str(e)}"
        return error_msg, error_msg


def create_app() -> gr.Blocks:
    """Cria e retorna a aplicação Gradio."""
    with gr.Blocks(title="Conversor de Temperatura") as demo:
        gr.Markdown("# Conversor de Temperatura")
        gr.Markdown(
            "Selecione a unidade de entrada, digite o valor e clique em "
            "**Converter** para obter os resultados em todas as unidades."
        )

        with gr.Row():
            # Seleção de unidade e entrada
            with gr.Column(scale=1):
                gr.Markdown("## Valor a Converter")

                unit_selector = gr.Radio(
                    choices=["Celsius (°C)", "Fahrenheit (°F)"],
                    value="Celsius (°C)",
                    label="Selecione a unidade de entrada",
                    info="Qual é a unidade do valor que você vai digitar?",
                )

                temperature_input = gr.Number(
                    value=0,
                    label="Temperatura",
                    info="Digite o valor da temperatura",
                )

            # Resultados
            with gr.Column(scale=1):
                gr.Markdown("## Resultados")

                celsius_result = gr.Textbox(
                    value="0.00",
                    label="Celsius (°C)",
                    interactive=False,
                )

                fahrenheit_result = gr.Textbox(
                    value="-17.78",
                    label="Fahrenheit (°F)",
                    interactive=False,
                )

        # Botão de ação para converter
        convert_button = gr.Button(
            "🔄 Converter",
            variant="primary",
            size="lg",
            scale=0,
        )

        # Event listener do botão
        convert_button.click(
            fn=convert_temperature,
            inputs=[unit_selector, temperature_input],
            outputs=[celsius_result, fahrenheit_result],
        )

        gr.Markdown(
            "---\n"
            "**Fórmulas utilizadas:**\n"
            "- °F = (°C × 9/5) + 32\n"
            "- °C = (°F - 32) × 5/9\n"
        )

    return demo


def main():
    """Função principal para executar a aplicação."""
    demo = create_app()
    demo.launch(share=False)


if __name__ == "__main__":
    main()
