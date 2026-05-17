"""
लॅब ३ — तार्किक ऑपरेटर्स (Logical: and, or, not)
==================================================
"""

vay = 17
ahe_vidyarthi = True

print("and उदाहरण:")
print(vay > 14 and vay < 18)
print(vay > 14 and ahe_vidyarthi)

print("\nor उदाहरण:")
print(vay > 18 or ahe_vidyarthi)
print(vay > 18 or vay < 10)

print("\nnot उदाहरण:")
print(not ahe_vidyarthi)
print(not (vay > 18))


"""
========================================================
स्पष्टीकरण — सत्यता सारणी (Truth Table):
========================================================

and (आणि)        |  निकाल
True  and True   ->  True
True  and False  ->  False
False and True   ->  False
False and False  ->  False
(दोन्ही खरी असतीलच तरच True)

or (किंवा)       |  निकाल
True  or True    ->  True
True  or False   ->  True
False or True    ->  True
False or False   ->  False
(एक तरी खरी असली की True)

not (नाही)       |  निकाल
not True         ->  False
not False        ->  True
(खर्‍याचे खोटे करते व खोट्याचे खरे)
"""
