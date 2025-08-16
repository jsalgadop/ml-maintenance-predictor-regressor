import boto3

def lambda_handler(event, context):

    region = 'us-east-1'
    endpoint_name = 'expense-xgboost'

    # Crear el cliente SageMaker Runtime
    runtime = boto3.client("sagemaker-runtime", region_name=region)

    # Payload: una sola feature (período contable)
    payload = event['body']['period']

    # Enviar la solicitud
    response = runtime.invoke_endpoint(
        EndpointName=endpoint_name,
        ContentType='text/csv',  # importante para modelos entrenados con CSV
        Body=payload
    )

    # Leer la respuesta
    expense = response['Body'].read().decode('utf-8')

    return {
        'statusCode': 200,
        'expense_prediction': expense
    }
