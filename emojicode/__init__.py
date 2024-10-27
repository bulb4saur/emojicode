from emojicode.encoder.salted import Salted
from emojicode.encoder.salted_hashed import SaltedHashed
from emojicode.encoder.simple import Basic

ENCODERS = {
    "BASIC": Basic(),
    "SALTED": Salted(),
    "SALTED_HASHED": SaltedHashed(),
}
