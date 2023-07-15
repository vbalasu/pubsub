source .env
echo $TOPIC_NAME
gcloud auth activate-service-account --key-file=hls-demo-pubsub.json
gcloud pubsub topics list
gcloud pubsub topics create $TOPIC_NAME
gcloud pubsub topics publish $TOPIC_NAME --message "Hello from Macbook"
gcloud pubsub subscriptions pull hls-demo-sub --auto-ack --limit=10
