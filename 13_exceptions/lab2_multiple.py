"""
लॅब २ — अनेक Exceptions
=========================
"""

def safe_divide():
    try:
        a = int(input("पहिली संख्या: "))
        b = int(input("दुसरी संख्या: "))
        print("निकाल:", a / b)
    except ValueError:
        print("चूक: फक्त संख्या टाइप करा")
    except ZeroDivisionError:
        print("चूक: शून्याने भाग शक्य नाही")
    except Exception as e:
        print("अज्ञात चूक:", e)


def safe_access():
    yadi = [10, 20, 30]
    sabd = {"naav": "राम"}
    try:
        i = int(input("Index: "))
        k = input("Key: ")
        print(yadi[i], sabd[k])
    except (IndexError, KeyError) as e:
        print(f"चूक: {type(e).__name__}: {e}")


print("--- 1. safe_divide ---")
print("(टीप: 0 टाइप करा -> error, abc टाइप करा -> error)")

print("\n--- 2. safe_access ---")


"""
========================================================
स्पष्टीकरण:
========================================================

अनेक except blocks:
   पहिला match होणारा चालतो.
   म्हणून specific exceptions आधी, generic नंतर.

except (A, B):
   एकाच block ने अनेक exceptions पकडता येतात.

except Exception as e:
   - Exception हा सगळ्यांचा parent class.
   - 'as e' म्हणजे error object e मध्ये साठव.
   - e मध्ये error चा संदेश असतो.

type(e).__name__:
   - error चे नाव string मध्ये देतो.
   - उदा. 'ValueError', 'KeyError'

best practice:
   - शक्य तितके specific exception पकडा
   - except: (कोणताही) टाळा
"""
