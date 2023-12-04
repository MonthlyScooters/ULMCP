def encode_message(message_type, sender_id, recipient_id, payload):
    # Validate message structure and fields before encoding
    required_fields = ["message_type", "sender", "recipient", "payload"]
    for field in required_fields:
        if not field:
            raise ValueError(f"Missing required field: {field}")

    # Validate message type
    if message_type not in VALID_MESSAGE_TYPES:
        raise ValueError(f"Invalid message type: {message_type}")

    # Validate sender ID and recipient ID
    if not validate_id(sender_id):
        raise ValueError(f"Invalid sender ID: {sender_id}")

    # Validate payload
    if not isinstance(payload, dict):
        raise ValueError(f"Payload must be a dictionary: {payload}")

    # Encode the message if valid
    message = {
        "message_type": message_type,
        "sender": sender_id,
        "recipient": recipient_id,
        "payload": payload,
    }

    return json.dumps(message)
