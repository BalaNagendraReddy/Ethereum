from web3 import Web3

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

account_1 = "0x100DD4B341f79DA8277e2989363Bf6259adD5AB2"
account_2 = "0x93898A536069907F9A744932970e400aD5614927"

private_key = "b90325bc7e80ccea0fac99ac75093d7ece5d43a648ba16498b21b440b5670bd0"

nonce = web3.eth.getTransactionCount(account_1)

tx= {
    'nonce': nonce,
    'to': account_2,
    'value': web3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('100', 'gwei')
}

signed_tx = web3.eth.account.signTransaction(tx, private_key)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))