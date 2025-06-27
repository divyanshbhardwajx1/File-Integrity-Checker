# 🛡️ File Integrity Checker (Windows Version)

A simple Python tool to monitor changes in files by calculating and comparing SHA-256 hash values.

## 🔍 Features

- Calculate SHA-256 hash of any file
- Store hash values in a JSON file for future comparison
- Detect changes, deletions, or integrity of monitored files
- Lightweight and dependency-free (only standard Python libraries)

## 🧰 Requirements

- Python 3.x (Download from [python.org](https://www.python.org/downloads/))

No external libraries required. Uses only built-in modules:
- `hashlib`
- `os`
- `json`

## 🚀 How to Use on Windows

### 1. **Download the Script**

Save `file_integrity_checker.py` to a known location, like your **Desktop**.

### 2. **Open Command Prompt**

Press `Win + R`, type `cmd`, and press **Enter**.

Navigate to the folder where your script is saved:

```cmd
cd Desktop

### 3. Run the Script
cmd
python file_integrity_checker.py
If Python isn’t recognized, use its full path like:
cmd
C:\Users\YourName\AppData\Local\Programs\Python\Python39\python.exe file_integrity_checker.py
🖱️ How to Use
After running the script, you will see this menu:

=== File Integrity Checker ===
1. Save current file hashes
2. Check file integrity
🔹 Option 1: Save File Hashes
Enter full file paths, separated by commas.
✅ Example:
C:\\Users\\YourName\\Desktop\\sample1.txt, C:\\Users\\YourName\\Desktop\\sample2.txt
This creates a file_hashes.json file that stores the hash values of the listed files.

🔹 Option 2: Check File Integrity
Re-checks all the files listed in file_hashes.json
Detects if any file was modified, unchanged, or is missing

🧪 Example Test

Step 1: Modify One File
Edit sample1.txt in Notepad and change its text.

Step 2: Check File Integrity
Run the script again and choose option 2.

🧾 Sample Output
=== File Integrity Checker ===
1. Save current file hashes
2. Check file integrity
Enter choice (1/2): 2
[✗] File modified: C:/Users/YourName/Desktop/sample1.txt
[✓] File unchanged: C:/Users/YourName/Desktop/sample2.txt

📂 Output File
file_hashes.json – a JSON file created in the same directory, storing each file's SHA-256 hash:

{
  "C:/Users/YourName/Desktop/sample1.txt": "a59f3c1d4e098dd9ab...f4",
  "C:/Users/YourName/Desktop/sample2.txt": "cf23df2207d99a74fbe...c42"
}
You can edit this file or delete it to reset the hash tracking.

🧠 How It Works (Internally)
Uses hashlib to generate SHA-256 hashes

Uses a dictionary to store and compare current hashes with saved ones

Identifies:

✓ Unchanged: Hash matches

✗ Modified: Hash mismatch

! Missing: File not found
