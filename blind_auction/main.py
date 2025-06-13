
dict = {}

max_value = 0

max_key = ''

print("Welcome to the secret auction program.")

while True:
    name = input("what is your name?: ")

    bid = int(input("What's your bid?: "))

    dict[name] = bid

    choice = input("Are there any more bidders? Type 'yes' or 'no'.\n").lower()
    
    if choice == 'no':
        for key in dict:
            if max_value == dict[key]:
                print("Two bidders have bid same amount...")
                break
            elif dict[key] > max_value:
                max_value = dict[key]
                max_key = key
        
        print(f"The highest bidder is {max_key} and the bid was {max_value}.")
        break
    if choice == 'yes':
        True
    else:
        print("Invalid Prompt..")
        break
