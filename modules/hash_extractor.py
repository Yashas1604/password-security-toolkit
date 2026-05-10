import hashlib

def extract_simulated_hashes(users: dict) -> dict:
    hashed = {}
    for user, pwd in users.items():
        ntlm = hashlib.new('md4', pwd.encode('utf-16-le')).hexdigest()
        hashed[user] = ntlm
    return hashed

def generate_shadow_hash(password: str) -> str:
    import hashlib
    return hashlib.sha512(password.encode()).hexdigest()