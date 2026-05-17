"""
लॅब ४ — Inheritance (वारसा)
=============================
"""

class Vyakti:
    def __init__(self, naav, vay):
        self.naav = naav
        self.vay = vay

    def parichay(self):
        print(f"मी {self.naav}, वय {self.vay}")


class Vidyarthi(Vyakti):
    def __init__(self, naav, vay, varg):
        super().__init__(naav, vay)
        self.varg = varg

    def abhyas(self):
        print(f"{self.naav} {self.varg} चा अभ्यास करत आहे")


class Shikshak(Vyakti):
    def __init__(self, naav, vay, vishay):
        super().__init__(naav, vay)
        self.vishay = vishay

    def shikvane(self):
        print(f"{self.naav} {self.vishay} शिकवत आहेत")

    def parichay(self):
        super().parichay()
        print(f"मी {self.vishay} शिकवतो")


v = Vidyarthi("राम", 15, "१०वी")
v.parichay()
v.abhyas()

print()
s = Shikshak("कुमार सर", 35, "गणित")
s.parichay()
s.shikvane()


"""
========================================================
स्पष्टीकरण:
========================================================

class Child(Parent):
   - Child ने Parent चे attributes व methods वारसा घेतले.
   - parent ला सहसा 'base class' किंवा 'superclass' म्हणतात.

super().__init__(...):
   - parent चे __init__ कॉल करते.
   - "तो पहिले त्याचे काम करू दे, मग माझे".

method override:
   - Shikshak ने parichay पुन्हा define केली.
   - म्हणजे parent ची ओव्हरराइड (replace).
   - पण super().parichay() ने जुन्या ची आठवण देखील वापरली.

inheritance चे फायदे:
   १. कोडची पुनरावृत्ती टळते (DRY).
   २. एकाच rooted structure ने मोठे प्रोग्राम.
   ३. polymorphism (पुढची लॅब).

isinstance:
   isinstance(v, Vidyarthi)  ->  True
   isinstance(v, Vyakti)     ->  True (Vidyarthi हा Vyakti आहे)
"""
