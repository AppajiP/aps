"""
लॅब ५ — स्वतःचा Exception class
=================================
"""

class MarksOutOfRangeError(Exception):
    """गुण 0 ते 100 च्या बाहेर असल्यास."""
    pass


class NegativeAgeError(Exception):
    pass


def vay_check(vay):
    if vay < 0:
        raise NegativeAgeError(f"वय ऋण ({vay}) असू शकत नाही")
    return True


def guna_check(guna):
    if guna < 0 or guna > 100:
        raise MarksOutOfRangeError(f"गुण {guna} योग्य नाही (0-100)")
    return True


try:
    vay_check(-3)
except NegativeAgeError as e:
    print("NegativeAgeError:", e)


try:
    guna_check(120)
except MarksOutOfRangeError as e:
    print("MarksOutOfRangeError:", e)


print("\nवय 20:", vay_check(20))
print("गुण 85:", guna_check(85))


"""
========================================================
स्पष्टीकरण:
========================================================

class MyError(Exception):
    pass

   - नवीन exception बनवायला.
   - Exception हा parent class.
   - pass म्हणजे "रिकामे" body.

का बनवावे?
   - तुमच्या प्रोग्रामसाठी अधिक स्पष्ट नावे.
   - try-except मध्ये specific पकडता येतात.
   - तुमची library वापरणाऱ्यांना समजायला सोपे.

नियम:
   - नाव शेवटी 'Error' लावा (परंपरा).
   - Exception पासून inherit करा.
   - अधिक माहिती हवी असल्यास __init__ override करा.

class का?
   - Exception एक class आहे.
   - तीच रचना तुम्ही पुढच्या प्रकरणात (OOP) शिकाल.
"""
