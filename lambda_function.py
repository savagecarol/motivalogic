import json


def lambda_handler(event, context):
    print("Received event:", json.dumps(event, indent=2))

    # HTTP API v2 fields
    http_method = event.get("requestContext", {}).get("http", {}).get("method")
    path = event.get("requestContext", {}).get("http", {}).get("path")

    print("HTTP Method:", http_method)
    print("Path:", path)

    response = {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"message": "working"})
    }

    try:
        # Base /lambda route
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

        # Custom endpoint
        elif path.endswith("/custom"):
            response["body"] = json.dumps({"message": "Custom endpoint reached"})

        else:
            response["statusCode"] = 400
            response["body"] = json.dumps({"message": "Unsupported path"})

    except Exception as e:
        print("Exception:", str(e))
        response["statusCode"] = 500
        response["body"] = json.dumps({"message": "Error occurred", "error": str(e)})

    return response
