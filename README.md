# 🌈 Emoji Secret Message Encoder 🔐

Welcome to the Emoji Secret Message Encoder! Ever wanted to smuggle a message through a series of random emojis? With this project, you can encode your messages into seemingly nonsensical emoji strings, then share them with friends who can decode them back into plain text. It’s cryptography - but with emojis! 🎉

## 🚀 Features

-  ASCII to Emoji Encoding: Converts each character into a unique sequence of emojis.
- Randomized Salt for Added Security: Adds a layer of randomness to ensure each encoded message is unique.
- Hashed Salt for Extra Obfuscation: Uses SHA-256 hashing to mix things up and make the encoding even harder to crack.
- Decode to Original Message: Includes a decoder that reverses the process for the rightful recipient.

## 📖 How It Works

- Convert Characters to ASCII and Hex: Each letter is converted to its ASCII value and then to hexadecimal.
- Map Hex to Emojis: Hexadecimal digits are mapped to specific emojis, creating the encoded message.
- Add a Salt: A random emoji (salt) is inserted to shuffle the encoding and make each message unique.
- Hash the Salt for Unpredictability: The salt is hashed to scramble the emoji mapping, using SHA-256 to make it impossible to reverse-engineer.
- Decode: The decoder extracts the salt, regenerates the emoji mapping, and retrieves the original message.

## 🔧 Setup

- Clone the repository:
- Install dependencies: We use Poetry to manage dependencies. Install Poetry if you haven’t already.

```bash
    poetry install
```

## 🛠️ Usage

```python
    from emojicode.emojicode import ENCODERS # Import encoders

    # EXAMPLE SALTED-HASHED USAGE
    print("EXAMPLE SALTED HASHED")
    encoder = ENCODERS["SALTED_HASHED"]  # Create an instance of the SaltedHashed encoder
    encoded_message = encoder.encode_message("Hello")  # Encode a message
    print(f"Encoded Message: {encoded_message}")  # Print the encoded message
    decoded_message = encoder.decode_message(encoded_message)  # Decode the message
    print(f"Decoded Message: {decoded_message}")  # Print the decoded message`
```


## 🎓 Example Walkthrough

Want to see how encoding works? Here’s a quick overview:

- Encoding ‘Hello’:
    - Converts ‘Hello’ to ASCII, then to hex.
    - Maps each hex digit to an emoji.
    - Adds a random salt to make the encoding unique.

- Decoding:
    - Reads the salt to recreate the emoji mapping.
    - Translates emojis back to hex, then to ASCII, and finally to the original message.

## 👽 Contribute

Got ideas for more encryption features or just want to add more emoji options? Fork the repo and submit a PR! Or open an issue with your suggestions.

## 📜 License

This project is licensed under the [MIT License](LICENSE).

## 🔮 Follow the Madness

- Follow the Conspiracy Bot on Twitter: [@fake_the_garlic](https://x.com/fake_the_garlic)
- Join our Discord: [Community](https://discord.gg/drG2JcWb)
- Youtube channel: [Youtube](https://www.youtube.com/@bugandbyte)

## Disclaimer

This project is for fun and educational purposes only. It’s not meant to replace actual encryption methods for sensitive data. Use responsibly! 😉
