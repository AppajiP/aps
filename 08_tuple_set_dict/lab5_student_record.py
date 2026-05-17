"""
लॅब ५ — विद्यार्थ्यांच्या नोंदी (Student Records)
==================================================
"""

vidyarthi_yadi = [
    {"naav": "अर्जुन", "vay": 15, "guna": {"मराठी": 85, "गणित": 92}},
    {"naav": "सीता",   "vay": 14, "guna": {"मराठी": 90, "गणित": 88}},
    {"naav": "गणेश",   "vay": 15, "guna": {"मराठी": 78, "गणित": 95}},
]

print("===== विद्यार्थी अहवाल =====\n")
for v in vidyarthi_yadi:
    naav = v["naav"]
    vay = v["vay"]
    guna = v["guna"]
    ekun = sum(guna.values())
    sarasari = ekun / len(guna)
    print(f"नाव: {naav}")
    print(f"वय: {vay}")
    print(f"गुण: {guna}")
    print(f"सरासरी: {sarasari:.2f}")
    print("-" * 30)


vakya = "मला पायथन शिकायला आवडते मला"
shabdh = vakya.split()
ganana = {}
for s in shabdh:
    if s in ganana:
        ganana[s] += 1
    else:
        ganana[s] = 1

print("\nशब्दांची मोजणी:")
for shabd, kiti in ganana.items():
    print(f"  {shabd:15} -> {kiti}")


"""
========================================================
स्पष्टीकरण:
========================================================

list of dicts:
   प्रत्येक विद्यार्थी = एक dictionary
   सर्व विद्यार्थी एकत्र = list

   [
     { ... },
     { ... }
   ]

nested access:
   v["guna"]["मराठी"]
   -> आधी v चे guna घे, मग त्यातले मराठी

शब्द मोजणी पॅटर्न:
   १. वाक्य split करा -> list of words
   २. प्रत्येक शब्द dict मध्ये नसेल तर 1, असेल तर +=1
   
   सोपी पद्धत:
       ganana[s] = ganana.get(s, 0) + 1
"""
