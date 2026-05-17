# प्रकरण १४ — क्लासेस व ऑब्जेक्ट (OOP)

## 🎯 शिकण्याची उद्दिष्टे

- Class व Object म्हणजे काय?
- Class तयार करणे
- `__init__` constructor
- `self` keyword
- Attributes व Methods
- Inheritance (वारसा)
- Encapsulation, Polymorphism
- Class vs Instance attributes

---

## १. OOP म्हणजे काय?

**OOP = Object-Oriented Programming**. वास्तविक जगातील गोष्टींना (object) प्रोग्राममध्ये दर्शविण्याची पद्धत.

### सामान्य भाषेत:

| जगातील | प्रोग्राममध्ये |
|---|---|
| "विद्यार्थी" ही संकल्पना | **Class** (साचा / template) |
| रामू नावाचा विशिष्ट विद्यार्थी | **Object** (instance) |
| त्याचे नाव, वय | **Attributes** (गुणधर्म) |
| तो अभ्यास करतो, खेळतो | **Methods** (कृती) |

---

## २. Class तयार करणे

### सिंटॅक्स

```python
class ClassName:
    def __init__(self, parameters):
        self.attribute = value
    
    def method_name(self):
        ...
```

### उदाहरण

```python
class Vidyarthi:
    def __init__(self, naav, vay, varg):
        self.naav = naav
        self.vay = vay
        self.varg = varg
    
    def parichay(self):
        print(f"मी {self.naav}, वय {self.vay}, वर्ग {self.varg}")

v1 = Vidyarthi("राम", 15, "१०वी")
v2 = Vidyarthi("सीता", 14, "९वी")

v1.parichay()
v2.parichay()
```

---

## ३. `__init__` व `self`

- `__init__` हा **constructor** — object तयार झाल्यावर **आपोआप** चालतो.
- `self` म्हणजे **"हाच object"** — कोणत्या object वर काम होतंय ते.

```python
class Demo:
    def __init__(self):
        print("नवीन object तयार!")

d = Demo()    # "नवीन object तयार!" छापते
```

`self` नेहमी method चा **पहिला parameter** असतो (कॉल करताना देत नाही).

---

## ४. Inheritance (वारसा)

एका class ने दुसर्‍याचे गुणधर्म **वारसा** मिळवणे.

```python
class Vyakti:
    def __init__(self, naav):
        self.naav = naav
    
    def parichay(self):
        print(f"मी {self.naav}")


class Vidyarthi(Vyakti):              # Vyakti चे वारस
    def __init__(self, naav, varg):
        super().__init__(naav)        # parent चे __init__
        self.varg = varg
    
    def abhyas(self):
        print(f"{self.naav} अभ्यास करत आहे")


v = Vidyarthi("राम", "१०वी")
v.parichay()    # parent कडून मिळाले
v.abhyas()      # स्वतःचे
```

---

## ५. Encapsulation (गोपनीयता)

private attribute — सुरुवातीला `_` किंवा `__`.

```python
class Bank:
    def __init__(self, naav, paise):
        self.naav = naav
        self.__paise = paise        # private
    
    def jamavat(self):
        return self.__paise
```

---

## ६. Polymorphism

एकाच नावाची method, वेगवेगळ्या class मध्ये वेगळी:

```python
class Kutra:
    def avaz(self):
        return "भू भू"

class Manjar:
    def avaz(self):
        return "म्याव"

for p in [Kutra(), Manjar()]:
    print(p.avaz())
```

---

## ७. Class vs Instance Attributes

```python
class Vidyarthi:
    shala = "ज्ञानदीप विद्यालय"      # class attribute (सर्वांसाठी common)
    
    def __init__(self, naav):
        self.naav = naav             # instance attribute (प्रत्येकाचे वेगळे)
```

---

## 🧪 हँड्स-ऑन लॅब्स

| फाइल | विषय |
|---|---|
| `lab1_basic_class.py` | class ची मूळ रचना |
| `lab2_init_self.py` | `__init__` व `self` |
| `lab3_methods.py` | methods |
| `lab4_inheritance.py` | inheritance |
| `lab5_encapsulation.py` | encapsulation |
| `lab6_polymorphism.py` | polymorphism |
| `lab7_bank_account.py` | संपूर्ण उदाहरण |

---

## 📝 शब्दकोश

| शब्द | अर्थ |
|---|---|
| **Class** | object चा साचा |
| **Object / Instance** | class पासून बनलेली विशिष्ट गोष्ट |
| **Attribute** | object चा गुणधर्म |
| **Method** | object ची क्रिया |
| **`__init__`** | constructor — object तयार होताना |
| **`self`** | हाच object |
| **Inheritance** | वारसा |
| **Parent / Child class** | वडील-मुलगा वर्ग |
| **`super()`** | parent कडे जा |
| **Encapsulation** | गोपनीयता |
| **Polymorphism** | अनेक रूपे |
| **Private** | `__naav` किंवा `_naav` |

---

## ✅ स्वाध्याय

1. `Pustak` class बनवा (नाव, लेखक, किंमत) आणि माहिती छापायचे method.
2. `Vahan` class आणि त्यापासून `Car`, `Bike` child classes बनवा.
3. `BankAccount` class — पैसे जमा (deposit), काढणे (withdraw), शिल्लक (balance).
4. `Aakar` (shape) class आणि त्यापासून `Vartul`, `Chaukon`, `Tribhuj` — प्रत्येकाची `area()` method.

➡️ **पुढील भाग:** [`../projects/`](../projects/)
