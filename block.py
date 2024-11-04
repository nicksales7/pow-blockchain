import hashlib 

def calculate_hash(previous_hash, transaction_data, nonce_value) -> str:
    combined = f"{previous_hash}{transaction_data}{nonce_value}"
    return hashlib.sha256(combined.encode('utf-8')).hexdigest()

def mine_block(previous_hash, prefix_difficulty, transaction_data) -> tuple[str, int]:
    nonce_value = 0
    hash_value = "1"

    while hash_value[:len(prefix_difficulty)] != prefix_difficulty:
        hash_value = calculate_hash(previous_hash, transaction_data, nonce_value)
        nonce_value += 1
        print(hash_value)

    return hash_value, nonce_value

mine_block("i34iuthreklhghdkhdkjgh34bj", "00", "idk sends x 5 BTC")
