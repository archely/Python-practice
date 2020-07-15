rawstr = input ("Enter a number: ")

try:
    ival = int(rawstr)
except:
    ival = -1

if ival > 0:
    print("Nice work! ")
else:
    print ("Not a number")



---------------------------------------------------
#Another loop

a = "bob"

try:
    print("Hello")
    int(a)
    ptint("There")
except:
    istr = -1
    print("Done",istr)


-----------------------------------------------------


#Function Loops

def great(lang):
    if lang == "es":
        return "Hola"
    elif lang == "fr":
        return "Bonjour"
    elif lang == "hu":
        return szia
    elif lang == "tr":
        return "Merhaba"
    else:
        return "Hello"

    print(great("fr"), "Arda")





---------------------------------------------------

#While Loop

while True:

    line = input (">")
    if line == "done":
        break
    print("line")
print("done")


-------------------------------------------------------
#List

friends = ["Arda", "Orçun" , "Kerem"]

for friend in friends:
    print("Happy new year", friend)
print("Done! ")


--------------------------------------------------------
# for value in variable]

print("Before")
for thing in [2,4,6,8]:
    print(thing)
print("After")


-------------------------------------------------------------

longest_so_far = -1
print("Before", largest_so_far)
for the_num in [3,3,4,6,5,]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)
print("After", largest_so_far)
