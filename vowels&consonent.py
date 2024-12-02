count_vowels = 0     #for show the value 0 replace with ''
conut_consonent = 0  #for show the value 0 replace with ''

variable = input("Enter any string values: ")
vowels = "AEIOUaeiou"

for i in variable:
    if i in vowels:
        count_vowels += 1         #for show the value 1 replace with i
    else:
        conut_consonent +=1       #for show the value 1 replace with i

print(variable," string vowels: ", count_vowels, " & consonent: ", conut_consonent)