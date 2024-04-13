
print("\n---- convert int to binary using bin()")
num = 42
ans = bin(num)
print(num, "=", ans)


print("\n---- convert int to hex using hex()")
num = 42
ans = hex(num)
print(num, "=", ans)



print("\n---- convert binary to int using int()")
num = '101011'
ans = int(num, base=2)
print(num, "=", ans)


num = '0b101011'
ans = int(num, base=2)
print(num, "=", ans)


print("\n---- convert hex to int using int()")
num = '0x2a'
ans = int(num, base=16)
print(num, "=", ans)
num = '2a'
ans = int(num, base=16)
print(num, "=", ans)s



print("\n---- convert text to ascii using ord()")
letters = 'hello'
for item in letters:
    print(item, "=", ord(item))



print("\n\n---- convert ascii to text using chr()")
encoded = [104, 101, 108, 108, 111]
for item in encoded:
    print(item, "=", chr(item))
