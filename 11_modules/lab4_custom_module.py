"""
लॅब ४ — स्वतःचे module वापरणे
================================
हे चालवण्यासाठी maza_module.py त्याच फोल्डरमध्ये असावे.
"""

import maza_module

print("बेरीज:", maza_module.berij(10, 5))
print("वजाबाकी:", maza_module.vajabaki(10, 5))
print("PI:", maza_module.PI)

from maza_module import varg, varta_kshetraphal

print("\n5 चा वर्ग:", varg(5))
print("त्रिज्या 7 चे क्षेत्रफळ:", varta_kshetraphal(7))

import maza_module as mm
print("\nas वापरून gunakar:", mm.gunakar(6, 7))


"""
========================================================
स्पष्टीकरण:
========================================================

स्वतःचे module बनवायला:
   १. एक .py फाइल बनवा (उदा. maza_module.py)
   २. त्यात function/चल लिहा
   ३. दुसर्‍या फाइलमधून import करा

import पद्धती:
   १. import maza_module
      -> सर्व काही, पण माझे.berij() असे वापरा

   २. from maza_module import berij, varg
      -> थेट berij() व varg() वापरा

   ३. from maza_module import *
      -> सर्व काही थेट (टाळा)

   ४. import maza_module as mm
      -> छोटे नाव

लक्षात ठेवा:
   दोन्ही फाइल्स एकाच फोल्डरमध्ये असाव्यात.
"""
