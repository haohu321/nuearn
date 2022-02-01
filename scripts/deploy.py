from brownie import accounts, config, NuVault, network
from typing import List


def deploy_vault():
    account = get_account()
    nu_vault = NuVault.deploy({"from": account})
    add_account_to_vault(
        nu_vault=nu_vault, account_name="Tiger", num_tokens=666, eth_account=account
    )
    add_account_to_vault(
        nu_vault=nu_vault, account_name="Dragon", num_tokens=888, eth_account=account
    )
    print_balance_for_accounts(
        nu_vault=nu_vault, account_names=["Tiger", "Dragon", "testAccount"]
    )


def print_balance_for_accounts(nu_vault: NuVault, account_names: List[str]):
    for account_name in account_names:
        print_balance(nu_vault, account_name)


def print_balance(nu_vault: NuVault, account_name: str):
    num_tokens = nu_vault.getNumTokens(account_name)
    print(f"Balance for {account_name}={num_tokens}")


def add_account_to_vault(
    nu_vault: NuVault,
    account_name: str,
    num_tokens: int,
    eth_account,
    wait_time: int = 1,
):
    transaction = nu_vault.addAccount(account_name, num_tokens, {"from": eth_account})
    transaction.wait(wait_time)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        print(f'config: {config["wallets"]["from_key"]}')
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_vault()
