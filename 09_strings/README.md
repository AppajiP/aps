# प्रकरण ०९ — स्ट्रिंग्स (Strings)

## 🎯 शिकण्याची उद्दिष्टे

- string तयार करण्याचे प्रकार
- string indexing व slicing
- string च्या उपयोगी methods
- string concatenation व repetition
- string formatting (पुनरावलोकन)

---

## १. String तयार करणे

```python
s1 = "नमस्कार"
s2 = 'पायथन'
s3 = """अनेक
ओळींची
string"""
```

`"..."` व `'...'` यांत फरक नाही. पण आत quote असेल तर:

```python
print("त्याने म्हटले 'नमस्कार'")
print('ती म्हणाली "हो"')
```

---

## २. String Indexing व Slicing

```python
s = "पायथन"
#    0  1 2 3
print(s[0])      # प
print(s[-1])     # न
print(s[1:3])    # ायथ
print(s[::-1])   # नथयाप (उलटी)
```

⚠️ string **immutable** आहे — `s[0] = "ख"` चालत नाही!

---

## ३. String च्या महत्त्वाच्या methods

| Method | काम | उदाहरण |
|---|---|---|
| `upper()` | मोठ्या अक्षरांत | `"hello".upper()` → `"HELLO"` |
| `lower()` | लहान अक्षरांत | `"HELLO".lower()` → `"hello"` |
| `title()` | प्रत्येक शब्दाचे पहिले मोठे | `"ram sham".title()` |
| `capitalize()` | फक्त पहिले मोठे | `"ram".capitalize()` |
| `strip()` | दोन्ही बाजूची space काढा | `"  hi  ".strip()` |
| `lstrip()` | डाव्या बाजूची | |
| `rstrip()` | उजव्या बाजूची | |
| `replace(a, b)` | a च्या जागी b | `"राम".replace("रा", "श्या")` |
| `split(sep)` | sep ने तोडून list | `"a,b,c".split(",")` |
| `join(list)` | list ला एकत्र | `",".join(["a","b"])` |
| `find(x)` | x पहिल्यांदा कुठे? (-1 नसेल तर) | |
| `count(x)` | x किती वेळा? | |
| `startswith(x)` | x ने सुरू होते? | |
| `endswith(x)` | x ने संपते? | |
| `isdigit()` | फक्त संख्या आहे? | |
| `isalpha()` | फक्त अक्षरे? | |
| `len(s)` | लांबी | |

---

## ४. Concatenation व Repetition

```python
naav = "राम"
adnaav = "शर्मा"
purna = naav + " " + adnaav         # जोडणे
print(purna)

print("नमस्कार " * 3)               # repeat
```

---

## ५. String iteration

```python
for akshar in "पायथन":
    print(akshar)
```

---

## 🧪 हँड्स-ऑन लॅब्स

| फाइल | विषय |
|---|---|
| `lab1_string_basic.py` | string मूळ क्रिया |
| `lab2_indexing.py` | indexing व slicing |
| `lab3_methods.py` | string methods |
| `lab4_split_join.py` | split, join |
| `lab5_word_count.py` | शब्द/अक्षर मोजणी |

---

## 📝 शब्दकोश

| शब्द | अर्थ |
|---|---|
| **String** | अक्षरांचा क्रम |
| **Concatenation** | जोडणे (`+`) |
| **Substring** | string चा तुकडा |
| **Immutable** | बदलता येत नाही |
| **strip** | अतिरिक्त space काढणे |
| **split** | तुकडे करणे |
| **join** | जोडून एक string करणे |

---

## ✅ स्वाध्याय

1. एक वाक्य घ्या व त्यातील स्वर (अ, इ, उ, ए, ओ) किती ते छापा.
2. एक शब्द palindrome आहे का तपासा (पुढून आणि मागून सारखा).
3. एका वाक्यातील सर्व शब्द उलट करा.
4. वापरकर्त्याकडून email घेऊन त्यात `@` व `.` आहे का तपासा.
5. एक वाक्य घेऊन त्यातील प्रत्येक शब्दाचे पहिले अक्षर मोठे करा.

➡️ **पुढील प्रकरण:** [`10_functions`](../10_functions/)
