# Como ativar o ambiente python
# Saia do ambiente atual
deactivate

# Crie um novo virtualenv usando python3
python3 -m venv kafka-env

# Ative o ambiente
source kafka-env/bin/activate

# Instale as bibliotecas
pip install -r requirements.txt
