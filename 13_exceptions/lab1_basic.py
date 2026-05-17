"""
लॅब १ — try-except मूळ
========================
"""

try:
    a = 10 / 0
except ZeroDivisionError:
    print("शून्याने भाग करता येत नाही!")


try:
    n = int("abc")
except ValueError:
    print("'abc' ला integer मध्ये बदलता येत नाही")


try:
    yadi = [1, 2, 3]
    print(yadi[10])
except IndexError:
    print("list च्या बाहेरचा index!")


print("\nप्रोग्राम बंद पडला नाही — सर्व errors हाताळले!")


"""
========================================================
स्पष्टीकरण:
========================================================

try:
   ...
except ExceptionType:
   ...

कसे काम करते?
   १. try block मधला कोड चालवायचा प्रयत्न.
   २. error नसेल -> except skip.
   ३. error असेल -> लगेच त्या प्रकाराच्या except कडे.
   ४. हाताळला नाही -> प्रोग्राम बंद.

ZeroDivisionError -> शून्याने भाग
ValueError       -> चुकीची किंमत (e.g. int("abc"))
IndexError       -> list/string च्या index बाहेर
KeyError         -> dict मध्ये नसलेली key

try-except नसताना:
   error आला की प्रोग्राम तिथेच बंद पडतो (crash).
   try-except वापरून ते टाळतो.
"""
