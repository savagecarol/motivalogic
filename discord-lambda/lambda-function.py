import json
import urllib3

http = urllib3.PoolManager()
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/<ACCESS_TOKEN>"

def lambda_handler(event, context):
    print("Lambda triggered by EventBridge!")
    print("Event received:", json.dumps(event))

    detail = event.get('detail', {})
    alarm_name = detail.get('alarmName', 'Unknown Alarm')
    old_state = detail.get('previousStateValue', 'UNKNOWN')
    new_state = detail.get('stateValue', 'UNKNOWN')
    reason = detail.get('stateReason', 'No reason provided')
    timestamp = detail.get('stateChangeTime', 'Unknown time')

    message = (
        f"⚠️ **AWS CloudWatch Alarm Triggered**\n"
        f"**Alarm Name:** {alarm_name}\n"
        f"**Old State:** {old_state}\n"
        f"**New State:** {new_state}\n"
        f"**Reason:** {reason}\n"
        f"**Time:** {timestamp}"
    )

    payload = {"content": message}
    encoded_payload = json.dumps(payload).encode('utf-8')

    try:
        response = http.request(
            'POST',
            DISCORD_WEBHOOK_URL,
            body=encoded_payload,
            headers={'Content-Type': 'application/json'}
        )
        print(f"Discord response status: {response.status}")
        print(f"Discord response data: {response.data.decode('utf-8')}")
    except Exception as e:
        print(f"Error sending to Discord: {str(e)}")
