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


def display_home_screen():
    print("\n╔═══════════════════════════════════════════╗")
    print("║                 Enphosobits               ║")
    print("╚═══════════════════════════════════════════╝")


def display_menu():
    print("\n╔═══════════════════════════════════════════╗")
    print("║                 Enphosobits               ║")
    print("╚═══════════════════════════════════════════╝")
    print("\nMenu:")
    print("1. Encrypt Data")
    print("2. Decrypt Data")
    print("3. Exit")



def main():
    display_title_screen()
    enphosobits = Enphosobits()

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

        choice = input("Enter your choice (1/2/3): ")

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
        else:
            print("\nInvalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()