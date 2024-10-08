Image Encryption using AES in Cyber Security
Introduction
This project demonstrates the encryption and decryption of images using the AES (Advanced Encryption Standard) encryption algorithm. AES is a widely used symmetric key encryption standard known for its security and efficiency. The project converts an image into a byte array, encrypts it using a secret key, and allows decryption back into its original form.

The goal of this project is to ensure secure transmission of images, protecting them from unauthorized access by using encryption techniques.

Features
Symmetric Key Encryption: Uses AES in CBC mode for encryption and decryption.
Image Encryption: Converts image files into encrypted binary format.
Image Decryption: Restores the original image from the encrypted binary data.
Initialization Vector (IV): Ensures randomness in encryption even when encrypting the same image multiple times.
Technologies Used
Programming Language: Python
Libraries:
Pillow: For image processing and conversion.
pycryptodome: For implementing AES encryption and decryption.
Prerequisites
Python 3.x
Pip for installing Python packages.
