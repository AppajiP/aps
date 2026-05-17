"""
लॅब २ — return विधान
======================
"""

def berij(a, b):
    return a + b


def gunakar(a, b):
    return a * b


uttar = berij(10, 5)
print("बेरीज:", uttar)
print("गुणाकार:", gunakar(4, 5))
print("बेरीज + गुणाकार:", berij(3, 2) + gunakar(2, 3))


def varg_va_ghan(n):
    return n * n, n * n * n


v, g = varg_va_ghan(5)
print(f"\n5 चा वर्ग: {v}, घन: {g}")


def is_sam(n):
    if n % 2 == 0:
        return True
    return False

print("\n10 सम?:", is_sam(10))
print("7 सम?:", is_sam(7))


"""
========================================================
स्पष्टीकरण:
========================================================

return       ->  function मधून किंमत 'परत' देतो.
                 return नंतरचा कोड चालत नाही (function संपते).

return नसल्यास:
   function आपोआप None परत करते.

multiple return:
   return a, b, c   ->  tuple (a, b, c) परत
   x, y, z = func() ->  unpack करून घ्या

return vs print:
   print  ->  फक्त स्क्रीनवर दाखवते
   return ->  किंमत परत देते - पुढे वापरता येते

टीप:
   if-else मध्ये दोन्ही ठिकाणी return असेल तर
   "early return pattern" — कोड वाचायला सोपा होतो.
"""
