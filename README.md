# pubsub

CLI commands to perform common operations with Google Pub/Sub

1. List topics
2. Create topic
3. Publish a message to the topic
4. Consume messages from the topic and print it to the console

##### [cli.sh](cli.sh)
```
source .env
echo $TOPIC_NAME
gcloud auth activate-service-account --key-file=hls-demo-pubsub.json
gcloud pubsub topics list
gcloud pubsub topics create $TOPIC_NAME
gcloud pubsub topics publish $TOPIC_NAME --message "Hello from Macbook"
gcloud pubsub subscriptions pull hls-demo-sub --auto-ack --limit=10
```

If you want to use Python, use these scripts:

[publish.py](publish.py)

[consume.py](consume.py)

