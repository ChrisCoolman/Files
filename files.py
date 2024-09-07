import random

for i in range(0, 10000000):
    file = open("Spam/file" + str(random.randint(0, 100000)) + ".txt", "w")
    file.write("Hello, World!" + str(random.randint(0, 1000000)))