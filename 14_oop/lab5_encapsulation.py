"""
लॅब ५ — Encapsulation (गोपनीयता)
==================================
"""

class BankKhata:
    def __init__(self, dharak, prarambh):
        self.dharak = dharak
        self.__shillak = prarambh

    def jama(self, paise):
        if paise <= 0:
            print("ऋण/शून्य रक्कम नाही")
            return
        self.__shillak += paise
        print(f"₹{paise} जमा. नवीन शिल्लक: ₹{self.__shillak}")

    def kadhne(self, paise):
        if paise > self.__shillak:
            print("अपुरी शिल्लक")
            return
        self.__shillak -= paise
        print(f"₹{paise} काढले. नवीन शिल्लक: ₹{self.__shillak}")

    def shillak(self):
        return self.__shillak


khata = BankKhata("रामचंद्र", 1000)
print("शिल्लक:", khata.shillak())

khata.jama(500)
khata.kadhne(200)
khata.kadhne(5000)

try:
    print(khata.__shillak)
except AttributeError as e:
    print("\nथेट access नाही:", e)


print("\n(पायथन private name-mangle करते:)")
print("via _BankKhata__shillak:", khata._BankKhata__shillak)


"""
========================================================
स्पष्टीकरण:
========================================================

Encapsulation = "आत बंदिस्त ठेवणे"

प्रकार:
   self.naav     ->  public  (कुणीही access)
   self._naav    ->  protected (परंपरा — आत राहावा)
   self.__naav   ->  private (पायथन name-mangle करते)

का?
   १. महत्त्वाची माहिती सुरक्षित ठेवायला.
   २. method द्वारेच access — validation जोडता येते.
   ३. बदल करायला सोपे.

उदा:
   thेट self.shillak = -1000 केले तर वाईट.
   पण method मध्ये "ऋण नाही" तपासू शकतो.

Name Mangling:
   __shillak  ->  _ClassName__shillak असे होते.
   म्हणून थेट access कठीण.
"""
