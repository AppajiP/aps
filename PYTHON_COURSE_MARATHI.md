# महाराष्ट्र राज्य मंडळ विद्यार्थ्यांसाठी Python कोर्स (मराठीत)

## 1) कोर्सचा उद्देश
- Python प्रोग्रामिंगची पायाभूत समज निर्माण करणे
- प्रत्येक syntax चा **अर्थ (Meaning)** आणि **वापर (Use)** शिकवणे
- प्रत्येक अध्यायानंतर **Hands-on Lab** करून प्रत्यक्ष सराव
- Lab मधील सर्व महत्त्वाच्या संज्ञा (terms) सोप्या भाषेत समजावणे
- शेवटी लहान-मोठे प्रोजेक्ट करून बोर्ड परीक्षेसाठी आणि कौशल्य विकासासाठी तयारी

---

## 2) कोणासाठी?
- महाराष्ट्र राज्य मंडळ (इयत्ता 11वी/12वी – IT/CS/सामान्य विद्यार्थी)
- ज्यांनी आधी कधीही coding केलेले नाही अशा विद्यार्थ्यांसाठीही उपयुक्त

---

## 3) आवश्यक साधने
1. Python 3 (नवीन आवृत्ती)
2. Code Editor (VS Code / IDLE / Thonny)
3. Terminal किंवा Command Prompt

---

## 4) Python म्हणजे काय?
**Python** ही एक high-level, easy-to-read programming language आहे.  
ती web development, data science, AI, automation, scripting, app development अशा अनेक क्षेत्रांत वापरली जाते.

---

## 5) अध्यायनिहाय अभ्यासक्रम

## अध्याय 1: Python ची ओळख आणि पहिला प्रोग्राम

### Syntax 1: `print()`
**Meaning:** स्क्रीनवर मजकूर/मूल्य दाखवण्यासाठी function  
**Use:** Output देण्यासाठी

```python
print("नमस्कार महाराष्ट्र!")
```

### Syntax 2: Comment (`#`)
**Meaning:** प्रोग्राममध्ये नोट्स लिहिण्यासाठी ओळ  
**Use:** कोड समजायला सोपे होते; comment execute होत नाही

```python
# हा माझा पहिला Python प्रोग्राम आहे
print("Hello")
```

### Hands-on Lab 1
1. तुमचे नाव print करा
2. तुमच्या शाळेचे नाव print करा
3. दोन वेगवेगळ्या ओळींमध्ये output दाखवा

```python
print("माझे नाव: आर्या")
print("शाळा: जिल्हा परिषद विद्यालय")
```

### Lab Terms (अर्थ)
- **Output:** स्क्रीनवर दिसणारा निकाल
- **Function:** विशिष्ट काम करणारा तयार कोड ब्लॉक
- **Comment:** कोडमध्ये लिहिलेली स्पष्टीकरण ओळ

---

## अध्याय 2: Variables आणि Data Types

### Syntax 1: Variable Assignment (`=`)
**Meaning:** मूल्य साठवण्यासाठी नाव देणे  
**Use:** डेटा पुन्हा पुन्हा वापरण्यासाठी

```python
name = "रोहन"
age = 16
percentage = 89.5
```

### Syntax 2: `type()`
**Meaning:** variable चा data type तपासतो  
**Use:** कोणत्या प्रकारचा डेटा आहे हे समजते

```python
print(type(name))        # str
print(type(age))         # int
print(type(percentage))  # float
```

### मुख्य Data Types
- `int` : पूर्णांक (उदा. 10)
- `float` : दशांश संख्या (उदा. 12.5)
- `str` : मजकूर (उदा. "Pune")
- `bool` : True / False

### Hands-on Lab 2
विद्यार्थ्याचे नाव, रोल नंबर, टक्केवारी, पास/फेल स्थिती variables मध्ये घ्या आणि print करा.

```python
student_name = "सई"
roll_no = 23
marks_percent = 91.2
is_pass = True

print(student_name, roll_no, marks_percent, is_pass)
```

### Lab Terms
- **Variable:** डेटा ठेवण्यासाठी मेमरीतील लेबल
- **Data Type:** डेटाचा प्रकार
- **Assignment:** variable ला value देणे

---

