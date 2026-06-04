import time
import json
from kafka import KafkaProducer


producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print("Producer strictly initialized. Ready to send messages...")


message = {"status": "Testing", "message": "Kafka producer is working!"}
producer.send('vehicle-events', value=message)


producer.flush()
print(f"Sent message successfully: {message}")
