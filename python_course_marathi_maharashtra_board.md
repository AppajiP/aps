# महाराष्ट्र राज्य मंडळासाठी Python कोर्स (मराठी)

## 1) कोर्सचा उद्देश
हा कोर्स महाराष्ट्र राज्य मंडळातील (इयत्ता 11वी/12वी) विद्यार्थ्यांसाठी तयार केला आहे. कोर्समध्ये:
- Python मधील महत्त्वाच्या syntax चा **अर्थ (meaning)** आणि **वापर (use-case)** सोप्या भाषेत
- प्रत्येक संकल्पनेनंतर **hands-on lab**
- प्रत्येक lab आणि project मध्ये वापरलेल्या तांत्रिक शब्दांचा **मराठीत अर्थ**
- शालेय पातळीवर उपयुक्त **project-based practicals**

---

## 2) पूर्वतयारी
- संगणक/लॅपटॉप (Windows/Linux/Mac)
- Python 3 स्थापित असणे
- Text Editor (VS Code/IDLE/Thonny)
- मूलभूत इंग्रजी keyword ओळख (if, for, def, class)

---

## 3) अभ्यासक्रम रचना (Module-wise)
1. Python परिचय, `print()`, `input()`, comments  
2. Variables, Data Types, Type Conversion  
3. Operators  
4. Decision Making (`if`, `elif`, `else`)  
5. Loops (`for`, `while`, `break`, `continue`)  
6. Strings  
7. List, Tuple, Set, Dictionary  
8. Functions  
9. File Handling  
10. Exception Handling  
11. OOP ची ओळख  
12. Modules आणि Mini Revision

---

## 4) Syntax: अर्थ आणि वापर (Quick Reference)

| Syntax | अर्थ (Meaning) | वापर (Use) |
|---|---|---|
| `print(x)` | आउटपुट दाखवणे | निकाल स्क्रीनवर दाखवण्यासाठी |
| `input()` | वापरकर्त्याकडून माहिती घेणे | नाव, गुण, संख्या घेण्यासाठी |
| `#` | एक ओळीतील comment | कोड समजावण्यासाठी |
| `""" ... """` | Multi-line comment/docstring | मोठा वर्णनात्मक मजकूर |
| `=` | Value assignment | variable ला मूल्य देण्यासाठी |
| `type(x)` | data type तपासणे | `int/str/float` पडताळणी |
| `int(x)` | पूर्णांकात रूपांतर | `input()` मधील संख्या वापरायला |
| `float(x)` | दशांशात रूपांतर | टक्केवारी/मापनांसाठी |
| `str(x)` | string मध्ये रूपांतर | मजकूर जोडण्यासाठी |
| `+ - * / // % **` | गणितीय operators | बेरीज, भागाकार, उर्वरित, घात |
| `== != > < >= <=` | तुलना operators | अट तपासण्यासाठी |
| `and or not` | logical operators | अनेक अटी एकत्र तपासण्यासाठी |
| `if` | अट खरी असेल तर ब्लॉक चालवा | निर्णय घेणे |
| `elif` | दुसरी अट तपासा | अनेक पर्यायांसाठी |
| `else` | कोणतीही अट खरी नसल्यास | default निकाल |
| `for` | sequence वर loop | list/string/range वर पुनरावृत्ती |
| `while` | अट true असेपर्यंत loop | condition-based loop |
| `break` | loop थांबवणे | शोध पूर्ण झाल्यावर बाहेर येणे |
| `continue` | current iteration skip | काही values टाळण्यासाठी |
| `range(n)` | 0 ते n-1 क्रमांक | counting loops |
| `len(x)` | लांबी काढणे | string/list elements मोजणे |
| `x[i]` | indexing | विशिष्ट घटक घेणे |
| `x[a:b]` | slicing | उपभाग (substring/sublist) घेणे |
| `list.append(v)` | list शेवटी मूल्य जोडणे | dynamic data store |
| `list.pop()` | list मधून शेवटचा घटक काढणे | remove operation |
| `tuple()` | immutable collection | बदल न होणारी डेटा रचना |
| `set()` | unique values collection | duplicate काढण्यासाठी |
| `dict[key] = value` | key-value mapping | विद्यार्थी-गुण नोंदणी |
| `def fn():` | function तयार करणे | पुनर्वापरयोग्य कोड |
| `return` | function मधून value देणे | निकाल परत पाठवणे |
| `open(file, mode)` | file उघडणे | वाचणे/लिहिणे |
| `with open(...) as f:` | safe file handling | auto close file |
| `try ... except` | error हाताळणी | program crash टाळणे |
| `class` | object चा साचा | OOP पायाभूत रचना |
| `self` | object चा संदर्भ | class attributes वापरणे |
| `import module` | बाह्य module वापरणे | `math`, `random` इ. |