## अध्याय 3: Input आणि Type Casting

### Syntax 1: `input()`
**Meaning:** वापरकर्त्याकडून माहिती घेते  
**Use:** dynamic program तयार करणे

```python
name = input("तुमचे नाव लिहा: ")
print("नमस्कार", name)
```

### Syntax 2: Type Casting (`int()`, `float()`, `str()`)
**Meaning:** एका type मधून दुसऱ्या type मध्ये बदल  
**Use:** गणितासाठी string input ला संख्या बनवणे

```python
a = int(input("पहिला अंक: "))
b = int(input("दुसरा अंक: "))
print("बेरीज =", a + b)
```

### Hands-on Lab 3
वापरकर्त्याचे नाव, गणित आणि विज्ञान गुण input घ्या. सरासरी काढा.

```python
name = input("नाव: ")
math = float(input("गणित गुण: "))
science = float(input("विज्ञान गुण: "))
avg = (math + science) / 2
print(name, "ची सरासरी =", avg)
```

### Lab Terms
- **User Input:** वापरकर्त्याने दिलेला डेटा
- **Type Casting:** data type बदलण्याची प्रक्रिया
- **Average:** एकूण गुण / विषयांची संख्या

---

## अध्याय 4: Operators

### Arithmetic Operators
- `+` बेरीज
- `-` वजाबाकी
- `*` गुणाकार
- `/` भागाकार
- `//` पूर्णांक भागाकार
- `%` बाकी (remainder)
- `**` घातांक

### Comparison Operators
- `==`, `!=`, `>`, `<`, `>=`, `<=`

### Logical Operators
- `and`, `or`, `not`

### Hands-on Lab 4
दोन संख्या घेऊन सर्व arithmetic operations दाखवा.

```python
x = int(input("x: "))
y = int(input("y: "))

print("बेरीज:", x + y)
print("वजाबाकी:", x - y)
print("गुणाकार:", x * y)
print("भागाकार:", x / y)
print("बाकी:", x % y)
```

### Lab Terms
- **Operator:** क्रिया करणारे चिन्ह
- **Operand:** operator वर काम करणारी values
- **Expression:** operator + operands यांचा एकत्रित भाग

---

## अध्याय 5: Decision Making (`if`, `elif`, `else`)

### Syntax
```python
if condition:
    # कोड
elif condition:
    # कोड
else:
    # कोड
```

**Meaning:** अटींनुसार निर्णय घेणे  
**Use:** पास/फेल, grade, मतदान पात्रता, discount logic

### Hands-on Lab 5
टक्केवारीनुसार grade ठरवा.

```python
marks = float(input("टक्केवारी: "))

if marks >= 75:
    print("Grade: Distinction")
elif marks >= 60:
    print("Grade: First Class")
elif marks >= 35:
    print("Grade: Pass")
else:
    print("Grade: Fail")
```

### Lab Terms
- **Condition:** True/False देणारी अट
- **Block:** indentation ने ठरलेला कोडचा गट
- **Indentation:** Python मध्ये spacing वापरून block दाखवणे

---

## अध्याय 6: Loops (`for`, `while`)

### Syntax 1: `for`
**Meaning:** मर्यादित वेळा पुनरावृत्ती  
**Use:** range वर iterate करणे

```python
for i in range(1, 6):
    print(i)
```

### Syntax 2: `while`
**Meaning:** अट खरी असेपर्यंत loop  
**Use:** condition based repetition

```python
n = 1
while n <= 5:
    print(n)
    n += 1
```

### Loop Control
- `break` : loop थांबवतो
- `continue` : चालू iteration skip करतो

### Hands-on Lab 6
1 ते 10 पर्यंत सम संख्या print करा.

```python
for n in range(1, 11):
    if n % 2 == 0:
        print(n)
```

### Lab Terms
- **Iteration:** loop ची एक फेरी
- **Counter:** मोजणीसाठी variable
- **Infinite Loop:** कधीही न थांबणारा loop

---

## अध्याय 7: Strings

### Syntax आणि वापर
- Indexing: `text[0]`
- Slicing: `text[0:4]`
- Methods: `.upper()`, `.lower()`, `.strip()`, `.replace()`
- Length: `len(text)`

```python
text = " Maharashtra "
print(text.strip().upper())
```

