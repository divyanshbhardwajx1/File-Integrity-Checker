
import hashlib
import os
import json

HASH_DB = "file_hashes.json"

def calculate_hash(filepath):
    """Calculate SHA-256 hash of a file."""
    sha256 = hashlib.sha256()
    try:
        with open(filepath, 'rb') as f:
            for block in iter(lambda: f.read(4096), b''):
                sha256.update(block)
        return sha256.hexdigest()
    except FileNotFoundError:
        return None

def save_hashes(file_list):
    """Save hashes of files to HASH_DB."""
    hashes = {}
    for file in file_list:
        file_hash = calculate_hash(file)
        if file_hash:
            hashes[file] = file_hash
        else:
            print(f"[!] File not found: {file}")
    with open(HASH_DB, 'w') as db:
        json.dump(hashes, db, indent=4)
    print("[+] Hashes saved successfully.")

def check_integrity():
    """Check if files have been modified."""
    try:
        with open(HASH_DB, 'r') as db:
            old_hashes = json.load(db)
    except FileNotFoundError:
        print("[!] No hash database found. Please run save_hashes() first.")
        return

    for file, old_hash in old_hashes.items():
        current_hash = calculate_hash(file)
        if current_hash is None:
            print(f"[!] File missing: {file}")
        elif current_hash != old_hash:
            print(f"[✗] File modified: {file}")
        else:
            print(f"[✓] File unchanged: {file}")

def main():
    print("=== File Integrity Checker ===")
    print("1. Save current file hashes")
    print("2. Check file integrity")
    choice = input("Enter choice (1/2): ")

    if choice == '1':
        files = input("Enter comma-separated file paths: ").split(',')
        files = [f.strip() for f in files]
        save_hashes(files)
    elif choice == '2':
        check_integrity()
    else:
        print("[!] Invalid choice")

if __name__ == "__main__":
    main()
