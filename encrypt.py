from PIL import Image
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import os

# Function to convert image to byte array
def image_to_byte_array(image_path):
    with open(image_path, 'rb') as image_file:
        return image_file.read()

# Function to save byte array as image
def save_byte_array_as_image(byte_array, output_path):
    with open(output_path, 'wb') as image_file:
        image_file.write(byte_array)

# Encrypt image using AES
def encrypt_image(image_path, key):
    # Read image into byte array
    image_data = image_to_byte_array(image_path)

    # Generate random initialization vector (IV)
    iv = get_random_bytes(16)

    # Create AES cipher with key and IV in CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Pad the image data and encrypt
    encrypted_data = cipher.encrypt(pad(image_data, AES.block_size))

    return iv, encrypted_data

# Example usage:
key = get_random_bytes(16)  # AES key (16 bytes for AES-128)

# Encrypt an image (replace 'input_image.png' with your image path)
iv, encrypted_image_data = encrypt_image('input.jpeg', key)

# Save encrypted image data
save_byte_array_as_image(iv + encrypted_image_data, 'encrypted_image.aes')


# Decrypt the image
def decrypt_image(encrypted_image_path, key):
    # Read the encrypted image data
    with open(encrypted_image_path, 'rb') as file:
        encrypted_image_data = file.read()

    # Extract IV and encrypted data
    iv = encrypted_image_data[:16]
    encrypted_data = encrypted_image_data[16:]

    # Create AES cipher with key and IV
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Decrypt and unpad the data
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

    return decrypted_data

# Example usage:
decrypted_image_data = decrypt_image('encrypted_image.aes', key)

# Save the decrypted data back as an image (replace 'output_image.png' with desired output name)
save_byte_array_as_image(decrypted_image_data, 'output_image.png')
