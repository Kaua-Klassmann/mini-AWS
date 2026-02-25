import json

def lambda_handler(event, context):
    body = event.get('body')

    if body is None:
        message = event.get('message')
    else:
        if isinstance(body, str):
            body = json.loads(body)
            
        message = body.get('message')

    if message is None:
        return {
            'statusCode': 400,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps('No message provided')
        }

    message = message.upper()[::-1]

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(message)
    }
