test = """
global hi
hi = "Hello World!"
"""
test = exec(test)
print(hi)