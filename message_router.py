class MessageRouter:
    def __init__(self):
        self.topic_subscriptions = {}

    def route_message(self, encoded_message):
        try:
            message = decode_message(encoded_message)
        except ValueError as e:
            # Handle invalid message format
            print(f"Invalid message format: {e}")
            return

        if message.message_type == "request":
            # Route request messages directly to the specified recipient
            recipient_id = message.recipient
            self.deliver_message(message, recipient_id)

        elif message.message_type == "response":
            # Route response messages to the sender of the corresponding request
            request_id = message.payload["request_id"]
            sender_id = message.payload["sender_id"]

            recipients = self.topic_subscriptions.get(request_id, [])
            if not recipients:
                # No subscribers for this request, discard the message
                return

            for recipient in recipients:
                self.deliver_message(message, recipient)

        elif message.message_type == "information":
            # Broadcast information messages to all subscribed language models
            topic = message.payload["information_type"]

            recipients = self.topic_subscriptions.get(topic, [])
            if not recipients:
                # No subscribers for this topic, discard the message
                return

            for recipient in recipients:
                self.deliver_message(message, recipient)

        elif message.message_type == "acknowledgement":
            # Not applicable for routing, simply discard
            return

