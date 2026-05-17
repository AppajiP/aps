# प्रकरण १० — फंक्शन्स (Functions)

## 🎯 शिकण्याची उद्दिष्टे

- function म्हणजे काय व का?
- function तयार करणे (`def`) व कॉल करणे
- Parameters व Arguments
- `return` विधान
- Default arguments, Keyword arguments, `*args`, `**kwargs`
- Scope (Local, Global)
- Lambda functions

---

## १. Function म्हणजे काय?

**Function** म्हणजे **विशिष्ट काम करणारा कोडचा गट**. एकदा लिहा, अनेक वेळा वापरा.

### फायदे:
- कोडाची पुनरावृत्ती टळते (DRY — Don't Repeat Yourself)
- कोड वाचायला सोपा
- एका जागी बदल केला तरी सर्वत्र लागू
- मोठा problem लहान भागांत विभागायला

---

## २. Function तयार करणे

### सिंटॅक्स

```python
def function_naav(parameters):
    """docstring (टीप)"""
    कोड
    return किंमत
```

| भाग | अर्थ |
|---|---|
| `def` | "define" — function तयार करणारा keyword |
| `function_naav` | function चे नाव |
| `(parameters)` | function ला लागणारी माहिती |
| `:` | block सुरू |
| `return` | किंमत परत द्यायला (ऐच्छिक) |

### उदाहरण

```python
def namaskar():
    print("नमस्कार!")

namaskar()    # function call - "नमस्कार!" छापते
```

---

## ३. Parameters व Arguments

```python
def namaskar(naav):       # naav हा parameter
    print(f"नमस्कार, {naav}!")

namaskar("राम")           # "राम" हा argument
namaskar("सीता")
```

- **Parameter** = function लिहिताना दिलेले चल
- **Argument** = function कॉल करताना दिलेली किंमत

---

## ४. `return` विधान

```python
def berij(a, b):
    return a + b

uttar = berij(5, 3)
print(uttar)    # 8
```

`return` ने function किंमत **परत** करते. ती चलात साठवता येते किंवा वापरता येते.

---

## ५. Default Arguments

```python
def namaskar(naav="मित्र"):
    print(f"नमस्कार, {naav}!")

namaskar()           # नमस्कार, मित्र!
namaskar("राम")      # नमस्कार, राम!
```

---

## ६. Keyword Arguments

```python
def vidyarthi(naav, vay, varg):
    print(naav, vay, varg)

vidyarthi(naav="राम", varg="१०वी", vay=15)
```

क्रम लक्षात ठेवायची गरज नाही!

---

## ७. `*args` व `**kwargs`

`*args` — कितीही positional arguments:

```python
def berij(*sankhya):
    return sum(sankhya)

print(berij(1, 2, 3))           # 6
print(berij(1, 2, 3, 4, 5))     # 15
```

`**kwargs` — कितीही keyword arguments:

```python
def vidyarthi(**mahiti):
    for k, v in mahiti.items():
        print(k, ":", v)

vidyarthi(naav="राम", vay=15, gaav="पुणे")
```

---

## ८. Scope (कार्यक्षेत्र)

- **Local** — function च्या आत
- **Global** — function च्या बाहेर

```python
x = 10           # global

def test():
    y = 5        # local
    print(x)     # global वापरू शकतो
    print(y)

test()
# print(y)   # ERROR — y बाहेर उपलब्ध नाही
```

---

## ९. Lambda Function (अनामी function)

एका ओळीचे, नाव नसलेले function.

```python
varg = lambda x: x * x
print(varg(5))        # 25

berij = lambda a, b: a + b
print(berij(3, 4))    # 7
```

`sorted`, `map`, `filter` सोबत खूप उपयोगी:

```python
sankhya = [3, 1, 4, 1, 5, 9, 2]
print(sorted(sankhya))                      # नैसर्गिक
print(sorted(sankhya, key=lambda x: -x))    # उलट
```

---

## 🧪 हँड्स-ऑन लॅब्स

| फाइल | विषय |
|---|---|
| `lab1_basic_function.py` | function मूळ रचना |
| `lab2_return.py` | return विधान |
| `lab3_arguments.py` | default, keyword |
| `lab4_args_kwargs.py` | *args, **kwargs |
| `lab5_scope.py` | scope, global |
| `lab6_lambda.py` | lambda functions |
| `lab7_calculator.py` | function-based calculator |

---

## 📝 शब्दकोश

| शब्द | अर्थ |
|---|---|
| **Function** | विशिष्ट काम करणारा कोड-गट |
| **def** | function तयार करायचा keyword |
| **Parameter** | function ला दिलेले चल |
| **Argument** | function ला दिलेली किंमत |
| **return** | किंमत परत देणे |
| **Docstring** | function ची माहिती `"""..."""` |
| **Scope** | चल कुठे उपलब्ध आहे |
| **Local** | function च्या आत |
| **Global** | सर्वत्र |
| **Lambda** | एका ओळीचे function |
| **Recursion** | function स्वतःलाच कॉल करते |

---

## ✅ स्वाध्याय

1. एका संख्येचे factorial काढायचे function लिहा.
2. एक संख्या prime आहे का तपासायचे function लिहा.
3. वर्तुळाचे क्षेत्रफळ काढायचे function (default π=3.14).
4. एका list ची सरासरी काढायचे function.
5. Lambda वापरून list मधल्या प्रत्येक संख्येचा वर्ग काढा (`map` वापरून).

➡️ **पुढील प्रकरण:** [`11_modules`](../11_modules/)
