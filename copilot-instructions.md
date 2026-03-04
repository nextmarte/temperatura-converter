# Copilot Instructions for **Temperatura Converter**

## Overview
- **Domain**: Aplicação web para conversão de unidades de temperatura (Celsius ↔ Fahrenheit ↔ Kelvin)
- **Framework**: Gradio 6.8 com Python 3.12
- **Package Manager**: UV (uv)
- **Core functionality**: Interface interativa para conversão bidirecional de temperaturas em tempo real

## Project Structure

```
temperatura-converter/
├── temperatura_converter/          # Pacote Python principal
│   ├── __init__.py                # Inicialização do pacote
│   ├── app.py                     # Interface Gradio (gr.Blocks)
│   └── utils/
│       ├── __init__.py            # Inicialização do módulo utils
│       └── converter.py           # Funções de conversão
├── pyproject.toml                 # Configuração do projeto (UV + dependências)
├── .gitignore                     # Padrões para controle de versão
└── copilot-instructions.md        # Este arquivo
```

## Architecture & Data Flow

```
┌────────────────────────────────────────────────────────────┐
│               Gradio Interface (gr.Blocks)                 │
│                                                            │
│  ┌─────────────────────────────────────────────────────┐ │
│  │ INPUT SECTION                                       │ │
│  │ ┌─────────────────────────────────────────────────┐ │ │
│  │ │ Unit Selector (gr.Radio)                       │ │ │
│  │ │ • Celsius (°C)  • Fahrenheit (°F)  • Kelvin (K)│ │ │
│  │ └─────────────────────────────────────────────────┘ │ │
│  │ ┌─────────────────────────────────────────────────┐ │ │
│  │ │ Temperature Input (gr.Number)                  │ │ │
│  │ │ [digite o valor]                               │ │ │
│  │ └─────────────────────────────────────────────────┘ │ │
│  └─────────────────────────────────────────────────────┘ │
│                                                            │
│  ┌──────────────────────────────────────────────────────┐ │
│  │ 🔄 CONVERTER (gr.Button) - Click para disparar      │ │
│  └──────────────┬───────────────────────────────────────┘ │
│                 │                                          │
│                 ▼                                          │
│  ┌──────────────────────────────────────────────────────┐ │
│  │ Função: convert_temperature(unit, value)            │ │
│  │         └─ Determina qual Conv. usar baseado em unit│ │
│  └──────────────┬───────────────────────────────────────┘ │
│                 │                                          │
│                 ▼                                          │
│  ┌──────────────────────────────────────────────────────┐ │
│  │ Conversion Functions (utils/converter.py)           │ │
│  │ ┌──────────────────────────────────────────────────┐ │ │
│  │ │ celsius_to_fahrenheit() | celsius_to_kelvin()   │ │ │
│  │ │ fahrenheit_to_celsius() | fahrenheit_to_kelvin()│ │ │
│  │ │ kelvin_to_celsius()     | kelvin_to_fahrenheit()│ │ │
│  │ └──────────────────────────────────────────────────┘ │ │
│  └──────────────┬───────────────────────────────────────┘ │
│                 │                                          │
│                 ▼                                          │
│  ┌─────────────────────────────────────────────────────┐ │
│  │ OUTPUT SECTION (Results)                           │ │
│  │ ┌─────────────────────────────────────────────────┐ │ │
│  │ │ Celsius Output (Textbox read-only)              │ │ │
│  │ │ Fahrenheit Output (Textbox read-only)           │ │ │
│  │ │ Kelvin Output (Textbox read-only)               │ │ │
│  │ └─────────────────────────────────────────────────┘ │ │
│  └─────────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────────┘
```

### Conversion Logic

**De Celsius:**
- Para Fahrenheit: F = (C × 9/5) + 32
- Para Kelvin: K = C + 273.15

**De Fahrenheit:**
- Para Celsius: C = (F - 32) × 5/9
- Para Kelvin: K = (F - 32) × 5/9 + 273.15

**De Kelvin:**
- Para Celsius: C = K - 273.15 (requer validação K ≥ 0)
- Para Fahrenheit: F = (K - 273.15) × 9/5 + 32 (requer validação K ≥ 0)

## Development Workflow

