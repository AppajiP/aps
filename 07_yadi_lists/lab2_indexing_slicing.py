"""
लॅब २ — Indexing व Slicing
============================
"""

phale = ["आंबा", "केळी", "सफरचंद", "द्राक्ष", "पेरू"]

print("phale[0]  =", phale[0])
print("phale[1]  =", phale[1])
print("phale[-1] =", phale[-1])
print("phale[-2] =", phale[-2])

print("\n--- Slicing ---")
print("phale[1:4]   =", phale[1:4])
print("phale[:3]    =", phale[:3])
print("phale[2:]    =", phale[2:])
print("phale[::2]   =", phale[::2])
print("phale[::-1]  =", phale[::-1])

print("\n--- बदलणे ---")
phale[0] = "पपई"
print("बदलल्यानंतर:", phale)


"""
========================================================
स्पष्टीकरण:
========================================================

Indexing:
   list[0]    ->  पहिले
   list[-1]   ->  शेवटचे
   list[-2]   ->  शेवटून दुसरे

Slicing — list[start:stop:step]
   list[1:4]    ->  index 1, 2, 3 (4 चा समावेश नाही!)
   list[:3]     ->  सुरुवातीपासून index 2 पर्यंत
   list[2:]     ->  index 2 पासून शेवटपर्यंत
   list[::2]    ->  दर दुसरा
   list[::-1]   ->  उलट क्रम

list बदलणे:
   list[0] = "नवीन"  ->  pos 0 ची किंमत बदलते.
   (कारण list 'mutable' आहे)
"""
