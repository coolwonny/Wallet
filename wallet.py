from constants import *
import subprocess
import json
import os
from dotenv import load_dotenv
from web3 import Web3
from web3.middleware import geth_poa_middleware
from eth_account import Account
from pathlib import Path
from getpass import getpass
from bit import PrivateKeyTestnet
from bit.network import NetworkAPI

# Load mnemonic in env file and assign it a variable called 'mnemonic'
load_dotenv('c:/Users/Sungwon Kim/fintech/.env')
mnemonic = os.getenv('MNEMONIC_2')

def derive_wallets(mnemonic, coin, numderive):
    command = f'php hd-wallet-derive/hd-wallet-derive.php -g --mnemonic="{mnemonic}" --coin="{coin}" --numderive="{numderive}" --cols=address,index,path,privkey,pubkey,pubkeyhash,xprv,xpub --format=json'
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()

    keys = json.loads(output)
    # print all the addresses
    return keys

# Create an object called coins that derives ETH and BTCTEST wallets with this function
coin = [ETH, BTCTEST]
# Create a dictionary comprehension for the list of coin.
coins = {k:v for k in coin for v in [derive_wallets(mnemonic, k, 3)]}

#  Add middleware to web3.py to support the PoA algorithm
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

def priv_key_to_account(coin, priv_key):
    if coin == ETH:
        return Account.privateKeyToAccount(priv_key)
    elif coin == BTCTEST:
        return PrivateKeyTestnet(priv_key)

# For convenience, contain the account information by assigning them variables
eth_account = priv_key_to_account(ETH, coins['eth'][0]['privkey'])
btc_account = priv_key_to_account(BTCTEST, coins['btc-test'][0]['privkey'])

def create_tx(coin, account, to, amount):
    if coin == ETH:
        gasEstimate = w3.eth.estimateGas(
        {"from": account.address, "to": to, "value": amount}
    )
        return {
            "to": to,
            "from": account.address,
            "value": amount,
            "gas": gasEstimate,
            "gasPrice": w3.eth.gasPrice,
            "nonce": w3.eth.getTransactionCount(account.address),
            
    }
    elif coin == BTCTEST:
        return PrivateKeyTestnet.prepare_transaction(account.address, [(to, amount, BTC)])

def send_tx(coin, account, to, amount):
    tx = create_tx(coin, account, to, amount)
    if coin == ETH:
        signed_tx = account.sign_transaction(tx)
        result = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        return result.hex()
    elif coin == BTCTEST:
        signed_tx = account.sign_transaction(tx)
        return NetworkAPI.broadcast_tx_testnet(signed_tx)


