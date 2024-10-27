from emojicode import ENCODERS

# EXAMPLE BASIC USAGE
print("EXAMPLE BASIC")
encoder = ENCODERS["BASIC"]  # Create an instance of the Basic encoder
encoded_message = encoder.encode_message("Hello")  # Encode a message
print(f"Encoded Message: {encoded_message}")  # Print the encoded message
decoded_message = encoder.decode_message(encoded_message)  # Decode the message
print(f"Decoded Message: {decoded_message}")  # Print the decoded message
print("\n")

# EXAMPLE SALTED USAGE
print("EXAMPLE SALTED")
encoder = ENCODERS["SALTED"]  # Create an instance of the Salted encoder
encoded_message = encoder.encode_message("Hello")  # Encode a message
print(f"Encoded Message: {encoded_message}")  # Print the encoded message
decoded_message = encoder.decode_message(encoded_message)  # Decode the message
print(f"Decoded Message: {decoded_message}")  # Print the decoded message
print("\n")

# EXAMPLE SALTED-HASHED USAGE
print("EXAMPLE SALTED HASHED")
encoder = ENCODERS["SALTED_HASHED"]  # Create an instance of the SaltedHashed encoder
encoded_message = encoder.encode_message("Hello")  # Encode a message
print(f"Encoded Message: {encoded_message}")  # Print the encoded message
decoded_message = encoder.decode_message(encoded_message)  # Decode the message
print(f"Decoded Message: {decoded_message}")  # Print the decoded message
print("\n")
