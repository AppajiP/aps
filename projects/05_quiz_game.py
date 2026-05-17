"""
========================================================
प्रोजेक्ट ५ — प्रश्नमंजुषा (Quiz Game)
========================================================

उद्दिष्ट:
   महाराष्ट्र राज्य, सामान्य ज्ञान आणि पायथन
   यांविषयी मराठी प्रश्नमंजुषा.

वापरलेल्या संकल्पना:
   - lists, dictionaries
   - random module
   - functions
   - if-else
   - loops
   - score tracking
   - timer (optional)
"""

import random

PRASHN_PEDHI = [
    {
        "prashn": "महाराष्ट्राची राजधानी कोणती?",
        "paryay": ["पुणे", "मुंबई", "नागपूर", "नाशिक"],
        "uttar": 2,
    },
    {
        "prashn": "छत्रपती शिवाजी महाराजांचा जन्म कोणत्या वर्षी झाला?",
        "paryay": ["१६२७", "१६३०", "१६३५", "१६४२"],
        "uttar": 2,
    },
    {
        "prashn": "महाराष्ट्र राज्य कोणत्या तारखेला स्थापन झाले?",
        "paryay": ["१५ ऑगस्ट १९४७", "२६ जानेवारी १९५०", "१ मे १९६०", "१४ नोव्हेंबर १९४८"],
        "uttar": 3,
    },
    {
        "prashn": "भारताचे राष्ट्रीय फूल कोणते?",
        "paryay": ["गुलाब", "कमळ", "मोगरा", "सूर्यफूल"],
        "uttar": 2,
    },
    {
        "prashn": "पायथन प्रोग्रामिंग भाषा कुणी तयार केली?",
        "paryay": ["डेनिस रिची", "गुइडो व्हॅन रॉसम", "जेम्स गोस्लिंग", "ब्रॅंडन आइच"],
        "uttar": 2,
    },
    {
        "prashn": "पायथनमध्ये टीप कोणत्या चिन्हाने सुरू होते?",
        "paryay": ["//", "#", "/*", "--"],
        "uttar": 2,
    },
    {
        "prashn": "खालीलपैकी कोणता डेटा प्रकार mutable आहे?",
        "paryay": ["tuple", "string", "int", "list"],
        "uttar": 4,
    },
    {
        "prashn": "१ ते १० मधील सर्व संख्यांची बेरीज किती?",
        "paryay": ["४५", "५०", "५५", "६०"],
        "uttar": 3,
    },
    {
        "prashn": "len('पायथन') ची किंमत किती?",
        "paryay": ["५", "६", "४", "७"],
        "uttar": 1,
    },
    {
        "prashn": "महाराष्ट्राचे राज्यगीत कोणते?",
        "paryay": ["वंदे मातरम्", "जय जय महाराष्ट्र माझा", "ऐ मेरे वतन के लोगो", "सारे जहाँ से अच्छा"],
        "uttar": 2,
    },
]


def ek_prashn_vichara(k, p):
    print(f"\n{k}. {p['prashn']}")
    for i, par in enumerate(p['paryay'], 1):
        print(f"   {i}. {par}")
    while True:
        try:
            u = int(input("तुमचे उत्तर (१-४): "))
            if 1 <= u <= 4:
                return u == p['uttar']
            print("१ ते ४ मध्ये टाइप करा")
        except ValueError:
            print("कृपया फक्त संख्या टाइप करा")


def khel(prashn_kiti=5):
    nivad = random.sample(PRASHN_PEDHI, min(prashn_kiti, len(PRASHN_PEDHI)))
    barobar = 0
    chukich = []

    print("\n" + "=" * 50)
    print(f"   प्रश्नमंजुषा सुरू! एकूण प्रश्न: {len(nivad)}")
    print("=" * 50)

    for i, p in enumerate(nivad, 1):
        if ek_prashn_vichara(i, p):
            print("✅ बरोबर!")
            barobar += 1
        else:
            print(f"❌ चुकीचे. योग्य उत्तर: {p['paryay'][p['uttar'] - 1]}")
            chukich.append(p)

    nikal_dakhva(barobar, len(nivad), chukich)


def nikal_dakhva(barobar, ekun, chukich):
    tak = (barobar / ekun) * 100
    print("\n" + "=" * 50)
    print("            निकाल")
    print("=" * 50)
    print(f"  बरोबर       : {barobar}/{ekun}")
    print(f"  टक्केवारी    : {tak:.1f}%")

    if tak == 100:
        rating = "🏆 अद्भुत! परिपूर्ण गुण!"
    elif tak >= 80:
        rating = "🌟 खूप छान!"
    elif tak >= 60:
        rating = "👍 चांगले!"
    elif tak >= 40:
        rating = "🙂 सरासरी"
    else:
        rating = "📚 अधिक अभ्यास हवा"

    print(f"  रेटिंग      : {rating}")
    print("=" * 50)

    if chukich:
        print("\nपुनरावलोकनासाठी चुकलेले प्रश्न:")
        for p in chukich:
            print(f"  • {p['prashn']}")
            print(f"    योग्य उत्तर: {p['paryay'][p['uttar'] - 1]}")


def main():
    print("===== मराठी प्रश्नमंजुषा =====")
    while True:
        try:
            n = int(input(f"\nकिती प्रश्न खेळायचे? (१-{len(PRASHN_PEDHI)}): "))
            if 1 <= n <= len(PRASHN_PEDHI):
                break
        except ValueError:
            pass
        print("कृपया योग्य संख्या टाइप करा")

    khel(n)

    punha = input("\nपुन्हा खेळायचे? (हो/नाही): ").strip().lower()
    if punha in ("हो", "ho", "y", "yes"):
        main()
    else:
        print("खेळ संपला. धन्यवाद!")


if __name__ == "__main__":
    main()


"""
========================================================
स्पष्टीकरण:
========================================================

PRASHN_PEDHI:
   - list of dictionaries
   - प्रत्येक dict मध्ये: prashn, paryay (list), uttar (index)
   - uttar 1 पासून (वापरकर्त्याच्या सोयीसाठी)

random.sample(list, n):
   - n वेगवेगळे यादृच्छिक — पुनरावृत्ती नाही.
   - shuffle पेक्षा वेगळे.

enumerate(list, start=1):
   - index व item एकत्र, 1 पासून.

return u == p['uttar']:
   - direct boolean return.

list of चुकलेले:
   - शेवटी पुनरावलोकनासाठी ठेवले.

विस्तार सूचना:
   १. श्रेणीनुसार प्रश्न (इतिहास, विज्ञान, गणित).
   २. कठीणता स्तर.
   ३. timer — प्रत्येक प्रश्नाला १० सेकंद.
   ४. high score फाइलमध्ये.
   ५. नवीन प्रश्न जोडायचे menu.
"""
