"""
लॅब ५ — Scope (Local आणि Global)
==================================
"""

x = 100

def show():
    print("function मधून x =", x)

show()
print("बाहेरून x =", x)


def local_test():
    y = 50
    print("function मधले y =", y)

local_test()


def update_global():
    global x
    x = 999

update_global()
print("\nupdate नंतर x =", x)


def chukich():
    z = 5

chukich()
try:
    print(z)
except NameError as e:
    print("\nNameError:", e)


"""
========================================================
स्पष्टीकरण:
========================================================

Local Scope:
   function च्या आत तयार झालेले चल फक्त त्या function मध्ये.
   बाहेरून त्यांना वापरता येत नाही.

Global Scope:
   function च्या बाहेरचे चल — सर्वत्र वाचता येतात.
   पण बदलायला 'global' keyword लागतो.

   def f():
       global x       ->  x global आहे हे सांगायला
       x = 5

global keyword का?
   जर तुम्ही फक्त x = 5 लिहिले तर पायथन नवीन local x बनवते,
   global x बदलत नाही!

LEGB नियम (पायथन कुठे शोधते):
   L - Local
   E - Enclosing (बाहेरचे function)
   G - Global
   B - Built-in
"""
