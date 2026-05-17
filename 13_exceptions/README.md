# प्रकरण १३ — एरर / अपवाद हाताळणी (Exception Handling)

## 🎯 शिकण्याची उद्दिष्टे

- Error आणि Exception म्हणजे काय?
- सामान्य exceptions
- `try-except` ब्लॉक
- `else` व `finally`
- अनेक exceptions
- `raise` — स्वतःचा error टाकणे
- स्वतःचे exceptions

---

## १. Error/Exception म्हणजे काय?

प्रोग्राम चालू असताना **अचानक झालेली चूक** = **error / exception**. जर हाताळली नाही तर **प्रोग्राम बंद** पडतो.

### सामान्य Exceptions

| नाव | केव्हा? |
|---|---|
| `SyntaxError` | चुकीचा कोड लिहिला |
| `ValueError` | चुकीचा प्रकार बदल (`int("abc")`) |
| `TypeError` | चुकीच्या प्रकारावर क्रिया (`"a" + 5`) |
| `NameError` | नसलेले चल वापरले |
| `ZeroDivisionError` | शून्याने भाग |
| `IndexError` | list बाहेरचा index |
| `KeyError` | dict मध्ये नसलेली key |
| `FileNotFoundError` | फाइल नाही |
| `AttributeError` | object ला नसलेले attribute |
| `ImportError` | module न मिळणे |

---

## २. `try-except`

### सिंटॅक्स

```python
try:
    # जो कोड error देईल
except ExceptionName:
    # error आला तर काय करायचे
```

### उदाहरण

```python
try:
    a = int(input("संख्या: "))
    print(10 / a)
except ZeroDivisionError:
    print("शून्याने भाग शक्य नाही")
except ValueError:
    print("कृपया योग्य संख्या टाइप करा")
```

---

## ३. `try-except-else-finally`

```python
try:
    कोड
except SomeError:
    error आला तर
else:
    error आला नाही तर
finally:
    नेहमी (error आला किंवा नाही)
```

### उदाहरण

```python
try:
    f = open("data.txt", "r")
    data = f.read()
except FileNotFoundError:
    print("फाइल नाही")
else:
    print(data)
finally:
    print("कार्य पूर्ण")
```

- `else` → error न आला तर
- `finally` → नेहमी (cleanup, close)

---

## ४. एकाच ठिकाणी अनेक exceptions

```python
try:
    ...
except (ValueError, TypeError):
    print("एकतर value किंवा type चूक")
```

### सर्व errors पकडणे

```python
try:
    ...
except Exception as e:
    print("error:", e)
```

⚠️ `except Exception:` फक्त शेवटचा उपाय — सहसा specific exception वापरा.

---

## ५. `raise` — स्वतःचा error टाकणे

```python
vay = -5
if vay < 0:
    raise ValueError("वय ऋण असू शकत नाही")
```

---

## ६. स्वतःचे Exception

```python
class WrongAgeError(Exception):
    pass

if vay > 200:
    raise WrongAgeError("वय खूप जास्त")
```

---

## 🧪 हँड्स-ऑन लॅब्स

| फाइल | विषय |
|---|---|
| `lab1_basic.py` | try-except मूळ |
| `lab2_multiple.py` | अनेक exceptions |
| `lab3_else_finally.py` | else, finally |
| `lab4_raise.py` | raise |
| `lab5_custom_exception.py` | स्वतःचा exception |

---

## 📝 शब्दकोश

| शब्द | अर्थ |
|---|---|
| **Exception** | प्रोग्राम चालताना झालेली चूक |
| **try** | धोक्याचा कोड |
| **except** | error पकडणारा block |
| **raise** | error स्वतःहून टाकणे |
| **else** | error न आल्यास |
| **finally** | नेहमी चालणारा block |
| **traceback** | error कुठे झाला त्याचा मार्ग |

---

## ✅ स्वाध्याय

1. वापरकर्त्याकडून संख्या घेऊन तिचा भागाकार करा. ValueError व ZeroDivisionError हाताळा.
2. एक फाइल वाचा. नसल्यास "फाइल नाही" छापा.
3. वय -1 ते 150 च्या मधेच असावे अशी तपासणी `raise` ने करा.
4. एक `MarksOutOfRangeError` स्वतःचा exception बनवा.

➡️ **पुढील प्रकरण:** [`14_oop`](../14_oop/)
