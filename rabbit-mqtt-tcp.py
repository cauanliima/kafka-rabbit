import paho.mqtt.client as mqtt

BROKER = "10.7.53.100"
PORT = 1883
USERNAME = "rabbitmq"
PASSWORD = "PASS@12345"
TOPIC = "teste_conexao"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Conectado ao broker MQTT com sucesso!")
        # Inscreve no tópico para receber mensagens
        client.subscribe(TOPIC)
        # Publica a mensagem inicial
        client.publish(TOPIC, "Mensagem de teste")
    else:
        print(f"❌ Falha na conexão. Código: {rc}")

def on_publish(client, userdata, mid):
    print("📤 Mensagem publicada com sucesso!")

def on_message(client, userdata, msg):
    print(f"📩 Mensagem recebida no tópico '{msg.topic}': {msg.payload.decode()}")

client = mqtt.Client()
client.username_pw_set(USERNAME, PASSWORD)

client.on_connect = on_connect
client.on_publish = on_publish
client.on_message = on_message

print(f"🔌 Conectando ao broker MQTT {BROKER}:{PORT}...")
client.connect(BROKER, PORT, 60)
client.loop_forever()

