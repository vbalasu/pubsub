#pip install google-cloud-pubsub
from google.cloud import pubsub_v1

def publish_message(project_id, topic_name, credential_file_path, message):
    # Set the environment variable for the service account credentials
    import os
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credential_file_path

    # Create a PublisherClient with the specified project and credentials
    publisher = pubsub_v1.PublisherClient()

    # Get the full topic path
    topic_path = publisher.topic_path(project_id, topic_name)

    # Publish the message
    data = message.encode('utf-8')  # Encode the message data
    future = publisher.publish(topic_path, data=data)

    # Wait for the message to be published
    future.result()

    print(f"Published message '{message}' to {topic_path}.")

# Usage example
project_id = "fe-dev-sandbox"
topic_name = "hls-demo"
credential_file_path = "hls-demo-pubsub.json"
message = "Hello from Macbook!"

publish_message(project_id, topic_name, credential_file_path, message)
