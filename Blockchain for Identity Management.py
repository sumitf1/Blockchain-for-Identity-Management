import hashlib
import json
from datetime import datetime

# Block Class
class Block:
    def __init__(self, index, identity_hash, previous_hash):
        self.index = index
        self.timestamp = str(datetime.now())
        self.identity_hash = identity_hash
        self.previous_hash = previous_hash

        # Generate hash for this block
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_data = (
            str(self.index)
            + self.timestamp
            + self.identity_hash
            + self.previous_hash
        )

        return hashlib.sha256(block_data.encode()).hexdigest()


# Blockchain Class
class Blockchain:
    def __init__(self):
        self.chain = []

        # Create Genesis Block
        genesis_block = Block(
            0,
            "GENESIS",
            "0"
        )

        self.chain.append(genesis_block)

    def add_identity(self, identity_hash):
        previous_block = self.chain[-1]

        new_block = Block(
            len(self.chain),
            identity_hash,
            previous_block.hash
        )

        self.chain.append(new_block)

    def verify_blockchain(self):
        for i in range(1, len(self.chain)):

            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check current block hash
            if current_block.hash != current_block.calculate_hash():
                return False

            # Check connection with previous block
            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def display_chain(self):
        for block in self.chain:
            print("\n-----------------------------")
            print("Block Number :", block.index)
            print("Timestamp    :", block.timestamp)
            print("Identity Hash:", block.identity_hash)
            print("Previous Hash:", block.previous_hash)
            print("Block Hash   :", block.hash)


# Identity Management Functions
def create_identity():
    print("\n===== Create Digital Identity =====")

    name = input("Enter Name: ")
    user_id = input("Enter User ID: ")
    email = input("Enter Email: ")

    # Identity information
    identity = {
        "name": name,
        "user_id": user_id,
        "email": email
    }

    # Convert identity to JSON
    identity_data = json.dumps(identity, sort_keys=True)

    # Generate SHA-256 hash
    identity_hash = hashlib.sha256(
        identity_data.encode()
    ).hexdigest()

    return identity, identity_hash


# Main Program
blockchain = Blockchain()

while True:

    print("\n================================")
    print(" BLOCKCHAIN IDENTITY MANAGEMENT")
    print("================================")

    print("1. Register Identity")
    print("2. Display Blockchain")
    print("3. Verify Blockchain")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        identity, identity_hash = create_identity()

        blockchain.add_identity(identity_hash)

        print("\nIdentity Registered Successfully!")
        print("Name :", identity["name"])
        print("User ID :", identity["user_id"])
        print("Email :", identity["email"])

        print("\nIdentity Hash:")
        print(identity_hash)

    elif choice == "2":

        blockchain.display_chain()

    elif choice == "3":

        if blockchain.verify_blockchain():
            print("\nBlockchain Status: VALID")
            print("No tampering detected.")
        else:
            print("\nBlockchain Status: INVALID")
            print("Tampering detected!")

    elif choice == "4":

        print("\nExiting program...")
        break

    else:

        print("\nInvalid choice!")