from setuptools import setup, find_packages

setup(
    name='bitcoin_wealth_management',
    version='0.21',
    packages=find_packages(),
    install_requires=[
        'click',
        'mnemonic',
        'bip_utils',
    ],
    entry_points={
        'console_scripts': [
            'generate-new-wallet=wallet_generator.wallet_generator:generate_new_wallet',
            'generate-wallet-from-mnemonic=wallet_generator.wallet_generator:generate_wallet_from_mnemonic',
        ],
    },
)
