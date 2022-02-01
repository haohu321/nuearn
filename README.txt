# Note
Currently the SmartContract associated with this repo is deployed
to ropsten testnet. You can play with it by just setting up Python & Node
following the instructions below.

The web app uses Node Web3 module to send request to the Eth node on Infura.
Currently only the ropsten testnet endpoint is used (to save money for testing).
Swapping with mainnet should be super easy.

# Development Environment Setup
## MacOS
1. Setup Python & Pip
`brew install python3`

2. Setup Brownie
* Note, this is only needed if you want to development smart contract. Otherwise skip to the next step.

`pip3 install eth-brownie`

3. Setup Node
`brew install node && npm install web3`

## Deploy Smart Contract
`brownie run scripts/deploy.py [--network ${YOUR_DESIRED_ETH_NETWORK}`

## To test with the toy index page:
1. Inside the repor directory, run:
  `python -m SimpleHTTPServer 8000`

2. In the browser, access localhost:8000
3. You should be able to see an naive html page that lets you query vaultInfo and balance for account.
Currently only account "Tiger" and "Dragon" has positive balance. Feel free to try it out.






