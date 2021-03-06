#!/usr/bin/env python3

from mnemonic.mnemonic import Mnemonic
from binascii import hexlify, unhexlify
from random import choice

import string
import os
import hashlib

# Alphabet and digits.
letters = string.ascii_letters + string.digits


def generate_passphrase(length=32):
    """
    Generate entropy hex string.

    :param length: Passphrase length, default to 32.
    :type length: int
    :returns:  str -- Passphrase hex string.

    >>> from swap.utils import generate_passphrase
    >>> generate_passphrase(length=32)
    "N39rPfa3QvF2Tm2nPyoBpXNiBFXJywTz"
    """

    return str().join(choice(letters) for _ in range(length))


def generate_entropy(strength=128):
    """
    Generate entropy hex string.

    :param strength: Entropy strength, default to 128.
    :type strength: int
    :returns:  str -- Entropy hex string.

    >>> from swap.utils import generate_entropy
    >>> generate_entropy(strength=128)
    "ee535b143b0d9d1f87546f9df0d06b1a"
    """

    if strength not in [128, 160, 192, 224, 256]:
        raise ValueError(
            "Strength should be one of the following "
            "[128, 160, 192, 224, 256], but it is not (%d)."
            % strength
        )
    return hexlify(os.urandom(strength // 8)).decode()


def generate_mnemonic(language="english", strength=128):
    """
    Generate 12 word mnemonic.

    :param language: Mnemonic language, default to english.
    :type language: str
    :param strength: Entropy strength, default to 128.
    :type strength: int
    :returns:  mnemonic -- 12 word mnemonic.

    >>> from swap.utils import generate_mnemonic
    >>> generate_mnemonic(language="french")
    "sceptre capter séquence girafe absolu relatif fleur zoologie muscle sirop saboter parure"
    """

    if language and language not in ["english", "french", "italian", "japanese",
                                     "chinese_simplified", "chinese_traditional", "korean", "spanish"]:
        raise ValueError("invalid language, use only this options english, french, "
                         "italian, spanish, chinese_simplified, chinese_traditional, japanese or korean languages.")
    if strength not in [128, 160, 192, 224, 256]:
        raise ValueError(
            "Strength should be one of the following "
            "[128, 160, 192, 224, 256], but it is not (%d)."
            % strength
        )

    return Mnemonic(language=language).generate(strength=strength)


def is_mnemonic(mnemonic, language=None):
    """
    Check 12 word mnemonic is Valid.

    :param mnemonic: 12 word mnemonic.
    :type mnemonic: str
    :param language: Mnemonic language, default to None.
    :type language: str
    :returns:  mnemonic -- True/False.

    >>> from swap.utils import is_mnemonic
    >>> is_mnemonic("sceptre capter séquence girafe absolu relatif fleur zoologie muscle sirop saboter parure")
    True
    """

    if language and language not in ["english", "french", "italian", "japanese",
                                     "chinese_simplified", "chinese_traditional", "korean", "spanish"]:
        raise ValueError("invalid language, use only this options english, french, "
                         "italian, spanish, chinese_simplified, chinese_traditional, japanese or korean languages.")
    try:
        if language is None:
            for _language in ["english", "french", "italian",
                              "chinese_simplified", "chinese_traditional", "japanese", "korean", "spanish"]:
                valid = False
                if Mnemonic(language=_language).check(mnemonic=mnemonic) is True:
                    valid = True
                    break
            return valid
        else:
            return Mnemonic(language=language).check(mnemonic=mnemonic)
    except:
        return False


def get_mnemonic_language(mnemonic):
    """
    Get mnemonic language.

    :param mnemonic: 12 word mnemonic.
    :type mnemonic: str
    :returns:  language -- Mnemonic language.

    >>> from swap.utils import get_mnemonic_language
    >>> get_mnemonic_language("sceptre capter séquence girafe absolu relatif fleur zoologie muscle sirop saboter parure")
    "french"
    """

    if not is_mnemonic(mnemonic=mnemonic):
        raise ValueError("invalid 12 word mnemonic.")

    language = None
    for _language in ["english", "french", "italian",
                      "chinese_simplified", "chinese_traditional", "japanese", "korean", "spanish"]:
        if Mnemonic(language=_language).check(mnemonic=mnemonic) is True:
            language = _language
            break
    return language


def sha256(data):
    """
    SHA256 hash.

    :param data: encoded data.
    :type data: str, bytes
    :returns: str -- hashed sha256.

    >>> from swap.utils import sha256
    >>> sha256("Hello Meheret!")
    "3a26da82ead15a80533a02696656b14b5dbfd84eb14790f2e1be5e9e45820eeb"
    """

    if isinstance(data, str):
        return hashlib.sha256(data.encode()).digest().hex()
    elif isinstance(data, bytes):
        return hashlib.sha256(data).digest().hex()
    raise TypeError("data must be str/bytes format!")


def double_sha256(data):
    """
    Double SHA256 hash.

    :param data: encoded data.
    :type data: str, bytes
    :returns: bytearray -- hashed double sha256.

    >>> from swap.utils import double_sha256
    >>> double_sha256("Hello Meheret!")
    "821124b554d13f247b1e5d10b84e44fb1296f18f38bbaa1bea34a12c843e0158"
    """

    if isinstance(data, str) or isinstance(data, bytes):
        return hashlib.sha256(unhexlify(sha256(data))).digest().hex()
    raise TypeError("data must be str/bytes format!")
