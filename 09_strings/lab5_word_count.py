"""
लॅब ५ — शब्द व अक्षर मोजणी
============================
"""

vakya = "मला पायथन आवडते मला कोडिंग आवडते"

shabd_yadi = vakya.split()
print(f"एकूण शब्द: {len(shabd_yadi)}")

akshare = 0
for c in vakya:
    if c != " ":
        akshare += 1
print(f"एकूण अक्षरे (space सोडून): {akshare}")

ganana = {}
for s in shabd_yadi:
    ganana[s] = ganana.get(s, 0) + 1

print("\nप्रत्येक शब्द किती वेळा:")
for s, k in ganana.items():
    print(f"  {s:15} -> {k}")

ulta = vakya[::-1]
print(f"\nउलटे वाक्य: {ulta}")

vakya_simple = "level"
if vakya_simple == vakya_simple[::-1]:
    print(f"\n'{vakya_simple}' हा palindrome आहे")
else:
    print(f"\n'{vakya_simple}' हा palindrome नाही")


"""
========================================================
स्पष्टीकरण:
========================================================

len(vakya.split())    ->  शब्दांची संख्या

अक्षर मोजणी:
   प्रत्येक character वर लूप
   जर space नसेल तर counter वाढव

dictionary वापरून मोजणी:
   ganana.get(key, 0)  ->  key नसेल तर 0
   + 1 करून परत साठव

palindrome:
   string उलटी केली तरी सारखीच असेल तर palindrome.
   उदा: "level", "madam", "नमन"

   s == s[::-1]  ->  True तर palindrome
"""
