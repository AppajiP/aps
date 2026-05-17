"""
लॅब ३ — if-elif-else (अनेक अटी)
==================================
"""

guna = 78

if guna >= 90:
    shreni = "A"
elif guna >= 75:
    shreni = "B"
elif guna >= 60:
    shreni = "C"
elif guna >= 35:
    shreni = "D"
else:
    shreni = "नापास"

print(f"गुण: {guna} | श्रेणी: {shreni}")


varsh = 2024
if varsh % 400 == 0:
    print(varsh, "leap year आहे")
elif varsh % 100 == 0:
    print(varsh, "leap year नाही")
elif varsh % 4 == 0:
    print(varsh, "leap year आहे")
else:
    print(varsh, "leap year नाही")


"""
========================================================
स्पष्टीकरण:
========================================================

elif        ->  "else if" चे लघुरूप.
                आधीच्या if/elif खोटे असतील तरच तपासले जाते.

क्रम महत्त्वाचा:
   पायथन वरून खाली जातो. जिथे पहिली अट खरी मिळते,
   तिथेच थांबून तो block चालवतो. बाकीचे elif/else वगळते.

म्हणून अटी क्रमाने योग्य लिहाव्यात.

leap year चे नियम:
   - ४ ने भागले जात असेल -> leap
   - पण १०० ने भागले जात असेल -> leap नाही
   - पण ४०० ने भागले जात असेल -> leap (अपवाद)
"""
