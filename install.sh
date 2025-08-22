#!/bin/bash

# Nome do virtualenv
VENV_NAME="kafka-env"

# Verifica se o Python3 está instalado
if ! command -v python3 &> /dev/null
then
    echo "❌ Python3 não encontrado. Instale o Python3 antes de continuar."
    exit 1
fi

# Instala virtualenv se não estiver instalado
if ! python3 -m pip show virtualenv &> /dev/null
then
    echo "🔧 Instalando virtualenv..."
    python3 -m pip install --user virtualenv
fi

# Cria o virtualenv
echo "🛠 Criando virtualenv: $VENV_NAME"
python3 -m virtualenv $VENV_NAME

# Ativa o virtualenv
echo "⚡ Ativando virtualenv..."
source $VENV_NAME/bin/activate

# Instala as bibliotecas do requirements.txt
if [ -f "requirements.txt" ]; then
    echo "📦 Instalando dependências do requirements.txt..."
    pip install --upgrade pip
    pip install -r requirements.txt
else
    echo "❌ Arquivo requirements.txt não encontrado!"
fi

echo "✅ Setup concluído! Para ativar no futuro, use: source $VENV_NAME/bin/activate"

