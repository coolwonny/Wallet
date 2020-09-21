from constants import *
import subprocess
import json
import os

# mnemonic = os.getenv('MNEMONIC', 'van spirit reward accident opera load option slow fortune acid picnic genuine')
# The php command that will get our derived addresses
# --coin ETH will derive ethereum addresses
# --format=json changes the terminal output to json format
def derive_wallets(mnemonic, coin, numderive):
    command = f'php hd-wallet-derive/hd-wallet-derive.php -g --mnemonic="{mnemonic}" --coin ="{coin}" --numderive="{numderive}" --cols=path,address,privkey,pubkey --format=json'

    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()

    keys = json.loads(output)
    # print all the addresses
    return keys

derive_wallets('van spirit reward accident opera load option slow fortune acid picnic genuine', BTC, 3)

