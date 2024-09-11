import serverless_wsgi
from flask import Flask, request, jsonify
from kafka import KafkaProducer
import json

# Cria uma instância da aplicação Flask
app = Flask(__name__)


# Define uma rota para o webhook do Active Campaign, que aceita apenas requisições POST
@app.route("/active-campaign", methods=["POST"])
def botmaker_webhook():

    # Extrai parâmetros do corpo da requisição POST usando o método request.form.get
    params = {
        "contact_id": request.form.get("contact[id]"),
        "deal_id": request.form.get("deal[id]"),
        "deal_create_date": request.form.get("deal[create_date]"),
        "contact_first_name": request.form.get("contact[first_name]"),
        "contact_email": request.form.get("contact[email]"),
        "contact_phone": request.form.get("contact[phone]"),
        "utm_source": request.form.get("contact[fields][27]"),  # source
        "utm_campaign": request.form.get("contact[fields][29]"),  # campanha
        "modality": request.form.get("contact[fields][7]"),  # modalidade
        "faculty": request.form.get("contact[fields][23]"),  # faculdade
        "pipeline": request.form.get("contact[fields][318]"),  # pipeline
        "deal_stage_title": request.form.get("deal[stage_title]"),
        "deal_owner_firstname": request.form.get("deal[owner_firstname]"),
    }
    
    
    #defini variaveis do producer
    boostrap_servers = ['IP_DO_SEU_HOST:9092']
    topic_name = 'deals'
    
    #inicializa o consumer
    producer = KafkaProducer(bootstrap_servers=boostrap_servers, value_serializer=lambda v: json.dumps(v).encode("utf-8"))
    producer.send(topic_name, params)
    # Garantir que todas as mensagens sejam enviadas antes de fechar
    producer.flush()
    # Fechamento do produtor
    producer.close()

    #retorno da requisição
    return jsonify({"message": "Dados recebidos com sucesso!"})


# Função para tratar solicitações Lambda usando serverless_wsgi
def lambda_handler(event, context):
    # Usar o serverless_wsgi para tratar a solicitação
    return serverless_wsgi.handle_request(app, event, context)
