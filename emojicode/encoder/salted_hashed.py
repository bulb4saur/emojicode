import hashlib
import random

from emojicode.encoder.base import BaseEmojiCode


class SaltedHashed(BaseEmojiCode):

    def __init__(self):
        super().__init__()

    def generate_emoji_mapping(self, salt: str | None = None) -> dict:
        # STEP 1: Hash the salt to create a uniform 64-character string.
        # This ensures that even small changes to the salt lead to a completely different hash.
        salt_hash = hashlib.sha256(salt.encode("utf-8")).hexdigest()

        # STEP 2: Shuffle the hexadecimal digits ('0' - 'f') using the salt_hash.
        # Each hex digit ('0'-'f') is concatenated with the salt_hash and hashed again.
        # The resulting hash is used as a key to sort the hex digits in a new order.
        # This ensures that the hex digits are shuffled uniquely based on the salt.
        shuffled_hex_digits = sorted(
            self._hex_digits,
            key=lambda x: hashlib.sha256((x + salt_hash).encode("utf-8")).hexdigest(),
        )

        # STEP 3: Create the emoji mapping by pairing shuffled hex digits with emojis.
        # The shuffled hex digits are mapped to a predefined list of emojis.
        # This final mapping is what we use to convert hex values into emojis.
        return {
            digit: emoji
            for digit, emoji in zip(shuffled_hex_digits, self._default_emoji_list)
        }

    def encode_message(self, text: str) -> str:
        salt = random.choice(self._default_emoji_list)  # Choose a random emoji as salt
        print(f"Random Salt Chosen: {salt}")

        # Generate the emoji mapping based on the random salt
        emoji_mapping = self.generate_emoji_mapping(salt=salt)

        encoded_message = []
        salt_inserted = False

        # Iterate over the characters in the message
        for i, char in enumerate(text):
            if i == 2 and not salt_inserted:
                # Insert the salt at the third position
                encoded_message.append(salt)
                salt_inserted = True

            # Convert the character to its ASCII code, then to hex, and map to emojis
            ascii_code = ord(char)
            hex_code = f"{ascii_code:02x}"  # Convert to hex
            emojis = "".join(emoji_mapping[digit] for digit in hex_code)
            encoded_message.append(emojis)

        return "".join(encoded_message)
