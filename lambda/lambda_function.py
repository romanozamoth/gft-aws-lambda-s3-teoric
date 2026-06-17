import json

def lambda_handler(event, context):

    print("Evento recebido:")
    print(json.dumps(event))

    bucket = event['Records'][0]['s3']['bucket']['name']
    arquivo = event['Records'][0]['s3']['object']['key']

    print(f"Arquivo recebido: {arquivo}")
    print(f"Bucket: {bucket}")

    return {
        "statusCode": 200,
        "message": "Processamento concluído"
    }
