import random

# Function to generate a prime number using the Miller-Rabin primality test
def generate_prime(bits):
    while True:
        potential_prime = random.getrandbits(bits)
        if is_prime(potential_prime):
            return potential_prime

# Function to check if a number is prime using the Miller-Rabin primality test
def is_prime(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True

    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True

# Function to compute the greatest common divisor
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to compute the modular multiplicative inverse
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Function to generate RSA keys
def generate_rsa_keys(bits):
    p = 13
    q = 17
    
    n = p * q
    phi_n = (p - 1) * (q - 1)
    
    e = 5
    while gcd(e, phi_n) != 1:
        e = 5
    
    d = mod_inverse(e, phi_n)
    
    public_key = (n, e)
    private_key = (n, d)
    
    return public_key, private_key

# Function to encrypt a message using RSA
def rsa_encrypt(public_key, plaintext):
    n, e = public_key
    encrypted_text = [pow(ord(char), e, n) for char in plaintext]
    return encrypted_text

# Example usage
bits = 128
public_key, private_key = generate_rsa_keys(bits)
message = "HELLO"
encrypted_message = rsa_encrypt(public_key, message)
print("Public Key (n, e):", public_key)
print("Encrypted Message:", encrypted_message)
