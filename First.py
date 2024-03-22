string_1 = [1,2,3,4,5,6,'M']
string_2 = [7,8,8,9,10,'W']

print("Here is Two string.")

str_3 = string_1 +string_2

if 'W' in str_3:
    print("W is here.")
    num = str_3.index('W')
    print(str_3[:num+1])
elif 'H' in str_3:
    print("H is here.")
    
if 'M' in str_3:
    print("M is here.")
    num = str_3.index('M')
    print(str_3[:num+1])
else:
    print("Nothing is here.")


    