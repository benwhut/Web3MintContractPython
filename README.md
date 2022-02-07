# Web3MintContractPython
Example of how to mint an Ethereum based token from a given Smart Contract using Web3 in Python

1. Create Python virtual environment (optional)  
`python -m venv venv`  
`source venv/bin/activate`

2. Install web3.py  
`pip install web3`

3. Enter your Ethereum endpoint URL using Infura or equivalent  
This is required to query the Ethereum blockchain  
`infura_url = "https://rinkeby.infura.io/v3/00000000000000000000000"`  

4. Enter the address and ABI of the Smart Contract (From)  
You can get this from etherscan.io  
`contract_address = web3.toChecksumAddress("0x00000000000000000000000")`  
`abi = '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"} ... ]'`  

5. Enter the Smart Contract owner's wallet address and private key  
WARNING: the Private Key is SENSITIVE and should NOT be stored here in production!! This is stored here in this example to keep things simple  
`contractowner_address = "0x00000000000000000000000"`  
`contactowner_private_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"`  

6. Enter the the purchaser's (To) wallet address  
`towallet_address = "0x00000000000000000000000"`  

7. In build the transaction (tx), specify the gas and price to be paid  
'gas' is the gas fee you pay in Wei (in the example below, 1,000,000 Wei = 0.000000000001 ETH)  
'value' is the amount you pay to mint the token (in the example below, 10 Finney = 0.01 ETH)  
```
tx = contract.functions.safeMint(
    towallet_address).buildTransaction({
    'gas': 1000000,
    'gasPrice': web3.toWei('1', 'gwei'),
    'from': contractowner_address,
    'nonce': nonce,
    'value': web3.toWei('10', 'finney'),
    }) 
```

8. run web3MintContract.py  
`python3 web3MintContract.py`  


Output should be similar to this:  

```
Minting from contract: 0x00000000000000000000000
Minting to wallet address: 0x00000000000000000000000
Nonce: 69
Signing transaction
Sending transaction
Transaction Successful!
Transaction Hash:
0x000000000000000000000000000000000000000
```

Questions?  
benwhut@gmail.com
