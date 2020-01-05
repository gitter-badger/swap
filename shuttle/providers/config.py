# Bytom network
def bytom():
    return {
        "mainnet": {
            "bytom": "http://localhost:9888",
            "blockmeta": "https://blockmeta.com/api/v2",
            "blockcenter": "https://bcapi.bystack.com/api/v2/btm"
        },
        "testnet": {
            "bytom": "http://localhost:9888",
            "blockmeta": "https://blockmeta.com/api/wisdom",
            "blockcenter": "https://bcapi.bystack.com/api/v2/wisdom"
        },
        "timeout": 5,
        "fee": 40000000,
        "confirmations": 40000000,
    }


# Bitcoin network
def bitcoin(blockcypher_token=None):
    if blockcypher_token is None:
        blockcypher_token = "c6ef693d3c024088810e6fac2a1494ee"
    return {
        "mainnet": {
            "coin_type": "0",
            "blockchain": "https://blockchain.info",
            "blockcypher": {
                "url": "https://api.blockcypher.com/v1/btc/main",
                "token": blockcypher_token
            }
        },
        "testnet": {
            "coin_type": "1",
            "blockchain": "https://testnet.blockchain.info",
            "blockcypher": {
                "url": "https://api.blockcypher.com/v1/btc/test3",
                "token": blockcypher_token
            }
        },
        "timeout": 5
    }
