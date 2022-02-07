#!/usr/bin/python

import json
import requests
from web3 import Web3

def fetch_abi(address):
    ABI_ENDPOINT = 'https://rinkeby.etherscan.io/api?module=contract&action=getabi&address='

    response = requests.get('%s%s'%(ABI_ENDPOINT, address))
    response_json = response.json()
    abi_json = json.loads(response_json['result'])
    result = json.dumps(abi_json)
    
    return result

def __main__():
    # Enter your own Ethereum blockchain endpoint (Infura or equivalent)
    infura_url = "https://rinkeby.infura.io/v3/00000000000000000000"
    web3 = Web3(Web3.HTTPProvider(infura_url))

    # Enter address of the Smart Contract (From)
    contract_address = web3.toChecksumAddress("0x00000000000000000000")
    print("Minting from contract: " + contract_address)
    
    # Enter Smart Contract's ABI (can get this from etherscan.io)
    #abi = fetch_abi(contract_address)
    abi = '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"approved","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[],"name":"MAX_SUPPLY","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"approve","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getApproved","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"mintRate","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"safeMint","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenOfOwnerByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"tokenURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"transferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"}]'
    contract = web3.eth.contract(address=contract_address, abi=abi)

    abi_output = json.loads(abi)
    array_length = len(abi_output)

    # Enter contract owner's wallet address
    contractowner_address = "0x00000000000000000000"
    # Enter contract owner's private key (SENSITIVE! Don't store this here in production)
    contactowner_private_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

    # Enter the purchaser's (To) wallet address
    towallet_address = "0x00000000000000000000"
    print("Minting to wallet address: " + towallet_address)

    # get the nonce
    nonce = web3.eth.getTransactionCount(contractowner_address)
    print("Nonce:", nonce)

    # Build the transaction
    # 'gas' is the gas fee you pay in Wei (in this case, 1,000,000 Wei = 0.000000000001 ETH)
    # 'value' is the amount you pay for the transaction (in this case, 10 Finney = 0.01 ETH)
    tx = contract.functions.safeMint(
        towallet_address).buildTransaction({
        'gas': 1000000,
        'gasPrice': web3.toWei('1', 'gwei'),
        'from': contractowner_address,
        'nonce': nonce,
        'value': web3.toWei('10', 'finney'),
        }) 

    # Sign the transaction
    print("Signing transaction")
    signed_txn = web3.eth.account.signTransaction(tx, private_key=contactowner_private_key)
    # Process the transaction
    print("Sending transaction")
    txn_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    # Print the confirmed transaction hash
    print("Transaction Successful!\nTransaction Hash:")
    print(web3.toHex(txn_hash))


if __name__ == '__main__':
    __main__()
