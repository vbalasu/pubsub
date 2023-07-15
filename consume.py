from google.cloud import pubsub_v1

def receive_messages(project_id, subscription_name, credential_file_path):
    # Set the environment variable for the service account credentials
    import os
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credential_file_path

    # Create a SubscriberClient with the specified project and credentials
    subscriber = pubsub_v1.SubscriberClient()

    # Get the full subscription path
    subscription_path = subscriber.subscription_path(project_id, subscription_name)

    def callback(message):
        print(f"Received message: {message.data.decode()}")

        # Acknowledge the message to remove it from the subscription
        message.ack()

    # Subscribe to the topic and attach the callback function
    subscriber.subscribe(subscription_path, callback=callback)

    # Keep the application running to continue receiving messages
    print(f"Listening for messages on {subscription_path}...")
    while True:
        pass


# Usage example
project_id = "fe-dev-sandbox"
subscription_name = "hls-demo-sub"
credential_file_path = "hls-demo-pubsub.json"

receive_messages(project_id, subscription_name, credential_file_path)

