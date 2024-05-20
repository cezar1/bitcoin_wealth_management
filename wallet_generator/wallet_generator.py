import click
from mnemonic import Mnemonic
from bip_utils import Bip39SeedGenerator, Bip44, Bip49, Bip84, Bip44Coins, Bip49Coins, Bip84Coins, Bip44Changes

# Function to generate addresses from seed
def generate_addresses(seed, num_addresses, label, coin, change, bip_class):
    bip_mst_ctx = bip_class.FromSeed(seed, coin)
    bip_acc_ctx = bip_mst_ctx.Purpose().Coin().Account(0)
    bip_chg_ctx = bip_acc_ctx.Change(change)

    click.echo(f"\n{label} Addresses:")
    for i in range(num_addresses):
        bip_addr_ctx = bip_chg_ctx.AddressIndex(i)
        click.echo(f"Address {i + 1}: {bip_addr_ctx.PublicKey().ToAddress()}")
        click.echo(f"Private Key {i + 1}: {bip_addr_ctx.PrivateKey().Raw().ToHex()}")

# Function to generate a new wallet
@click.command()
@click.option('--num-addresses', default=5, help='Number of addresses to generate.')
def generate_new_wallet(num_addresses):
    mnemo = Mnemonic("english")
    mnemonic_24_words = mnemo.generate(strength=256)
    click.echo(f"24-word mnemonic: {mnemonic_24_words}")
    seed = Bip39SeedGenerator(mnemonic_24_words).Generate()
    generate_all_addresses(seed, num_addresses)

# Function to generate wallet from existing mnemonic
@click.command()
@click.option('--num-addresses', default=5, help='Number of addresses to generate.')
@click.argument('mnemonic_24_words')
def generate_wallet_from_mnemonic(num_addresses, mnemonic_24_words):
    seed = Bip39SeedGenerator(mnemonic_24_words).Generate()
    generate_all_addresses(seed, num_addresses)

# Function to generate all types of addresses
def generate_all_addresses(seed, num_addresses):
    generate_addresses(seed, num_addresses, "Legacy (P2PKH)", Bip44Coins.BITCOIN, Bip44Changes.CHAIN_EXT, Bip44)
    generate_addresses(seed, num_addresses, "P2SH-SegWit (P2WPKH in P2SH)", Bip49Coins.BITCOIN, Bip44Changes.CHAIN_EXT, Bip49)
    generate_addresses(seed, num_addresses, "Native SegWit (Bech32)", Bip84Coins.BITCOIN, Bip44Changes.CHAIN_EXT, Bip84)

@click.group()
def cli():
    pass

cli.add_command(generate_new_wallet)
cli.add_command(generate_wallet_from_mnemonic)

if __name__ == '__main__':
    cli()
