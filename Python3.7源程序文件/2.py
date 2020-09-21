import random
menu = ["coffee","tea","cola","milk","water"]
print("menu:",menu)
name = input("your name please:")
drink = random.choice(menu)
print("hello",name,"!enjoy your",drink)
