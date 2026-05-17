"""
लॅब २ — Set
=============
"""

phale = {"आंबा", "केळी", "सफरचंद", "आंबा"}
print("Set:", phale)
print("एकूण:", len(phale))

phale.add("पेरू")
print("add नंतर:", phale)

phale.discard("केळी")
print("discard नंतर:", phale)

ganit_avadte = {"राम", "सीता", "गणेश"}
vidnyan_avadte = {"सीता", "लक्ष्मण", "गणेश"}

print("\n--- सेट क्रिया ---")
print("दोन्हीपैकी कुणाला तरी (union):", ganit_avadte | vidnyan_avadte)
print("दोन्ही (intersection):", ganit_avadte & vidnyan_avadte)
print("फक्त गणित (difference):", ganit_avadte - vidnyan_avadte)
print("फक्त एकाला (symmetric):", ganit_avadte ^ vidnyan_avadte)


"""
========================================================
स्पष्टीकरण:
========================================================

{ }        ->  set तयार करायला.
              पण रिकामा { } हा dictionary होतो!
              रिकामा set: set()

Duplicates आपोआप काढले जातात:
   {"आंबा", "केळी", "आंबा"} -> {"आंबा", "केळी"}

क्रम नसतो:
   प्रत्येक वेळी छापला तर क्रम वेगळा असू शकतो.

Set क्रिया (sets ची गणितीय कामे):

   | किंवा union()         ->  दोन्ही set मिळून (∪)
   & किंवा intersection() ->  common वस्तू (∩)
   - किंवा difference()   ->  पहिल्यात आहे पण दुसऱ्यात नाही
   ^ किंवा symmetric_difference() -> एकातच आहेत त्या

उपयोग:
   - duplicate काढायला
   - common शोधायला
   - membership test (खूप वेगवान)
"""
