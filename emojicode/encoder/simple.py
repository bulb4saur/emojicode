from emojicode.encoder.base import BaseEmojiCode


class Basic(BaseEmojiCode):

    def __init__(self):
        super().__init__()

    def generate_emoji_mapping(self) -> dict:
        return {
            digit: emoji
            for digit, emoji in zip(
                self._hex_digits,
                self._default_emoji_list,
            )
        }

    def encode_message(self, text: str) -> str:
        emoji_mapping = self.generate_emoji_mapping()

        encoded_message = []

        # Iterate over the characters in the message
        for char in text:
            # Convert the character to its ASCII code, then to hex, and map to emojis
            ascii_code = ord(char)
            hex_code = f"{ascii_code:02x}"  # Convert to hex
            emojis = "".join(emoji_mapping[digit] for digit in hex_code)
            # for emoji in emojis:
            #     print(emoji)
            encoded_message.append(emojis)

        return "".join(encoded_message)

    def decode_message(self, text: str) -> str:

        emoji_mapping = self.generate_emoji_mapping()
        inverse_emoji_mapping = {v: k for k, v in emoji_mapping.items()}

        decoded_message = []
        i = 0
        while i < len(text):
            emoji_pair = text[i : i + 2]
            hex_digits_in_pair = ""

            for emoji in emoji_pair:
                if emoji in inverse_emoji_mapping:
                    hex_digit = inverse_emoji_mapping[emoji]
                    hex_digits_in_pair += hex_digit

            ascii_code = int(hex_digits_in_pair, 16)
            decoded_char = chr(ascii_code)
            decoded_message.append(decoded_char)
            i += 2

        return "".join(decoded_message)
