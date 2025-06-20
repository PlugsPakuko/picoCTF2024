# This script exploit rsa that vulnerable to homomorphic encryption property.
# c1 * c2 = pow(m1*m2,e,n)
# if c1 = pow(m1,e,n), c2 = pow(m2,e,n)

c1 = open('password.enc', 'r').read().strip()
c1 = int(c1)
m2 = int(input("Enter message as HEX (m2): "),16)
c2 = int(input("Enter ciphertext from oracle (c2 = E(m2)): "))

c3 = c1 * c2
print(f"Have the oracle decrypt this message (c3 = c1 * c2): {c3}\n")
m3 = int(input("Enter decrypted ciphertext as HEX (m3 = D(c3): "), 16)
m1 = m3 // int(m2)
print(f"Password (m1 = m3 / m2) as HEX: {m1}")
print(f"Password (m1 = m3 / m2) as ASCII: {bytes.fromhex(hex(m1)[2:]).decode('utf-8')}")