### 1. Setup do Ambiente
```bash
# Criar ambiente virtual
uv venv .venv

# Ativar
source .venv/bin/activate

# Instalar dependências
uv sync
```

### 2. Executar a Aplicação
```bash
# Opção 1: Via script definido em pyproject.toml
uv run temperatura

# Opção 2: Direto com Gradio CLI (hot-reload)
gradio temperatura_converter/app.py

# Opção 3: Com Python direto
uv run python -m temperatura_converter.app
```

A aplicação estará acessível em: **http://localhost:7860**

### 3. Hot Reload Development
```bash
# Usar Gradio CLI para desenvolvimento com auto-reload
gradio temperatura_converter/app.py --reload-dirs temperatura_converter
```

## Coding Standards & Conventions

### Imports
- Imports padrão primeiro (e.g., `sys`, `os`)
- Imports terceiros em seguida (e.g., `gradio`)
- Imports locais por último (e.g., `.utils.converter`)

### Nomeação
- **Variáveis e funções**: `snake_case` (ex: `celsius_input`, `convert_from_celsius`)
- **Classes**: `PascalCase` (futuro uso, se aplicável)
- **Constantes**: `UPPER_SNAKE_CASE` (futuro uso)

### Documentação
- Docstrings em português (PEP 257)
- Type hints obrigatórios em funções
- Comments para lógica complexa

### Exemplo de Função
```python
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
```

## Component Guide (Gradio 6.8)

### `gr.Blocks`
- Container para interfaces customizáveis
- Permite múltiplas linhas (`gr.Row`) e colunas (`gr.Column`)
- Suporta event listeners para interação em tempo real

### `gr.Radio`
- Seletor de múltiplas opções (uma por vez)
- Exibe opções como botões radio
- Ideal para selecionar a unidade de entrada

### `gr.Number`
- Componente de entrada/saída numérica
- Retorna `float` ou `int` dependendo de `precision`
- Ideal para entradas de temperatura

### `gr.Button`
- Botão acionável que dispara uma função
- Parâmetros úteis:
  - `variant`: "primary" (azul), "secondary" (cinza), "stop" (vermelho)
  - `size`: "sm", "lg", "xl"
- Event listener: `button.click(fn, inputs, outputs)`

### `gr.Textbox`
- Componente para texto (customizado como output read-only)
- Exibe resultados formatados
- `interactive=False` para modo somente leitura

### `gr.Row` e `gr.Column`
- Layout grid responsivo
- Parâmetro `scale` para proporcionar largura
- Aninhamento permitido

### Event Listeners
```python
# Click em botão
button.click(
    fn=minha_funcao,
    inputs=[input1, input2],
    outputs=[output1, output2],
)

# Change em campo (automático)
number_input.change(
    fn=outra_funcao,
    inputs=number_input,
    outputs=output_field,
)
```

## External References

- **Gradio Documentation**: https://www.gradio.app/docs/
- **Gradio Quickstart**: https://www.gradio.app/guides/quickstart
- **Gradio Blocks Guide**: https://www.gradio.app/guides/blocks-and-event-listeners
- **UV Package Manager**: https://docs.astral.sh/uv/

## Tips for Copilot

1. **Fluxo atual com botão**: O app usa `gr.Radio` para selecionar unidade e um `gr.Button` para disparar conversão. A função `convert_temperature(unit, value)` centraliza a lógica.
2. **Adicionar nova conversão**: Estenda `convert_temperature()` em `app.py` para novas unidades, ou crie conversões customizadas em `utils/converter.py`.
3. **Mudar para conversão em tempo real**: Substitua `convert_button.click()` por event listeners no campo de entrada (e.g., `temperature_input.change()`).
4. **Validações**: Sempre validar Kelvin ≥ 0 (zero absoluto). Usar try/except em conversões.
5. **Formatação numérica**: Usar `.2f` para 2 casas decimais (já implementado).
6. **Estender interface**: Use `gr.Row()` e `gr.Column()` para reorganizar layouts sem quebrar interatividade.
7. **Testing**: Futuro uso de `pytest` para unit tests em `tests/test_converter.py`.

---

*Versão: 0.1.0*  
*Última atualização: 04/03/2026*
