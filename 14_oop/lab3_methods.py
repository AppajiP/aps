"""
लॅब ३ — Methods
=================
"""

class Vidyarthi:
    shala = "ज्ञानदीप विद्यालय"

    def __init__(self, naav, guna):
        self.naav = naav
        self.guna = guna

    def parichay(self):
        print(f"नमस्कार, मी {self.naav} ({Vidyarthi.shala})")

    def sarasari(self):
        return sum(self.guna) / len(self.guna)

    def shreni(self):
        avg = self.sarasari()
        if avg >= 75:
            return "A"
        elif avg >= 60:
            return "B"
        elif avg >= 35:
            return "C"
        return "नापास"

    def __str__(self):
        return f"<Vidyarthi: {self.naav}, सरासरी: {self.sarasari():.2f}>"


v = Vidyarthi("अर्जुन", [85, 92, 78, 90, 88])
v.parichay()
print(f"सरासरी: {v.sarasari():.2f}")
print(f"श्रेणी: {v.shreni()}")
print(v)


"""
========================================================
स्पष्टीकरण:
========================================================

methods:
   class च्या आत define केलेले functions.
   पहिला parameter self असतो.

class attribute:
   shala = "..." (init च्या बाहेर)
   सर्व objects साठी common.
   Vidyarthi.shala असे access करता येते.

instance attribute:
   self.naav, self.guna (init च्या आत)
   प्रत्येक object साठी वेगळे.

self आत्ली method दुसरीला कॉल करते:
   self.sarasari()  ->  त्याच object ची method

__str__:
   - dunder method ('special' method).
   - print(object) केल्यावर हे चालते.
   - object ला string मध्ये बदलते.

dunder methods:
   __init__   ->  constructor
   __str__    ->  print साठी
   __len__    ->  len() साठी
   __eq__     ->  == साठी
   ... आणि बरेच
"""
