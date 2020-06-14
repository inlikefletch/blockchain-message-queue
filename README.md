# blockchain-message-queue

The following documents development of a message queue service using RSA encryption and blockchain technology.

Sign up/login generates 1024 bit RSA keys, client side, based on unique usernames and passwords. Only user public keys are posted back to the server. Message posts/gets uses the desired public key and client side private key to encrypt/decrypt messages. Encrypted messages are sent to a decentralized, open blockchain database.

Demo:
https://tinyurl.com/blockchainmq

Questions or comments:
jason@solvingnet.com
