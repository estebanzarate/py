f = open('clase8/miMascota.txt', 'r')
content = f.read()
print(content)
f.close()

f = open('clase8/miMascota.txt', 'r')
print(f.readline())
f.close()

f = open('clase8/miMascota.txt', 'r')
for line in f.readlines():
    print(line)
f.close()

f = open('clase8/miMascota.txt', 'r')
f.seek(3)
print(f.read())
f.close()
