"""
लॅब ४ — raise (स्वतःचा error टाकणे)
======================================
"""

def vay_set(vay):
    if vay < 0:
        raise ValueError("वय ऋण असू शकत नाही")
    if vay > 150:
        raise ValueError("वय 150 पेक्षा जास्त असू शकत नाही")
    print(f"वय {vay} स्वीकारले")


try:
    vay_set(25)
    vay_set(-5)
except ValueError as e:
    print("चूक:", e)


def guna_check(guna):
    if not isinstance(guna, (int, float)):
        raise TypeError("गुण ही संख्या असावी")
    if guna < 0 or guna > 100:
        raise ValueError("गुण 0 ते 100 च्या मधे असावेत")
    return guna >= 35


try:
    print("\n45:", guna_check(45))
    print("105:", guna_check(105))
except (ValueError, TypeError) as e:
    print("चूक:", e)


"""
========================================================
स्पष्टीकरण:
========================================================

raise ExceptionType("संदेश")
   - error स्वतःहून तयार करते.
   - प्रोग्रामला सांगते "हे चुकीचे आहे, थांब".

कधी वापरावे?
   १. input validation (वय, गुण योग्य आहेत का)
   २. business rules (पैसे ऋण नकोत)
   ३. नियम तोडल्यास

raise vs print:
   print  ->  फक्त संदेश, प्रोग्राम चालू राहतो
   raise  ->  exception, हाताळला नाही तर बंद

builtin exceptions:
   ValueError    -> चुकीची किंमत
   TypeError     -> चुकीचा प्रकार
   KeyError      -> चुकीची key
   IndexError    -> चुकीचा index
   RuntimeError  -> सामान्य चूक

isinstance(x, type):
   - x त्या type चा आहे का?
   - isinstance(5, int)  ->  True
   - isinstance(5, (int, float))  ->  True
"""
