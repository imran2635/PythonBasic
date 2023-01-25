"""
Logical operator:
1. AND
2. OR
3. NOT
"""

"""
AND: Check whether two conditions are equal.Returns True if they are equal else False.
OR: Check multiple conditions are equal.Returns True if either ot both are equal else False.
NOT: Check single condition.Reverse order.Returns True if the condition is False.
"""


def AND(condition1, condition2):
    if condition1 and condition2:
        return True
    else:
        return False


print(AND(True, False))


def OR(condition1, condition2, condition3):
    if condition1 or condition2 or condition3:
        return True
    else:
        return False


print(OR(False, False, True))


def NOT(condition):
    if not condition:
        return True
    else:
        return False


print(NOT(True))
