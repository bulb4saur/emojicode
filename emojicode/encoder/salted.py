import random

from emojicode.encoder.base import BaseEmojiCode


class Salted(BaseEmojiCode):

    def __init__(self):
        super().__init__()

    def generate_emoji_mapping(self, salt: str | None = None) -> dict:
        """
        Generate a mapping between hex digits and emojis using the salt for added randomness.
        """

        # Convert the salt (an emoji) into its ASCII value for shifting the hex digits
        salt_value = ord(salt)

        # Shuffle the hex digits based on the salt's ASCII value, ensuring randomness
        shuffled_hex_digits = sorted(
            self._hex_digits,
            key=lambda x: (ord(x) + salt_value) % len(self._hex_digits),
        )

        # Create a mapping between the shuffled hex digits and the default emoji list
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
