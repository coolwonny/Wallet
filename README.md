# Multi-Blockchain Wallet in Python

In this assignment, we are going to create a code in Python that allows us to transact and manage a blockchain wallet not pertaining to one coin but acrosss 300+ coins. For this assignment, we are to make 2 coins working: Ethereum and Bitcoin Testnet. Ethereum keys are the same format on any network, so the Ethereum keys should work with your custom networks or testnets.    

The process can be divided into three parts: 
- Writing a function that derives the wallet keys
- Writing a function that links the derived keys to the accouts we want to make a transaction.
- Testing some transactions using the code.

## Deriving the wallet keys

In this section, we are to create a function using `subprocess` library that derives wallet information such as address, index, path, private key and public key. With this information, we can call each necessary private key for desired transaction.   

## Linking the transaction signing libraries

In this section, we are to create three more functions as below.    

1. `priv_key_to_account` -- this will convert the privkey string in a child key to an account object
that bit or web3.py can use to transact.
This function needs the following parameters:
- coin -- the coin type (defined in constants.py).
- priv_key -- the privkey string will be passed through here.
- For ETH, return Account.privateKeyToAccount(priv_key)
- For BTCTEST, return PrivateKeyTestnet(priv_key)

2. `create_tx` -- this will create the raw, unsigned transaction that contains all metadata needed to transact.
This function needs the following parameters:
- coin -- the coin type (defined in constants.py).
- account -- the account object from priv_key_to_account.
- to -- the recipient address.
- amount -- the amount of the coin to send.
- For ETH, return an object containing `to`, `from`, `value`, `gas`, `gasPrice` and `nonce`
- For BTCTEST, return `PrivateKeyTestnet.prepare_transaction(account.address, [(to, amount, BTC)])`

3. `send_tx` -- this will call create_tx, sign the transaction, then send it to the designated network.
This function needs the following parameters:
- coin -- the coin type (defined in constants.py).
- account -- the account object from priv_key_to_account.
- to -- the recipient address.
- amount -- the amount of the coin to send.
- For ETH, return `w3.eth.sendRawTransaction(signed.rawTransaction)`
- For BTCTEST, return `NetworkAPI.broadcast_tx_testnet(signed)`    

Once you've signed the transaction, you will need to send it to the designated blockchain network.    






