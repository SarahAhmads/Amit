def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"

name = input("Enter your name: ")
result = are_you_playing_banjo(name)
print(result)