---

## 5) Module-wise तपशील + Hands-on Labs

## Module 1: Python ची सुरुवात
### शिकण्याची उद्दिष्टे
- Python program कसा चालतो ते समजणे
- `print()`, `input()` आणि comments वापरणे

### Syntax अर्थ व उपयोग
1. `print("नमस्कार")`  
   - अर्थ: मजकूर स्क्रीनवर दाखवतो  
   - उपयोग: user ला संदेश/निकाल दाखवण्यासाठी  
2. `name = input("नाव टाका: ")`  
   - अर्थ: user कडून value घेते  
   - उपयोग: interactive program तयार करणे  
3. `# हा comment आहे`  
   - अर्थ: Python या ओळीला चालवत नाही  
   - उपयोग: कोडचे स्पष्टीकरण लिहिणे  

### Lab 1: माझी ओळख कार्यक्रम
**Task:** नाव, इयत्ता आणि शाळेचे नाव घेऊन स्क्रीनवर छापणे.

```python
name = input("तुमचे नाव टाका: ")
std = input("इयत्ता टाका: ")
school = input("शाळेचे नाव टाका: ")

print("विद्यार्थ्याची माहिती")
print("नाव:", name)
print("इयत्ता:", std)
print("शाळा:", school)
```

### Lab 1 शब्दार्थ
- **Interpreter**: Python कोड ओळीनुसार चालवणारे साधन  
- **Statement**: कोडमधील एक सूचना  
- **String**: अक्षरे/मजकूर (`"abc"`)  
- **Prompt**: `input()` मध्ये दिसणारा प्रश्न  

---

## Module 2: Variables आणि Data Types
### Syntax अर्थ व उपयोग
1. `age = 16` -> variable मध्ये value साठवणे  
2. `type(age)` -> data type तपासणे  
3. `marks = float(input("गुण: "))` -> string ते float रूपांतर  

### Lab 2: साधी गुणपत्रिका
```python
name = input("विद्यार्थ्याचे नाव: ")
m1 = int(input("गणित गुण: "))
m2 = int(input("विज्ञान गुण: "))
m3 = int(input("इंग्रजी गुण: "))

total = m1 + m2 + m3
avg = total / 3

print("नाव:", name)
print("एकूण गुण:", total)
print("सरासरी:", avg)
```

### Lab 2 शब्दार्थ
- **Variable**: value साठवण्याची नाव असलेली जागा  
- **Data Type**: value चा प्रकार (`int`, `float`, `str`, `bool`)  
- **Type Conversion**: एक प्रकार दुसऱ्यात बदलणे  
- **Average**: सरासरी (`एकूण / विषयांची संख्या`)  

---

## Module 3: Operators
### Syntax अर्थ व उपयोग
- Arithmetic: `+ - * / // % **`
- Comparison: `== != > < >= <=`
- Logical: `and or not`

### Lab 3: Calculator
```python
a = float(input("पहिली संख्या: "))
b = float(input("दुसरी संख्या: "))

print("बेरीज:", a + b)
print("वजाबाकी:", a - b)
print("गुणाकार:", a * b)
print("भागाकार:", a / b)
print("उर्वरित (mod):", a % b)
```

