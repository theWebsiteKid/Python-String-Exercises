message = raw_input("Type a string: ")
new_message = ''

lowercase = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
uppercase = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

for char in message:
    letter = char
    for i in range(len(lowercase)):
        lowerletter = lowercase[i]
        if lowerletter == char:
            letter = uppercase[i]
            break
            
    new_message += letter
print new_message