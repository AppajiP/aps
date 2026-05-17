"""
लॅब ३ — Default व Keyword Arguments
=====================================
"""

def namaskar(naav="मित्र"):
    print(f"नमस्कार, {naav}!")

namaskar()
namaskar("राम")


def vidyarthi(naav, vay=15, varg="१०वी"):
    print(f"{naav}, वय {vay}, वर्ग {varg}")

vidyarthi("अर्जुन")
vidyarthi("सीता", 14)
vidyarthi("गणेश", 16, "११वी")


print("\n--- Keyword arguments ---")
vidyarthi(naav="मीरा", varg="९वी", vay=13)


def kshetraphal(lambai, rundi=1, unchi=1):
    return lambai * rundi * unchi

print("\nlambai=5 तर:", kshetraphal(5))
print("lambai=5, rundi=4:", kshetraphal(5, 4))
print("सर्व:", kshetraphal(5, 4, 3))
print("keyword:", kshetraphal(lambai=10, unchi=2))


"""
========================================================
स्पष्टीकरण:
========================================================

default argument:
   def f(x=10):   ->  x न दिल्यास 10 घेते.

नियम:
   default parameters नेहमी शेवटी असावेत.
   def f(a, b=5)   ->  ✅
   def f(a=5, b)   ->  ❌ SyntaxError

keyword arguments:
   f(b=10, a=5)   ->  क्रमाची चिंता नाही.
   वाचायला सुटसुटीत.

मिश्र वापर:
   f(5, b=10)     ->  ✅ (positional आधी, मग keyword)
   f(b=10, 5)     ->  ❌
"""
