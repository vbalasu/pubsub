from pubsub_tools import receive_messages

# Usage example
project_id = "fe-dev-sandbox"
subscription_name = "hls-demo-sub"
credential_file_path = "hls-demo-pubsub.json"

def handler(message):
    print(f"Received message: {message.data.decode()}")

receive_messages(project_id, subscription_name, credential_file_path, handler)