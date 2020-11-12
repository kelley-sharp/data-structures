from dynamic_array import DynamicArray
from stack_da import Stack

values = Stack()

for i in range(16):
    if i % 2 == 0:
        values.push(i)
    elif i % 3 == 0:
        values.pop()

print(values)
print(i)
print(values.da.size)
print(values.da.capacity)
