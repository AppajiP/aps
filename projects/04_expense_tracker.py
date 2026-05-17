"""
========================================================
प्रोजेक्ट ४ — खर्चाची नोंद (Expense Tracker)
========================================================

उद्दिष्ट:
   दैनंदिन खर्च नोंदवा, श्रेणीनुसार सारांश पाहा.

वापरलेल्या संकल्पना:
   - csv module
   - file handling
   - functions
   - dictionaries
   - datetime
   - sorting
   - aggregation
"""

import csv
import os
from datetime import datetime

CSV_FAIL = "expenses.csv"
HEADERS = ["तारीख", "श्रेणी", "वर्णन", "रक्कम"]
SHRENI = ["जेवण", "प्रवास", "शिक्षण", "मनोरंजन", "वस्त्र", "औषध", "इतर"]


def ensure_csv():
    if not os.path.exists(CSV_FAIL):
        with open(CSV_FAIL, "w", encoding="utf-8", newline="") as f:
            csv.writer(f).writerow(HEADERS)


def kharch_jodne():
    print("\n--- नवीन खर्च ---")
    print("श्रेण्या:", ", ".join(SHRENI))
    shreni = input("श्रेणी: ").strip()
    if shreni not in SHRENI:
        print("अमान्य श्रेणी, 'इतर' म्हणून जोडले")
        shreni = "इतर"

    varnan = input("वर्णन: ").strip()
    try:
        rakkam = float(input("रक्कम (₹): "))
    except ValueError:
        print("चुकीची रक्कम")
        return

    tarikh = datetime.now().strftime("%Y-%m-%d")

    with open(CSV_FAIL, "a", encoding="utf-8", newline="") as f:
        csv.writer(f).writerow([tarikh, shreni, varnan, rakkam])
    print(f"✅ ₹{rakkam} {shreni}मध्ये जोडले")


def sarvа_kharch():
    with open(CSV_FAIL, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        nondi = list(reader)
    return nondi


def yadi_dakhva():
    nondi = sarvа_kharch()
    if not nondi:
        print("\n(कोणताही खर्च नाही)")
        return
    print("\n" + "-" * 60)
    print(f"  {'तारीख':12} {'श्रेणी':10} {'वर्णन':20} {'रक्कम':>8}")
    print("-" * 60)
    for n in nondi:
        print(f"  {n['तारीख']:12} {n['श्रेणी']:10} {n['वर्णन']:20} ₹{float(n['रक्कम']):>7.2f}")
    ekun = sum(float(n['रक्कम']) for n in nondi)
    print("-" * 60)
    print(f"  एकूण खर्च: ₹{ekun:.2f}")


def shreni_sararнsh():
    nondi = sarvа_kharch()
    if not nondi:
        print("\n(कोणताही खर्च नाही)")
        return
    sararnsh = {}
    for n in nondi:
        s = n["श्रेणी"]
        sararnsh[s] = sararnsh.get(s, 0) + float(n["रक्कम"])

    krmavari = sorted(sararnsh.items(), key=lambda x: x[1], reverse=True)
    ekun = sum(sararnsh.values())

    print("\n--- श्रेणीनुसार खर्च ---")
    print("-" * 40)
    for s, r in krmavari:
        tak = (r / ekun) * 100
        bar = "█" * int(tak / 2)
        print(f"  {s:10} ₹{r:>8.2f}  {tak:5.1f}% {bar}")
    print("-" * 40)
    print(f"  एकूण     ₹{ekun:.2f}")


def main():
    ensure_csv()
    while True:
        print("\n===== खर्च नोंद =====")
        print("१. नवीन खर्च नोंदवा")
        print("२. सर्व खर्च पाहा")
        print("३. श्रेणीनुसार सारांश")
        print("४. बाहेर पडा")
        n = input("निवड: ").strip()

        if n in ("1", "१"):
            kharch_jodne()
        elif n in ("2", "२"):
            yadi_dakhva()
        elif n in ("3", "३"):
            shreni_sararnsh()
        elif n in ("4", "४"):
            print("बाय!")
            break
        else:
            print("चुकीची निवड")


if __name__ == "__main__":
    main()


"""
========================================================
स्पष्टीकरण:
========================================================

CSV का?
   - साधा format
   - Excel मध्ये उघडता येते
   - share करायला सोपे

csv.DictReader(f):
   - प्रत्येक row dictionary म्हणून मिळते
   - column नावे keys

sararnsh.get(s, 0) + float(n["रक्कम"]):
   - dictionary वापरून aggregation
   - key नसेल तर 0 पासून सुरू

sorted(..., key=lambda x: x[1], reverse=True):
   - किंमतीनुसार उतरत्या क्रमाने
   - x[1]  ->  tuple चा 2रा भाग (किंमत)

bar chart (text):
   - "█" * n  ->  साधा bar
   - टक्केवारी दर्शविण्यासाठी

विस्तार सूचना:
   १. महिन्यानुसार अहवाल.
   २. बजेट सेट करा — पार झाले की warning.
   ३. matplotlib ने pie chart.
   ४. व्यक्तिनुसार multi-user.
"""
