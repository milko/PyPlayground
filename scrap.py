# Sorting maps.
a = {"uno": 1, "due": 2, "tre": 3}
print(a)
b = sorted(a)
print(b)
print("===========================")
# Sets.
# a = set(["uno", "due", "tre", "uno"])
a = set()
print(str(a))
a.add("quattro")
print(str(a))
a.add("quattro")
print(str(a))
a.add("uno")
print(str(a))
print("===========================")
# x = set(["uno", "due", "tre"])
x = ["uno", "due", "tre"]
x.extend(["quattro", "cinque"])
print( str(x) )
print("===========================")
a = {"uno", "due", "tre", "qua", "cin"}
print(a)
b = {"uno", "tre"}
print(b)
print( str(a - b) )
print("===========================")
a = ['A', 'C', 'F', 'D', 'B', 'E']
x = a.index('F')
print(str(x))
print(str(a[x]))
print("===========================")
print("===========================")
