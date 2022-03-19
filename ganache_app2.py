from web3 import Web3

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

account_1 = "0x93898A536069907F9A744932970e400aD5614927"
account_2 = "0x24c6F035b50885d7259Fb9B20fa7A91b2fdEE271"

private_key = "00b87cbd212f17c9fa7c8a8f81d05ca7033774f52dc44d6c1f7731bf2ba42927"

nonce = web3.eth.getTransactionCount(account_1)

tx= {
    'nonce': nonce,
    'to': account_2,
    'value': web3.toWei(5, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('100', 'gwei')
}

signed_tx = web3.eth.account.signTransaction(tx, private_key)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))