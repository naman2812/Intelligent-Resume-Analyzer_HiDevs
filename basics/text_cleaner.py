import sys

def main():
    full_text = sys.stdin.read()
    lines = full_text.splitlines()
    
    name = "Not found."
    email = "Not found."
    
    for line in lines:
        lower_line = line.lower()
        if lower_line.startswith("name:"):
            extracted = line[5:].strip()
            name = extracted.title()
        elif lower_line.startswith("email:"):
            email = line[6:].strip()
            
    words = full_text.split()
    word_count = len(words)
    
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Word count: {word_count}")

if __name__ == "__main__":
    main()
