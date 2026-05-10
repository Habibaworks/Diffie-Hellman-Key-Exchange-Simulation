Import random

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def find_primitive_root(p):
    for g in range(2, p):
        powers = set()
        for i in range(1, p):
            powers.add(pow(g, i, p))
        if len(powers) == p - 1:
            return g
    return None

# Step 1: Get public prime number p and primitive root g from user
while True:
    try:
        p = int(input("Enter a prime number (p): "))
        if is_prime(p):
            break
        else:
            print("That's not a prime number. Try again.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Optional: Find primitive root or let user choose
g = find_primitive_root(p)
print(f"Primitive root modulo {p} is {g}")

# Step 2: Choose private keys
choice = input("Do you want to input private keys? (y/n): ").strip().lower()

if choice == 'y':
    a = int(input("Enter Alice's private key (a): "))
    b = int(input("Enter Bob's private key (b): "))
else:
    a = random.randint(2, p - 2)
    b = random.randint(2, p - 2)
    print(f"Alice's private key (a): {a}")
    print(f"Bob's private key (b): {b}")

# Step 3: Compute public keys
A = pow(g, a, p)  # Alice's public key
B = pow(g, b, p)  # Bob's public key

print(f"Alice's public key (A = g^a mod p): {A}")
print(f"Bob's public key (B = g^b mod p): {B}")

# Step 4: Compute shared secrets
shared_secret_alice = pow(B, a, p)
shared_secret_bob = pow(A, b, p)

print(f"Alice's computed shared secret: {shared_secret_alice}")
print(f"Bob's computed shared secret: {shared_secret_bob}")

# Check if they match
if shared_secret_alice == shared_secret_bob:
    print("\n✅ Key exchange successful! Shared secret established.")
else:
    print("\n❌ Key exchange failed. Shared secrets do not match.")
