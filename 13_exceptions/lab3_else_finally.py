"""
लॅब ३ — else आणि finally
==========================
"""

try:
    a = 10
    b = 5
    c = a / b
except ZeroDivisionError:
    print("शून्याने भाग")
else:
    print("निकाल:", c)
finally:
    print("---- खंड १ संपला ----")


try:
    f = open("nahi_aslele.txt", "r", encoding="utf-8")
except FileNotFoundError:
    print("फाइल सापडली नाही")
else:
    print(f.read())
    f.close()
finally:
    print("---- खंड २ संपला ----")


def safe_file_read(filename):
    f = None
    try:
        f = open(filename, "r", encoding="utf-8")
        return f.read()
    except FileNotFoundError:
        return None
    finally:
        if f:
            f.close()
            print(f"({filename} बंद केली)")

result = safe_file_read("nahi_aslele.txt")
print("निकाल:", result)


"""
========================================================
स्पष्टीकरण:
========================================================

else:
   - फक्त error न आल्यासच चालतो.
   - try block यशस्वी झाला तर.

finally:
   - नेहमी चालतो (error आला किंवा नाही).
   - return असला तरी चालतो!
   - cleanup कामांसाठी (फाइल बंद, network बंद).

म्हणून:
   try:        ->  धोक्याचा कोड
   except:     ->  error पकड
   else:       ->  सर्व ठीक झाले तर
   finally:    ->  शेवटी काय करायचे (नेहमी)

with ने finally ची गरज नाही:
   with open(...) as f: ने आपोआप close.
"""
