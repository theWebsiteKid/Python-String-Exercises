message = raw_input("Type a string: ")
new_message = ''

lowercase = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
uppercase = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

for i in range(len(message)):
    if message[i] in lowercase:
        pos = lowercase.index(message[i])
        if i == 0:
            new_message += uppercase[pos]
        elif message[i - 1] == ' ':
            new_message += uppercase[pos]
        else:
            new_message += message[i]
    else:
        new_message += message[i]
print new_message