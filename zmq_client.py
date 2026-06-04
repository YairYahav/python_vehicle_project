import zmq
import json
import time

context = zmq.Context()

zmq_socket = context.socket(zmq.REQ)
zmq_socket.connect("tcp://localhost:5555")


vehicle_event = {
    "status": "ZMQ_Origin",
    "message": "This message started in ZMQ and will end in Kafka!",
    "timestamp": time.time()
}

print(f"Sending event via ZMQ: {vehicle_event}")
zmq_socket.send_string(json.dumps(vehicle_event))


response = zmq_socket.recv_string()
print(f"Server response: {response}")
