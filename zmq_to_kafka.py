import zmq
import json
from kafka import KafkaProducer


producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)


context = zmq.Context()
zmq_socket = context.socket(zmq.REP) 
zmq_socket.bind("tcp://*:5555")

print("ZMQ-to-Kafka Bridge is running. Listening on ZMQ port 5555...")

while True:
    message_string = zmq_socket.recv_string()
    print(f"[ZMQ] Received raw message: {message_string}")


    try:
        data = json.loads(message_string)
        producer.send('vehicle-events', value=data)
        producer.flush()
        print(f"[Kafka] Successfully forwarded to Kafka!")

        zmq_socket.send_string("OK")
    except Exception as e:
        print(f"Error parsing message: {e}")
        zmq_socket.send_string("ERROR")
