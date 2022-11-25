import time
from kafka import KafkaProducer

bootstrap_server=["localhost:9092"]
topic="Test"
producer=KafkaProducer(bootstrap_servers=bootstrap_server)
producer=KafkaProducer()
data="Gods own country"
def senddata():
    message=producer.send(topic,bytes(data,"utf-8"))
    metadata = message.get()
    print(metadata.topic)
    print(metadata.partition)
    print("test")
    time.sleep(5)

while True:
    senddata()