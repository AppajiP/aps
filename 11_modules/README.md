# प्रकरण ११ — मॉड्यूल्स व लायब्ररी (Modules & Libraries)

## 🎯 शिकण्याची उद्दिष्टे

- मॉड्यूल म्हणजे काय?
- `import` कसे करायचे?
- महत्त्वाचे built-in modules: `math`, `random`, `datetime`, `os`
- स्वतःचे module बनवणे
- `pip` द्वारे बाहेरचे packages install करणे

---

## १. Module म्हणजे काय?

**Module** म्हणजे **पायथन कोडची एक फाइल** ज्यात उपयोगी फंक्शन्स आणि चल असतात. आपण ती **import** करून तिचा वापर करू शकतो.

> उदा. `math` module मध्ये गणितीय फंक्शन्स आहेत — `sqrt`, `pi`, इ.

---

## २. `import` चे प्रकार

### अ. संपूर्ण module

```python
import math
print(math.pi)
print(math.sqrt(25))
```

### आ. विशिष्ट गोष्ट

```python
from math import pi, sqrt
print(pi)
print(sqrt(25))
```

### इ. नवीन नाव देऊन (alias)

```python
import math as m
print(m.pi)

from numpy import array as arr
```

### ई. सर्व काही (शिफारस नाही)

```python
from math import *
```

---

## ३. महत्त्वाचे Built-in Modules

### `math` — गणित

| | अर्थ |
|---|---|
| `math.pi` | π = 3.14159... |
| `math.e` | e = 2.71828... |
| `math.sqrt(x)` | √x |
| `math.pow(a, b)` | a^b |
| `math.factorial(n)` | n! |
| `math.floor(x)` | खालचे |
| `math.ceil(x)` | वरचे |
| `math.gcd(a, b)` | म.सा.वि. |

### `random` — यादृच्छिक (Random)

| | अर्थ |
|---|---|
| `random.random()` | 0.0 ते 1.0 |
| `random.randint(a, b)` | a ते b पैकी एक integer |
| `random.choice(list)` | list मधून एक |
| `random.shuffle(list)` | फेरबदल |
| `random.sample(list, n)` | list मधून n वेगवेगळ्या |

### `datetime` — दिनांक व वेळ

```python
import datetime
aaj = datetime.date.today()
print(aaj)

ata = datetime.datetime.now()
print(ata)
```

### `os` — operating system

```python
import os
print(os.getcwd())          # current directory
print(os.listdir())          # files यादी
```

---

## ४. स्वतःचे Module बनवणे

`maza_module.py` नावाची फाइल बनवा:

```python
def namaskar(naav):
    print(f"नमस्कार, {naav}!")

PI = 3.14159
```

मग दुसरीकडे:

```python
import maza_module
maza_module.namaskar("राम")
print(maza_module.PI)
```

---

## ५. `pip` — Package Manager

बाहेरचे लायब्ररी install करायला `pip` वापरतात.

```bash
pip install numpy
pip install pandas
pip install requests
```

---

## 🧪 हँड्स-ऑन लॅब्स

| फाइल | विषय |
|---|---|
| `lab1_math_module.py` | `math` module |
| `lab2_random_module.py` | `random` module |
| `lab3_datetime_module.py` | `datetime` module |
| `lab4_custom_module.py` | + `maza_module.py` स्वतःचे module |

---

## 📝 शब्दकोश

| शब्द | अर्थ |
|---|---|
| **Module** | `.py` फाइल |
| **Package** | अनेक modules एकत्र |
| **Library** | वापरण्यायोग्य कोडचा संग्रह |
| **import** | module आणण्याचा keyword |
| **as** | alias देणारा keyword |
| **pip** | Python चे package manager |

---

## ✅ स्वाध्याय

1. `random` वापरून ५ ते ५० मधील ५ random संख्या छापा.
2. `math` वापरून त्रिकोणाचे क्षेत्रफळ (हेरॉनचे सूत्र) काढा.
3. `datetime` वापरून तुमचे जन्मवर्ष द्या आणि वय छापा.
4. एक स्वतःचे `ganit.py` module बनवा ज्यात `berij`, `vajabaki` फंक्शन्स आहेत. ते दुसर्‍या फाइलमध्ये वापरा.

➡️ **पुढील प्रकरण:** [`12_file_handling`](../12_file_handling/)
