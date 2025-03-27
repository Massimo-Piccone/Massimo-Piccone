IPsec protocols
PKI structures

### Counter-mode encryption 

##### ECB - Electronic Codebook
> Data is divided into fixed-size blocks and each block is encrypted using the same key.

| Advantages:        | Simple and fast since each block is encrypted independently                                                                  |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| **Disadvantages:** | Lack of randomness, as identical plaintext blocks produce identical cipher-text blocks, making patterns easily recognizable. |
| **Use case:**      | **Not recommended due to the predictability and lack of security.**                                                          |
##### CBC - Cipher Block Chaining
> Each plaintext block is XORed with the previous ciphertext block before encryption. An Initialization Vector (IV) is used for the first block to introduce randomness.

| Advantages:        | More secure than ECB because identical plaintext blocks result in different ciphertext blocks due to chaining.                               |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **Disadvantages:** | Sequential encryption, meaning it cannot be parallelized efficiently; also vulnerable to padding oracle attacks if not implemented properly. |
| **Use case:**      | Suitable for file encryption and older protocols, but being replaced by more secure modes.                                                   |
##### CFB - Cipher Feedback Mode
> Operates in a stream-like fashion. The IV is encrypted, and the output is XORed with the plaintext to produce ciphertext. The result is then fed back into the encryption process.

| Advantages:        | Converts block ciphers into stream ciphers, making it useful for scenarios that require streaming data encryption. |
| ------------------ | ------------------------------------------------------------------------------------------------------------------ |
| **Disadvantages:** | Susceptible to bit flipping attacks if not properly authenticated.                                                 |
| **Use case:**      | Streaming data encryption where data is continuously received and encrypted.                                       |
#####  OFB - Output Feedback Mode
> Similar to CFB, except the IV and subsequent encrypted outputs (keystream) are fed back into the cipher and XORed with the plaintext to produce ciphertext. The difference is that the feedback is independent of the ciphertext.

| Advantages:        | Prevents error propagation because encryption doesn’t depend on previous ciphertext blocks.   |
| ------------------ | --------------------------------------------------------------------------------------------- |
| **Disadvantages:** | Like CFB, vulnerable to bit flipping attacks unless authenticated.                            |
| **Use case:**      | Secure data transmission where errors need to be minimized, such as satellite communications. |
##### CTR - Counter Mode
>A counter is used as an input for encryption, which is then XORed with the plaintext. Each block of plaintext is combined with a unique output from the counter, which is incremented for each block.

| Advantages:        | High efficiency and supports parallel encryption, making it suitable for high-performance environments. No need for padding like in CBC. |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **Disadvantages:** | If the counter values repeat (nonce reuse), the encryption can be broken, leading to severe security flaws.                              |
| **Use case:**      | Modern encryption schemes, including internet communications and high-speed data encryption.                                             |

##### GCM - Galois/Counter Mode
>GCM is a type of counter mode that provides both encryption and message authentication. It uses a counter for block encryption and a Galois field multiplication for authentication.

| Advantages:        | Provides authenticated encryption, ensuring both confidentiality and data integrity. It’s fast and highly secure when used with unique nonces. |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **Disadvantages:** | Same weakness as CTR mode if nonces (IVs) are reused. Also, requires a reliable way to manage nonces.                                          |
| **Use case:**      | Widely used in secure communications protocols like TLS, SSH, and IPsec because it combines encryption with message integrity.                 |

##### Summary of Key Differences:

• **ECB**: Fast, but insecure due to pattern repetition.

• **CBC**: More secure than ECB, but requires sequential processing, limiting efficiency.

• **CFB and OFB**: Stream-like modes with the ability to encrypt smaller amounts of data continuously, but vulnerable to bit flipping.

• **CTR**: Highly efficient, allows parallel processing, but requires careful management of nonces.

• **GCM**: Adds data authentication to CTR, offering both confidentiality and integrity.

• **XTS-AES**: Specialized mode for disk encryption, ensuring secure storage.

