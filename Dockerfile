# Produção: Python 3.12 slim com a aplicação temperatura-converter rodando branch main
FROM python:3.12-slim

# Definir diretório de trabalho
WORKDIR /app

# Instalar git (necessário para clonar o repositório)
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Instalar uv (gerenciador de pacotes Python)
RUN pip install --no-cache-dir uv

# Clonar repositório do GitHub na branch main
RUN git clone --branch main https://github.com/nextmarte/temperatura-converter.git .

# Instalar dependências usando uv
RUN uv sync --frozen

# Expor porta 7860 (padrão Gradio)
EXPOSE 7860

# Health check: verificar porta aberta (sem dependências extras)
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD python -c "import socket; socket.create_connection(('localhost', 7860), timeout=2)" || exit 1

# Executar aplicação Gradio
CMD ["uv", "run", "temperatura"]
