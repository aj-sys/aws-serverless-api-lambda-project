import json

def lambda_handler(event, context):
    # Read the name from the URL query string.
    query_parameters = event.get("queryStringParameters") or {}
    name = query_parameters.get("name", "World")

    # Prepare the response.
    response_body = {
        "message": f"Hello, {name}!",
        "status": "success"
    }

    # Return the response in the format expected by API Gateway.
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(response_body)
    }