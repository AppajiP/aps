"""
लॅब ६ — Patterns (* चे आकार)
=============================
"""

print("Pattern 1: चौकोनी त्रिकोण")
for i in range(1, 6):
    print("* " * i)

print("\nPattern 2: उलटा त्रिकोण")
for i in range(5, 0, -1):
    print("* " * i)

print("\nPattern 3: मध्यवर्ती त्रिकोण")
for i in range(1, 6):
    print("  " * (5 - i) + "* " * i)

print("\nPattern 4: संख्यांचा त्रिकोण")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


"""
========================================================
स्पष्टीकरण:
========================================================

"* " * i     ->  string ला i वेळा repeat करते.
                 i = 3 असेल -> "* * * "

print()      ->  रिकामा print -> नवीन ओळ देतो.

end=" "      ->  print नंतर newline ऐवजी space.

मध्यवर्ती त्रिकोणासाठी:
   आधी काही space (कमी होत जाणारे)
   मग * (वाढत जाणारे)
"""
