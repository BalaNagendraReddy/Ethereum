# Build Ethereum Dapps with python
import json
from web3 import Web3

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

web3.eth.defaultAccount = web3.eth.accounts[0]

abi = json.loads('[{"constant":false,"inputs":[{"name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"greet","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"greeting","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]')
# Remix.Ethereum.org->Deploy and run Transactions-> Deployed Contracts Address
address = Web3.toChecksumAddress("0xF1035e1Dd892685527D17D3E2B65A231e595fcF3")

contract = web3.eth.contract(address= address, abi=abi)
print(contract.functions.greet().call())

tx_hash = contract.functions.setGreeting('NEW GREETING3').transact()
print(tx_hash)
print(web3.toHex(tx_hash))

web3.eth.waitForTransactionReceipt(tx_hash)

print('Updated greeting: {}'.format(
    contract.functions.greet().call()
))