### Lab 3 शब्दार्थ
- **Operand**: operator च्या दोन्ही बाजूची values  
- **Operator**: गणित/तुलना करणारे चिन्ह  
- **Modulo (`%`)**: भागाकारानंतर उरलेली बाकी  
- **Floor Division (`//`)**: दशांश वगळून भागाकार  

---

## Module 4: Decision Making (`if-elif-else`)
### Syntax अर्थ व उपयोग
```python
if condition:
    ...
elif another_condition:
    ...
else:
    ...
```
- अर्थ: अटींनुसार वेगळा कोड चालतो  
- उपयोग: Grade, Eligibility, Menu program

### Lab 4: Grade शोधा
```python
marks = int(input("गुण टाका: "))

if marks >= 75:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 35:
    print("Grade C")
else:
    print("नापास")
```

### Lab 4 शब्दार्थ
- **Condition**: true/false देणारी अट  
- **Branching**: अटीवरून वेगळा मार्ग निवडणे  
- **Block**: indent केलेल्या ओळींचा समूह  
- **Indentation**: Python मध्ये space ने block दर्शवणे  

---

## Module 5: Loops
### Syntax अर्थ व उपयोग
1. `for i in range(1, 6):` -> 1 ते 5 पुनरावृत्ती  
2. `while x <= 10:` -> अट true असेपर्यंत चालू  
3. `break`, `continue` -> loop control

### Lab 5: पाढा (Table Generator)
```python
n = int(input("कोणता पाढा हवा? "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)
```

### Lab 5 शब्दार्थ
- **Iteration**: loop मधील प्रत्येक फेरी  
- **Counter**: मोजणी करणारा variable (`i`)  
- **Range**: क्रम तयार करणारे function  
- **Loop Control**: `break/continue` ने loop चे वर्तन बदलणे  

---

## Module 6: Strings
### Syntax अर्थ व उपयोग
- `text[0]` -> पहिला अक्षर  
- `text[0:3]` -> substring  
- `text.lower()`, `text.upper()`, `text.replace()` -> text process

### Lab 6: मजकूर विश्लेषण
```python
text = input("एक वाक्य टाका: ")

print("लांबी:", len(text))
print("मोठ्या अक्षरात:", text.upper())
print("लहान अक्षरात:", text.lower())
print("पहिली 5 अक्षरे:", text[:5])
```

### Lab 6 शब्दार्थ
- **Index**: स्थान क्रमांक (0 पासून सुरू)  
- **Slice**: सलग भाग काढणे  
- **Method**: object वर चालणारे function  
- **Immutable**: थेट बदल न होणारी रचना (string)  

---

## Module 7: Data Structures
### 7.1 List
- Syntax: `marks = [78, 88, 91]`
- उपयोग: बदलणारी (mutable) values ची यादी

### 7.2 Tuple
- Syntax: `point = (10, 20)`
- उपयोग: न बदलणारी values

### 7.3 Set
- Syntax: `cities = {"Pune", "Nashik", "Pune"}`
- उपयोग: unique elements

### 7.4 Dictionary
- Syntax: `student = {"name": "Asha", "marks": 92}`
- उपयोग: key-value data

### Lab 7: विद्यार्थी नोंदणी
```python
student = {}
student["name"] = input("नाव: ")
student["roll"] = int(input("रोल नंबर: "))
student["marks"] = int(input("गुण: "))

print("विद्यार्थी माहिती:", student)
```

### Lab 7 शब्दार्थ
- **Mutable**: बदलता येणारे (list, dict, set)  
- **Immutable**: बदलता न येणारे (tuple, string)  
- **Key-Value Pair**: शब्दकोशातील नोंद (`key: value`)  
- **Unique**: पुनरावृत्ती नसलेली मूल्ये  

---

## Module 8: Functions
### Syntax अर्थ व उपयोग
```python
def function_name(parameters):
    # code
    return value
```
- अर्थ: पुनर्वापरयोग्य code block
- उपयोग: मोठा program छोटे भागात विभागणे

