"""
लॅब १ — Tuple
==============
"""

vaar = ("सोम", "मंगळ", "बुध", "गुरू", "शुक्र", "शनी", "रवी")
print("वार:", vaar)
print("एकूण:", len(vaar))
print("पहिला:", vaar[0])
print("शेवटचा:", vaar[-1])
print("कामाचे दिवस:", vaar[:5])

ek = (5,)
ek_chukich = (5)
print("\n(5,) चा प्रकार:", type(ek))
print("(5) चा प्रकार:", type(ek_chukich))

print("\n--- unpacking ---")
naav, vay, varg = ("अर्जुन", 15, "१०वी")
print(naav, vay, varg)

print("\n--- count व index ---")
sankhya = (1, 2, 3, 2, 4, 2, 5)
print("2 किती वेळा?", sankhya.count(2))
print("3 चा index:", sankhya.index(3))


"""
========================================================
स्पष्टीकरण:
========================================================

( )        ->  tuple तयार करायला.
,          ->  वस्तू वेगळ्या करायला.

एका वस्तूचा tuple:
   (5,)   ->  tuple
   (5)    ->  फक्त 5 — सामान्य integer
   म्हणून शेवटी comma आवश्यक!

Unpacking:
   एकाच ओळीत tuple मधल्या वस्तू वेगवेगळ्या चलात ठेवणे.
   x, y, z = (1, 2, 3)

बदलू शकत नाही:
   vaar[0] = "नवीन"  ->  TypeError

का? कारण tuple immutable आहे.
"""
