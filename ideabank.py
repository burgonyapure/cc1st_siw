idea = input("What is your new idea:")
idea = idea + "\n"
file = open("idea.txt","a")

file.write(idea)
file.close()

file = open("idea.txt","r")
print(file.read())
file.close()
