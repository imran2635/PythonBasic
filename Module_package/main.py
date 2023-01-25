"""
# Import full module
import mymodule

full_name_new = mymodule.generate_full_name("Mr.", "Green")
print(full_name_new)
"""


"""
# Import full module by different name
import mymodule as fullname

full_name_new = fullname.generate_full_name("Mr.", "Green")
print(full_name_new)
"""

"""
# Import specific function from module
from mymodule import generate_full_name,summation

full_name_new = generate_full_name("Mr.", "Kevin")
print(full_name_new)

result = summation(10,20)
print(result)
"""


