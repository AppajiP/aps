# प्रकरण ०८ — Tuple, Set, Dictionary

## 🎯 शिकण्याची उद्दिष्टे

- **Tuple (ट्यूपल)** — न बदलणारी यादी
- **Set (सेट)** — एकमेव वस्तूंचा संच
- **Dictionary (शब्दकोश)** — key-value जोड्या

---

## १. Tuple (ट्यूपल)

**Tuple** हा list सारखाच आहे, पण **बदलता येत नाही (immutable)**.

### सिंटॅक्स

```python
t = (1, 2, 3)
t = "राम", "सीता"
ek = (5,)   # एका वस्तूचा tuple — , आवश्यक!
```

### का वापरावा?

- माहिती **बदलू नये** अशी असेल तर (उदा. वार: सोम, मंगळ, ...)
- list पेक्षा वेगवान
- dictionary चे key म्हणून वापरता येते

### कोणत्या क्रिया चालतात?

```python
t = (10, 20, 30, 40)
print(t[0])       # 10
print(t[1:3])     # (20, 30)
print(len(t))     # 4
print(t.count(20))
print(t.index(30))
```

❌ `t[0] = 5` — ERROR! बदलता येत नाही.

---

## २. Set (सेट)

**Set** = **एकमेव वस्तूंचा संच**. क्रम नसतो, repeated वस्तू नसतात.

### सिंटॅक्स

```python
s = {1, 2, 3, 4}
s = {"राम", "सीता", "राम"}  # राम एकदाच राहील
rikama_set = set()          # रिकामा set — { } नाही!
```

### Set methods

| Method | काम |
|---|---|
| `add(x)` | x जोडा |
| `remove(x)` | x काढा (नसेल तर error) |
| `discard(x)` | x काढा (नसले तरी error नाही) |
| `union(s2)` | संघटन (∪) |
| `intersection(s2)` | छेद (∩) |
| `difference(s2)` | फरक |
| `len(s)` | किती वस्तू |

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)   # union: {1, 2, 3, 4, 5, 6}
print(a & b)   # intersection: {3, 4}
print(a - b)   # difference: {1, 2}
```

---

## ३. Dictionary (शब्दकोश)

**Dictionary** = **key-value जोड्या**. प्रत्येक key ला एक value असते.

### सिंटॅक्स

```python
vidyarthi = {
    "naav": "अर्जुन",
    "vay": 15,
    "varg": "१०वी"
}
```

### वापर

```python
print(vidyarthi["naav"])           # अर्जुन
print(vidyarthi.get("vay"))        # 15
print(vidyarthi.get("phone", "नाही"))  # default

vidyarthi["gaav"] = "पुणे"        # नवीन key जोडली
vidyarthi["vay"] = 16             # बदलली

del vidyarthi["varg"]             # काढून टाकली

print(vidyarthi.keys())
print(vidyarthi.values())
print(vidyarthi.items())
```

### Dictionary वर loop

```python
for key in vidyarthi:
    print(key, "->", vidyarthi[key])

for key, value in vidyarthi.items():
    print(key, "->", value)
```

---

## 🆚 तुलना

| गुण | List | Tuple | Set | Dict |
|---|---|---|---|---|
| कंस | `[ ]` | `( )` | `{ }` | `{ k:v }` |
| क्रम | ✅ | ✅ | ❌ | ✅ (3.7+) |
| बदलता येतो | ✅ | ❌ | ✅ | ✅ |
| Duplicate | ✅ | ✅ | ❌ | keys ❌ |
| Indexing | ✅ | ✅ | ❌ | by key |

---

## 🧪 हँड्स-ऑन लॅब्स

| फाइल | विषय |
|---|---|
| `lab1_tuple.py` | tuple |
| `lab2_set.py` | set व त्याच्या क्रिया |
| `lab3_dict_basic.py` | dictionary ची ओळख |
| `lab4_dict_methods.py` | dictionary methods |
| `lab5_student_record.py` | विद्यार्थ्यांची माहिती |

---

## 📝 शब्दकोश

| शब्द | अर्थ |
|---|---|
| **Tuple** | न बदलणारी क्रमबद्ध यादी |
| **Set** | एकमेव वस्तूंचा अक्रमबद्ध संच |
| **Dictionary** | key-value जोड्यांचा संग्रह |
| **Key** | dictionary मधील नाव |
| **Value** | त्या key ची किंमत |
| **Mutable** | बदलता येते |
| **Immutable** | बदलता येत नाही |
| **Union** | दोन set एकत्र |
| **Intersection** | दोन set मधले common |

---

## ✅ स्वाध्याय

1. आठवड्याचे ७ वार tuple मध्ये साठवून छापा.
2. दोन sets — गणित आवडणारे आणि विज्ञान आवडणारे — मधून दोन्ही आवडणारे शोधा.
3. एका विद्यार्थ्याची माहिती (नाव, वय, गुण) dictionary मध्ये साठवा.
4. एका वाक्यात प्रत्येक अक्षर किती वेळा आले हे dictionary वापरून मोजा.

➡️ **पुढील प्रकरण:** [`09_strings`](../09_strings/)
