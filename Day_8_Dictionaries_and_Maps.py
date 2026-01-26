n = int(input())
phoneBook = {}
expression =[]

while n > 0:
    keyValue = input()
    result = keyValue.split(" ")
    phoneBook[result[0]] = result[1]
    n-=1


while True:
    try:
        name = input()
        if name in phoneBook:
            expression.append(f"{name}={phoneBook.get(name)}")
        else:
            expression.append("Not found")
    except EOFError:
        break


for e in expression:
    print(e)

    