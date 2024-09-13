# Use uma imagem base com Python
FROM python:3.10

# Define o diretório de trabalho
WORKDIR /app

# Atualize o pip
RUN pip install --upgrade pip

# Instale pacotes do sistema se necessário
RUN apt-get update && apt-get install -y \
    build-essential \
    libffi-dev \
    libssl-dev \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Copie o arquivo de requisitos para dentro do container
COPY requirements.txt .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o código da aplicação para dentro do container
COPY . .

# Comando para rodar o script Python
CMD ["python", "app.py"]
