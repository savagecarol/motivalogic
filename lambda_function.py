import json

def lambda_handler(event, context):
    http_method = event.get("requestContext", {}).get("http", {}).get("method"
    path = event.get("requestContext", {}).get("http", {}).get("path")

    response = {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"message": "working"})
    }

    try:
        # Simulated failure for specific endpoints
        if path == "/lambda" and http_method == "POST":
            raise Exception("Simulated POST failure for testing alarms")

        elif path.endswith("/custom") and http_method == "GET":
            raise Exception("Simulated GET /custom failure for testing alarms")

        # Normal handling
        if path == "/lambda":
            if http_method == "GET":
                response["body"] = json.dumps({"message": "GET request successful"})
            elif http_method == "PUT":
                body = json.loads(event.get("body", "{}"))
                response["body"] = json.dumps({"message": "PUT request successful", "data": body})
            elif http_method == "DELETE":
                response["body"] = json.dumps({"message": "DELETE request successful"})
            else:
                response["statusCode"] = 400
                response["body"] = json.dumps({"message": "Unsupported method"})

        elif path.endswith("/custom"):
            response["body"] = json.dumps({"message": "Custom endpoint reached"})

        else:
            response["statusCode"] = 400
            response["body"] = json.dumps({"message": "Unsupported path"})

    except Exception as e:
        response["statusCode"] = 500
        response["body"] = json.dumps({"message": "Error occurred", "error": str(e)})
        # This will count as an error in CloudWatch
        raise e  # Re-raise to make CloudWatch treat it as a Lambda error

    return response
