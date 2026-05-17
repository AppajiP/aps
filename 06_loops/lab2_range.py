"""
लॅब २ — range() चे प्रकार
==========================
"""

print("range(5):")
for i in range(5):
    print(i, end=" ")
print()

print("\nrange(1, 6):")
for i in range(1, 6):
    print(i, end=" ")
print()

print("\nrange(1, 11, 2):  (विषम)")
for i in range(1, 11, 2):
    print(i, end=" ")
print()

print("\nrange(2, 21, 2):  (सम)")
for i in range(2, 21, 2):
    print(i, end=" ")
print()

print("\nrange(10, 0, -1):  (उलट)")
for i in range(10, 0, -1):
    print(i, end=" ")
print()


"""
========================================================
स्पष्टीकरण:
========================================================

range(stop)               ->  0 पासून stop-1 पर्यंत
range(start, stop)        ->  start पासून stop-1 पर्यंत
range(start, stop, step)  ->  step ने वाढत/कमी होत

लक्षात ठेवा:
   stop चा समावेश नसतो!
   range(1, 6) -> 1, 2, 3, 4, 5 (6 नाही)

step = -1 म्हणजे उलट क्रमाने जा.
"""
