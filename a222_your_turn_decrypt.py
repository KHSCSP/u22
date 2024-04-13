# encryption
mess = "Don't raise your voice, improve your argument."
step1 = [ord(item) for item in mess]
step2 = [hex(item) for item in step1]

# for item in step2:
#     print(item)




# decrypt the text in the input file
# you can copy the text to a list in this file
# or import sys and use for line in sys.stdin, then run from the bash terminal
import sys

data = []
for line in sys.stdin:
    data.append(line.strip())
# print(data)

for item in data:
    print(chr(int(item, base=16)), end="")