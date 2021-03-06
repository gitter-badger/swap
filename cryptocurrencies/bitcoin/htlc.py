#!/usr/bin/env python3

from swap.providers.bitcoin.wallet import Wallet
from swap.providers.bitcoin.htlc import HTLC
from swap.providers.bitcoin.rpc import get_balance
from swap.utils import sha256


# Bitcoin network
NETWORK = "testnet"
# Secret password/passphrase hash
SECRET_HASH = sha256("Hello Meheret!")
# Recipient Bitcoin address
RECIPIENT_ADDRESS = "mwHXvCcug5Rn24c2rpgcRDSo3PyfxZJQQT"
# Sender Bitcoin address
SENDER_ADDRESS = "miAcLpYbaqE8KowBu2PwvqXG6y6vpQcfTJ"
# Expiration block (Sequence)
SEQUENCE = 1000

print("=" * 10, "Sender Bitcoin Account")

# Initializing sender Bitcoin wallet
sender_wallet = Wallet(network=NETWORK)
# Initializing Bitcoin wallet from address
sender_wallet.from_address(address=SENDER_ADDRESS)
# Getting sender wallet information's
sender_address = sender_wallet.address()
print("Sender Address:", sender_address)
sender_hash = sender_wallet.hash()
print("Sender Hash:", sender_hash)
sender_p2pkh = sender_wallet.p2pkh()
print("Sender P2PKH:", sender_p2pkh)
sender_p2sh = sender_wallet.p2sh()
print("Sender P2SH:", sender_p2sh)
sender_balance = sender_wallet.balance()
print("Sender Balance:", sender_balance)

print("=" * 10, "Recipient Bitcoin Account")

# Initializing recipient Bitcoin wallet
recipient_wallet = Wallet(network=NETWORK)
# Initializing Bitcoin wallet from address
recipient_wallet.from_address(address=RECIPIENT_ADDRESS)
# Getting recipient wallet information's
recipient_address = recipient_wallet.address()
print("Recipient Address:", recipient_address)
recipient_hash = recipient_wallet.hash()
print("Recipient Hash:", recipient_hash)
recipient_p2pkh = recipient_wallet.p2pkh()
print("Recipient P2PKH:", recipient_p2pkh)
recipient_p2sh = recipient_wallet.p2sh()
print("Recipient P2SH:", recipient_p2sh)
recipient_balance = recipient_wallet.balance()
print("Recipient Balance:", recipient_balance)

print("=" * 10, "Hash Time Lock Contract (HTLC) between Sender and Recipient")

# Initializing Hash Time Lock Contract (HTLC)
htlc = HTLC(network=NETWORK)
# Building new HTLC contract
htlc.init(
    secret_hash=SECRET_HASH,
    recipient_address=recipient_address,
    sender_address=sender_address,
    sequence=SEQUENCE,
)

htlc_bytecode = htlc.bytecode()
print("HTLC Bytecode:", htlc_bytecode)
htlc_opcode = htlc.opcode()
print("HTLC OP_Code:", htlc_opcode)
htlc_hash = htlc.hash()
print("HTLC Hash:", htlc_hash)
htlc_address = htlc.address()
print("HTLC Address:", htlc_address)

# Getting HTLC balance
htlc_balance = get_balance(address=htlc_address, network=NETWORK)
print("HTLC Balance:", htlc_balance)
