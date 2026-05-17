"""
लॅब ३ — Dictionary ची ओळख
==========================
"""

vidyarthi = {
    "naav": "अर्जुन",
    "vay": 15,
    "varg": "१०वी",
    "shala": "ज्ञानदीप विद्यालय"
}

print("संपूर्ण:", vidyarthi)
print("नाव:", vidyarthi["naav"])
print("वय:", vidyarthi["vay"])

print("\nphone:", vidyarthi.get("phone", "उपलब्ध नाही"))

vidyarthi["gaav"] = "पुणे"
print("\ngaav जोडल्यानंतर:", vidyarthi)

vidyarthi["vay"] = 16
print("\nvay बदलल्यानंतर:", vidyarthi["vay"])

del vidyarthi["shala"]
print("\nshala काढल्यानंतर:", vidyarthi)

print("\n'naav' आहे का?:", "naav" in vidyarthi)
print("'phone' आहे का?:", "phone" in vidyarthi)


"""
========================================================
स्पष्टीकरण:
========================================================

{ key: value, ... }   ->  dictionary तयार करायला.

key       ->  नाव (बहुधा string किंवा integer)
value     ->  त्या नावाची किंमत (काहीही)

d[key]    ->  त्या key ची किंमत मिळवायला.
              key नसेल तर KeyError येतो.

d.get(key, default)   ->  सुरक्षित पद्धत.
                          key नसेल तर default देतो.

d[key] = x   ->  नवीन जोडायला किंवा बदलायला.

del d[key]   ->  जोडी काढून टाकायला.

key in d     ->  key आहे का तपासायला.

dictionary चे key-value:
   जणू एक खर्‍या शब्दकोशासारखे —
   शब्द (key)  ->  अर्थ (value)
"""
