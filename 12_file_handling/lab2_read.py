"""
लॅब २ — फाइल वाचणे
====================
हे चालवण्यापूर्वी lab1_write.py चालवा.
"""

f = open("namaste.txt", "r", encoding="utf-8")
sarv = f.read()
f.close()
print("--- संपूर्ण ---")
print(sarv)

f = open("namaste.txt", "r", encoding="utf-8")
pahili = f.readline()
dusari = f.readline()
f.close()
print("--- एक-एक ओळ ---")
print("पहिली:", pahili.strip())
print("दुसरी:", dusari.strip())

f = open("phale.txt", "r", encoding="utf-8")
oli = f.readlines()
f.close()
print("--- list स्वरूपात ---")
print(oli)

print("\n--- लूप ---")
f = open("phale.txt", "r", encoding="utf-8")
for o in f:
    print(">>", o.strip())
f.close()


"""
========================================================
स्पष्टीकरण:
========================================================

mode "r":
   - फाइल वाचण्यासाठी
   - फाइल अस्तित्वात नसेल तर FileNotFoundError

f.read():
   - संपूर्ण फाइल एका string मध्ये.

f.readline():
   - फक्त एक ओळ वाचते (\n सकट).
   - पुढच्या call ला पुढची ओळ.

f.readlines():
   - सर्व ओळी list मध्ये परत.
   - प्रत्येकाच्या शेवटी \n असतो.

for o in f:
   - फाइल थेट loopable.
   - मोठ्या फाइल्ससाठी सर्वोत्तम (memory कमी).

.strip():
   - शेवटचा \n व आजूबाजूचे spaces काढते.
"""
