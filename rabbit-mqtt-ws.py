import paho.mqtt.client as mqtt

BROKER = "10.7.53.100"
PORT = 15675
USERNAME = "rabbitmq"
PASSWORD = "PASS@12345"
TOPIC = "teste_conexao"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Conectado via WebSocket!")
        # Inscreve no tópico para receber mensagens
        client.subscribe(TOPIC)
        # Publica a mensagem inicial
        client.publish(TOPIC, "Mensagem de teste via WebSocket")
    else:
        print(f"❌ Falha na conexão. Código: {rc}")

def on_publish(client, userdata, mid):
    print("📤 Mensagem publicada com sucesso!")

def on_message(client, userdata, msg):
    print(f"📩 Mensagem recebida no tópico '{msg.topic}': {msg.payload.decode()}")

# Criando o cliente MQTT com WebSocket
client = mqtt.Client(transport="websockets")
client.username_pw_set(USERNAME, PASSWORD)
# Configura o caminho correto do WebSocket
client.ws_set_options(path="/ws")

client.on_connect = on_connect
client.on_publish = on_publish
client.on_message = on_message

print(f"🔌 Conectando ao broker via WebSocket {BROKER}:{PORT}...")
client.connect(BROKER, PORT, 60)
client.loop_forever()

