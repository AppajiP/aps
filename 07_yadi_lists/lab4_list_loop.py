"""
लॅब ४ — list वर loop
=======================
"""

vidyarthi = ["राम", "सीता", "लक्ष्मण", "गणेश", "सरस्वती"]

print("--- साधा for लूप ---")
for naav in vidyarthi:
    print(naav)

print("\n--- index सह ---")
for i in range(len(vidyarthi)):
    print(i, ":", vidyarthi[i])

print("\n--- enumerate सह (सर्वात चांगले) ---")
for i, naav in enumerate(vidyarthi, start=1):
    print(f"{i}. {naav}")

print("\n--- गुणांची बेरीज ---")
guna = [85, 92, 78, 65, 90]
ekun = 0
for g in guna:
    ekun += g
print("एकूण गुण:", ekun)
print("सरासरी:", ekun / len(guna))


"""
========================================================
स्पष्टीकरण:
========================================================

साधा for:
   प्रत्येक iteration ला 'naav' ला एक वस्तू मिळते.

range(len(list)):
   index वापरून लूप. जुनी पद्धत.

enumerate(list, start=1):
   एकाच वेळी index व item दोन्ही मिळते.
   start=1 -> क्रमांक १ पासून सुरू.

बेरीज पॅटर्न:
   १. ekun = 0
   २. प्रत्येक वस्तू मध्ये जोडत जा
   ३. शेवटी ekun मध्ये बेरीज तयार
"""
