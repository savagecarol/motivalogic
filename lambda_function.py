import json


def lambda_handler(event, context):
    # Print the full event for debugging
    print("Received event:", json.dumps(event, indent=2))

    # Get HTTP method
    http_method = event.get("httpMethod")
    print("HTTP Method:", http_method)

    # Get path
    path = event.get("path", "/")
    print("Path:", path)

    # Default response
    response = {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"message": "working"})
    }

    try:
        # Handle base /lambda path
        if path == "/lambda":
            print("Matched base /lambda path")
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
            print("Matched /custom path")
            response["body"] = json.dumps({"message": "Custom endpoint reached"})

        else:
            print("Unsupported path")
            response["statusCode"] = 400
            response["body"] = json.dumps({"message": "Unsupported path"})

    except Exception as e:
        print("Exception occurred:", str(e))
        response["statusCode"] = 500
        response["body"] = json.dumps({"message": "Error occurred", "error": str(e)})

    return response
