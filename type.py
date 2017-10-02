x = ['magical unicorns',19,'hello',98.98,'world']
#x = [2,3,1,7,4,12]
#x = ['magical', 'unicorns']
y = ""
z = 0
p = ""
for i in range(0, len(x)):
    if isinstance(x[i], str):
        y = y + " " + x[i]
    elif isinstance(x[i], int):
        z = z + x[i]
        float(z)
    elif isinstance(x[i], float):
        z = z + x[i]
k = "Sum : " + str(z)
j = "String: " + y
if z != 0 and y != "":
    p = "The list entered was mixed"
    print j
    print k
elif z == 0 and len(y) > 0:
    p = "The list entered is a string"
    print j
elif z != 0 and y == "":
    p = "The list entered is a integer"
    print k
print p