# प्रकरण ०६ — लूप्स (Loops)

## 🎯 शिकण्याची उद्दिष्टे

- `for` लूप — ठराविक वेळा पुनरावृत्ती
- `while` लूप — अट खरी असेपर्यंत
- `range()` फंक्शन
- `break` व `continue`
- `else` लूपसोबत
- Nested loops

---

## लूप म्हणजे काय?

**लूप (Loop)** म्हणजे **पुनरावृत्ती (repetition)**. एकच कोड अनेक वेळा चालवण्यासाठी लूप वापरतात.

> उदा. १ ते १०० सर्व संख्या छापायच्या असतील तर १०० वेळा `print()` लिहिणे शक्य नाही — लूप वापरला तर ३ ओळीत होते.

---

## १. `for` लूप

### सिंटॅक्स

```python
for चल in यादी:
    कोड
```

### `range()` सोबत

`range(start, stop, step)` — संख्यांची मालिका तयार करते.

| उपयोग | अर्थ |
|---|---|
| `range(5)` | `0, 1, 2, 3, 4` |
| `range(1, 6)` | `1, 2, 3, 4, 5` |
| `range(1, 10, 2)` | `1, 3, 5, 7, 9` |
| `range(10, 0, -1)` | `10, 9, 8, ... 1` |

### उदाहरण

```python
for i in range(1, 6):
    print(i)
```

```python
phale = ["आंबा", "केळी", "सफरचंद"]
for phal in phale:
    print(phal)
```

---

## २. `while` लूप

### सिंटॅक्स

```python
while अट:
    कोड
```

जोपर्यंत अट **खरी** आहे, तोपर्यंत कोड पुन्हा-पुन्हा चालतो.

### उदाहरण

```python
i = 1
while i <= 5:
    print(i)
    i += 1   # हे विसरू नका, नाहीतर infinite loop!
```

⚠️ **Infinite Loop:** अट कधीच खोटी होत नसेल तर लूप कायमचा चालत राहतो. `Ctrl + C` दाबून थांबवावा लागतो.

---

## ३. `break` व `continue`

| शब्द | अर्थ |
|---|---|
| `break` | लूप ताबडतोब थांबव |
| `continue` | ही वेळ skip कर, पुढच्या वेळेस जा |

### `break` उदाहरण

```python
for i in range(1, 10):
    if i == 5:
        break
    print(i)
# output: 1 2 3 4
```

### `continue` उदाहरण

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
# output: 1 2 4 5 (3 वगळला)
```

---

## ४. `else` लूपसोबत

लूप **break न होता पूर्ण** झाला तर `else` चालतो.

```python
for i in range(1, 4):
    print(i)
else:
    print("लूप पूर्ण झाला!")
```

---

## ५. Nested Loops (एका आत दुसरा)

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
```

---

## 🧪 हँड्स-ऑन लॅब्स

| फाइल | विषय |
|---|---|
| `lab1_for_basic.py` | `for` लूप |
| `lab2_range.py` | `range()` चे प्रकार |
| `lab3_while.py` | `while` लूप |
| `lab4_break_continue.py` | break, continue |
| `lab5_nested.py` | nested लूप — पाढे |
| `lab6_patterns.py` | * चे आकार |

---

## 📝 शब्दकोश

| शब्द | अर्थ |
|---|---|
| **Loop** | पुनरावृत्ती |
| **Iteration** | लूपची एक वेळ |
| **Iterable** | ज्यावर लूप करता येते (list, string, tuple, range) |
| **range()** | संख्यांची मालिका |
| **break** | लूप तोडणे |
| **continue** | एक iteration skip करणे |
| **Infinite Loop** | कधीच न संपणारा लूप |

---

## ✅ स्वाध्याय

1. १ ते १०० मधील सर्व सम संख्यांची बेरीज छापा.
2. एखाद्या संख्येचे factorial (n!) काढा.
3. १ ते १००० मधील सर्व मूळ संख्या (prime numbers) छापा.
4. एका संख्येचे पाढे (multiplication table) छापा.
5. एका संख्येचा उलटा (reverse) काढा.

➡️ **पुढील प्रकरण:** [`07_yadi_lists`](../07_yadi_lists/)
