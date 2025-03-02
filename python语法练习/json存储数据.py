import json

filename = "practice.json"
with open(filename,'w') as file:
    print("You will enter some digits:")
    print("enter 'q' to quit")
    numbers_added=[]
    while True:
        number = input("enter some digits:")
        if number == 'q':
            break
        numbers_added.append(number)
    json.dump(numbers_added,file)
with open(filename,'r') as file:
    numbers_added_displayed = json.load(file)
    print(numbers_added_displayed)