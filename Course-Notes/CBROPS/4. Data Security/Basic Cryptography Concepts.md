Encryption has 2 main attack vectors, breaking the algorithm, and using the algorithm. 
If an attacker can reverse the encryption this has very obvious consequences. 
Instead of breaking the algorithm, Attackers can also use cryptography to conceal their own actions, potentially bypassing firewalls and other defences.

#### Circumventing cryptographic algorithms. 

For example, the OpenSSL Heartbleed vulnerability was assigned the Common Vulnerabilities and Exposure ID CVE-2014-0160. This vulnerability uses the implementation of the TLS heartbeat extension (RFC 6520) and the way an SSL enabled server validates heartbeat requests to provide a response. The vulnerability could allow an attacker that has crafted a heartbeat request with an improper length to receive responses that contain private data that is stored in the server memory.

#### Cryptography as an attack technology. 

For example, attackers can also use TLS/SSL encryption to hide their attack's command and control traffic. Attackers use their command and control infrastructure to maintain communications with the compromised machines. TLS/SSL encryption makes the detection of the command and control communications very difficult. One detection method is to perform TLS/SSL decryption and inspection, and then run signatures that are based on detection over the decrypted traffic. Another method of detection is to perform traffic analysis using NetFlow to detect anomalous TLS/SSL flows. NetFlow will be discussed in a later section.

## Digital Certificates

Valid:
![22](/Course-Notes/.assets/Pasted_image_20241116142752_1.png)

Not valid:
![21](/Course-Notes/.assets/Pasted_image_20241116142803_1.png)

# Cryptography Overview

Cryptology is an umbrella term which covers both cryptography and cryptanalysis.

Cryptoanalysis is the practice and study of determining and exploiting weakness in cryptographic techniques.

Cryptography is the practice and study of techniques to secure communications in the presence of third parties, and includes:

- **Confidentiality:** Ensuring that only authorized parties can read a message
- **Data integrity:** Ensuring that any changes to data in transit will be detected and rejected
- **Origin authentication:** Ensuring that any messages received were actually sent from the perceived origin
- **Non-repudiation:** Ensuring that the original source of a secured message cannot deny having produced the message

![20](/Course-Notes/.assets/Screenshot_2024-11-16_at_14.33.57_1.png)
![19](/Course-Notes/.assets/Screenshot_2024-11-16_at_14.37.24_1.png)

## Ciphers for Everyone

A cipher is an algorithm for performing encryption and decryption. Ciphers are a series of well-defined steps that you can follow as a procedure. Different types of ciphers have proven useful historically.

- **Substitution ciphers:** Substitution ciphers substitute one letter for another. In their simplest form, substitution ciphers retain the letter frequency of the original message. The cipher that was attributed to Julius Caesar was a substitution cipher. Every day was assigned a different key, and that key was used to adjust the alphabet accordingly. For example, if the key for a certain day was five, then an “A” was moved five letters ahead in the alphabet, resulting in an encoded message that used “F” in place of “A.” “B” was then “G,” “C” was “H,” and so on. The next day, the key might be eight, and the process would begin again with “A” now becoming “I,” “B” becoming “J,” and so on.
    
    One of the drawbacks of substitution ciphers is that if the message is long enough, it may be vulnerable to what is called “frequency analysis,” because it retains the frequency patterns of letters that are found in the original message. Because of this weakness, poly alphabetic ciphers were invented.
    
- **Poly alphabetic ciphers:** Polyalphabetic ciphers are based on substitution, using multiple substitution alphabets. The famous Vigenère cipher is an example. That cipher uses a series of different Caesar ciphers that are based on the letters of a keyword. It is a simple form of poly alphabetic substitution and is therefore invulnerable to frequency analysis.
    
    To illustrate how this type of cipher works, suppose that a key of “SECRETKEY” is used to encode “ATTACK AT DAWN.” The “A” is encoded by looking at the row starting with “S” for the letter in the “A” column. In this case, the “A” is replaced with “S.” Then you look for the row that begins with “E” for the letter “T,” resulting in “X” as the second character. If you continue this encoding method, the message “ATTACK AT DAWN” is encrypted as “SXVRGDKXBSAP.”
    
- **Transposition ciphers:** Transposition ciphers rearrange or permutate letters, instead of replacing them. Transposition is also known as permutation. An example of this type of cipher takes the message “THE PACKAGE IS DELIVERED” and transposes it to read “DEREVILEDSIEGAKCAPEHT.” In this example, the key is to reverse the letters. The Rail Fence Cipher is a transposition cipher in which the words are spelled out as if they are a rail fence. Each subsequent letter of the text is written downwards and diagonally on successive "rails" of an imaginary fence until the bottom rail is reached. At that point, each subsequent letter is written upwards and diagonally until the top rail is reached, and so on. The number of rails used is the cipher key. The example below illustrates a key of three.
 ![18](/Course-Notes/.assets/Pasted_image_20241116145446_1.png)
