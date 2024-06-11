from kafka import KafkaConsumer
from config import endpoint, username, password

consumer = KafkaConsumer(
    'sink',
    bootstrap_servers=endpoint,
    sasl_mechanism='SCRAM-SHA-256',
    security_protocol='SASL_SSL',
    sasl_plain_username=username,
    sasl_plain_password=password,
    # group_id='YOUR_CONSUMER_GROUP',
    # auto_offset_reset='earliest'
    auto_offset_reset='latest'
)

print("Consumer started!")

try:
    for message in consumer:
        print(f"Received message: {message.value}")
except KeyboardInterrupt:
    pass
finally:
    consumer.close()