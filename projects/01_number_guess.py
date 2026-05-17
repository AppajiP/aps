"""
========================================================
प्रोजेक्ट १ — संख्या अंदाज खेळ (Number Guessing Game)
========================================================

उद्दिष्ट:
   संगणक १ ते १०० मधील एक गुप्त संख्या निवडतो.
   खेळाडूने ती कमीत कमी प्रयत्नांत अंदाज करायची.

वापरलेल्या संकल्पना:
   - import (random module)
   - input/output
   - type casting (int)
   - while loop
   - if-elif-else
   - try-except (ValueError साठी)
   - f-strings

कसे चालवायचे?
   python 01_number_guess.py
"""

import random


def khel_khelane():
    print("=" * 40)
    print("    संख्या अंदाज खेळ")
    print("=" * 40)
    print("मी १ ते १०० मधली एक संख्या निवडली आहे.")
    print("तुम्ही ती अंदाज करा!\n")

    gupt = random.randint(1, 100)
    prayatna = 0
    max_prayatna = 10

    while prayatna < max_prayatna:
        try:
            andaaz = int(input(f"प्रयत्न {prayatna + 1}/{max_prayatna} — तुमचा अंदाज: "))
        except ValueError:
            print("कृपया योग्य संख्या टाइप करा\n")
            continue

        prayatna += 1

        if andaaz < 1 or andaaz > 100:
            print("१ ते १०० मध्ये असावी\n")
            continue

        if andaaz == gupt:
            print(f"\n🎉 बरोबर! संख्या होती {gupt}.")
            print(f"तुम्ही {prayatna} प्रयत्नात जिंकलात!")
            return True
        elif andaaz < gupt:
            print("मोठी संख्या वापरा\n")
        else:
            print("लहान संख्या वापरा\n")

    print(f"\n😞 प्रयत्न संपले. योग्य संख्या होती: {gupt}")
    return False


def main():
    jinkle = 0
    haarle = 0
    while True:
        nikal = khel_khelane()
        if nikal:
            jinkle += 1
        else:
            haarle += 1

        punha = input("\nपुन्हा खेळायचे? (हो/नाही): ").strip().lower()
        if punha not in ("हो", "ho", "y", "yes"):
            break

    print("\n" + "=" * 40)
    print(f"  जिंकले: {jinkle} | हरले: {haarle}")
    print("=" * 40)
    print("खेळाबद्दल धन्यवाद!")


if __name__ == "__main__":
    main()


"""
========================================================
प्रत्येक भागाचे स्पष्टीकरण:
========================================================

import random:
   random.randint(1, 100) ने गुप्त संख्या तयार.

while prayatna < max_prayatna:
   जोपर्यंत प्रयत्न शिल्लक, तोपर्यंत खेळ.

try-except ValueError:
   जर वापरकर्ता "abc" टाइप करेल तर crash होऊ नये.
   continue ने त्या प्रयत्नाची गणना नाही.

if-elif-else:
   योग्य/मोठी/लहान — तीन अवस्था.

return True / False:
   main मधून जिंक/हार ची गणना करायला.

if __name__ == "__main__":
   - फाइल थेट चालवली तर main() चालते.
   - फाइल import केली तर चालत नाही.
   - व्यावसायिक Python चा standard pattern.

विस्तार सूचना:
   १. कठीणता स्तर (easy/medium/hard) — range वेगळी.
   २. timer — किती सेकंदात अंदाज?
   ३. score इतिहास फाइलमध्ये साठवा.
   ४. computer ने अंदाज करायचा — आपण उत्तर द्यायचे.
"""
