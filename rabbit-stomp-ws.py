import websocket
import threading
import time

BROKER = "10.7.53.100"
PORT = 15674
USERNAME = "rabbitmq"
PASSWORD = "PASS@12345"
TOPIC = "/topic/teste_conexao"  # Destino válido: /topic/ ou /queue/

def on_message(ws, message):
    print(f"📩 Received:\n{message}\n")

def on_error(ws, error):
    print(f"❌ Error: {error}")

def on_close(ws, close_status_code, close_msg):
    print("🛑 Connection closed")

def on_open(ws):
    print("✅ Connected to RabbitMQ Web-STOMP")

    # Envia CONNECT frame
    connect_frame = f"CONNECT\nlogin:{USERNAME}\npasscode:{PASSWORD}\n\n\x00"
    ws.send(connect_frame)

    # Inscreve no tópico
    subscribe_frame = f"SUBSCRIBE\nid:sub-0\ndestination:{TOPIC}\nack:auto\n\n\x00"
    ws.send(subscribe_frame)

    # Envia mensagem inicial
    send_frame = f"SEND\ndestination:{TOPIC}\n\nMensagem inicial via Web-STOMP\x00"
    ws.send(send_frame)
    print("📤 Initial message sent!")

    # Thread para envio interativo de mensagens do terminal
    def send_loop():
        try:
            while True:
                msg = input()
                if msg.strip():
                    send_frame = f"SEND\ndestination:{TOPIC}\n\n{msg}\x00"
                    ws.send(send_frame)
                    print("📤 Message sent!")
        except KeyboardInterrupt:
            print("🛑 Stopping message sender...")

    threading.Thread(target=send_loop, daemon=True).start()

# Habilita debug WebSocket
websocket.enableTrace(True)
ws_url = f"ws://{BROKER}:{PORT}/ws"
ws = websocket.WebSocketApp(ws_url,
                            on_open=on_open,
                            on_message=on_message,
                            on_error=on_error,
                            on_close=on_close)

ws.run_forever()