- **One-time pad:** The one-time pad was invented and patented by Gilbert Vernam in 1917 while working at AT&T. A one-time pad is also known as a Vernam cipher. Vernam's idea was a stream cipher that would apply the XOR operation to plaintext with a key. Joseph Mauborgne, a captain in the U.S. Army Signal Corps, contributed the idea of using random data as a key. This combined idea is so significant that the NSA has called this patent “perhaps the most important in the history of cryptography.”

	There are several difficulties inherent in using one-time pads in the real world. The first is the challenge of creating random data. Computers, because they have a mathematical foundation, are incapable of creating truly random data. Also, if the key is used more than once, it is trivial to break. Key distribution is also challenging.

# Hash Algorithms
Hashing is a mechanism for data integrity assurance. It relies on a one-way mathematical function. It is like a fingerprint, used to identify, but you cannot reconstruct.

Hash algorithms are used to generate hash codes, hash values, and hash sums.

## Cryptographic Authentication Using Hash Technology

Two systems that have agreed on a secret key can use the key along with a hash function to verify data integrity of communication between them by using a keyed hash. A message authentication code is produced by passing the message data along with the secret key through a hash algorithm. Only the sender and the receiver know the secret key, and the output of the hash function now depends on the message data and the secret key. Therefore, only parties who have access to that secret key can compute the appropriate hash digest. This behavior defeats man-in-the-middle attacks and provides authentication of the data origin. If two parties share a secret key and use hash technology for authentication, receipt of a properly constructed message authentication code indicates that the other party was the originator of the message, because it is the only other entity possessing the secret key.

![17](/Course-Notes/.assets/Pasted_image_20241116154057_1.png)

## Cryptographic Authentication in Action

The following figure illustrates cryptographic authentication in action. The sender wants to ensure that the message is not altered in transit and wants to provide a way for the receiver to authenticate the origin of the message.

![16](/Course-Notes/.assets/Pasted_image_20241116154147_1.png)

he sending device inputs data and the secret key into the hashing algorithm and calculates the fixed-length message authentication code, or fingerprint. This authenticated fingerprint is then attached to the message and sent to the receiver. The receiving device removes the fingerprint from the message and uses the received message with its copy of the secret key as input to the same hashing function. If the fingerprint that is calculated is identical to the fingerprint that was received, then data integrity has been verified. Also, the origin of the message is authenticated, because only the sender possesses a copy of the shared secret key. The keyed hash function has ensured the authenticity of the message.

Cisco products use hashing for entity authentication, data integrity, and data authenticity purposes:

- IPsec gateways and clients use hashing algorithms to verify packet integrity and authenticity. The algorithm, which is defined in RFC 2104, is more complex than a simple keyed hash and uses two hash computations to produce the message authentication code.
    
- Cisco IOS routers use keyed hashing with secret keys to add authentication information to routing protocol updates.
    
- Cisco software images that you can download from Cisco.com have an MD5-based checksum that is available, so that customers can check the integrity of downloaded images.
    
- Hashing can also be used in a feedback-like mode to encrypt data.
    

The following figure shows how route authentication occurs on Cisco routers. Route authentication using a keyed hash allows the validation of route integrity. If the route information is tampered with during transit, the receiving router upon calculating the keyed hash finds the computed hash to be different from the received hash. Even if an attacker intercepts the route information and injects a new hash after changing the route information, the attempt fails, because the attacker does not know the secret key. Without the secret key, the attacker cannot produce a message authentication code that will be accepted by the receiver.

![15](/Course-Notes/.assets/Pasted_image_20241116165230_1.png)

This technique is only as strong as the secret key. If the attacker knows the secret key, they can generate a malicious routing update and the appropriate keyed hash that will be accepted by the peer routers. Also note that this technique does not provide privacy. While it prevents an attacker from manipulating a routing update that they intercept, it does not prevent the attacker from reading the routing update.

## Comparing Hashing Algorithms

Common Cryptographic Hash Functions: MD5, SHA-1, and SHA-2.

- MD5 Algorithm: A one-way function with collision vulnerabilities, not recommended for new applications.

- SHA-1 Algorithm: A secure hash algorithm with a larger message digest, more secure against attacks.

- SHA-2 Algorithms: Six algorithms (SHA-224, SHA-256, SHA-384, SHA-512, SHA-512/224, and SHA-512/256) that generate message digests of varying lengths (224-512 bits) based on input message length.

- SHA-512 Efficiency: More efficient than SHA-256 on 64-bit systems, but SHA-512/224 and SHA-512/256 were introduced to provide a smaller digest size.

- SHA-2 Adoption: Approved by NIST in 2006 for federal agencies, mandating its use for collision-resistant applications after 2010 due to SHA-1 vulnerabilities.

