# Substitution Cipher Web App 🔐

Welcome to the Substitution Cipher repository! This project is a simple yet effective web-based tool for encrypting and decrypting messages using a substitution cipher with a shift-based key. It is built using Python's Flask framework and demonstrates basic cryptographic transformation logic with a user-friendly interface.

## 🚀 Features

- **Encrypt & Decrypt Messages**: Choose between encryption and decryption with a simple toggle.
- **Shift Key Control**: Users can specify a numeric key (0–26) for shifting characters.
- **Input & Output Areas**: Easily type your message and view the result instantly.
- **Error Handling**: Displays a clear error message if the key is not in the valid range (0–26).

## 🛠 Installation

Follow these steps to run the project locally:

1. **Clone the Repository**

   `git clone https://github.com/your-username/substitution-cipher.git`
   
   `cd substitution-cipher`
2. **Create a Virtual Environment (Optional but Recommended)**
   
   `python -m venv venv`
   
   `source venv/bin/activate`  (On Windows: `venv\Scripts\activate`)
3. **Install Dependencies**
   
   `pip install flask`
4. **Run the Flask App**

   `python substitution_cipher.py`
5. **Access the Web App**

   Open your browser and go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## ✨ Usage

- Enter the plaintext you want to encrypt or the ciphertext you want to decrypt.
- Select the operation mode – Encrypt or Decrypt.
- Provide a key between 0 and 26.
- Click Submit.
- View the resulting text in the Ciphertext section.

## Contact

If you have any questions or suggestions regarding this project, feel free to contact us at [atharvat.code@gmail.com](mailto:atharvat.code@gmail.com).