### Hands-on Lab 7
नाव input घ्या आणि:
1. मोठ्या अक्षरात
2. लांबी
3. पहिले 3 अक्षरे

```python
name = input("नाव: ")
print("Upper:", name.upper())
print("Length:", len(name))
print("पहिले 3 अक्षरे:", name[:3])
```

### Lab Terms
- **String:** अक्षरांची मालिका
- **Index:** अक्षराचा क्रमांक (0 पासून)
- **Slice:** string चा काही भाग

---

## अध्याय 8: Lists, Tuples, Sets, Dictionaries

### List (`[]`)
बदलता (mutable) collection

### Tuple (`()`)
न बदलणारा (immutable) collection

### Set (`{}`)
unique values, duplicate काढते

### Dictionary (`{key: value}`)
key-value जोडी

```python
marks = [78, 85, 90]
student = {"name": "अमोल", "std": 11}
```

### Hands-on Lab 8
5 विषयांचे गुण list मध्ये घ्या आणि total व max शोधा.

```python
marks = [67, 72, 88, 91, 79]
print("Total:", sum(marks))
print("Highest:", max(marks))
```

### Lab Terms
- **Mutable:** बदलता येणारा
- **Immutable:** बदलता न येणारा
- **Key:** dictionary मधील ओळख चिन्ह

---

## अध्याय 9: Functions

### Syntax
```python
def function_name(parameters):
    # कोड
    return value
```

**Meaning:** पुन्हा वापरता येणारा कोड ब्लॉक  
**Use:** modular coding, duplication कमी करणे

```python
def add(a, b):
    return a + b

print(add(5, 3))
```

### Hands-on Lab 9
`calculate_area(length, breadth)` function तयार करा.

```python
def calculate_area(length, breadth):
    return length * breadth

print("Area:", calculate_area(10, 5))
```

### Lab Terms
- **Parameter:** function definition मधील variable
- **Argument:** function call वेळी दिलेली value
- **Return:** function मधून परत येणारे मूल्य

---

## अध्याय 10: File Handling

### Syntax
- `open("file.txt", "r")` वाचण्यासाठी
- `open("file.txt", "w")` लिहिण्यासाठी
- `open("file.txt", "a")` शेवटी जोडण्यासाठी

```python
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("Python lab notes")
```

**Use:** डेटा कायमस्वरूपी साठवणे

### Hands-on Lab 10
`students.txt` मध्ये 3 नावे लिहा आणि ती पुन्हा वाचा.

```python
with open("students.txt", "w", encoding="utf-8") as f:
    f.write("सोनाली\n")
    f.write("ओंकार\n")
    f.write("वैष्णवी\n")

with open("students.txt", "r", encoding="utf-8") as f:
    data = f.read()
    print(data)
```

### Lab Terms
- **File Mode:** r/w/a सारखा mode
- **Encoding:** अक्षरांचा साठवणूक प्रकार (UTF-8)
- **Context Manager (`with`):** file आपोआप close करणारी पद्धत

---

## अध्याय 11: Exception Handling

### Syntax
```python
try:
    # धोका असलेला कोड
except:
    # error हाताळणे
finally:
    # शेवटी नेहमी चालणारा कोड
```

```python
try:
    x = int(input("अंक: "))
    print(100 / x)
except ZeroDivisionError:
    print("0 ने भागाकार करता येत नाही.")
except ValueError:
    print("कृपया वैध अंक द्या.")
```

### Hands-on Lab 11
division calculator तयार करा आणि invalid input हाताळा.

### Lab Terms
- **Exception:** प्रोग्राम चालताना येणारी चूक
- **Runtime Error:** execution दरम्यान येणारी त्रुटी
- **Handling:** चूक येऊनही प्रोग्राम नियंत्रणात ठेवणे

---

## अध्याय 12: Mini OOP (Object Oriented Programming) परिचय

### Syntax
```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show(self):
        print(self.name, self.marks)
```

**Meaning:** class म्हणजे template, object म्हणजे त्या template ची प्रत्यक्ष instance  
**Use:** मोठ्या प्रोजेक्टमध्ये code structure सुधारते

### Hands-on Lab 12
`Book` class तयार करा (title, price) आणि details print करा.

