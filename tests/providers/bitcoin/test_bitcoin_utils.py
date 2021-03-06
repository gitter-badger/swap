#!/usr/bin/env python3

from swap.providers.bitcoin.utils import *
from swap.utils.exceptions import AddressError, NetworkError

import pytest


def test_bitcoin_utils():

    assert expiration_to_script(7) == "OP_7"

    assert str(script_from_address("2N3NKQpymf1KunR4W8BpZjs8za5La5pV5hF", "testnet"))

    assert address_to_hash("mrmtGq2HMmqAogSsGDjCtXUpxrb7rHThFH") == \
           "7b7c4431a43b612a72f8229935c469f1f6903658"

    assert is_address("3DRqFYMG2dFpVb8uTpCu8WoBhRBQ2FCphb", "mainnet")
    assert is_address("3DRqFYMG2dFpVb8uTpCu8WoBhRBQ2FCphb")
    assert expiration_to_script(17)


def test_bitcoin_utils_exceptions():

    with pytest.raises(ValueError, match="invalid Bitcoin transaction raw"):
        decode_transaction_raw("YXNkZg==")

    with pytest.raises(ValueError, match="invalid Bitcoin transaction raw"):
        decode_transaction_raw("eyJub25lIjogbnVsbH0=")

    with pytest.raises(TypeError, match="transaction raw must be string format!"):
        submit_payment(int(123))

    with pytest.raises(ValueError, match="invalid Bitcoin transaction raw"):
        submit_transaction_raw("YXNkZg==")

    with pytest.raises(ValueError, match="invalid Bitcoin transaction raw"):
        submit_transaction_raw("eyJub25lIjogbnVsbH0=")

    with pytest.raises(TypeError, match="address must be string format!"):
        is_address(int(123214213213213))

    with pytest.raises(NetworkError, match=r"invalid .*"):
        is_address("mrmtGq2HMmqAogSsGDjCtXUpxrb7rHThFH", "unknown")

    with pytest.raises(TypeError, match="Sequence must be integer format!"):
        expiration_to_script(str("unknown"))

    with pytest.raises(AddressError, match=r"invalid .*"):
        script_from_address("mrmtGq2HMmqAogSsGDjCtXUpxrb7rHThFH", "mainnet")

    with pytest.raises(AddressError, match=r"invalid .*"):
        address_to_hash("mrmtGq2HMmqAogSsGDjCtXUpxrb7rHThFH", "mainnet")
