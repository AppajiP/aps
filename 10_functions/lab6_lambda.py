"""
लॅब ६ — Lambda Functions
==========================
"""

varg = lambda x: x * x
print("5 चा वर्ग:", varg(5))

berij = lambda a, b: a + b
print("3 + 7 =", berij(3, 7))

is_sam = lambda n: n % 2 == 0
print("10 सम?:", is_sam(10))
print("7 सम?:", is_sam(7))

sankhya = [1, 2, 3, 4, 5]

varg_yadi = list(map(lambda x: x * x, sankhya))
print("\nवर्ग यादी:", varg_yadi)

sam_yadi = list(filter(lambda x: x % 2 == 0, sankhya))
print("सम यादी:", sam_yadi)

vidyarthi = [
    {"naav": "राम", "vay": 15},
    {"naav": "सीता", "vay": 14},
    {"naav": "गणेश", "vay": 16},
]
laghuvar = sorted(vidyarthi, key=lambda v: v["vay"])
print("\nवयानुसार:", laghuvar)


"""
========================================================
स्पष्टीकरण:
========================================================

lambda सिंटॅक्स:
   lambda parameters: expression

   म्हणजे:
   def varg(x):
       return x * x
   --- च्याऐवजी ---
   varg = lambda x: x * x

lambda मध्ये:
   - फक्त एक expression
   - return लिहायची गरज नाही (आपोआप होते)
   - print, if-else block वगैरे नाही (एक ternary चालेल)

map(f, iterable):
   प्रत्येक वस्तूवर f लागू करून नवीन iterable.

filter(f, iterable):
   ज्यांच्यासाठी f(x) True तेच ठेवते.

sorted(list, key=f):
   f च्या निकालानुसार क्रमवारी.

   key=lambda v: v["vay"]  ->  प्रत्येक dict च्या vay वर sort.
"""
