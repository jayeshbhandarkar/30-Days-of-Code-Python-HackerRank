n = int(input())
phone_book = {}

for _ in range(n):
    name, phone_number = input().split()
    phone_book[name] = phone_number

while True:
    try:
        query = input()
        if query in phone_book:
            print(f"{query}={phone_book[query]}")
        else:
            print("Not found")
    except EOFError:
        break
