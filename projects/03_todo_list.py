"""
========================================================
प्रोजेक्ट ३ — टू-डू लिस्ट (फाइल आधारित)
========================================================

उद्दिष्ट:
   कामांची यादी फाइलमध्ये साठवा. प्रोग्राम बंद केला
   तरीही माहिती जात नाही.

वापरलेल्या संकल्पना:
   - file handling (with open)
   - JSON serialization
   - functions
   - dictionaries, lists
   - while loop, menu
   - exceptions
"""

import json
import os
from datetime import datetime

FAIL_NAAV = "todo_data.json"


def load_kaame():
    if not os.path.exists(FAIL_NAAV):
        return []
    try:
        with open(FAIL_NAAV, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return []


def save_kaame(kaame):
    with open(FAIL_NAAV, "w", encoding="utf-8") as f:
        json.dump(kaame, f, ensure_ascii=False, indent=2)


def kaam_jodne(kaame):
    text = input("कामाचे वर्णन: ").strip()
    if not text:
        print("रिकामे काम जोडू शकत नाही")
        return
    nava_kaam = {
        "id": len(kaame) + 1,
        "kaam": text,
        "purna": False,
        "tayar": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    kaame.append(nava_kaam)
    save_kaame(kaame)
    print(f"✅ '{text}' जोडले")


def kaame_dakhva(kaame):
    if not kaame:
        print("\n(यादी रिकामी आहे)")
        return
    print("\n" + "-" * 50)
    print(f"  {'क्र.':4} {'सिथ.':5} {'काम':25} {'तारीख':15}")
    print("-" * 50)
    for k in kaame:
        chinha = "✅" if k["purna"] else "⬜"
        print(f"  {k['id']:<4} {chinha:5} {k['kaam']:25} {k['tayar']:15}")
    print("-" * 50)
    purna = sum(1 for k in kaame if k["purna"])
    print(f"  एकूण: {len(kaame)} | पूर्ण: {purna} | बाकी: {len(kaame) - purna}")


def kaam_purna(kaame):
    try:
        kid = int(input("कोणता क्रमांक पूर्ण? "))
    except ValueError:
        print("योग्य क्रमांक टाइप करा")
        return

    for k in kaame:
        if k["id"] == kid:
            k["purna"] = True
            save_kaame(kaame)
            print(f"✅ '{k['kaam']}' पूर्ण झाले")
            return
    print("तो क्रमांक सापडला नाही")


def kaam_kadhne(kaame):
    try:
        kid = int(input("कोणता क्रमांक काढायचा? "))
    except ValueError:
        print("योग्य क्रमांक टाइप करा")
        return

    for i, k in enumerate(kaame):
        if k["id"] == kid:
            kadhle = kaame.pop(i)
            save_kaame(kaame)
            print(f"🗑️  '{kadhle['kaam']}' काढले")
            return
    print("तो क्रमांक सापडला नाही")


def main():
    kaame = load_kaame()
    while True:
        print("\n===== TODO यादी =====")
        print("१. यादी पाहा")
        print("२. नवीन काम जोडा")
        print("३. काम पूर्ण म्हणून लावा")
        print("४. काम काढून टाका")
        print("५. बाहेर पडा")
        nivad = input("तुमची निवड: ").strip()

        if nivad == "1" or nivad == "१":
            kaame_dakhva(kaame)
        elif nivad == "2" or nivad == "२":
            kaam_jodne(kaame)
        elif nivad == "3" or nivad == "३":
            kaam_purna(kaame)
        elif nivad == "4" or nivad == "४":
            kaam_kadhne(kaame)
        elif nivad == "5" or nivad == "५":
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

JSON (JavaScript Object Notation):
   - पायथन dict/list ला text मध्ये साठवायचा format.
   - माणसांना वाचण्यासारखे.
   - json.dump(data, file)   ->  साठवायला
   - json.load(file)          ->  वाचायला
   - ensure_ascii=False        ->  मराठी अक्षरे जशीच्या तशी
   - indent=2                  ->  सुंदर format

os.path.exists(file):
   - फाइल आहे का तपासायला.

datetime.now().strftime(...):
   - सध्याची तारीख string मध्ये.

dictionary चा वापर:
   प्रत्येक कामासाठी एक dict:
   { id, kaam, purna, tayar }

list of dicts:
   सर्व कामे एका list मध्ये.

menu loop:
   while True + input + if-elif
   व्यावसायिक app design pattern.

विस्तार सूचना:
   १. श्रेणी (category) जोडा — काम, घर, शाळा.
   २. priority (low/medium/high).
   ३. deadline व remind.
   ४. GUI साठी tkinter वापरा.
"""
