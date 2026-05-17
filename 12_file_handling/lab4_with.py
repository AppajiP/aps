"""
लॅब ४ — with विधान (Best Practice)
====================================
"""

with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("टीप १: with वापरा\n")
    f.write("टीप २: आपोआप close होते\n")
    f.write("टीप ३: errors असले तरीही\n")

with open("notes.txt", "r", encoding="utf-8") as f:
    for oli in f:
        print(oli.strip())

print("\n--- ओळी मोजणे ---")
with open("notes.txt", "r", encoding="utf-8") as f:
    count = 0
    for _ in f:
        count += 1
print("एकूण ओळी:", count)


print("\n--- शोध ---")
shabd = "with"
with open("notes.txt", "r", encoding="utf-8") as f:
    for i, oli in enumerate(f, 1):
        if shabd in oli:
            print(f"ओळ {i}: {oli.strip()}")


"""
========================================================
स्पष्टीकरण:
========================================================

with open(...) as f:
   ...

with हे 'context manager' आहे.
   - block संपला की आपोआप f.close() होते.
   - कोडमध्ये error आला तरी close होते.
   - म्हणून सर्वत्र with वापरा!

जुनी पद्धत vs नवीन:
   जुनी:
       f = open(...)
       try:
           ...
       finally:
           f.close()

   नवीन:
       with open(...) as f:
           ...

with खूप सोपे, सुरक्षित, छोटे.
"""
