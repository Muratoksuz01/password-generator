import random
import string

def generate_password(length=12):
    # Şifre karakterleri
    characters = string.ascii_letters + string.digits + string.punctuation+" "

    # Rastgele şifre oluştur
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

# Örnek: 12 karakter uzunluğunda bir şifre oluştur
lenght=int(input("how many character:"))
piece=int(input("how many pieces:"))
for _ in range(piece):
    generated_password = generate_password(lenght)
    print(generated_password)