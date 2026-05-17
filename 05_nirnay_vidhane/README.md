# प्रकरण ०५ — निर्णय विधाने (Conditional Statements)

## 🎯 शिकण्याची उद्दिष्टे

- `if` विधान — एखादी अट खरी असेल तर काय?
- `if-else` — खरी असेल तर एक, खोटी असेल तर दुसरे
- `if-elif-else` — अनेक अटी
- `nested if` — एका आत दुसरे
- एका ओळीचे (ternary / conditional) expression

---

## १. `if` विधान

### अर्थ

जर (if) काही अट **खरी** असेल तर **काही कोड** चालेल; नाहीतर तो skip होईल.

### सिंटॅक्स

```python
if अट:
    कोड
```

> ⚠️ कोडाच्या आधी **`:`** आणि नंतर **indent (४ spaces)** हवीच!

### उदाहरण

```python
vay = 18
if vay >= 18:
    print("तू मतदार होऊ शकतोस")
```

---

## २. `if-else`

```python
if अट:
    कोड १
else:
    कोड २
```

```python
vay = 15
if vay >= 18:
    print("मतदार")
else:
    print("अद्याप मतदार नाहीस")
```

---

## ३. `if-elif-else`

**elif** = "else if" — आधीची अट खोटी असली तर ही तपासते.

```python
if अट१:
    कोड १
elif अट२:
    कोड २
elif अट३:
    कोड ३
else:
    अंतिम कोड
```

### उदाहरण — श्रेणी (Grade)

```python
guna = 75
if guna >= 90:
    print("A श्रेणी")
elif guna >= 75:
    print("B श्रेणी")
elif guna >= 60:
    print("C श्रेणी")
elif guna >= 35:
    print("D श्रेणी")
else:
    print("नापास")
```

---

## ४. Nested if (एका आत दुसरे)

```python
vay = 20
nagrik = True

if nagrik:
    if vay >= 18:
        print("तू मतदार आहेस")
    else:
        print("वय कमी")
else:
    print("भारतीय नागरिक नाहीस")
```

---

## ५. एका ओळीचे `if` (Ternary)

```python
status = "मतदार" if vay >= 18 else "अद्याप नाही"
```

---

## इंडेंटेशन (Indentation) — सर्वात महत्वाचे!

पायथन कोडाचे "block" (गट) **जागेने (spaces)** ओळखते. साधारणपणे **४ spaces** वापरतात.

```python
if True:
    print("आत")      # ४ space - if चा भाग
print("बाहेर")        # space नाही - if बाहेर
```

❌ चुकीचा (mixing tabs/spaces / unequal indent):
```python
if True:
    print("a")
   print("b")   # IndentationError
```

---

## 🧪 हँड्स-ऑन लॅब्स

| फाइल | विषय |
|---|---|
| `lab1_if.py` | फक्त `if` |
| `lab2_if_else.py` | `if-else` |
| `lab3_elif.py` | अनेक अटी |
| `lab4_nested.py` | nested if |
| `lab5_grading.py` | गुणांची श्रेणी |
| `lab6_leap_year.py` | leap year तपासणी |

---

## 📝 शब्दकोश

| शब्द | अर्थ |
|---|---|
| **Condition (अट)** | खरी/खोटी ठरणारी expression |
| **Block** | एकाच indent वर लिहिलेला कोडचा गट |
| **Indentation** | कोडाच्या आधी सोडलेली जागा |
| **Ternary** | एका ओळीत `if-else` |
| **Boolean Expression** | `True`/`False` देणारी expression |

---

## ✅ स्वाध्याय

1. एक संख्या घ्या आणि सम (even) की विषम (odd) ते छापा.
2. वय घेऊन — लहान बाळ (०-२), बालक (३-१२), किशोर (१३-१९), तरुण (२०-५९), वृद्ध (६०+) — श्रेणी छापा.
3. ३ संख्यांपैकी सर्वात मोठी संख्या शोधा.
4. वर्ष leap year आहे का तपासा.
5. साधी कॅल्क्युलेटर — `+`, `-`, `*`, `/` साठी प्रश्न विचारून योग्य उत्तर द्या.

➡️ **पुढील प्रकरण:** [`06_loops`](../06_loops/)
