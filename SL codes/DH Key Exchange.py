# Shared prime number (prime) and a primitive root modulo prime (g)
prime = 23
g = 5

# Alice's private key
private_key_alice = 6

# Bob's private key
private_key_bob = 15

# Calculate public keys for Alice and Bob
public_key_alice = (g ** private_key_alice) % prime
public_key_bob = (g ** private_key_bob) % prime

# Simulate exchange of public keys

# Alice and Bob share public keys and calculate shared secret
shared_secret_alice = (public_key_bob ** private_key_alice) % prime
shared_secret_bob = (public_key_alice ** private_key_bob) % prime

# Both Alice and Bob should now have the same shared secret
print("Shared Secret (Alice):", shared_secret_alice)
print("Shared Secret (Bob):", shared_secret_bob)