student={"name":"arun","age":20,"address":"ktm"}
print(student.keys())
print(student.values())
print(student.items())

data=("a","b","c","d","e","f","g","h","i","j")
print(data[:5])
print(data[2:9])
print(data[8:3])
print(data[7:])
print(data[0:6])
print(data[-9:-2])
print(data[2:-2])
print(data[-3:])
print(data[:-2])
print(data[2:9:2])


#swapping values in through tuple packing and unpacking
a=3
b=6
a,b=b,a
print(a)
print(b)