"""
लॅब ४ — Dictionary methods
============================
"""

guna = {
    "मराठी": 85,
    "हिंदी": 78,
    "इंग्रजी": 92,
    "गणित": 95,
    "विज्ञान": 88
}

print("सर्व keys:", guna.keys())
print("सर्व values:", guna.values())
print("सर्व items:", guna.items())

print("\n--- loop ---")
for vishay, marks in guna.items():
    print(f"{vishay:10} -> {marks}")

ekun = sum(guna.values())
sarasari = ekun / len(guna)
print(f"\nएकूण: {ekun}, सरासरी: {sarasari:.2f}")

ekun_guna = guna.pop("गणित")
print(f"\nगणित (काढलेले): {ekun_guna}")
print("उरलेले:", guna)


guna.update({"समाजशास्त्र": 80, "हिंदी": 82})
print("\nupdate नंतर:", guna)


"""
========================================================
स्पष्टीकरण:
========================================================

.keys()      ->  सर्व key
.values()    ->  सर्व किंमती
.items()     ->  (key, value) जोड्या

.pop(key)    ->  जोडी काढून value देतो.
.update(d2)  ->  d2 मधले key-value जोडतो/बदलतो.

.clear()     ->  सर्व काढून रिकामा करतो.
.copy()      ->  प्रत बनवतो.

dictionary loop:
   for k in d:              # फक्त keys वर
   for v in d.values():     # फक्त values
   for k, v in d.items():   # दोन्ही - सर्वात उपयोगी
"""
