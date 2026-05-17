"""
लॅब २ — __init__ आणि self
==========================
"""

class Vidyarthi:
    def __init__(self, naav, vay, varg):
        self.naav = naav
        self.vay = vay
        self.varg = varg
        print(f"नवीन विद्यार्थी तयार: {self.naav}")


v1 = Vidyarthi("राम", 15, "१०वी")
v2 = Vidyarthi("सीता", 14, "९वी")

print(f"\nv1.naav = {v1.naav}")
print(f"v1.vay  = {v1.vay}")
print(f"v1.varg = {v1.varg}")

print(f"\nv2.naav = {v2.naav}")
print(f"v2.varg = {v2.varg}")

v1.vay = 16
print(f"\nबदलल्यानंतर v1.vay = {v1.vay}")
print(f"v2.vay अबाधित = {v2.vay}")


"""
========================================================
स्पष्टीकरण:
========================================================

__init__(self, ...):
   - 'dunder init' म्हणतात (double underscore).
   - object तयार झाल्यावर आपोआप चालतो.
   - म्हणून याला 'constructor' म्हणतात.

self:
   - method चा पहिला parameter.
   - object स्वतःला निर्देशित करते.
   - कॉल करताना देत नाही — आपोआप जाते.

   Vidyarthi("राम", 15, "१०वी")
   -> __init__(self, "राम", 15, "१०वी")
      (self = नवीन object)

self.naav = naav:
   - self.naav -> object चा attribute (कायमचा साठतो)
   - naav     -> __init__ चा parameter (तात्पुरता)

प्रत्येक object चे स्वतःचे attributes:
   v1 बदलला तरी v2 अबाधित.
"""
