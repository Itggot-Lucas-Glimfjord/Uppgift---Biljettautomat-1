def ask_age():
    age = raw_input("your age: ")
    age = int(age)
    while age < 0:
        age = raw_input("That's not a valid age: ")

    return age

def ticket_price(age):
    if age < 18:
        return "10Kr"
    elif age < 65:
        return "20Kr"
    else:
        return "15Kr"


older = ask_age()
print (ticket_price(age=older) )