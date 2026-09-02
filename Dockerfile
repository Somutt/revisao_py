# Imagem base do python
FROM python:3.12-slim

# Instalação do uv no container
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

WORKDIR /app

# Cópia de requirements antes do código p/ cache
COPY requirements.txt .

RUN uv pip install --system -r requirements.txt

# Copia o código
COPY . .

# Porta padrão do jupyter notebook
EXPOSE 8888

# Comando p/ iniciar Jupyter Server no navegador
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''"]