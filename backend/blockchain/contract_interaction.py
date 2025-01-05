from web3 import Web3

# Connect to the local blockchain (Ganache)
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Check connection
if not web3.isConnected():
    raise Exception("Cannot connect to Ganache")

# Set default account (first account in Ganache)
web3.eth.default_account = web3.eth.accounts[0]

# Load the contract
contract_address = "<DEPLOYED_CONTRACT_ADDRESS>"
contract_abi = [
    {
        "inputs": [{"internalType": "string", "name": "candidate", "type": "string"}],
        "name": "vote",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [{"internalType": "string", "name": "candidate", "type": "string"}],
        "name": "getVotes",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function"
    }
]

contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# Function to submit a vote
def vote(candidate):
    tx = contract.functions.vote(candidate).transact()
    return tx.hex()

# Function to get votes for a candidate
def get_votes(candidate):
    return contract.functions.getVotes(candidate).call()

