"""
लॅब ७ — संपूर्ण उदाहरण: BankAccount
=====================================
"""

class Khata:
    bank_naav = "महाराष्ट्र बँक"
    pudhcha_kramank = 1001

    def __init__(self, dharak, prarambh=0):
        self.dharak = dharak
        self.__shillak = prarambh
        self.khata_kramank = Khata.pudhcha_kramank
        Khata.pudhcha_kramank += 1
        self.itihaas = []
        self.__nond(f"खाते उघडले - प्रारंभिक ₹{prarambh}")

    def __nond(self, sandesh):
        self.itihaas.append(sandesh)

    def jama(self, paise):
        if paise <= 0:
            raise ValueError("रक्कम ऋण/शून्य नाही")
        self.__shillak += paise
        self.__nond(f"जमा ₹{paise}, शिल्लक ₹{self.__shillak}")

    def kadhne(self, paise):
        if paise <= 0:
            raise ValueError("रक्कम ऋण/शून्य नाही")
        if paise > self.__shillak:
            raise ValueError("अपुरी शिल्लक")
        self.__shillak -= paise
        self.__nond(f"काढले ₹{paise}, शिल्लक ₹{self.__shillak}")

    @property
    def shillak(self):
        return self.__shillak

    def itihaas_dakhva(self):
        print(f"\n--- {self.dharak} ({self.khata_kramank}) ---")
        for n in self.itihaas:
            print(" *", n)

    def __str__(self):
        return f"Khata({self.dharak}, ₹{self.__shillak})"


class BachatKhata(Khata):
    vyaj_dar = 0.04

    def vyaj_jodne(self):
        vyaj = self.shillak * BachatKhata.vyaj_dar
        self.jama(vyaj)
        return vyaj


print(f"बँक: {Khata.bank_naav}\n")

k1 = Khata("रामचंद्र", 5000)
k2 = BachatKhata("सीताबाई", 10000)

k1.jama(2000)
k1.kadhne(1500)
k2.jama(5000)
v = k2.vyaj_jodne()
print(f"\nसीताबाईंना मिळालेले व्याज: ₹{v}")

k1.itihaas_dakhva()
k2.itihaas_dakhva()

print(f"\n{k1}")
print(f"{k2}")

try:
    k1.kadhne(100000)
except ValueError as e:
    print(f"\nचूक: {e}")


"""
========================================================
स्पष्टीकरण:
========================================================

या लॅबमध्ये एकत्र आहेत:
   १. Class व object
   २. Constructor (__init__)
   3. Instance attributes (self.dharak, self.__shillak)
   ४. Class attributes (bank_naav, pudhcha_kramank)
   ५. Private method (__nond)
   ६. Public methods (jama, kadhne)
   ७. @property — method ला attribute सारखे access
   ८. __str__ — print साठी
   ९. Inheritance (BachatKhata extends Khata)
   १०. Exception (raise ValueError)

@property:
   def shillak(self): ...
   k1.shillak()  ऐवजी  k1.shillak  (कंस न लागता)

   म्हणजे method पण attribute सारखी दिसते.

class attribute pudhcha_kramank:
   प्रत्येक नवीन खात्याला unique number देण्यासाठी.
   सर्व objects ला एकच (shared).
"""
