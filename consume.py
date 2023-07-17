from pubsub_tools import receive_messages

# Usage example
project_id = "fe-dev-sandbox"
subscription_name = "hls-demo-sub"
# with open("hls-demo-pubsub.json") as f:                                         # Read credentials_json from file; OR
#     credentials_json = f.read()
credentials_json = dbutils.secrets.get(scope='hls-demo', key='hls-demo-pubsub')   # Read credentials_json from Databricks secrets

def handler(message):
    print(f"Received message: {message.data.decode()}")

receive_messages(project_id, subscription_name, credentials_json, handler)