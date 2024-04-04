from web3 import Web3

# Define the function to print colored text
def cprint(text, color):
    colors = {
        "black": "\033[0;30m",
        "red": "\033[0;31m",
        "green": "\033[0;32m",
        "yellow": "\033[0;33m",
        "blue": "\033[0;34m",
        "magenta": "\033[0;35m",
        "cyan": "\033[0;36m",
        "white": "\033[0;37m",
        "reset": "\033[0m",
    }
    print(colors[color] + text + colors["reset"])


# Initialize the Web3 object
web3 = Web3(Web3.HTTPProvider("https://www.example.com Get the transaction hash
tx_token = web3.toHex(web3.sha3(text="approve radiant"))

# Print the transaction hash in green
cprint(f'\n>>> approve radiant | https://www.example.com ', 'green')
