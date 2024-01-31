class Enphosobits:
    def __init__(self):
        self.key = "enphosian_secret_key"

    def encrypt(self, data):
        encrypted_data = ""
        for char in data:
            encrypted_data += chr(ord(char) + len(self.key))
        return encrypted_data

    def decrypt(self, encrypted_data):
        decrypted_data = ""
        for char in encrypted_data:
            decrypted_data += chr(ord(char) - len(self.key))
        return decrypted_data


class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift

    def encrypt(self, data):
        encrypted_data = ""
        for char in data:
            if char.isalpha():
                shifted = ord(char) + self.shift
                if char.islower():
                    if shifted > ord('z'):
                        shifted -= 26
                elif char.isupper():
                    if shifted > ord('Z'):
                        shifted -= 26
                encrypted_data += chr(shifted)
            else:
                encrypted_data += char
        return encrypted_data

    def decrypt(self, encrypted_data):
        decrypted_data = ""
        for char in encrypted_data:
            if char.isalpha():
                shifted = ord(char) - self.shift
                if char.islower():
                    if shifted < ord('a'):
                        shifted += 26
                elif char.isupper():
                    if shifted < ord('A'):
                        shifted += 26
                decrypted_data += chr(shifted)
            else:
                decrypted_data += char
        return decrypted_data


class SubstitutionCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, data):
        encrypted_data = ""
        for char in data:
            if char.isalpha():
                if char.islower():
                    encrypted_data += self.key[ord(char) - ord('a')].lower()
                elif char.isupper():
                    encrypted_data += self.key[ord(char) - ord('A')].upper()
            else:
                encrypted_data += char
        return encrypted_data

    def decrypt(self, encrypted_data):
        decrypted_data = ""
        for char in encrypted_data:
            if char.isalpha():
                if char.islower():
                    index = self.key.lower().find(char.lower())
                    decrypted_data += chr(index + ord('a'))
                elif char.isupper():
                    index = self.key.find(char.lower())
                    decrypted_data += chr(index + ord('A'))
            else:
                decrypted_data += char
        return decrypted_data


class ASCIIShiftCipher:
    def __init__(self, shift):
        self.shift = shift

    def encrypt(self, data):
        encrypted_data = ""
        for char in data:
            encrypted_data += chr(ord(char) + self.shift)
        return encrypted_data

    def decrypt(self, encrypted_data):
        decrypted_data = ""
        for char in encrypted_data:
            decrypted_data += chr(ord(char) - self.shift)
        return decrypted_data


def display_title_screen():
    print("╔═══════════════════════════════════════════╗")
    print("║                 Enphosobits               ║")
    print("║           Welcome to Enphosobits!         ║")
    print("╚═══════════════════════════════════════════╝")
    print("               Press Enter to continue         ")
    input()


def display_login_screen():
    print("\n╔═══════════════════════════════════════════╗")
    print("║                 Enphosobits               ║")
    print("╚═══════════════════════════════════════════╝")
    print("                 Login Screen                  ")
    print("-----------------------------------------------")
    username = input("Username: ")
    password = input("Password: ")
    print("-----------------------------------------------")
    return username, password


def display_menu():
    print("\n╔═══════════════════════════════════════════╗")
    print("║                 Enphosobits               ║")
    print("╚═══════════════════════════════════════════╝")
    print("\nMenu:")
    print("1. Encrypt Data")
    print("2. Decrypt Data")
    print("3. Exit")
    print("4. Use Caesar Cipher")
    print("5. Use Substitution Cipher")
    print("6. Use Regular ASCII Shift Cipher")
    print("7. Use All Ciphers (Encryption)")
    print("8. Decrypt Caesar Cipher")
    print("9. Decrypt Substitution Cipher")
    print("10. Decrypt Regular ASCII Shift Cipher")
    print("11. Decrypt All Ciphers")


