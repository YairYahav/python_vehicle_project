import json
from kafka import KafkaConsumer

print("Consumer starting... Listening for messages...")


consumer = KafkaConsumer(
    'vehicle-events',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)


for message in consumer:
    print(f"Received new event: {message.value}")
