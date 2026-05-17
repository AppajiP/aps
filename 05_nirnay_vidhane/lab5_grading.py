"""
लॅब ५ — विद्यार्थ्याची श्रेणी ठरवणे
=====================================
"""

print("===== श्रेणी ठरवा =====")

marathi = float(input("मराठी गुण: "))
hindi = float(input("हिंदी गुण: "))
english = float(input("इंग्रजी गुण: "))
ganit = float(input("गणित गुण: "))
vidnyan = float(input("विज्ञान गुण: "))

ekun = marathi + hindi + english + ganit + vidnyan
sarasari = ekun / 5

print(f"\nएकूण गुण  : {ekun}/500")
print(f"सरासरी %  : {sarasari:.2f}%")

if marathi < 35 or hindi < 35 or english < 35 or ganit < 35 or vidnyan < 35:
    nikal = "नापास"
elif sarasari >= 75:
    nikal = "विशेष प्रावीण्य (Distinction)"
elif sarasari >= 60:
    nikal = "प्रथम श्रेणी"
elif sarasari >= 45:
    nikal = "द्वितीय श्रेणी"
else:
    nikal = "उत्तीर्ण"

print(f"निकाल    : {nikal}")


"""
========================================================
स्पष्टीकरण:
========================================================

float(input())   ->  वापरकर्त्याकडून दशांश संख्या घेतो.

सरासरी           ->  एकूण भागिले विषयांची संख्या.

or               ->  कोणताही एक विषय < 35 असेल तर नापास.

elif             ->  सरासरीनुसार श्रेणी.

लक्षात ठेवा:
   महाराष्ट्र बोर्ड नियम — प्रत्येक विषयात ३५ गुण आवश्यक.
"""
