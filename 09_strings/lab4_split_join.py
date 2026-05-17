"""
लॅब ४ — split() व join()
==========================
"""

vakya = "मला पायथन प्रोग्रामिंग आवडते"
shabdh = vakya.split()
print("शब्द:", shabdh)
print("एकूण शब्द:", len(shabdh))

csv = "राम,सीता,लक्ष्मण,गणेश"
naave = csv.split(",")
print("\nनावे:", naave)

bahu_olit = """ओळ १
ओळ २
ओळ ३"""
oli = bahu_olit.split("\n")
print("\nओळी:", oli)

phale = ["आंबा", "केळी", "सफरचंद"]
print("\nजोडणी:")
print(", ".join(phale))
print(" -> ".join(phale))
print("".join(phale))

ulta_vakya = " ".join(vakya.split()[::-1])
print("\nउलटे वाक्य:", ulta_vakya)


"""
========================================================
स्पष्टीकरण:
========================================================

split(sep)   ->  string ला sep च्या ठिकाणी तोडून list बनवते.
                 sep न दिल्यास whitespace (space, tab, newline) वर तोडते.

   "a,b,c".split(",")  -> ["a", "b", "c"]
   "a b c".split()     -> ["a", "b", "c"]

join(list)   ->  list च्या वस्तू एकत्र करून string बनवते.
                 string च्या मध्ये येते.

   ",".join(["a","b","c"])  -> "a,b,c"
   "".join(["a","b","c"])   -> "abc"

split() व join() हे एकमेकांचे उलट आहेत.

[::-1]       ->  list/string उलट करते.

म्हणून:
   "x y z" -> split -> ["x","y","z"] -> reverse -> ["z","y","x"]
   -> join -> "z y x"
"""
