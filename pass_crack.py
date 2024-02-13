import random, string
import hashlib



def generate_random_string(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def check_md5(input):
    input = input.encode('utf-8')
    return hashlib.md5(input).hexdigest()

while True:
    #  password = input("Enter the hash you would like to crack: ")
    test_password = LeesEpicPasswordThatIsVerySecure 
    password = check_md5(test_password)
    guess = generate_random_string(len(password))
    guesshash = check_md5(guess)
  
    if password == guesshash:
        print(f'Password cracked! Password: {guess}')
        break
