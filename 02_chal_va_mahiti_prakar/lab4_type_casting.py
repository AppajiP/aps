"""
लॅब ४ — प्रकार बदलणे (Type Casting)
=====================================
"""

s = "100"
print("string:", s, type(s))
n = int(s)
print("integer:", n, type(n))
print("बेरीज:", n + 50)

x = 25
y = float(x)
print("float:", y, type(y))

age = 15
msg = "माझे वय " + str(age) + " वर्षे आहे."
print(msg)

print(bool(0))      # False
print(bool(1))      # True
print(bool(""))     # False
print(bool("राम"))  # True

pi = 3.99
print(int(pi))


"""
========================================================
स्पष्टीकरण:
========================================================

int(x)    ->  x ला integer मध्ये बदलते.
              "100" -> 100
              3.99 -> 3 (दशांश गाळून टाकते, गोल नाही)

float(x)  ->  x ला float मध्ये बदलते.
              25 -> 25.0

str(x)    ->  x ला string मध्ये बदलते.
              15 -> "15"
              आवश्यक: integer ला string सोबत + करायला.

bool(x)   ->  x ला boolean मध्ये बदलते.
              False साठी: 0, 0.0, "", None, [], (), {}
              बाकी सगळे -> True

महत्त्वाचे:
   int("राम") असे केले तर ERROR येईल कारण "राम" ला integer
   मध्ये बदलता येत नाही.
"""
