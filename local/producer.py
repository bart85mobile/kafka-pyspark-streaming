from kafka import KafkaProducer
from faker import Faker
from random import randrange
import json
import time
from config import endpoint, username, password

producer = KafkaProducer(
    bootstrap_servers=endpoint,
    sasl_mechanism='SCRAM-SHA-256',
    security_protocol='SASL_SSL',
    sasl_plain_username=username,
    sasl_plain_password=password,
    api_version_auto_timeout_ms=100000,    
)

print("Producer started!")

fake = Faker()

while True:
    # Define message to publish
    data_dict = {
        'name': fake.name(),
        'address': fake.address(),
        'age': randrange(10, 100)
    }
    data_json_str = json.dumps(data_dict).encode('utf-8')
    
    # Publish message
    try:
        result = producer.send('source', data_json_str).get(timeout = 60)
        print("Message produced:", data_dict)
    except Exception as e:
        print(f"Error producing message: {e}")
    
    # Wait 1-3 seconds
    time.sleep(randrange(5,8))

producer.close()