### Lab 8: टक्केवारी function
```python
def percentage(total, out_of):
    return (total / out_of) * 100

total = int(input("एकूण गुण: "))
out_of = int(input("पूर्ण गुण: "))

per = percentage(total, out_of)
print("टक्केवारी:", per)
```

### Lab 8 शब्दार्थ
- **Function**: नाव दिलेला code block  
- **Parameter**: function define करताना घेतलेले input नाव  
- **Argument**: function call करताना दिलेली वास्तविक value  
- **Return**: function मधून बाहेर जाणारा निकाल  

---

## Module 9: File Handling
### Syntax अर्थ व उपयोग
- `open("file.txt", "w")` -> लिहिणे
- `open("file.txt", "r")` -> वाचणे
- `with open(...) as f:` -> सुरक्षित पद्धत

### Lab 9: उपस्थिती फाईल
```python
name = input("विद्यार्थ्याचे नाव: ")
status = input("Present/Absent: ")

with open("attendance.txt", "a", encoding="utf-8") as f:
    f.write(name + " - " + status + "\n")

print("नोंद यशस्वी.")
```

### Lab 9 शब्दार्थ
- **File Mode**: `r/w/a` (read/write/append)  
- **Append**: जुना मजकूर न पुसता शेवटी नवा मजकूर जोडणे  
- **Encoding**: अक्षरांचे binary रूप (`utf-8`)  
- **Resource**: file सारखी बाह्य गोष्ट  

---

## Module 10: Exception Handling
### Syntax अर्थ व उपयोग
```python
try:
    ...
except:
    ...
finally:
    ...
```
- अर्थ: error आले तरी program नियंत्रणात ठेवणे
- उपयोग: division by zero, invalid input हाताळणे

### Lab 10: सुरक्षित भागाकार
```python
try:
    a = int(input("संख्या 1: "))
    b = int(input("संख्या 2: "))
    print("भागाकार:", a / b)
except ValueError:
    print("कृपया वैध पूर्णांक टाका.")
except ZeroDivisionError:
    print("0 ने भागाकार करता येत नाही.")
finally:
    print("प्रक्रिया पूर्ण.")
```

### Lab 10 शब्दार्थ
- **Exception**: रनटाइम दरम्यान आलेली त्रुटी  
- **Runtime Error**: program चालू असताना आलेली चूक  
- **ValueError**: चुकीचा प्रकारचा input  
- **ZeroDivisionError**: 0 ने भागाकार केल्याची त्रुटी  

---

## Module 11: OOP ची ओळख
### Syntax अर्थ व उपयोग
```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
```
- अर्थ: `class` हा object चा blueprint
- उपयोग: संबंधित data + behavior एकत्र ठेवणे

### Lab 11: Student Class
```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show(self):
        print("नाव:", self.name)
        print("गुण:", self.marks)

s1 = Student("Rutuja", 87)
s1.show()
```

### Lab 11 शब्दार्थ
- **Class**: साचा (blueprint)  
- **Object**: class पासून तयार instance  
- **Attribute**: object मधील data (`name`, `marks`)  
- **Method**: class मध्ये लिहिलेले function  

---

## Module 12: Modules आणि Revision
### Syntax अर्थ व उपयोग
- `import math` -> math module वापरणे
- `from random import randint` -> विशिष्ट function import

### Lab 12: Random Quiz Number
```python
from random import randint

num = randint(1, 10)
guess = int(input("1 ते 10 मधून अंदाज लावा: "))

if guess == num:
    print("बरोबर!")
else:
    print("चुकीचे. योग्य संख्या:", num)
```

### Lab 12 शब्दार्थ
- **Module**: Python code चे वेगळे फाईल-पॅकेज  
- **Import**: बाह्य code program मध्ये आणणे  
- **Library**: अनेक modules चा संग्रह  

---

## 6) Project-based Practicals (Hands-on)

## Project 1: विद्यार्थी गुणपत्रिका व्यवस्थापन
### उद्देश
विद्यार्थ्याचे नाव, 5 विषयांचे गुण घेऊन एकूण, सरासरी, टक्केवारी आणि grade दाखवणे.

