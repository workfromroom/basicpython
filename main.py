import requests

print("Masukkan alamat web: ")
x = input()

try:
    r = requests.get(x)
    print(r.status_code)
    if r.status_code == 200:
        print(r.text)
except Exception as e:
    print("ada error \n", e)
