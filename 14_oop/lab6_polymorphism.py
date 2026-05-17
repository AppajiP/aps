"""
लॅब ६ — Polymorphism
======================
"""

class Aakar:
    def area(self):
        return 0

    def parichay(self):
        print(f"मी एक आकार आहे. क्षेत्रफळ: {self.area()}")


class Vartul(Aakar):
    def __init__(self, trijya):
        self.trijya = trijya

    def area(self):
        return 3.14 * self.trijya ** 2


class Chaukon(Aakar):
    def __init__(self, baju):
        self.baju = baju

    def area(self):
        return self.baju ** 2


class Aayat(Aakar):
    def __init__(self, lambai, rundi):
        self.lambai = lambai
        self.rundi = rundi

    def area(self):
        return self.lambai * self.rundi


aakar_yadi = [Vartul(5), Chaukon(4), Aayat(6, 3)]

for a in aakar_yadi:
    a.parichay()


class Kutra:
    def avaz(self):
        return "भू भू"

class Manjar:
    def avaz(self):
        return "म्याव"

class Gay:
    def avaz(self):
        return "हंबा"

print("\n--- प्राण्यांचे आवाज ---")
for prani in [Kutra(), Manjar(), Gay()]:
    print(f"{type(prani).__name__}: {prani.avaz()}")


"""
========================================================
स्पष्टीकरण:
========================================================

Polymorphism = "अनेक रूपे"

समजुती:
   एकाच नावाची method, वेगवेगळ्या class मध्ये वेगळी.
   कॉल करताना class वेगळी जरी, method चालते.

उदा:
   प्रत्येक प्राण्याची 'avaz' method —
   पण प्रत्येकाचा आवाज वेगळा.

म्हणून:
   for प्राणी in यादी:
       प्राणी.avaz()

   पायथनला आधी कळते का प्राणी कोण?
   चालवताना ठरवते — हे dynamic polymorphism.

duck typing:
   "बदकासारखे चालले व बदकासारखे ओरडले तर बदक!"
   पायथनला specific class माहित नसले तरी
   method असेल तर चालते.
"""
