import string
dict = {}
data = ""
file = open("enscrypted.txt","w")
for i in range(len(string.ascii_letters)):
    dict[string.ascii_letters[i]] = string.ascii_letters[i-5]
print("Original Dictionary: ", dict)
with open ("cipher.txt", "r") as f:
    while True:
        c = f.read(1)
        if not c:
            print("end of file")
            break
        if c in dict:
            data = dict[c]
        else:
            data = c
        file.write(data)
        print (data)
file.close()