### Lab Terms
- **Class:** गुणधर्म आणि methods असलेला नकाशा
- **Object:** class वरून तयार केलेली वस्तू
- **Method:** class मधील function

---

## 6) Projects (Hands-on)

## Project 1: विद्यार्थी गुणपत्रक प्रणाली
### उद्देश
5 विषयांचे गुण घेऊन total, average, grade दाखवणे

### अपेक्षित वैशिष्ट्ये
- Input घेणे
- Loop वापरणे
- Decision (`if-elif-else`) वापरणे
- Function वापरणे

### Project Lab Steps
1. विद्यार्थ्याचे नाव घ्या
2. 5 विषयांचे गुण list मध्ये घ्या
3. total आणि average काढा
4. grade logic लागू करा
5. report print करा

### वापरलेले Terms
- **Report:** माहितीचे सादरीकरण
- **Logic:** निर्णय घेण्यासाठी अटींची रचना
- **Validation:** चुकीचा input तपासणे

---

## Project 2: किराणा बिल जनरेटर
### उद्देश
वस्तू, प्रमाण, किंमत घेऊन बिल तयार करणे

### Project Lab
1. dictionary मध्ये वस्तू व दर ठेवा
2. user कडून quantity घ्या
3. subtotal, tax, final amount काढा
4. फॉरमॅटेड बिल print करा

### वापरलेले Terms
- **Subtotal:** करापूर्वीची एकूण रक्कम
- **Tax:** कर
- **Final Amount:** अंतिम देय रक्कम

---

## Project 3: Quiz Application (MCQ)
### उद्देश
Python मध्ये प्रश्नोत्तरी अॅप बनवणे

### Project Lab
1. प्रश्न list/dictionary मध्ये साठवा
2. प्रत्येक प्रश्नासाठी पर्याय दाखवा
3. उत्तर तपासा
4. score मोजा
5. शेवटी निकाल आणि टक्केवारी दाखवा

### वापरलेले Terms
- **Score:** बरोबर उत्तरांची संख्या
- **MCQ:** Multiple Choice Question
- **Result Analysis:** निकालाचा आढावा

---

## Project 4: विद्यार्थी उपस्थिती नोंद (File आधारित)
### उद्देश
विद्यार्थ्यांची उपस्थिती file मध्ये save/read करणे

### Project Lab
1. नाव input घ्या
2. उपस्थित/अनुपस्थित status निवडा
3. file मध्ये तारीखसह save करा
4. आधीच्या नोंदी वाचा आणि दाखवा

### वापरलेले Terms
- **Record:** साठवलेली नोंद
- **Timestamp/Date:** वेळ/तारीख माहिती
- **Persistent Data:** प्रोग्राम बंद झाल्यावरही टिकणारा डेटा

---

## 7) मूल्यमापन पद्धती (Assessment)
- Lab performance: 30%
- Mini projects: 30%
- Theory + syntax meaning test: 20%
- Final practical exam: 20%

---

## 8) सराव प्रश्न (Practice)
1. `input()` आणि `print()` मधील फरक लिहा.
2. `list` आणि `tuple` मधील 3 फरक लिहा.
3. 1 ते 50 मधील 3 ने भाग जाणाऱ्या संख्या print करणारा प्रोग्राम लिहा.
4. function वापरून साधा व्याज (Simple Interest) काढा.
5. file मध्ये 10 विद्यार्थ्यांची नावे साठवून पुन्हा वाचा.

---

## 9) शिक्षकांसाठी अध्यापन सूचना
- प्रत्येक अध्यायात: 20% theory, 80% practical
- विद्यार्थ्यांना pair programming द्या
- प्रत्येक lab नंतर reflection लिहायला सांगा:
  - काय समजले?
  - कुठे अडचण आली?
  - पुढे काय सुधारायचे?

---

## 10) संक्षेप
हा कोर्स विद्यार्थ्यांना Python ची मूलभूत ते मध्यम स्तरातील संपूर्ण तयारी देतो.  
प्रत्येक syntax चा अर्थ, वापर, प्रयोग, terms आणि projects मुळे विद्यार्थी बोर्ड परीक्षा तसेच कौशल्याधारित शिक्षणासाठी सक्षम होतात.