- SHA-3 Functionality: SHA-3 is a family of cryptographic hash functions and extendable-output functions, including SHA3-224, SHA3-256, SHA3-384, SHA3-512, SHAKE128, and SHAKE256.
- SHA-3 Applications: SHA-3 functions are used in digital signatures, key derivation, pseudorandom bit generation, and other security applications.
- SHA-3 Advantages: SHA-3 offers a backup to SHA-2 and can be implemented with minimal circuitry, making it suitable for small devices.

# Encryption Overview

Encryption is the process of disguising a message in such a way as to hide its original contents. With encryption, the plaintext readable message is converted to ciphertext, which is the disguised and unreadable message.

![14](/Course-Notes/.assets/Pasted_image_20241116170740_1.png)

Encryption can provide confidentiality at various layers of the Open Systems Interconnection (OSI) model, such as the following:

- Encrypt application layer data, such as encrypting email messages with PGP.
- Encrypt session layer data using a protocol such as SSL or TLS.
- Encrypt network layer data using protocols such as those provided in the IPsec protocol suite.
- Encrypt data link layer using MACsec (IEEE 802.1AE) or proprietary link-encrypting devices.

## Encryption Algorithm Features

A good cryptographic algorithm is resilient to attacks.
Resists common attacks by requiring a long key length, making brute force attacks unfeasible.

- Key Length and Scalability: Longer keys provide stronger encryption, while scalability allows for flexible key selection.
- Avalanche Effect: Small changes in plaintext result in significant changes in ciphertext, ensuring message confidentiality.

# Cryptanalysis

The practice of breaking encrypted codes. 

- **Brute-force attack:** Tries every possible key with the decryption algorithm, knowing that eventually one of the keys will work. _All encryption algorithms are vulnerable to a brute-force attack_. On average, a brute-force attack will succeed about 50 percent of the way through the key space, which is the set of all possible keys. The objective of modern cryptographers is to have a key space large enough that it takes too much money and too much time to accomplish a brute-force attack.
    
    ## Note
    
    Existing technology and computing power has resulted in machines that are able to crack DES in just a few hours. It is estimated that it would take 149 trillion years to crack AES using the same method.
    
- **Ciphertext-only attack:** The attacker has the ciphertext of several messages, all of which have been encrypted using the same encryption algorithm, but the attacker has no knowledge of the underlying plaintext. The job of the attacker is to recover the plaintext of as many messages as possible—or better yet, to deduce the key or keys that are used to encrypt the messages to decrypt other messages that are encrypted with the same keys. The attacker can use statistical analysis to achieve the result. These kinds of attacks are no longer practical, because modern algorithms produce pseudorandom output that is resistant to statistical analysis.
    
- **Known-plaintext attack:** In a known-plaintext attack, the attacker has access to the ciphertext of several messages but also knows something about the plaintext that underlies that ciphertext. With knowledge of the underlying protocol, file type, or some characteristic strings that may appear in the plaintext, the attacker uses a brute-force attack to try keys, until decryption with the correct key produces a meaningful result. This attack may be the most practical attack, because attackers can usually assume the type and some features of the underlying plaintext, if they can only capture the ciphertext. However, modern algorithms with enormous key spaces make it unlikely for this attack to succeed, because on average an attacker has to search through at least half of the key space to be successful.
    
- **Chosen-plaintext attack:** In a chosen-plaintext attack, the attacker chooses what data the encryption device encrypts and observes the ciphertext output. A chosen-plaintext attack is more powerful than a known-plaintext attack, because the attacker gets to choose the plaintext blocks to encrypt, allowing the attacker to choose plaintext that might yield more information about the key. This attack might not be very practical, because it is often difficult or impossible to capture both the ciphertext and plaintext, unless the trusted network has been broken into and the attacker already has access to confidential information.
    
- **Chosen-ciphertext attack:** In a chosen-ciphertext attack, the attacker can choose different ciphertext to be decrypted and has access to the decrypted plaintext. With the pair, the attacker can search through the key space and determine which key decrypts the chosen ciphertext in the captured plaintext. For example, the attacker has access to a tamper-proof encryption device with an embedded key. The attacker must deduce the embedded key by sending data through the box. This attack is analogous to the chosen-plaintext attack. This attack might not be very practical, because it is often difficult or impossible to capture both the ciphertext and plaintext, unless the trusted network has been broken into, and the attacker already has access to confidential information.
    
- **Birthday attack:** The birthday attack gets its name because of an amazing statistical probability that is involved in two individuals having the same birthday. According to statisticians, the probability that two people in a group of 23 people share the same birthday is greater than 50 percent.
    
    The birthday attack is a form of brute-force attack against hash functions. If a specific function, when supplied with a random input, returns one of _k_ equally likely values, then by repeating the function with different inputs, the same output is expected after 1.2_k_1/2 number of times.
    
    ## Note
    
    To test the birthday theory, input 365 in the place of _k_.
    
- **Meet-in-the-middle:** The meet-in-the-middle attack is a known-plaintext attack. In a meet-in-the-middle attack, the attacker knows a portion of the plaintext and the corresponding ciphertext. The plaintext is encrypted with every possible key, and the results are stored. The ciphertext is then decrypted by using every key, until one of the results matches one of the stored values.

