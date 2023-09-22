from web3 import Web3

w3 = Web3(Web3.HTTPProvider("https://goerli.infura.io/v3/981bf063750e4519be1fd733881c6b59"))
account = w3.eth.account.create()
privateKey = account._private_key.hex()
address = account.address

print(address)
print(privateKey)