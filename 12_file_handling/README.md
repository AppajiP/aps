# प्रकरण १२ — फाइल हाताळणी (File Handling)

## 🎯 शिकण्याची उद्दिष्टे

- फाइल उघडणे (`open()`)
- फाइल mode — `r`, `w`, `a`, `r+`, `b`
- फाइल वाचणे (`read`, `readline`, `readlines`)
- फाइलमध्ये लिहिणे (`write`, `writelines`)
- `with` विधान (best practice)
- CSV फाइल्सची ओळख

---

## १. फाइल का?

प्रोग्राम बंद झाला की चलांमधली माहिती जाते. **कायम (permanent)** माहिती साठवायला **फाइल** वापरतात.

> उदा. विद्यार्थ्यांचे गुण, ग्राहकांची यादी, log files.

---

## २. `open()` फंक्शन

### सिंटॅक्स

```python
file = open("filename", "mode", encoding="utf-8")
```

### Mode (पद्धत)

| Mode | अर्थ |
|---|---|
| `"r"` | फक्त वाचा (Read) — default |
| `"w"` | लिहा (Write) — जुनी माहिती मिटते! |
| `"a"` | जोडा (Append) — शेवटी |
| `"r+"` | वाचा व लिहा |
| `"x"` | नवीन फाइल बनवा (अस्तित्वात असल्यास error) |
| `"b"` | binary mode (`rb`, `wb`) |
| `"t"` | text mode (default) |

⚠️ **encoding="utf-8"** हे मराठीसाठी आवश्यक!

---

## ३. वाचणे (Reading)

```python
f = open("data.txt", "r", encoding="utf-8")

mahiti = f.read()           # संपूर्ण फाइल
oli = f.readline()          # एक ओळ
sarv_oli = f.readlines()    # सर्व ओळी list मध्ये

f.close()                   # महत्त्वाचे!
```

### `with` विधान (शिफारस)

`with` वापरले की **आपोआप close** होते.

```python
with open("data.txt", "r", encoding="utf-8") as f:
    mahiti = f.read()
    print(mahiti)
# इथे f आपोआप बंद झाली
```

---

## ४. लिहिणे (Writing)

```python
with open("data.txt", "w", encoding="utf-8") as f:
    f.write("पहिली ओळ\n")
    f.write("दुसरी ओळ\n")
```

⚠️ `"w"` mode मध्ये **जुनी माहिती मिटते**. जोडण्यासाठी `"a"`.

```python
with open("data.txt", "a", encoding="utf-8") as f:
    f.write("नवीन ओळ\n")
```

### अनेक ओळी

```python
oli = ["ओळ १\n", "ओळ २\n", "ओळ ३\n"]
with open("data.txt", "w", encoding="utf-8") as f:
    f.writelines(oli)
```

---

## ५. ओळींवर लूप

```python
with open("data.txt", "r", encoding="utf-8") as f:
    for oli in f:
        print(oli.strip())
```

---

## ६. CSV फाइल

```python
import csv

with open("vidyarthi.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["नाव", "वय", "वर्ग"])
    writer.writerow(["राम", 15, "१०वी"])
    writer.writerow(["सीता", 14, "९वी"])

with open("vidyarthi.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

---

## 🧪 हँड्स-ऑन लॅब्स

| फाइल | विषय |
|---|---|
| `lab1_write.py` | फाइलमध्ये लिहिणे |
| `lab2_read.py` | फाइल वाचणे |
| `lab3_append.py` | जोडणे |
| `lab4_with.py` | `with` विधान |
| `lab5_csv.py` | CSV फाइल |

---

## 📝 शब्दकोश

| शब्द | अर्थ |
|---|---|
| **File Handle** | open() ने मिळणारा object |
| **Mode** | फाइल कशासाठी उघडली |
| **Encoding** | अक्षरे साठवण्याचा मार्ग (utf-8 = सर्व भाषा) |
| **Read** | वाचणे |
| **Write** | लिहिणे |
| **Append** | जोडणे |
| **close** | फाइल बंद करणे |
| **with** | आपोआप close करणारा keyword |
| **CSV** | Comma Separated Values |

---

## ✅ स्वाध्याय

1. आपल्या आवडत्या ५ पुस्तकांची नावे एका फाइलमध्ये साठवा.
2. एक फाइल वाचून त्यातील ओळींची संख्या मोजा.
3. एका फाइलमध्ये सर्व ओळींची संख्या जोडून छापा.
4. विद्यार्थ्यांची माहिती (नाव, गुण) CSV मध्ये साठवून त्यातून पास/नापास list बनवा.

➡️ **पुढील प्रकरण:** [`13_exceptions`](../13_exceptions/)
