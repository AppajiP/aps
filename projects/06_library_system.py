"""
========================================================
प्रोजेक्ट ६ — ग्रंथालय व्यवस्थापन (OOP आधारित)
========================================================

उद्दिष्ट:
   पुस्तके, सदस्य, उधार-परत हे सर्व व्यवस्थापित करा.
   पूर्णपणे OOP वापरून.

वापरलेल्या संकल्पना:
   - classes, objects
   - __init__, methods
   - inheritance
   - encapsulation (private attributes)
   - exception handling (custom exceptions)
   - file storage (JSON)
   - data structures
"""

import json
import os
from datetime import datetime, timedelta


class LibraryError(Exception):
    pass


class BookNotAvailableError(LibraryError):
    pass


class MemberNotFoundError(LibraryError):
    pass


class Pustak:
    def __init__(self, kramank, naav, lekhak, varsh):
        self.kramank = kramank
        self.naav = naav
        self.lekhak = lekhak
        self.varsh = varsh
        self.uplabdh = True
        self.udhar_la = None

    def to_dict(self):
        return {
            "kramank": self.kramank,
            "naav": self.naav,
            "lekhak": self.lekhak,
            "varsh": self.varsh,
            "uplabdh": self.uplabdh,
            "udhar_la": self.udhar_la,
        }

    @classmethod
    def from_dict(cls, d):
        p = cls(d["kramank"], d["naav"], d["lekhak"], d["varsh"])
        p.uplabdh = d.get("uplabdh", True)
        p.udhar_la = d.get("udhar_la")
        return p

    def __str__(self):
        sthiti = "उपलब्ध" if self.uplabdh else f"({self.udhar_la} कडे)"
        return f"[{self.kramank}] '{self.naav}' - {self.lekhak} ({self.varsh}) {sthiti}"


class Sadasya:
    def __init__(self, kramank, naav, varg):
        self.kramank = kramank
        self.naav = naav
        self.varg = varg
        self.udhar_pustake = []

    def to_dict(self):
        return {
            "kramank": self.kramank,
            "naav": self.naav,
            "varg": self.varg,
            "udhar_pustake": self.udhar_pustake,
        }

    @classmethod
    def from_dict(cls, d):
        s = cls(d["kramank"], d["naav"], d["varg"])
        s.udhar_pustake = d.get("udhar_pustake", [])
        return s

    def __str__(self):
        return f"[{self.kramank}] {self.naav} ({self.varg}) - {len(self.udhar_pustake)} पुस्तके"


