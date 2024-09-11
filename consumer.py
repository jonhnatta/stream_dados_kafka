# import kafkaConsumer
from kafka import KafkaConsumer

# Define servidor do kafka
boostrap_servers = ['<IP_DO_HOST>:9092']

# Define topic
topic_name = 'deals'

# Inicializa consumer
consumer = KafkaConsumer(
    topic_name,
    bootstrap_servers=boostrap_servers,
    auto_offset_reset='earliest',
    group_id=None
)

# Consome mensagens do tópico
for message in consumer:
    print(f"Topic: {message.topic} | Menssagem: {message.value} ")

# Fechamento do consumidor
consumer.close()
