import random
import string
import hashlib
import threading

def generate_random_string(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def check_md5(input):
    input = input.encode('utf-8')
    return hashlib.md5(input).hexdigest()

def crack_password(password):
    while True:
        guess = generate_random_string(len(password))
        guesshash = check_md5(guess)
      
        if password == guesshash:
            print(f'Password cracked! Password: {guess}')
            break

def main():
    test_password = "LeesFakePassword"
    password = check_md5(test_password)
    
    threads = []
    for _ in range(4):
        thread = threading.Thread(target=crack_password, args=(password,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
