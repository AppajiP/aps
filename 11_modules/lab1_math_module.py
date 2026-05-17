"""
लॅब १ — math module
=====================
"""

import math

print("π (pi) =", math.pi)
print("e =", math.e)
print("√25 =", math.sqrt(25))
print("2^10 =", math.pow(2, 10))
print("5! =", math.factorial(5))
print("floor(3.7) =", math.floor(3.7))
print("ceil(3.2) =", math.ceil(3.2))
print("gcd(12, 18) =", math.gcd(12, 18))

trijya = 7
kshetraphal = math.pi * math.pow(trijya, 2)
print(f"\nत्रिज्या {trijya} असेल तर वर्तुळाचे क्षेत्रफळ = {kshetraphal:.2f}")

paridhi = 2 * math.pi * trijya
print(f"परिघ = {paridhi:.2f}")

print(f"\nsin(30°) = {math.sin(math.radians(30)):.4f}")
print(f"cos(60°) = {math.cos(math.radians(60)):.4f}")


"""
========================================================
स्पष्टीकरण:
========================================================

import math   ->  math module संपूर्ण आणणे

math.pi       ->  π ची किंमत
math.sqrt(x)  ->  वर्गमूळ
math.pow(a,b) ->  a^b (पण ** ऑपरेटर पण चालतो)
math.factorial(n) -> n × (n-1) × ... × 1

math.floor(x) ->  खालची पूर्ण संख्या
math.ceil(x)  ->  वरची पूर्ण संख्या

math.radians(d) -> degree ला radian मध्ये
   कारण sin/cos/tan radian मध्ये काम करतात!

math.gcd(a,b) -> महत्तम सामान्य विभाजक
"""