# Symmetric Encryption Algorithms
AKA "private key encryption"

Hardest part is keeping the secret keys safe.

- Often found in IPsec technology. Fast and used for bulk encryption, VPN protection, and data privacy.
- Challenges: Secure key exchange between parties.
- Key Length: ≥80 bits are more secure against brute-force attacks, while shorter lengths are obsolete.

DES, 3DES, AES, IDEA, RC2/4/5/6, and Blowfish.

**DES**
- A block cipher that encrypts data in 64-bit blocks using a 56-bit key, vulnerable to brute-force attacks.
	- **Electronic Code Book (ECB):** Encrypts each 64-bit plaintext block using the same 56-bit key.
	- **Cipher Block Chaining (CBC):** Each 64-bit plaintext block is XORed bitwise with the previous ciphertext block and then is encrypted with the DES key. 

**3DES**
- Applies DES three times with different keys to increase security, considered unfeasible to brute-force.
- Encrypts with K1, decrypts with K2, and encrypts again with K3. Providing 168-bit encryption with K1, K2, K3, or 112-bit encryption with K1=K3.

**AES**
- An iterated block cipher based on Rijndael, using 128, 192, or 256-bit keys to encrypt 128-bit blocks.
- Advantages: Stronger key length than DES, faster than 3DES, and more efficient for high-throughput environments.

**RC4**
- Characteristics: A stream cipher used in SSL/TLS, known for its speed in software, and considered secure despite potential weaknesses.

**More**
- Alternative Symmetric Algorithms: SEAL, IDEA, Blowfish, Twofish, and Serpent are available options.

# Asymmetric Encryption Algorithms

- Key Length Range: 1024 to 4096 bits.
- Variable key length allows for trade-off between speed and security.
- Security Basis: Difficulty of factoring large numbers.

- Key Management: Asymmetric algorithms have simpler key management because one key can be public.
- Security Services: Asymmetric encryption provides confidentiality and origin authentication.
- Usage: Asymmetric algorithms are used for low-volume cryptographic mechanisms like digital signatures and key exchange due to their slower speed.

Asymmetric algorithms use a pair of keys for encryption and decryption. The paired keys are intimately related and are generated together.

because the public keys are exchanged over the internet we assume someone may have captured it. This does not effect privacy as long as the private keys remain secret.

![13](/Course-Notes/.assets/Pasted_image_20241117094405_1.png)

By Encrypting with the Public key of the recipient,
they are able to decrypt with their private key — This provides confidentiality. 

By Encrypting with the Private key and decrypting with the public key we can prove origin authentication.

PGP (Pretty Good Privacy)
- Email 
	- Public/Private Key Pair 
	- Share Public Keys
	- Encrypt Twice 
		- Private Key
		- Public Key

Receiving devices reverse the process by first decrypting with the private key then again with the public key

- Symmetric Encryption in Real-Time Protocols: Used for bulk data encryption in protocols like SSH, SSL, and IPsec due to its efficiency.

# [Diffie-Hellman Key Agreement]([https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange))

The Diffie-Hellman (DH) key agreement method allows two parties to share information over an untrusted network and mutually compute an identical shared secret that cannot be computed by eavesdroppers who intercept the shared information. The mathematical operations are relatively easy to describe, expensive to compute, and intractable to reverse.

The DH key agreement method can be used in protocols such as SSL/TLS, SSH, and IKE.

![12](/Course-Notes/.assets/Pasted_image_20241117100948_1.png)

- DH Key Agreement Process: Two parties (Alice and Bob) agree on a common color (large prime number p and generator g) and each selects a secret color (private key). They publicly exchange their mixed colors (public keys) and finally mix the received color with their private color to get the shared secret key.
- Public Key Calculation: Alice’s public key (A) is calculated using g, p, and her private key (a), while Bob’s public key (B) is calculated using g, p, and his private key (b).
- Shared Secret Key Calculation: Alice and Bob each mix the received public key with their private key to get the shared secret key.

- Shared Secret Key Calculation: Both parties calculate the same shared secret key (s) using their private keys, the other party’s public key, and a prime number (p).
- DH Group Strength and Computation Time: Different DH groups determine key strength and computation time, with higher group numbers offering greater security but requiring more time.
- Ephemeral Diffie-Hellman (EDH): EDH uses temporary private keys for each key exchange, ensuring perfect forward secrecy (PFS) even if a private key is exposed.

The mathematical model in the DH key exchange process:

