"""
count = 0

while count <= 10:
    print(count)
    count += 2
"""
"""
start_number = int(input("Enter Start Number: "))
end_number = int(input("Enter End Number: "))

while start_number <= end_number:
    print(start_number)
    start_number += 2

print("Start Number must be less or equal to End Number")
"""

"""
count = 0

while count <= 10:
    print(count)
    count += 1
    if count == 6:
        break
"""


count = 0

while count <= 10:
    print(count)
    count += 1
    if count == 6:
        continue
    if count == 10:
        break
