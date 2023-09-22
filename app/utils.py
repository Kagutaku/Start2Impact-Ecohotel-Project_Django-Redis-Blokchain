from web3 import Web3

def sendTransaction(message):
    w3 = Web3(Web3.HTTPProvider('https://goerli.infura.io/v3/981bf063750e4519be1fd733881c6b59'))
    address = '0x7717a3a6a4737Ea5DdE6cD6409C6f6B302222dDf'
    privateKey = '0xc15ddee83c9b2e9f3c7d401938582fd19184ba2ac1a85dc5b011564ed530a232'
    nonce = w3.eth.getTransactionCount(address)
    gasPrice = w3.eth.gasPrice
    value = w3.toWei(0,'ether')
    signedTx = w3.eth.account.signTransaction(dict(
        nonce=nonce,
        gasPrice=gasPrice,
        gas=100000,
        to='0x0000000000000000000000000000000000000000',
        value=value,
        data=message.encode('utf-8')
    ), privateKey)

    tx = w3.eth.sendRawTransaction(signedTx.rawTransaction)
    txId = w3.toHex(tx)
    return txId
