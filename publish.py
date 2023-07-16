from pubsub_tools import publish_message

# Usage example
project_id = "fe-dev-sandbox"
topic_name = "hls-demo"
credential_file_path = "hls-demo-pubsub.json"
message = "Hello from Macbook!"

message_id = publish_message(project_id, topic_name, credential_file_path, message)
print(f'Published message id {message_id} to topic {topic_name}: {message}')