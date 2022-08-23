# generate key pairs for each student

from Crypto.PublicKey import RSA

pawprints = open('pawprints','r')

for line in pawprints:
    pawprint = line.rstrip('\n')

    key = RSA.generate(1024)
    f = open('keys/' + pawprint + '.pem', 'wb')
    f.write(key.exportKey('PEM'))
    f.close()

    pubkey = key.publickey()
    f = open('keys/' + pawprint + '.pub', 'wb')
    f.write(pubkey.exportKey('OpenSSH'))
    f.close()