"""
लॅब ३ — datetime module
==========================
"""

import datetime

aaj = datetime.date.today()
print("आजची तारीख:", aaj)

ata = datetime.datetime.now()
print("सध्याचे:", ata)
print("वर्ष:", ata.year)
print("महिना:", ata.month)
print("दिवस:", ata.day)
print("वेळ:", ata.hour, ata.minute, ata.second)

janma = datetime.date(2010, 5, 15)
print("\nजन्मतारीख:", janma)

farak = aaj - janma
print("वय (दिवसांत):", farak.days)
print("वय (वर्षांत):", farak.days // 365)

format1 = ata.strftime("%d-%m-%Y")
format2 = ata.strftime("%d %B %Y, %I:%M %p")
print(f"\nformat 1: {format1}")
print(f"format 2: {format2}")


"""
========================================================
स्पष्टीकरण:
========================================================

datetime.date.today()    ->  आजची तारीख (no time)
datetime.datetime.now()  ->  आत्ताची तारीख + वेळ

date(year, month, day)   ->  विशिष्ट तारीख तयार

तारीख वजाबाकी (date1 - date2):
   timedelta object देते
   .days  ->  एकूण दिवस
   .seconds, etc.

strftime("format") - तारखेला छान string मध्ये:
   %d   ->  दिवस (01-31)
   %m   ->  महिना (01-12)
   %Y   ->  वर्ष (4 अंकी)
   %y   ->  वर्ष (2 अंकी)
   %B   ->  महिन्याचे नाव (January)
   %A   ->  वाराचे नाव (Monday)
   %H   ->  तास (24)
   %I   ->  तास (12)
   %M   ->  मिनिट
   %S   ->  सेकंद
   %p   ->  AM/PM
"""
