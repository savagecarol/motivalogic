import json


def lambda_handler(event, context):
    # Get HTTP method
    http_method = event.get("httpMethod")

    # Get path
    path = event.get("path", "/")

    # Default response
    response = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({"message": "working"})
    }

    try:
        # Handle base /lambda path
        if path == "/lambda":
            if http_method == "GET":
                response["body"] = json.dumps({"message": "GET request successful"})
            elif http_method == "POST":
                body = json.loads(event.get("body", "{}"))
                response["body"] = json.dumps({"message": "POST request successful", "data": body})
            elif http_method == "PUT":
                body = json.loads(event.get("body", "{}"))
                response["body"] = json.dumps({"message": "PUT request successful", "data": body})
            elif http_method == "DELETE":
                response["body"] = json.dumps({"message": "DELETE request successful"})
            else:
                response["statusCode"] = 400
                response["body"] = json.dumps({"message": "Unsupported method"})

        # Handle custom endpoint
        elif path.endswith("/custom"):
            response["body"] = json.dumps({"message": "Custom endpoint reached"})

        else:
            response["statusCode"] = 400
            response["body"] = json.dumps({"message": "Unsupported path"})

    except Exception as e:
        response["statusCode"] = 500
        response["body"] = json.dumps({"message": "Error occurred", "error": str(e)})

    return response
