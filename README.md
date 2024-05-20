**Bitcoin Wealth Management Script**
===============================

This script provides a simple way to generate addresses from a seed or a 24-word mnemonic. It supports various types of addresses, including Legacy (P2PKH), P2SH-SegWit (P2WPKH in P2SH), and Native SegWit (Bech32).

**Getting Started**
-------------------

To get started, you'll need to install the required dependencies:

* `click`
* `mnemonic`
* `bip_utils`

You can do this using pip:
```
pip install click mnemonic bip-utils
```
Once installed, you can run the script using the following commands:

* `generate-new-wallet`: generates a new wallet with 5 addresses (default)
* `generate-wallet-from-mnemonic`: generates a wallet from an existing 24-word mnemonic

**Examples**
------------

### Generate New Wallet
--------------------

```bash
$ generate-new-wallet --num-addresses=10
```
This will generate a new wallet with 10 addresses.

### Generate Wallet from Mnemonic
------------------------------

```bash
$ generate-wallet-from-mnemonic --num-addresses=5 my_mnemonic_24_words
```
Replace `my_mnemonic_24_words` with your 24-word mnemonic. This will generate a wallet with 5 addresses using the provided mnemonic.

**Disclaimer**
-------------

**You are responsible for managing the safety of your mnemonic phrase.**

Make sure to store your mnemonic phrase in a secure location, such as an encrypted file or a password-protected vault. Losing access to your mnemonic phrase can result in permanent loss of your Bitcoin funds.

**License**
----------

Copyright <2024> <cezar1>

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

**Author**
---------

[Cezar1] (https://github.com/cezar1)

**Contributing**
--------------

If you'd like to contribute to this project, please fork the repository and submit a pull request. We welcome bug fixes, new features, and improvements!

**Changelog**
------------

* 0.1: Initial release
* [Future releases]: upcoming features and updates will be listed here.

**Acknowledgments**
-----------------

Thank you to the Bitcoin community for their contributions to the development of this script.

**References**
--------------

* [BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki): Bitcoin Improvement Proposal 39
* [BIP44](https://github.com/bitcoin/bips/blob/master/bip-0044.mediawiki): Bitcoin Improvement Proposal 44

**Support**
---------

If you have any questions or issues, please feel free to open an issue on GitHub. We'll do our best to help you out!