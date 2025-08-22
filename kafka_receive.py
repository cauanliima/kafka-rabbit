from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'teste-topico',
    bootstrap_servers='10.7.53.100:9092',
    security_protocol='SASL_PLAINTEXT',
    sasl_mechanism='PLAIN',
    sasl_plain_username='meuusuario',
    sasl_plain_password='minhasenha',
    auto_offset_reset='earliest',
    group_id='teste-group',
    value_deserializer=lambda v: v.decode('utf-8')
)

print("Aguardando mensagens...")
for msg in consumer:
    print(f"Recebido: {msg.value}")

