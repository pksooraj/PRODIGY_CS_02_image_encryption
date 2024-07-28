# Image Encryption Tool

## Overview

The Image Encryption Tool is a simple Python application that allows users to encrypt and decrypt images using pixel manipulation techniques. This tool provides a basic implementation of image encryption with a user-friendly graphical interface.

## Features

- **Encrypt Images:** Modify pixel values using a key to encrypt an image.
- **Decrypt Images:** Reverse the encryption process using the same key to retrieve the original image.
- **Graphical User Interface (GUI):** Simple interface for selecting images and entering keys.

## Requirements

- Python 3.x
- Pillow library (`pip install pillow`)
- NumPy library (`pip install numpy`)
- Tkinter library (comes with Python standard library)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/pksooraj/PRODIGY_CS_02_image_encryption.git
   cd PRODIGY_CS_02_image_encryption
   ```

2. **Install the required libraries:**

   ```bash
   pip install pillow numpy
   ```

## Usage

1. **Run the application:**

   ```bash
   python image_encryption_gui.py
   ```

2. **Encrypting an Image:**

   - Click the "Encrypt Image" button.
   - Select the image file you want to encrypt.
   - Enter an encryption key in the prompt.
   - Save the encrypted image when prompted.

3. **Decrypting an Image:**

   - Click the "Decrypt Image" button.
   - Select the encrypted image file.
   - Enter the decryption key (must be the same as the encryption key) in the prompt.
   - Save the decrypted image when prompted.

## Example

- **Encrypting an Image:**
  ![Encrypt Example](images/encrypt_example.png)
  
- **Decrypting an Image:**
  ![Decrypt Example](images/decrypt_example.png)

## Key Management

- The encryption and decryption processes use a key that is converted to an integer. Ensure that the same key is used for both processes to correctly encrypt and decrypt images.

## Contributions

Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or issues, please open an issue on the GitHub repository or contact the repository owner.

---

Feel free to customize the README to better fit your project's specifics or add any additional information that might be useful to users.
