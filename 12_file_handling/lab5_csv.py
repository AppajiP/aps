"""
लॅब ५ — CSV फाइल हाताळणी
==========================
"""

import csv

vidyarthi = [
    ["नाव", "वय", "वर्ग", "गुण"],
    ["अर्जुन", 15, "१०वी", 85],
    ["सीता", 14, "९वी", 92],
    ["गणेश", 16, "११वी", 78],
    ["मीरा", 13, "८वी", 88],
]

with open("vidyarthi.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    for row in vidyarthi:
        writer.writerow(row)

print("CSV फाइल तयार झाली!")


print("\n--- CSV वाचणे ---")
with open("vidyarthi.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


print("\n--- DictReader वापरून ---")
with open("vidyarthi.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['नाव']:10} -> गुण: {row['गुण']}")


"""
========================================================
स्पष्टीकरण:
========================================================

CSV (Comma Separated Values):
   प्रत्येक ओळ = एक record
   प्रत्येक , = एक column

   उदा.
   नाव,वय,गुण
   राम,15,85
   सीता,14,92

csv.writer(f):
   - writer object
   - writerow(list)  ->  एक ओळ लिहितो
   - writerows(list_of_lists)  ->  अनेक ओळी

csv.reader(f):
   - reader object
   - प्रत्येक row एक list म्हणून मिळते

csv.DictReader(f):
   - प्रत्येक row dict म्हणून मिळते
   - पहिली ओळ headers मानली जाते
   - खूप सोयीस्कर

newline="":
   - csv सोबत हे लिहायला हवे, नाहीतर अनावश्यक रिकाम्या ओळी येतात.
"""
