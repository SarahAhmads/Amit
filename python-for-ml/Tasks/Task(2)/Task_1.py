Email = "Amit_ml@gmail.edu"
Username = Email.split("@")
Domain = Username[1].split(".")

print("The Domain is: " + Domain[0])
print("The Username is: " + Username[0])

if Domain[-1] == "edu":
    print("Educational Domain")
elif Domain[-1] == "com":
    print("Commercial Domain")
else:
    print("Other Domain")
