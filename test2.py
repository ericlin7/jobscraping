
email = input("Please enter email: ")

password = input("Please enter password ")

title = input("Please enter job title you are looking for: ")

location = input("Please type in your location: ")

skills = []
user = input("Enter Skills type x to stop: ")

while(user != "x"):
    user = input("Enter Skills type x to stop: ")
    skills.append(user)

skills.pop()
print(skills)
