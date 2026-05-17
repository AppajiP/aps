"""
लॅब ४ — break आणि continue
=============================
"""

print("break उदाहरण: ५ आला की थांबा")
for i in range(1, 10):
    if i == 5:
        break
    print(i)

print("\ncontinue उदाहरण: सम संख्या वगळून छापा")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

print("\nलूपला else:")
for i in range(1, 4):
    print(i)
else:
    print("लूप पूर्ण झाला (break झाला नाही)")

print("\nलूप break झाला तर else चालत नाही:")
for i in range(1, 4):
    if i == 2:
        break
    print(i)
else:
    print("हे छापणार नाही")


"""
========================================================
स्पष्टीकरण:
========================================================

break       ->  लूपमधून तात्काळ बाहेर पडतो.
                उरलेले iteration चालवत नाही.

continue    ->  या वेळचे iteration थांबवतो.
                पुढच्या iteration वर जातो.

लूपचा else:
   लूप break न होता पूर्ण झाला तरच else चालतो.
   जर break झाला -> else चालत नाही.

विषम छापायचा प्रोग्राम:
   जर i % 2 == 0 (म्हणजे सम)
   तर continue (skip)
   नाहीतर print (विषम छापला जाईल)
"""
