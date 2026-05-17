"""
लॅब ७ — Function-Based Calculator
====================================
"""

def berij(a, b):
    return a + b

def vajabaki(a, b):
    return a - b

def gunakar(a, b):
    return a * b

def bhagakar(a, b):
    if b == 0:
        return "शून्याने भाग शक्य नाही"
    return a / b


def calculate(kriya, a, b):
    if kriya == "+":
        return berij(a, b)
    elif kriya == "-":
        return vajabaki(a, b)
    elif kriya == "*":
        return gunakar(a, b)
    elif kriya == "/":
        return bhagakar(a, b)
    else:
        return "अज्ञात क्रिया"


print("===== कॅल्क्युलेटर =====")
print(f"10 + 5 = {calculate('+', 10, 5)}")
print(f"10 - 5 = {calculate('-', 10, 5)}")
print(f"10 * 5 = {calculate('*', 10, 5)}")
print(f"10 / 5 = {calculate('/', 10, 5)}")
print(f"10 / 0 = {calculate('/', 10, 0)}")


"""
========================================================
स्पष्टीकरण:
========================================================

प्रत्येक क्रियेसाठी वेगळे function:
   - कोड व्यवस्थित
   - testing सोपे
   - बदल करायला सोपे

calculate हा 'dispatcher' आहे:
   त्याला कोणती क्रिया करायची ते सांगितले की
   तो योग्य function कॉल करतो.

व्यावसायिक कोडमध्ये असेच विभाजन करतात:
   - प्रत्येक function एकच काम करते (Single Responsibility)
   - testing व बदल सोपे
"""
