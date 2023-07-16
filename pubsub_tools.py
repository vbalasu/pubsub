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
    result = future.result()
    return result


def receive_messages(project_id, subscription_name, credential_file_path, handler=None):
    # Set the environment variable for the service account credentials
    import os
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credential_file_path

    # Create a SubscriberClient with the specified project and credentials
    subscriber = pubsub_v1.SubscriberClient()

    # Get the full subscription path
    subscription_path = subscriber.subscription_path(project_id, subscription_name)

    def callback(message):
        if handler:
            handler(message)

        # Acknowledge the message to remove it from the subscription
        message.ack()

    # Subscribe to the topic and attach the callback function
    subscriber.subscribe(subscription_path, callback=callback)

    # Keep the application running to continue receiving messages
    print(f"Listening for messages on {subscription_path}...")
    while True:
        pass
