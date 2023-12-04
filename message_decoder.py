def decode_message(encoded_message):
    """
    Decodes a JSON-encoded message into a message object.

    Args:
        encoded_message (str): JSON-encoded message string

    Returns:
        Message: Decoded message object
    """
    message = json.loads(encoded_message)

    message_type = message["message_type"]
    sender_id = message["sender"]
    recipient_id = message["recipient"]
    payload = message["payload"]

    return Message(message_type, sender_id, recipient_id, payload)

def decode_message(encoded_message):
    # Decode the JSON message
    message = json.loads(encoded_message)

    # Check for missing or invalid fields
    ...

    # Raise an INVALID_MESSAGE_FORMAT error if invalid
    ...

    # Construct the Message object if valid
    return Message(message_type, sender_id, recipient_id, payload)
