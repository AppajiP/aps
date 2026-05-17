"""
लॅब ५ — List Comprehension
============================
"""

varg = [i * i for i in range(1, 6)]
print("वर्ग:", varg)

ghan = [i ** 3 for i in range(1, 6)]
print("घन:", ghan)

sam = [i for i in range(1, 21) if i % 2 == 0]
print("सम:", sam)

vishishtye = [i for i in range(1, 21) if i % 2 != 0]
print("विषम:", vishishtye)

naav_yadi = ["राम", "सीता", "लक्ष्मण"]
moth_naav = [n.upper() for n in naav_yadi]
print("मोठे:", moth_naav)

shreni = ["A" if g >= 75 else "B" if g >= 60 else "F" for g in [85, 60, 30, 95]]
print("श्रेण्या:", shreni)


"""
========================================================
स्पष्टीकरण:
========================================================

[expression for x in iterable]
   प्रत्येक x साठी expression काढून नवी list तयार.

[expression for x in iterable if condition]
   फक्त ज्यांची condition खरी, त्यांच्यासाठीच.

[A if cond else B for x in iterable]
   अटेनुसार A किंवा B.

सोप्या रूपात:
   varg = []
   for i in range(1, 6):
       varg.append(i * i)
   -- हे एका ओळीत --
   varg = [i*i for i in range(1, 6)]

का वापरावी?
   १. कमी कोड
   २. वेगवान
   ३. पायथन-शैली (Pythonic)
"""
