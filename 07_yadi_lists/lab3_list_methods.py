"""
लॅब ३ — List methods
======================
"""

phale = ["आंबा", "केळी"]
print("सुरुवात:", phale)

phale.append("सफरचंद")
print("append नंतर:", phale)

phale.insert(1, "पेरू")
print("insert(1) नंतर:", phale)

phale.remove("केळी")
print("remove नंतर:", phale)

shevatche = phale.pop()
print("pop केलेले:", shevatche)
print("उरलेले:", phale)

phale.extend(["पपई", "द्राक्ष"])
print("extend नंतर:", phale)

phale.sort()
print("sort नंतर:", phale)

phale.reverse()
print("reverse नंतर:", phale)

print("\n--- शोध ---")
print("index 'पपई' =", phale.index("पपई"))
print("count 'पपई' =", phale.count("पपई"))

print("\n--- copy ---")
nakal = phale.copy()
print("नक्कल:", nakal)


"""
========================================================
स्पष्टीकरण:
========================================================

append(x)    ->  शेवटी x जोडते.
insert(i,x)  ->  index i ठिकाणी x घालते.
remove(x)    ->  पहिल्या x ला काढते.
pop(i)       ->  index i ची वस्तू काढून परत देते.
                 (i न दिल्यास शेवटची)
extend(L)    ->  L मधल्या सर्व वस्तू एक-एक करून जोडते.
sort()       ->  क्रमवारी (अकारादी) लावते.
reverse()    ->  उलट करते.
index(x)     ->  x चा पहिला index देते.
count(x)     ->  x किती वेळा आहे ते मोजते.
copy()       ->  list ची प्रत बनवते.

लक्षात ठेवा:
   - sort() व reverse() list ला 'बदलतात'.
   - नवीन list परत देत नाहीत.
"""