### Step-by-step Lab
1. `input()` ने नाव आणि गुण घ्या  
2. `list` मध्ये गुण साठवा  
3. `sum()` ने total काढा  
4. function ने percentage काढा  
5. `if-elif-else` ने grade द्या  
6. `attendance_report.txt` मध्ये result लिहा  

### Project 1 शब्दार्थ
- **Validation**: input योग्य आहे का ते तपासणे  
- **Business Logic**: निकाल काढण्याचे नियम  
- **Reusable Function**: वारंवार वापरता येणारे function  

---

## Project 2: शाळेचे ग्रंथालय व्यवस्थापन (Mini LMS)
### उद्देश
पुस्तकांची यादी ठेवणे, पुस्तक issue/return करणे, उपलब्धता तपासणे.

### Step-by-step Lab
1. Dictionary मध्ये पुस्तक:प्रती संख्या ठेवा  
2. Menu program तयार करा (`while True`)  
3. Issue केल्यावर count कमी करा  
4. Return केल्यावर count वाढवा  
5. सर्व पुस्तके file मध्ये save करा  

### Project 2 शब्दार्थ
- **Menu-driven Program**: पर्याय निवडून चालणारा program  
- **State**: program ची वर्तमान स्थिती (उपलब्ध पुस्तके)  
- **Persistence**: data file मध्ये टिकवून ठेवणे  

---

## Project 3: कुटुंब खर्च ट्रॅकर
### उद्देश
दैनंदिन खर्च category नुसार नोंदवणे व महिन्याचा अहवाल तयार करणे.

### Step-by-step Lab
1. Category (`Food`, `Travel`, `Study`) आणि amount input घ्या  
2. Dictionary/List मध्ये data जमा करा  
3. loop वापरून category-wise total काढा  
4. सर्वात जास्त खर्च कोणत्या category मध्ये झाला ते शोधा  
5. रिपोर्ट CSV किंवा TXT मध्ये save करा  

### Project 3 शब्दार्थ
- **Category**: खर्चाचा प्रकार  
- **Aggregation**: समान प्रकारचा डेटा एकत्र करून total काढणे  
- **Report**: विश्लेषणानंतरचा सुसंगत निकाल  

---

## 7) मूल्यांकन पद्धती (Assessment)
- 30%: Concept quiz  
- 40%: Hands-on labs  
- 30%: Final project presentation

### सुचवलेली Rubric
1. Syntax योग्य वापर  
2. Logic अचूकता  
3. Code readability (नावे, spacing, comments)  
4. Input validation  
5. Output clarity

---

## 8) विद्यार्थ्यांसाठी सराव संच
1. दिलेल्या संख्येचा factorial काढा  
2. palindrome string तपासा  
3. list मधील सर्वात मोठी संख्या शोधा  
4. dictionary मधून highest marks विद्यार्थी शोधा  
5. CSV वाचून subject-wise average काढा  

---

## 9) शिक्षकांसाठी अंमलबजावणी टिप्स
- प्रत्येक module नंतर 15 मिनिटांची mini lab घ्या  
- syntax notes + practical notebook दोन्ही ठेवा  
- pair programming करून peer learning वाढवा  
- कमजोर विद्यार्थ्यांसाठी template code द्या  
- प्रत्येक आठवड्याला एक छोटा debugging test घ्या  

---

## 10) अंतिम पुनरावलोकन (One-page Summary)
- Input-Process-Output हा कोणत्याही program चा पाया आहे  
- Data Type योग्य निवडल्यास logic errors कमी होतात  
- Condition + Loop + Function = बहुतेक school-level programs  
- File handling मुळे data जतन होतो  
- Exception handling मुळे program robust होतो  
- Project work मुळे खऱ्या समस्येवर coding लागू करता येते  

---

## 11) पुढील पायरी
हा कोर्स पूर्ण झाल्यावर विद्यार्थी खालील विषय सहज शिकू शकतात:
- CSV आणि Pandas basics  
- Matplotlib वापरून graphs  
- Web basics (Flask ची ओळख)  
- Python वापरून simple automation

