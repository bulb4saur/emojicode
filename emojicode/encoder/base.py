from abc import ABC, abstractmethod


class BaseEmojiCode(ABC):

    _default_emoji_list = [
        "😈",
        "💣",
        "🔪",
        "🖕",
        "💀",
        "👹",
        "🍆",
        "🧨",
        "👽",
        "👾",
        "🤡",
        "🥀",
        "⚡",
        "🔥",
        "💧",
        "💉",
    ]

    _hex_digits = "0123456789abcdef"

    def __init__(self):
        pass

    @abstractmethod
    def generate_emoji_mapping(self, salt: str | None = None) -> dict:
        pass

    @abstractmethod
    def encode_message(self, message: str) -> str:
        pass

    def decode_message(self, encoded_message: str, salt_position: int = 4) -> str:
        # Extract the salt from the third position
        salt = encoded_message[
            salt_position
        ]  # The third position in the emoji sequence (accounting for 2 emojis per character)

        # Regenerate the emoji mapping based on the extracted salt
        emoji_mapping = self.generate_emoji_mapping(salt=salt)
        inverse_emoji_mapping = {v: k for k, v in emoji_mapping.items()}

        decoded_message = []
        i = 0
        while i < len(encoded_message):
            # Skip the salt when decoding
            if i == salt_position:
                i += 1
                continue

            emoji_pair = encoded_message[i : i + 2]  # Extract two emojis (hex pair)
            hex_digits_in_pair = ""

            for emoji in emoji_pair:
                if emoji in inverse_emoji_mapping:
                    hex_digit = inverse_emoji_mapping[emoji]
                    hex_digits_in_pair += hex_digit
                else:
                    print(f"Warning: Emoji '{emoji}' not found in emoji mapping.")

            ascii_code = int(hex_digits_in_pair, 16)
            decoded_char = chr(ascii_code)
            decoded_message.append(decoded_char)
            i += 2  # Move to the next pair of emojis

        return "".join(decoded_message)
