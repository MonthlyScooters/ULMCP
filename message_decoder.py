def decode_message(encoded_message):
    # Decode the JSON message
    message = json.loads(encoded_message)

    # Check for missing or invalid fields
    required_fields = ["message_type", "sender", "recipient", "payload"]
    for field in required_fields:
        if field not in message:
            raise ValueError(f"Missing required field: {field}")

    # Check if message type is valid
    if message["message_type"] not in VALID_MESSAGE_TYPES:
        raise ValueError(f"Invalid message type: {message['message_type']}")

    # Check if sender ID and recipient ID are valid
    if not validate_id(message["sender"]):
        raise ValueError(f"Invalid sender ID: {message['sender']}")
    if not validate_id(message["recipient"]):
        raise ValueError(f"Invalid recipient ID: {message['recipient']}")

    # Construct the Message object if valid
    return Message(message_type, sender_id, recipient_id, payload)