def main():
    display_title_screen()
    enphosobits = Enphosobits()
    caesar_cipher = None
    substitution_cipher = None
    ascii_shift_cipher = None

    # Login loop
    while True:
        username, password = display_login_screen()
        # Dummy authentication (replace with your authentication logic)
        if username == "enphoworldwide2" and password == "passwordphoso":
            print("Login successful!")
            break
        else:
            print("Invalid username or password. Please try again.")

    # Border added after login screen
    print("\n╔═══════════════════════════════════════════╗")
    print("║                 Main Menu                 ║")
    print("╚═══════════════════════════════════════════╝")

    # Main menu loop
    while True:
        display_menu()

        choice = input("Enter your choice (1-11): ")

        if choice == "1":
            data = input("Enter data to encrypt: ")
            encrypted_data = enphosobits.encrypt(data)
            print("\nEncrypted data:", encrypted_data)
        elif choice == "2":
            encrypted_data = input("Enter encrypted data: ")
            decrypted_data = enphosobits.decrypt(encrypted_data)
            print("\nDecrypted data:", decrypted_data)
        elif choice == "3":
            print("\nExiting Enphosobits Encryption App. Goodbye!")
            break
        elif choice == "4":
            if caesar_cipher is None:
                shift = int(input("Enter the shift value for Caesar Cipher: "))
                caesar_cipher = CaesarCipher(shift)
            data = input("Enter data to encrypt using Caesar Cipher: ")
            encrypted_data = caesar_cipher.encrypt(data)
            print("\nEncrypted data using Caesar Cipher:", encrypted_data)
        elif choice == "5":
            if substitution_cipher is None:
                key = input("Enter the substitution key (26 characters, no duplicates): ")
                substitution_cipher = SubstitutionCipher(key)
            data = input("Enter data to encrypt using Substitution Cipher: ")
            encrypted_data = substitution_cipher.encrypt(data)
            print("\nEncrypted data using Substitution Cipher:", encrypted_data)
        elif choice == "6":
            if ascii_shift_cipher is None:
                shift = int(input("Enter the shift value for ASCII Shift Cipher: "))
                ascii_shift_cipher = ASCIIShiftCipher(shift)
            data = input("Enter data to encrypt using ASCII Shift Cipher: ")
            encrypted_data = ascii_shift_cipher.encrypt(data)
            print("\nEncrypted data using ASCII Shift Cipher:", encrypted_data)
        elif choice == "7":
            data = input("Enter data to encrypt using all ciphers: ")
            encrypted_data = data
            if caesar_cipher:
                encrypted_data = caesar_cipher.encrypt(encrypted_data)
            if substitution_cipher:
                encrypted_data = substitution_cipher.encrypt(encrypted_data)
            if ascii_shift_cipher:
                encrypted_data = ascii_shift_cipher.encrypt(encrypted_data)
            encrypted_data = enphosobits.encrypt(encrypted_data)
            print("\nEncrypted data using all ciphers:", encrypted_data)
        elif choice == "8":
            if caesar_cipher is not None:
                encrypted_data = input("Enter encrypted data from Caesar Cipher: ")
                decrypted_data = caesar_cipher.decrypt(encrypted_data)
                print("\nDecrypted data from Caesar Cipher:", decrypted_data)
            else:
                print("\nCaesar Cipher has not been used yet.")
        elif choice == "9":
            if substitution_cipher is not None:
                encrypted_data = input("Enter encrypted data from Substitution Cipher: ")
                decrypted_data = substitution_cipher.decrypt(encrypted_data)
                print("\nDecrypted data from Substitution Cipher:", decrypted_data)
            else:
                print("\nSubstitution Cipher has not been used yet.")
        elif choice == "10":
            if ascii_shift_cipher is not None:
                encrypted_data = input("Enter encrypted data from ASCII Shift Cipher: ")
                decrypted_data = ascii_shift_cipher.decrypt(encrypted_data)
                print("\nDecrypted data from ASCII Shift Cipher:", decrypted_data)
            else:
                print("\nASCII Shift Cipher has not been used yet.")
        elif choice == "11":
            encrypted_data = input("Enter data encrypted with all ciphers: ")
            decrypted_data = encrypted_data
            if caesar_cipher:
                decrypted_data = caesar_cipher.decrypt(decrypted_data)
            if substitution_cipher:
                decrypted_data = substitution_cipher.decrypt(decrypted_data)
            if ascii_shift_cipher:
                decrypted_data = ascii_shift_cipher.decrypt(decrypted_data)
            decrypted_data = enphosobits.decrypt(decrypted_data)
            print("\nDecrypted data using all ciphers:", decrypted_data)
        else:
            print("\nInvalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()