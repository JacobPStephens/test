s1 = "abc"
s2 = "lecaabee" 
print(f"{s1=}\n{s2=}")
# generate reference dict
ref = [0] * 26
for i in range(len(s1)):
    ref[ord(s1[i]) - 97] += 1
    ref[ord(s2[i]) - 97] -= 1

i = 0
j = len(s1)
while j < len(s2):
    if ref == [0] * 26:
        print(f"Found at {(i, j)=}")
        print('True')
        exit()

    ref[ord(s2[i]) - 97] += 1
    ref[ord(s2[j]) - 97] -= 1

    i += 1
    j += 1

if ref == [0] * 26:
    print('True')
    exit()
    #print(ref)
print("False")