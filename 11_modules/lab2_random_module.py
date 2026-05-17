"""
लॅब २ — random module
=======================
"""

import random

print("random():", random.random())

print("randint(1, 100):", random.randint(1, 100))

phale = ["आंबा", "केळी", "सफरचंद", "द्राक्ष", "पेरू"]
print("\nchoice:", random.choice(phale))

print("\n--- फासा ५ वेळा ---")
for i in range(5):
    print(f"फेक {i+1}: {random.randint(1, 6)}")

patte = list(range(1, 11))
print("\nआधी:", patte)
random.shuffle(patte)
print("फेरबदल नंतर:", patte)

vidyarthi = ["राम", "सीता", "लक्ष्मण", "गणेश", "मीरा", "अर्जुन"]
nivd = random.sample(vidyarthi, 3)
print("\n३ निवडलेले:", nivd)

random.seed(42)
print("\nseed नंतर random:", random.random())


"""
========================================================
स्पष्टीकरण:
========================================================

random.random()        ->  0.0 ते 1.0 (1.0 नाही) मधली float
random.randint(a, b)   ->  a ते b मधली integer (दोन्ही समावेश)
random.choice(seq)     ->  क्रमामधून एक

random.shuffle(list)   ->  list ला फेरबदल करते (बदलते)
                          नवीन परत देत नाही!

random.sample(seq, n)  ->  n वेगवेगळ्या वस्तू निवडते
                          original बदलत नाही

random.seed(x)         ->  खर्‍या random ला 'fix' करते
                          एकाच seed ने एकच निकाल
                          - testing साठी उपयोगी
"""
