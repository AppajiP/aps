"""
========================================================
प्रोजेक्ट २ — विद्यार्थी निकाल व्यवस्थापन
========================================================

उद्दिष्ट:
   महाराष्ट्र बोर्डाच्या नियमानुसार विद्यार्थ्यांचे गुण
   घेणे, सरासरी काढणे, श्रेणी ठरवणे आणि निकाल छापणे.

वापरलेल्या संकल्पना:
   - functions
   - lists, dictionaries
   - loops
   - if-elif-else
   - input/output
   - f-strings
   - try-except
"""

VISHAY = ["मराठी", "हिंदी", "इंग्रजी", "गणित", "विज्ञान", "समाजशास्त्र"]
PASS_MARKS = 35
MAX_MARKS = 100


def guna_ghya(naav):
    print(f"\n--- {naav} चे गुण ---")
    guna = {}
    for v in VISHAY:
        while True:
            try:
                g = float(input(f"{v} (०-{MAX_MARKS}): "))
                if 0 <= g <= MAX_MARKS:
                    guna[v] = g
                    break
                print(f"० ते {MAX_MARKS} मध्ये असावे")
            except ValueError:
                print("कृपया योग्य संख्या टाइप करा")
    return guna


def shreni_thharva(sarasari, kahi_nirbeg):
    if kahi_nirbeg:
        return "नापास"
    if sarasari >= 75:
        return "विशेष प्रावीण्य"
    if sarasari >= 60:
        return "प्रथम श्रेणी"
    if sarasari >= 45:
        return "द्वितीय श्रेणी"
    return "उत्तीर्ण"


def nikal_chhapne(vidyarthi):
    naav = vidyarthi["naav"]
    guna = vidyarthi["guna"]
    ekun = sum(guna.values())
    sarasari = ekun / len(guna)
    kahi_nirbeg = any(g < PASS_MARKS for g in guna.values())
    shreni = shreni_thharva(sarasari, kahi_nirbeg)

    print("\n" + "=" * 50)
    print(f"   निकाल — {naav}")
    print("=" * 50)
    for v, g in guna.items():
        sthiti = "उत्तीर्ण" if g >= PASS_MARKS else "अनुत्तीर्ण"
        print(f"  {v:15} : {g:5.1f}  ({sthiti})")
    print("-" * 50)
    print(f"  एकूण गुण      : {ekun}/{MAX_MARKS * len(VISHAY)}")
    print(f"  सरासरी %      : {sarasari:.2f}%")
    print(f"  निकाल         : {shreni}")
    print("=" * 50)


def main():
    print("===== विद्यार्थी निकाल प्रणाली =====")
    n = int(input("किती विद्यार्थी? "))
    vidyarthi_yadi = []

    for i in range(n):
        naav = input(f"\nविद्यार्थी {i + 1} चे नाव: ").strip()
        guna = guna_ghya(naav)
        vidyarthi_yadi.append({"naav": naav, "guna": guna})

    for v in vidyarthi_yadi:
        nikal_chhapne(v)

    print("\n===== वर्गाची माहिती =====")
    sarvanchi_avg = [sum(v["guna"].values()) / len(v["guna"]) for v in vidyarthi_yadi]
    print(f"वर्गाची सरासरी: {sum(sarvanchi_avg) / len(sarvanchi_avg):.2f}%")
    print(f"सर्वोच्च: {max(sarvanchi_avg):.2f}%")
    print(f"सर्वात कमी: {min(sarvanchi_avg):.2f}%")


if __name__ == "__main__":
    main()


"""
========================================================
प्रत्येक भागाचे स्पष्टीकरण:
========================================================

VISHAY (constant list):
   - capital letters परंपरा — हे चल बदलू नये.

guna_ghya(naav):
   - प्रत्येक विषयासाठी गुण विचारतो.
   - while True ने योग्य input मिळेपर्यंत विचारतो.
   - try-except ने string ला crash टाळतो.

any(g < PASS_MARKS for g in guna.values()):
   - generator expression.
   - कोणताही एक विषय < 35 असेल तर True.

shreni_thharva():
   - early return pattern — स्वच्छ कोड.

list comprehension:
   [sum(v["guna"].values()) / len(v["guna"]) for v in vidyarthi_yadi]
   प्रत्येक विद्यार्थ्याची सरासरी एका list मध्ये.

विस्तार सूचना:
   १. निकाल फाइलमध्ये (txt/csv) साठवा.
   २. विद्यार्थ्यांची क्रमवारी (rank) काढा.
   ३. विषयानुसार topper शोधा.
   ४. PDF report तयार करा (reportlab library).
"""
