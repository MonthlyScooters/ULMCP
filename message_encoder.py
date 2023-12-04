def encode_message(message_type, sender_id, recipient_id, payload):
    """
    Encodes a message into JSON format.

    Args:
        message_type (str): Type of the message (e.g., request, response, information)
        sender_id (str): Identifier of the sending language model
        recipient_id (str): Identifier of the receiving language model (optional for broadcast messages)
        payload (dict): Data structure carrying the message content
    """
    message = {
        "message_type": message_type,
        "sender": sender_id,
        "recipient": recipient_id,
        "payload": payload
    }

    return json.dumps(message)

def encode_message(message_type, sender_id, recipient_id, payload):
    # Validate message structure and fields before encoding
    ...

    # Encode the message if valid
    message = {
        "message_type": message_type,
        "sender": sender_id,
        "recipient": recipient_id,
        "payload": payload
    }

    return json.dumps(message)
