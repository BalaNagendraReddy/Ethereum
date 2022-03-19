import json
from web3 import Web3

infura_url = "https://mainnet.infura.io/v3/61e02d4293e94c93b9829a8257255216"
web3 = Web3(Web3.HTTPProvider(infura_url))

latest = web3.eth.blockNumber
print(latest)
print(web3.eth.getBlock(latest))

for i in range(0,10):
    print(web3.eth.getBlock(latest-10))

hash = '0x03e38a5a8ffed91599b731f94f84614e10afbd290959f0c20f2b3137333b17eb'
print(web3.eth.getTransactionByBlock(hash, 2))


