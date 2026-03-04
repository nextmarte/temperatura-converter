# Temperatura Converter

Calculadora web interativa para conversão de unidades de temperatura (Celsius ↔ Fahrenheit ↔ Kelvin) construída com **Gradio 6.8** e **Python 3.12**.

## Características

✨ **Conversão com Botão** - Selecione a unidade, digite o valor e clique para converter
🎨 **Interface Moderna** - Interface intuitiva construída com Gradio
⚡ **Resposta Rápida** - Resultados instantâneos ao clicar no botão
🔢 **Precisão** - Resultados formatados com 2 casas decimais
✅ **Validações** - Verificação de zero absoluto para Kelvin
🎯 **Três unidades** - Celsius, Fahrenheit e Kelvin suportadas

## Instalação Rápida

### Pré-requisitos
- Python 3.12+
- [UV](https://docs.astral.sh/uv/) (instalador rápido de pacotes Python)

### Setup

```bash
# Clonar/entrar no projeto
cd temperatura-converter

# Criar ambiente virtual
uv venv .venv

# Ativar
source .venv/bin/activate  # No Windows: .venv\Scripts\activate

# Instalar dependências
uv sync
```

## Uso

### Iniciar a Aplicação

```bash
# Opção 1: via comando configurado
uv run temperatura

# Opção 2: via Gradio CLI (com hot-reload)
gradio temperatura_converter/app.py

# Opção 3: execução direta
uv run python -m temperatura_converter.app
```

A aplicação abrirá automaticamente em **http://localhost:7860**

### Interface

1. **Selecione a unidade**: Use o seletor Radio para escolher entre Celsius, Fahrenheit ou Kelvin
2. **Digite o valor**: Insira a temperatura que deseja converter
3. **Clique no botão 🔄 Converter**: Dispara a conversão para as três unidades
4. **Veja os resultados**: Os três campos de resultado serão preenchidos automaticamente

## Estrutura do Projeto

```
temperatura-converter/
├── temperatura_converter/
│   ├── __init__.py
│   ├── app.py              # Interface Gradio
│   └── utils/
│       ├── __init__.py
│       └── converter.py    # Funções de conversão
├── pyproject.toml          # Configuração
├── .gitignore
├── README.md               # Este arquivo
└── copilot-instructions.md # Documentação técnica
```

## Fórmulas Utilizadas

- **Celsius → Fahrenheit**: F = (C × 9/5) + 32
- **Celsius → Kelvin**: K = C + 273.15
- **Fahrenheit → Celsius**: C = (F - 32) × 5/9
- **Kelvin → Celsius**: C = K - 273.15 *(requer K ≥ 0)*

## Dependências

- `gradio==6.8` - Framework para interface web

*Para desenvolvimento opcional (dev deps):*
- `pytest` - Testes unitários
- `black` - Formatação de código
- `ruff` - Linter Python

## Desenvolvimento

Consulte [copilot-instructions.md](copilot-instructions.md) para:
- Arquitetura e fluxo de dados
- Padrões de código
- Guia de componentes Gradio
- Como estender a aplicação

## Licença

MIT

## Autor

Marcus