- **p** = large prime number, can be known to Alice, Bob, and Eve.
- **g** = based or generator, can be known to Alice, Bob, and Eve.
- **a** = Alice's chosen private key, which is known only to Alice.
- **b** = Bob's chosen private key, which is known only to Bob.
- **A** = Alice's calculated public key using **g**, **p**, and **a**, can be known to Alice, Bob, and Eve. **A** = **g**^**a** mod **p**.
- **B** = Bob's calculated public key using **g**, **p**, and **b**, can be known to Alice, Bob, and Eve. **B** = **g**^**b** mod **p**.
- **s** = The shared secret key, which is calculated by using the other party's public key, each party's own chosen secret key, and the prime number p, is known to both Alice and Bob, but not to Eve.
- **s** = **B**^**a** mod **p** (calculated by Alice).
- **s** = **A**^**b** mod **p** (calculated by Bob).
- **s** can also be calculated using the formula **s = g^ab** mod **p**, which requires knowledge of both parties chosen private key.
- After each party calculates the shared secret key **s** independently, each party will end up with the exact same value **s**. All three formulas for **s** will produce the same result. **s** = **g**^**ab** mod **p** = **B**^**a** mod **p** = **A**^**b** mod **p**.

# SSH Legacy Encryption

SSH is designed to provide privacy, data integrity, and origin authentication. SSHv1 should be considered legacy, as SSHv2 now used DH and was designed to overcome v1 shortcomings. 

Legacy SSHv1 makes clever use of asymmetric encryption to facilitate symmetric key exchange. Computationally expensive asymmetric encryption is only required for a small step in the negotiation process. After key exchange, much more computationally efficient symmetric encryption is used for bulk data encryption between the client and server.

- Key Exchange Mechanism: SSHv1 uses asymmetric encryption for key exchange and symmetric encryption for data encryption.

SSHv1 Connection Establishment: 
1. Client connects to server, 
2. Server presents public key, 
3. Client and server negotiate symmetric encryption algorithm (in clear text) 
4. Client encrypts session key with server’s public key, 
5. Server decrypts session key, and both parties share the session key for symmetric encryption.

- Data Protection: After key exchange, all user credentials and data are protected using symmetric encryption.

- Asymmetric Encryption Functionality: Facilitates symmetric key exchange and peer authentication.

- Peer Authentication Mechanism: Clients recognize non-authentic systems by comparing provided public keys with known server keys.

- User Authentication Challenge: Users often lack the knowledge to verify the authenticity of server public keys, despite client software displaying them.


# Digital Signatures

## RSA Digital signature

![11](/Course-Notes/.assets/Pasted_image_20241117110846_1.png)

The signature process:
1. The signer makes a hash, or fingerprint, of the document, which uniquely identifies the document and all its contents.
2. The signer encrypts the hash with only the private key of the signer.
3. The encrypted hash, which is known as the signature, is appended to the document.

The verification process:
4. The verifier obtains the public key of the signer.
5. The verifier decrypts the signature using the public key of the signer. This step unveils the assumed hash value of the signer.
6. The verifier makes a hash of the received document, without its signature, and compares this hash to the decrypted signature hash. If the hashes match, the document is authentic. The match means that the document has been signed by the assumed signer and has not changed since it was signed.

Digital signatures provide three basic security services in secure communications:

- ==**Authenticity of digitally signed data:**== Digital signatures authenticate a source, proving that a certain party has seen and has signed the data in question.
- ==**Integrity of digitally signed data:**== Digital signatures guarantee that the data has not changed from the time it was signed.
- ==**Nonrepudiation of the transaction:**== The recipient can take the data to a third party, and the third party accepts the digital signature as a proof that this data exchange did take place. The signing party cannot repudiate that it has signed the data.

To achieve these goals, digital signatures have the following properties:
- ==**The signature is authentic:**== The signature convinces the recipient of the document that the signer signed the document.
- ==**The signature is not forgeable:**== The signature is proof that the signer, and no one else, signed the document.
- ==**The signature is not reusable:**== The signature is a part of the document and cannot be moved to a different document.
- **==The signature is unalterable:==** After a document is signed, it cannot be altered.
- **==The signature cannot be repudiated:==** Signers cannot claim later that they did not sign it.

## Practical Example: Digitally Signed Cisco Software

 Digitally Signed Cisco Software Facilitates the use of Cisco networking software that is digitally signed through secure asymmetrical cryptography. 

-  Cisco IOS image file that contains a file extension that is based on the signing key that was used to sign images. 
	- SPA
	- SSA 

- Digitally Signed Cisco IOS Software Identification: Identified by a three-character extension in the image name, with the first “S” indicating digital signing, the second character specifying production or special image, and the third character indicating the key version.

- Digital Signing Process: Carries an encrypted hash of itself, and upon check, the device decrypts the hash with the corresponding public key and compares it with the calculated hash of the image to ensure authenticity.

- Running IOS Image Integrity Verification: Verifies the integrity of the running IOS image using the command “show software authenticity running”.

- Image Information: Displays information about the image, including signer details, certificate serial number, hash algorithm, signature algorithm, and key version.

- Image Location: The command “show software authenticity file flash:c2900-universalk9-mz.SPA.153-1.T.bin” is used to verify the integrity of the image stored in the flash memory.

