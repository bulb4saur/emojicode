from emojicode.encoder import Basic, Salted, SaltedHashed

ENCODERS = {
    "BASIC": Basic(),
    "SALTED": Salted(),
    "SALTED_HASHED": SaltedHashed(),
}
