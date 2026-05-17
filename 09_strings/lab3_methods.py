"""
लॅब ३ — String methods
=========================
"""

s = "Hello Python Programming"

print("original  :", s)
print("upper()   :", s.upper())
print("lower()   :", s.lower())
print("title()   :", s.title())
print("swapcase():", s.swapcase())

s2 = "   पायथन   "
print(f"strip()   : '{s2.strip()}'")
print(f"lstrip()  : '{s2.lstrip()}'")
print(f"rstrip()  : '{s2.rstrip()}'")

s3 = "मला पायथन आवडते. पायथन सोपे आहे."
print("\nreplace पायथन -> Python:", s3.replace("पायथन", "Python"))
print("count 'पायथन':", s3.count("पायथन"))
print("find 'आवडते':", s3.find("आवडते"))
print("find 'जावा' :", s3.find("जावा"))

email = "ram@gmail.com"
print("\n@ने सुरू?:", email.startswith("@"))
print("ram ने सुरू?:", email.startswith("ram"))
print(".com ने संपते?:", email.endswith(".com"))

print("\n--- तपासणी ---")
print("'123'.isdigit():", "123".isdigit())
print("'abc'.isalpha():", "abc".isalpha())
print("'abc123'.isalnum():", "abc123".isalnum())


"""
========================================================
स्पष्टीकरण:
========================================================

string methods नवीन string परत करतात.
मूळ string बदलत नाही (कारण immutable).

   s = "abc"
   s.upper()    ->  "ABC" परत
   s            ->  अजूनही "abc"!

म्हणून:
   s = s.upper()  ->  s ला नवीन किंमत दिली

method गट:
   केस बदलणे: upper, lower, title, capitalize, swapcase
   साफसफाई: strip, lstrip, rstrip
   शोध:     find, index, count, startswith, endswith
   बदल:     replace
   तपासणी:   isdigit, isalpha, isalnum, isspace
"""
