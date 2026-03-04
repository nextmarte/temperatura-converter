# Temperatura Converter

Calculadora web interativa para conversão de unidades de temperatura (Celsius ↔ Fahrenheit) construída com **Gradio 6.8** e **Python 3.12**.

## Características

✨ **Conversão com Botão** - Selecione a unidade, digite o valor e clique para converter
🎨 **Interface Moderna** - Interface intuitiva construída com Gradio
⚡ **Resposta Rápida** - Resultados instantâneos ao clicar no botão
🔢 **Precisão** - Resultados formatados com 2 casas decimais
🎯 **Duas unidades** - Celsius e Fahrenheit suportadas

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

1. **Selecione a unidade**: Use o seletor Radio para escolher entre Celsius ou Fahrenheit
2. **Digite o valor**: Insira a temperatura que deseja converter
3. **Clique no botão 🔄 Converter**: Dispara a conversão para as duas unidades
4. **Veja os resultados**: Os dois campos de resultado serão preenchidos automaticamente

## Docker & Containerização

### Desenvolvimento Local (Recomendado)

Continue usando o setup local com `uv` conforme descrito acima. Ideário não usar container para desenvolvimento:

```bash
source .venv/bin/activate
uv run temperatura
```

**Vantagens**: Hot-reload, debug fácil, dependências instaladas rápido.

### Produção em Container

A aplicação de produção roda em um container Docker que **sempre clona a branch `main`** do repositório GitHub, garantindo que a imagem esteja sempre sincronizada.

#### Pré-requisitos
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

#### Executar Produção

```bash
# Iniciar serviço de produção (constrói imagem se necessário)
docker-compose up -d

# Ver logs em tempo real
docker-compose logs -f temperatura-prod

# Acessar a aplicação
# http://localhost:7860
```

#### Sincronizar com a Branch Main (Atualizar Imagem)

Se houver mudanças em `main` e você quer que o container as reflita:

```bash
# Reconstruir a imagem (sem cache, garante pull do GitHub)
docker-compose build --no-cache

# Reiniciar o serviço
docker-compose up -d
```

#### Parar a Produção

```bash
docker-compose down
```

### Estrutura de Container

- **Dockerfile**: Cria imagem com Python 3.12, clona repo da branch `main`, instala dependências com `uv`
- **docker-compose.yml**: Orquestra o serviço `temperatura-prod` mapeando porta 7860
- **.dockerignore**: Otimiza tamanho da imagem (exclui `.git`, `__pycache__`, `.venv`, etc)
- **Healthcheck**: Container verificado a cada 30s (garante saúde da aplicação)

## Estrutura do Projeto

```
temperatura-converter/
├── temperatura_converter/
│   ├── __init__.py
│   ├── app.py              # Interface Gradio
│   └── utils/
│       ├── __init__.py
│       └── converter.py    # Funções de conversão
├── Dockerfile              # Imagem Docker para produção
├── docker-compose.yml      # Orquestração de serviços (produção)
├── .dockerignore           # Arquivos a ignorar no build Docker
├── pyproject.toml          # Configuração
├── .gitignore
├── README.md               # Este arquivo
└── copilot-instructions.md # Documentação técnica
```

## Fórmulas Utilizadas

- **Celsius → Fahrenheit**: F = (C × 9/5) + 32
- **Fahrenheit → Celsius**: C = (F - 32) × 5/9

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
