import hashlib
import itertools
import string
import time

def hash_password(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()

def dictionary_attack(target_hash: str, wordlist_file: str):
    try:
        with open(wordlist_file, 'r') as f:
            for word in f:
                word = word.strip()
                if hash_password(word) == target_hash:
                    return {"status": "success", "password": word}
        return {"status": "failed", "message": "Not found in dictionary"}
    except FileNotFoundError:
        return {"status": "error", "message": "Wordlist file not found"}

def brute_force_attack(target_hash: str, max_length=4):
    chars = string.ascii_lowercase + string.digits
    start = time.time()
    
    for length in range(1, max_length + 1):
        for combo in itertools.product(chars, repeat=length):
            attempt = ''.join(combo)
            if hash_password(attempt) == target_hash:
                elapsed = time.time() - start
                return {"status": "success", "password": attempt, "time": f"{elapsed:.2f}s"}
    
    return {"status": "failed", "message": "Password not found"}