```
Partner-ISR# show software authenticity running
SYSTEM IMAGE
------------
Image type                    : Production
    Signer Information
        Common Name           : CiscoSystems
        Organization Unit     : C2900
        Organization Name     : CiscoSystems
    Certificate Serial Number : 50B3F3FE
    Hash Algorithm            : SHA512
    Signature Algorithm       : 2048-bit RSA
    Key Version               : A

    Verifier Information
        Verifier Name         : ROMMON 1
        Verifier Version      : System Bootstrap, Version 15.0(1r)M16, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport

Partner-ISR#**show software authenticity file flash:c2900-universalk9-mz.SPA.153-1.T.bin**
File Name                     : flash:c2900-universalk9-mz.SPA.153-1.T.bin
Image type                    : Production
    Signer Information
        Common Name           : CiscoSystems
        Organization Unit     : C2900
        Organization Name     : CiscoSystems
    Certificate Serial Number : 50B3F3FE
    Hash Algorithm            : SHA512
    Signature Algorithm       : 2048-bit RSA
    Key Version               : A
```


# PKI Overview

- Public Key Distribution Challenge: Ensuring the authenticity of public keys to prevent man-in-the-middle attacks.
- Public Key Infrastructure (PKI) Solution: PKI provides a framework for secure public key distribution through digital certificates and certificate authorities (CAs).
- Certificate Authority (CA) Role: CAs act as trusted third parties, signing digital certificates to validate the authenticity of public keys.

## Trusted Third-Party Example
![10](/Course-Notes/.assets/Pasted_image_20241117131431_1.png)
Certificate authorities function like the driver’s license bureau in this example. The driver’s license is analogous to a certificate in a PKI or a technology that supports certificates.

## PKI Terminology and Components

A PKI is the service framework that is used to support large-scale public key-based technologies. It provides the base for security services such as encryption, authentication, and nonrepudiation. 

A PKI allows for very scalable solutions which require the management of systems identities, user identities, or both, and is an important authentication solution for VPNs. 

- **CA:** The trusted third party that signs the public keys of entities in a PKI-based system.

- **Certificate:** A document, which in essence binds together the name of the entity and its public key, which has been signed by the CA.

Many vendors offer CA servers as a managed service or as an end-user product: VeriSign, Entrust Technologies, and GoDaddy are some examples. Organizations may also implement private PKIs using Microsoft Server or Open SSL.

## Public-Key Cryptography Standards

- PKI Standardization: Allows interoperability across applications and vendors.
- PKCS Development: RSA Security Inc. devised and published PKCS standards in the early 1990s.
- PKCS Recognition: While not industry standards, some PKCS standards have been accepted by recognized standards organizations.

PKCS includes the following:

- **PKCS #1:** RSA Cryptography Standard
- **PKCS #3:** D-H Key Agreement Standard
- **PKCS #5:** Password-Based Cryptography Standard
- **PKCS #6:** Extended-Certificate Syntax Standard
- **PKCS #7:** Cryptographic Message Syntax Standard
- **PKCS #8:** Private-Key Information Syntax Standard
- **PKCS #10:** Certification Request Syntax Standard
- **PKCS #12:** Personal Information Exchange Syntax Standard
- **PKCS #13:** Elliptic Curve Cryptography Standard
- **PKCS #15:** Cryptographic Token Information Format Standard
### X.509v3 structure
- Version
- Serial number
- Algorithm ID
- Issuer
- Validity
    1. Not before
    2. Not after
- Subject
- Subject public key info
    1. Public key algorithm
    2. Subject public key
- Issuer unique identifier (optional)
- Subject unique identifier (optional)
- Extensions (optional)
- Certificate signature algorithm
- Certificate signature

 Certificate Signing: 
- The Certificate Authority (CA) signs the certificate by encrypting a hash of the certificate data using its private key.
 Certificate Validation: 
- Any system can validate a certificate by decrypting the signature using the CA’s public key and comparing it to the computed hash of the certificate data.

# PKI Operations
## Certificate Enrolment

![9](/Course-Notes/.assets/Pasted_image_20241117132940_1.png)

