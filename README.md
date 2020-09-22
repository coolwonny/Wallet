# Multi-Blockchain Wallet in Python

In this assignment, we are going to create a code in Python that allows us to transact and manage a blockchain wallet not pertaining to one coin but acrosss 300+ coins. For this assignment, we are to make 2 coins working: **Ethereum** and **Bitcoin Testnet**. Ethereum keys are the same format on any network, so the Ethereum keys should work with your custom networks or testnets.    

The process can be divided into three parts: 
- Writing a function that derives the wallet keys
- Writing a function that links the derived keys to the accouts we want to make a transaction.
- Testing some transactions using the code.
  
### You may see the code either in [Jupyter notebook](https://github.com/coolwonny/Wallet/blob/master/wallet.ipynb) or [wallet.py](https://github.com/coolwonny/Wallet/blob/master/wallet.py).    
    


## Deriving the wallet keys

In this section, we are to create a function using `subprocess` library that derives wallet information such as address, index, path, private key and public key. With this information, we can call each necessary private key for desired transaction.   

## Linking the transaction signing libraries

In this section, we are to create three more functions as below.    

**1. `priv_key_to_account` -- this will convert the privkey string in a child key to an account object
that bit or web3.py can use to transact.
This function needs the following parameters:**
 - coin -- the coin type (defined in [constants.py](https://github.com/coolwonny/Wallet/blob/master/constants.py)).
 - priv_key -- the privkey string will be passed through here.
 - For ETH, return Account.privateKeyToAccount(priv_key)
 - For BTCTEST, return PrivateKeyTestnet(priv_key)

**2. `create_tx` -- this will create the raw, unsigned transaction that contains all metadata needed to transact.
This function needs the following parameters:**
 - coin -- the coin type (defined in [constants.py](https://github.com/coolwonny/Wallet/blob/master/constants.py)).
 - account -- the account object from priv_key_to_account.
 - to -- the recipient address.
 - amount -- the amount of the coin to send.
 - For ETH, return an object containing `to`, `from`, `value`, `gas`, `gasPrice` and `nonce`
 - For BTCTEST, return `PrivateKeyTestnet.prepare_transaction(account.address, [(to, amount, BTC)])`

**3. `send_tx` -- this will call create_tx, sign the transaction, then send it to the designated network.
This function needs the following parameters:**
 - coin -- the coin type (defined in [constants.py](https://github.com/coolwonny/Wallet/blob/master/constants.py)).
 - account -- the account object from priv_key_to_account.
 - to -- the recipient address.
 - amount -- the amount of the coin to send.
 - For ETH, return `w3.eth.sendRawTransaction(signed.rawTransaction)`
 - For BTCTEST, return `NetworkAPI.broadcast_tx_testnet(signed)`    

Once you've signed the transaction, you will need to send it to the designated blockchain network.    

## Send some transactions!

This section is to test some transactions using the Python code we've created.    
  
### 1. Local PoA Ethereum transaction   
We can generate a transaction by calling the `send_tx` function with parameters ETH, eth_account(our account from which the transaction is made), recipient account and amount. For Ethereum, the amount represents in **Wei** so we need to get the exact Wei amount for the desired **Ether** by using **[converter](https://eth-converter.com/)**.    

Here is the code for the test transaction. We sent a value of 3000000000000000000 or equivalent to 3 Ether and we can see a transaction hash `'0xab3beab38d629af21aa34b809ad4835782a16731e199e67ec2f292ac993a6dc1'` generated.     

![eth_test](https://github.com/coolwonny/Wallet/blob/master/images/screenshot_eth_tx_python_.png)
   

The screenshot below shows our Ethereum accounts.     
![ethereum_account](https://github.com/coolwonny/Wallet/blob/705320f5723b0c5f539d5e0d2dab42fe8bf792d1/images/screenshot_eth_accts_after.png)    

And below is the result of transaction above.   
![eth_result](https://github.com/coolwonny/Wallet/blob/master/images/screenshot_eth_tx.png)
    
### 2. Bitcoin Testnet transaction    

Likewise, we now generate a transaction for Bitcoin Testnet. Below is the code for the test transaction. Please note that the amount here is the Bitcoin unit unlike Ethereum we used Wei amount instead. We are going to send 0.002 BTC to the recipient account of `msESMGGnzd5FXx8wjUsUc51MrFaNwUCHMb`.

![btc_test](https://github.com/coolwonny/Wallet/blob/master/images/screenshot_btc_tx_python.png)  
     
Bitcoin takes a time for a transaction to be confirmed because new blocks are mining about every ten minutes while Ethereum takes few seconds.    

The transaction result is as below.   
![btc_result](https://github.com/coolwonny/Wallet/blob/master/images/screenshot_btc_tx.png)    

We can see the outputs on the bottom-right side that 0.002 BTC was transferred to the recipient's account along with the sender's balance after the transaction(here is 0.00735712). The fee for this transaction amounts 0.00026180 BTC, resulting the total transaction amount to be 0.00226180 BTC.    

## Dependencies

- PHP must be installed on your operating system (any version, 5 or 7).

- You will need to clone the **[`hd-wallet-derive`](https://github.com/dan-da/hd-wallet-derive)** tool.

- **[`bit`](https://ofek.dev/bit/)** Python Bitcoin library.
- **[`web3.py`](https://github.com/ethereum/web3.py)** Python Ethereum library.

## hd-wallet-derive Installation

Execute the following steps:

* Navigate to the [Github website](https://github.com/dan-da/hd-wallet-derive) for the `hd-wallet-derive` library and scroll down to the installation instructions.

 ![hd-wallet-derive-github](Images/hd-wallet-derive-github.png)

* Next, open a terminal and execute the following commands. If you are using Windows, you will need to open the `git-bash` GUI via `C:\Program Files\Git\bin\bash.exe` directly to enable something called `tty` mode that makes the terminal more compatible with Unix systems. Once installed, you may move back to using the usual `git-bash` terminal.

 ```shell
 git clone https://github.com/dan-da/hd-wallet-derive
 cd hd-wallet-derive
 php -r "readfile('https://getcomposer.org/installer');" | php
 php -d pcre.jit=0 composer.phar install
 ```

* You should now have a folder called `hd-wallet-derive` containing the PHP library.

