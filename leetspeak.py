message = raw_input("What's happening?: ")
new_message = ''

alpha = ["A","E","G","I","O","S","T"]
numeric = ["4","3","6","1","0","5",]

for char in message:
    letter = char
    for i in range(len(alpha)):
        alpha_letter = alpha[i]
        if alpha_letter == char:
            letter = numeric[i]
            break
    new_message += letter
print new_message