To obtain an identity certificate, a system administrator will enroll with the PKI. 
1. Obtain the CA’s identity certificate. 
2. Certificate signing request (CSR) (PKCS #10). 
	- Identity information that is associated with the enrolling system
		- system name, 
		- the organization to which the system belongs, 
		- and location information.
3. System’s public key is included with the CSR

## Authentication Using Certificates

![8](/Course-Notes/.assets/Pasted_image_20241117133854_1.png)

- Certificate Authority (CA) Role: Not involved in certificate validation; systems use the root CA certificate to validate signatures on received certificates.
- Certificate Function: Identifies the valid public key of a peer, not the peer’s identity directly.
- Peer Identity Verification: Systems challenge peers to prove possession of the private key associated with the validated public key to confirm identity.

## Certificate Revocation

![7](/Course-Notes/.assets/Pasted_image_20241117134042_1.png)

- Certificate Revocation Reason: Keys are compromised or business use of the certificate calls for revocation.
- Certificate Revocation Process: Generating new keys forces the creation of a new digital certificate, rendering the old certificate invalid.
- Certificate Revocation Method: A centralized function providing “push” and “pull” methods to obtain a list of revoked certificates.

## Certificate Revocation Check Methods

CRL
- A list of revoked certificate serial numbers is distributed as a time-stamped, CA-signed file.
- PKI entities regularly poll the CRL repository to receive the current CRL.
- There is a window of opportunity for attackers while the new CRL is not yet propagated.

OCSP
- Entities can query the OCSP server at any time to check for validity of the received certificate.

# SSL/TLS

- Purpose of SSL/TLS: Provide secure transactions between web browsers and web servers.
- Standardization: SSL is obsolete, replaced by TLS, which is standardized by the IETF.
- TLS Version 1.3: Introduces changes to improve security, privacy, and performance compared to TLS 1.2.

- TLS Functionality: Provides secure communication between peers using PKI authentication and public key encryption for session key exchange.
- TLS Applications: Widely used for secure web communication (HTTPS) and also applied to applications like SMTP, LDAP, and POP3.
- TLS Goal: Establish a secure channel between communicating peers, relying on a reliable data stream from the underlying transport.

![6](/Course-Notes/.assets/Pasted_image_20241117150156_1.png)

- Cipher Suite Definition: Defined in protocol documents (RFC 5246 for TLS 1.2) and specify the structure and use of cipher suites.
- Mandatory Cipher Suite: TLS_RSA_WITH_AES_128_CBC_SHA, including RSA for authentication and key exchange, AES for confidentiality, and SHA for integrity.
- Cipher Suite Registry: Maintained by IANA and defined in RFC 2434 to support future protocols.

## SSL/TLS Certificate Example

Web browsers, using a built-in store of root CA certificates, hide the details of validating TLS sessions from the user, unless there is an issue with the validation process. But even with successful validation, users can drill down into the details of the connection. Here are the certificate details that can be examined within a web browser.

1. When the connection to the server is first initialized, the server provides its PKI certificate to the client, which contains the public key of the server and is signed with the private key of the CA that the owner of the server has used.![5](/Course-Notes/.assets/Pasted_image_20241117150442_1.png)
2. To verify that the PKI certificate can be trusted, the signature of the CA that is in the certificate is checked. If the signature can be traced back to a public key that already is known to the client, the connection is considered to be trusted.![4](/Course-Notes/.assets/Pasted_image_20241117150454_1.png)
3. Now that the connection is trusted, the client can send encrypted packets to the server.
   ![3](/Course-Notes/.assets/Pasted_image_20241117150502_1.png)
4. As public/private-key encryption is one-way encryption, only the server is capable of decrypting the traffic. ![2](/Course-Notes/.assets/Pasted_image_20241117150510_1.png)

In the Certification Path tab, you can view the path from the selected certificate to issuing CAs. To trust a certificate, recipients verify its source through path validation, processing public key and issuer certificates hierarchically until reaching a trusted, self-signed certificate, usually a root CA. If a certificate or the path is problematic, it’s considered untrusted. A typical path includes a root certificate and intermediate certificates. View Certificate provides details about each CA’s certificates.

## Web Browser Security Warnings

 If there are any issues that are associated with validating the certificate of a web server, web browsers will display a security warning to the user. Unfortunately, many users will ignore the security warnings and blindly proceed with the connection under potentially hazardous conditions. The three most common issues that are associated with security warnings are as follows:

==**Hostname/identity mismatch:**== URLs specify a web server name. If the name specified in the URL does not match the name that is specified in the server’s identity certificate, the browser will display a security warning. Hence, DNS is critical to support the use of PKI in web browsing, which may be benign under certain circumstances: for example, if the user knows the IP address of the server and specifies the IP address instead of the hostname. But attackers may register domain names that look very similar to authentic domain names. The browser will detect the mismatch, but the user may look at the certificate and think that it is acceptable.

==**Validity date range:**== X.509v3 certificates specify two dates, not before and not after. If the current date is within those two values, there will be no warning. If it is outside the range, the web browser displays a message. The validity date range specifies the amount of time that the PKI will provide certificate revocation information for the certificate. When certificates expire, it facilitates the periodic changing of public/private key pairs on web servers. Expired certificates may simply be the result of administrator oversight, but they may also reflect more serious conditions.

==**Signature validation error:**== If the browser cannot validate the signature on the certificate, there is no assurance that the public key in the certificate is authentic. Signature validation will fail if the root certificate of the CA hierarchy is not available in the browser’s certificate store. A common reason may be that the server uses a self-signed certificate. Many systems allow the creation of self-signed certificates to avoid the complexity or expense of joining a PKI. The use of self-signed certificates, however, puts the responsibility of certificate verification on the user, which is not optimal from a security perspective. Another possible cause of a signature verification error is that the certificate has been tampered with—for example, if an attacker has replaced the server’s real public key with the attacker’s public key.

# Cipher Suite

The following lists three TLS cipher suite examples that are using the ECDH exchange (ECDHE) and ECDSAs for authentication and key exchange, instead of using RSA (as shown in the previous topic).

- SSL/TLS Protocol Flexibility: Allows for the modification of encryption, key exchange, and message authentication algorithms without replacing the entire protocol.
- Cipher Suites in SSL/TLS: Define a set of cryptographic algorithms, including authentication, key exchange, encryption, message authentication code, and PRF algorithms.
- TLS Handshake Process: Involves a client hello and a server hello, where the client presents a list of supported cipher suites and the server selects one.

TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
    1. ECDHE_ECDSA is the authentication and key exchange algorithms. ECDHE_ECDSA is used to determine how the client and server will authenticate and establish the premaster secret during the TLS handshake. In this case, both the client and the server will derive the identical premaster secret using the DH parameters (sent in the additional ServerKeyExchange message). The premaster secret is then used to derive the master secret and the session-specific keys. With DH key exchanges, in order for the client to authenticate the server, the server will sign the DH parameters that are contained in ServerKeyExchange message with the server’s private key. The client verifies the signature with the server's public key in the server's certificate. Only if the signature is valid, the client will proceed with the TLS handshake.
    2. AES_256_GCM is the bulk encryption algorithm.
        - Galois Counter Mode (GCM) is a mode of operation for an authenticated symmetric key cryptographic block ciphers that has been widely adopted because of its efficiency and performance. GCM is an authenticated encryption algorithm that is designed to provide both data authenticity and confidentiality.
    3. SHA-384 is used for the pseudorandom function. Since an authenticated encryption mode (GCM) is used, the messages neither have nor require a message authentication code.
    4. The pseudo-random function is used to generate the keying materials that are used during the TLS session.

TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256
    1. ECDHE_ECDSA is the authentication and key exchange algorithms.
    2. AES_128_CBC is the bulk encryption algorithm. Unlike AES GCM, AES CBC mode does not provide data authenticity (integrity). Therefore, a message authentication code algorithm is required for data authenticity (integrity).
    3. SHA-256 is the Hashed Message Authentication Code algorithm.
    4. SHA-256 is also used for the pseudo-random function.
        - For TLS 1.2, the default pseudo-random function is SHA-256, unless otherwise stated.

TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA256_P384
    1. ECDHE_ECDSA is the authentication and key exchange algorithms.
    2. AES_256_CBC is the bulk encryption algorithm. Unlike AES GCM, AES CBC mode does not provide data authenticity (integrity). Therefore, a message authentication code algorithm is required for data authenticity (integrity).
    3. SHA-256 is the Hashed Message Authentication Code algorithm.
    4. SHA-384 is specified to be used for the pseudo-random function.

- NULL Cipher: Only for testing or debugging purposes, not for actual encryption.
- Insecure Cipher Suites: Legacy cipher suites using DES, RC4, or MD5 are not recommended due to security vulnerabilities.
- TLS v1.3 Security Enhancements: Removes support for outdated features like RSA, MD5, and weak elliptic curves, reducing the attack surface and ensuring perfect forward secrecy.

# Key Management

Key management deals with the secure generation, verification, exchange, storage, and destruction of keys. It is extremely important to have secure methods of key management.

- Key Management Importance: Crucial for cryptosystem design, often the most challenging aspect.
- Impact of Key Management: Mistakes can lead to cryptosystem failures, and modern algorithms rely on key management.
- Attack Focus: Most attacks target key management rather than the cryptographic algorithm itself.

## Key Management Components

- ==Key Generation:== Automated process requiring effective randomization to ensure equal key likelihood and prevent predictability for attackers.
- ==Key Storage:== Secure storage is crucial, considering potential vulnerabilities like memory swapping on multiuser systems.
- ==Key Management Procedures:==
	- Include key verification, 
	- secure key exchange, 
	- key revocation, and 
	- key destruction for robust security.

## Key Spaces

- Key Space: The set of all possible key values for an algorithm, with a key of n bits producing 2^n possible values.
- Key Space Size: Determined by the number of bits in the key, with 2n possible key values for an n-bit key.
- Weak Keys: Exist in almost every algorithm and should be prevented in implementation.

## Key Length Issues

- Brute-Force Attack: A method of breaking a cryptographic system by trying all possible keys, which becomes infeasible with sufficiently large key spaces.
- Key Length Selection: Determines the balance between protection strength and performance, with longer keys providing stronger protection but potentially impacting speed.

# NSA Suite B

![1](/Course-Notes/.assets/Screenshot_2024-11-17_at_18.00.33.png)

- Cryptographic Algorithms: Suite B cryptography uses AES, ECDSA, ECDH, and SHA-2 for encryption, digital signatures, key agreement, and message digesting, respectively.
- Information Assurance: The NSA considers these algorithms sufficient for protecting classified information.

 NSA Suite B cryptography for IPsec is standardized in RFC 6379 and has industry acceptance.