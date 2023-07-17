from pubsub_tools import publish_message

# Usage example
project_id = "fe-dev-sandbox"
topic_name = "hls-demo"
# with open("hls-demo-pubsub.json") as f:                                         # Read credentials_json from file; OR
#     credentials_json = f.read()
credentials_json = dbutils.secrets.get(scope='hls-demo', key='hls-demo-pubsub')   # Read credentials_json from Databricks secrets
message = "Hello from Databricks!"

message_id = publish_message(project_id, topic_name, credentials_json, message)
print(f'Published message id {message_id} to topic {topic_name}: {message}')