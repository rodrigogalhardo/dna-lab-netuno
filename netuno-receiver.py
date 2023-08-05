import pika


def callback(ch, method, properties, body):
    print(f" [x] Received {body}")


# Configurações de conexão
credentials = pika.PlainCredentials('dsqngzqh', 'SdHCABNVg71QnRthoaLwb690ukLK58kX')
parameters = pika.ConnectionParameters(
    host='porpoise.rmq.cloudamqp.com',
    port=5672,
    virtual_host='dsqngzqh',
    credentials=credentials,
    ssl=True,  # Use SSL para conexão segura
    ssl_options={
        "ssl_version": ssl.PROTOCOL_TLSv1_2
    }
)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
