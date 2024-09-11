#import kafkaProducer
from kafka import KafkaProducer

#Define servidor do kafka
boostrap_servers = ['<IP_HOST>:9092']

#Define topic
topic_name = 'deals'

#Inicializa producer
producer = KafkaProducer(bootstrap_servers=boostrap_servers)

#publicar no topico
producer.send(topic_name, 'Evento teste')

#print mensagem
print('messagem enviada')

# Garantir que todas as mensagens sejam enviadas antes de fechar
producer.flush()

# Fechamento do produtor
producer.close()
