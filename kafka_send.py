from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='10.7.53.100:9092',  # ou IP/hostname do broker
    security_protocol='SASL_PLAINTEXT',
    sasl_mechanism='PLAIN',
    sasl_plain_username='meuusuario',
    sasl_plain_password='minhasenha',
    value_serializer=lambda v: v.encode('utf-8')
)

for i in range(1, 6):
    msg = f"Mensagem {i}"
    producer.send('teste-topico', value=msg)
    print(f"Enviado: {msg}")

producer.flush()
producer.close()

