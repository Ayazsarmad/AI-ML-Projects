
name = "my name is! ayaz"

a1= name.upper()
print(a1)
a2 = name.lower()
print(a2)
a3 = name.title()
print(a3)
a4 = name.capitalize()
print(a4)
a5 = name.swapcase()
print(a5)
a6 = name.casefold()
print(a6)
a7 = name.count("a")
print(a7)
a8 = name.find("a")
print(a8)
a9 = name.split()
print(a8)
a10 = name.split("!")
print(a10)
a11 = name.replace("a","A")
print(a11)

a12 = name[0:12]
print(a12)

after_capital_name = a12 + "A" + name[-3:]
print(after_capital_name)

# working on list

# In Python, a list is a changeable and ordered sequence that allows duplicates, typically used to store multiple items in a single variable.

a=["apple","mango","banana","apple","mango"]
print(a)
print(type(a))

a.append("cherry")
print(a)

a.insert(2,"orange")
print(a)

a.count("apple")

a.remove("apple")
print(a)

a[2] = "melon"
print(a)



b=("apple","mango","banana","apple","mango")
print(b)
print(type(b))

c={"apple","mango","banana","apple","mango"}
print(c)
print(type(c))

d={"a":"apple","b":"mango","c":"banana","d":"apple","e":"mango"}
print(d)
print(type(d))

for i in range(5):
    print("hi it's me")

for i in range(1,11):
    print(f"3 * {i} = {3*i}")

num = 0
while num < 10:
    print(num)
    num += 1

password = ""
while password != "1234":
    password = input("Enter your password: ")
    if password == "1234":
        print("Password is correct")
    else:
        print("Password is incorrect")
print(f'correct password is: {password}')

animals = {
    "Mammal": "Lion",
    "Mammal2": "Elephant",
    "Reptile": "Crocodile",
    "Bird": "Penguin",
    "Mammal3": "Kangaroo"
}

count=["1st","2nd","3rd","4th","5th"]

animal_keys = list(animals.keys())
animal_values = list(animals.values())

print(animal_keys)
print(animal_values)

for i in range(len(animals)):
    print(f"{count[i]} animal is {animal_keys[i]} and it's name is {animal_values[i]}")

for val in animals.values():
    print(val)

for key in animals.keys():
    print(key)