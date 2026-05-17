# प्रकरण ०७ — यादी (Lists)

## 🎯 शिकण्याची उद्दिष्टे

- लिस्ट म्हणजे काय व ती कशी तयार करायची?
- Indexing व Slicing
- list च्या methods: `append`, `insert`, `remove`, `pop`, `sort`, `reverse`
- list वर लूप
- list comprehension

---

## १. लिस्ट म्हणजे काय?

**लिस्ट (List)** म्हणजे **अनेक गोष्टी एकत्र साठवण्याचा** पायथनचा मार्ग. ती **क्रमबद्ध (ordered)** आणि **बदलण्यायोग्य (mutable)** आहे.

### सिंटॅक्स

```python
यादी = [वस्तू1, वस्तू2, वस्तू3]
```

### उदाहरण

```python
phale = ["आंबा", "केळी", "सफरचंद"]
sankhya = [10, 20, 30, 40]
mishra = ["राम", 15, 5.6, True]  # वेगवेगळ्या प्रकारच्या वस्तू एकत्र
```

---

## २. Indexing — index चा वापर

प्रत्येक वस्तूला एक **index (क्रमांक)** असतो. **सुरुवात 0 पासून**!

```python
phale = ["आंबा", "केळी", "सफरचंद", "द्राक्ष"]
#         0       1       2          3
#        -4      -3      -2         -1   (मागून)

print(phale[0])    # आंबा (पहिले)
print(phale[2])    # सफरचंद
print(phale[-1])   # द्राक्ष (शेवटचे)
```

---

## ३. Slicing — तुकडा घेणे

`list[start:stop:step]`

```python
sankhya = [10, 20, 30, 40, 50, 60]
print(sankhya[1:4])     # [20, 30, 40]
print(sankhya[:3])      # [10, 20, 30]
print(sankhya[3:])      # [40, 50, 60]
print(sankhya[::2])     # [10, 30, 50]
print(sankhya[::-1])    # उलट
```

---

## ४. list च्या महत्त्वाच्या methods

| Method | काम | उदाहरण |
|---|---|---|
| `append(x)` | शेवटी जोडा | `phale.append("पेरू")` |
| `insert(i, x)` | i ठिकाणी जोडा | `phale.insert(1, "पेरू")` |
| `remove(x)` | x ला काढून टाका | `phale.remove("केळी")` |
| `pop(i)` | i ठिकाणचे काढा (default: शेवटचे) | `phale.pop()` |
| `sort()` | क्रमवारी लावा | `sankhya.sort()` |
| `reverse()` | उलट करा | `phale.reverse()` |
| `index(x)` | x चा index शोधा | `phale.index("आंबा")` |
| `count(x)` | x किती वेळा? | `phale.count("आंबा")` |
| `extend(y)` | दुसरी यादी जोडा | `phale.extend(["पपई"])` |
| `clear()` | सर्व काढा | `phale.clear()` |
| `copy()` | प्रत बनवा | `phale.copy()` |
| `len(list)` | लांबी | `len(phale)` |

---

## ५. list वर लूप

```python
for phal in phale:
    print(phal)

for i in range(len(phale)):
    print(i, phale[i])

for i, phal in enumerate(phale):
    print(i, phal)
```

---

## ६. list comprehension

एका ओळीत list तयार करण्याची सोपी पद्धत.

```python
varg = [i*i for i in range(1, 6)]   # [1, 4, 9, 16, 25]
sam = [i for i in range(1, 11) if i % 2 == 0]
```

---

## 🧪 हँड्स-ऑन लॅब्स

| फाइल | विषय |
|---|---|
| `lab1_list_basic.py` | list तयार करणे, छापणे |
| `lab2_indexing_slicing.py` | index व slice |
| `lab3_list_methods.py` | methods चा वापर |
| `lab4_list_loop.py` | list वर लूप |
| `lab5_comprehension.py` | list comprehension |

---

## 📝 शब्दकोश

| शब्द | अर्थ |
|---|---|
| **List** | अनेक वस्तूंचा क्रमबद्ध समूह |
| **Index** | वस्तूचा क्रमांक (० पासून) |
| **Slicing** | तुकडा घेणे |
| **Mutable** | बदलता येण्यासारखे |
| **Element / Item** | list मधील एक वस्तू |
| **Method** | object वर चालणारे फंक्शन |
| **enumerate** | index व item दोन्ही देणारे फंक्शन |
| **Comprehension** | एका ओळीत list बनवणे |

---

## ✅ स्वाध्याय

1. १० विद्यार्थ्यांचे गुण साठवा व सरासरी छापा.
2. एका list मधून सर्वात मोठी व सर्वात लहान संख्या शोधा.
3. वर्गातील विद्यार्थ्यांची नावे साठवून त्यांची क्रमवारी (alphabetical) लावा.
4. एक list उलटी करा (`reverse()` न वापरता).
5. १ ते २० मधील सर्व विषम संख्यांची list तयार करा (comprehension वापरून).

➡️ **पुढील प्रकरण:** [`08_tuple_set_dict`](../08_tuple_set_dict/)