class Granthalay:
    DATA_FAIL = "library.json"

    def __init__(self, naav):
        self.naav = naav
        self.pustake = {}
        self.sadasya = {}
        self.load()

    def pustak_jodne(self, naav, lekhak, varsh):
        k = max(self.pustake.keys(), default=100) + 1
        p = Pustak(k, naav, lekhak, varsh)
        self.pustake[k] = p
        self.save()
        return p

    def sadasya_jodne(self, naav, varg):
        k = max(self.sadasya.keys(), default=1000) + 1
        s = Sadasya(k, naav, varg)
        self.sadasya[k] = s
        self.save()
        return s

    def udhar(self, sad_k, pust_k):
        if sad_k not in self.sadasya:
            raise MemberNotFoundError(f"सदस्य {sad_k} सापडला नाही")
        if pust_k not in self.pustake:
            raise BookNotAvailableError(f"पुस्तक {pust_k} सापडले नाही")

        p = self.pustake[pust_k]
        if not p.uplabdh:
            raise BookNotAvailableError(f"'{p.naav}' आधीच उधार दिले आहे")

        s = self.sadasya[sad_k]
        if len(s.udhar_pustake) >= 3:
            raise LibraryError("एका वेळी फक्त 3 पुस्तके मिळतात")

        p.uplabdh = False
        p.udhar_la = s.naav
        s.udhar_pustake.append(pust_k)
        self.save()
        return p

    def parat(self, sad_k, pust_k):
        if sad_k not in self.sadasya:
            raise MemberNotFoundError(f"सदस्य {sad_k} सापडला नाही")
        if pust_k not in self.pustake:
            raise BookNotAvailableError(f"पुस्तक {pust_k} सापडले नाही")

        p = self.pustake[pust_k]
        s = self.sadasya[sad_k]
        if pust_k not in s.udhar_pustake:
            raise LibraryError("हे पुस्तक या सदस्याकडे नाही")

        p.uplabdh = True
        p.udhar_la = None
        s.udhar_pustake.remove(pust_k)
        self.save()

    def pustake_dakhva(self, फक्त_उपलब्ध=False):
        for p in self.pustake.values():
            if फक्त_उपलब्ध and not p.uplabdh:
                continue
            print(" *", p)

    def sadasya_dakhva(self):
        for s in self.sadasya.values():
            print(" *", s)

    def shodh(self, shabd):
        shabd = shabd.lower()
        result = []
        for p in self.pustake.values():
            if shabd in p.naav.lower() or shabd in p.lekhak.lower():
                result.append(p)
        return result

    def save(self):
        data = {
            "naav": self.naav,
            "pustake": [p.to_dict() for p in self.pustake.values()],
            "sadasya": [s.to_dict() for s in self.sadasya.values()],
        }
        with open(self.DATA_FAIL, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load(self):
        if not os.path.exists(self.DATA_FAIL):
            return
        try:
            with open(self.DATA_FAIL, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.pustake = {p["kramank"]: Pustak.from_dict(p) for p in data.get("pustake", [])}
            self.sadasya = {s["kramank"]: Sadasya.from_dict(s) for s in data.get("sadasya", [])}
        except (json.JSONDecodeError, OSError):
            pass


def menu():
    g = Granthalay("शाळेचे ग्रंथालय")

    if not g.pustake:
        print("नमुना डेटा जोडत आहे...")
        g.pustak_jodne("श्यामची आई", "साने गुरुजी", 1935)
        g.pustak_jodne("ययाती", "वि. स. खांडेकर", 1959)
        g.pustak_jodne("मृत्युंजय", "शिवाजी सावंत", 1967)
        g.pustak_jodne("कोसला", "भालचंद्र नेमाडे", 1963)
        g.sadasya_jodne("अर्जुन पाटील", "१०वी")
        g.sadasya_jodne("सीता जोशी", "९वी")

    while True:
        print("\n===== शाळेचे ग्रंथालय =====")
        print("१. सर्व पुस्तके")
        print("२. फक्त उपलब्ध पुस्तके")
        print("३. सदस्य यादी")
        print("४. नवीन पुस्तक")
        print("५. नवीन सदस्य")
        print("६. पुस्तक उधार")
        print("७. पुस्तक परत")
        print("८. पुस्तक शोधा")
        print("९. बाहेर पडा")
        n = input("निवड: ").strip()

        try:
            if n in ("1", "१"):
                g.pustake_dakhva()
            elif n in ("2", "२"):
                g.pustake_dakhva(फक्त_उपलब्ध=True)
            elif n in ("3", "३"):
                g.sadasya_dakhva()
            elif n in ("4", "४"):
                nav = input("पुस्तक नाव: ")
                lek = input("लेखक: ")
                var = int(input("वर्ष: "))
                p = g.pustak_jodne(nav, lek, var)
                print("जोडले:", p)
            elif n in ("5", "५"):
                nav = input("सदस्य नाव: ")
                vrg = input("वर्ग: ")
                s = g.sadasya_jodne(nav, vrg)
                print("जोडले:", s)
            elif n in ("6", "६"):
                sk = int(input("सदस्य क्रमांक: "))
                pk = int(input("पुस्तक क्रमांक: "))
                p = g.udhar(sk, pk)
                print(f"'{p.naav}' उधार दिले")
            elif n in ("7", "७"):
                sk = int(input("सदस्य क्रमांक: "))
                pk = int(input("पुस्तक क्रमांक: "))
                g.parat(sk, pk)
                print("परत स्वीकारले")
            elif n in ("8", "८"):
                sh = input("शोधायचा शब्द: ")
                r = g.shodh(sh)
                print(f"सापडले: {len(r)}")
                for p in r:
                    print(" *", p)
            elif n in ("9", "९"):
                print("बाय!")
                break
            else:
                print("चुकीची निवड")
        except LibraryError as e:
            print("चूक:", e)
        except ValueError:
            print("कृपया योग्य संख्या टाइप करा")


if __name__ == "__main__":
    menu()


"""
========================================================
स्पष्टीकरण:
========================================================

तीन classes:
   - Pustak    : पुस्तकाची माहिती
   - Sadasya   : सदस्याची माहिती
   - Granthalay: एकूण व्यवस्था (दोघांना सांभाळते)

custom exceptions:
   class LibraryError(Exception)         <- base
       BookNotAvailableError             <- inherit
       MemberNotFoundError               <- inherit

   - try-except मध्ये specific पकडता येतात.
   - inheritance ने पदानुक्रम (hierarchy).

@classmethod from_dict(cls, d):
   - dict मधून object तयार करायला.
   - JSON वरून लोड करायला आवश्यक.
   - cls = class स्वतःच — Pustak.from_dict() म्हणजे cls = Pustak.

to_dict() व from_dict():
   - serialization pattern.
   - object <-> dict <-> JSON

dictionary वापर:
   self.pustake = {kramank: Pustak_object}
   क्रमांकावरून थेट access — खूप वेगवान.

max(keys, default=N):
   - रिकामी असल्यास default वापरते.
   - पहिल्या पुस्तकाला क्रमांक 101 पासून.

विस्तार सूचना:
   १. उधार तारीख व परत मुदत (15 दिवस).
   २. fine system (दंड).
   ३. पुस्तकाची श्रेणी (शास्त्र, कथा, चरित्र).
   ४. user authentication.
   ५. SQLite database ने upgrade.
   ६. Web interface (Flask).
"""
