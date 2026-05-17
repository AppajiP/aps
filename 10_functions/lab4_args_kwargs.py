"""
लॅब ४ — *args आणि **kwargs
============================
"""

def berij(*sankhya):
    print("मिळालेले:", sankhya)
    return sum(sankhya)

print("berij(1, 2):", berij(1, 2))
print("berij(1, 2, 3, 4, 5):", berij(1, 2, 3, 4, 5))


def vidyarthi(**mahiti):
    print("---")
    for k, v in mahiti.items():
        print(f"{k}: {v}")

vidyarthi(naav="राम", vay=15)
vidyarthi(naav="सीता", vay=14, gaav="पुणे", varg="९वी")


def mishra(naav, *guna, **etar):
    print(f"\nनाव: {naav}")
    print(f"गुण: {guna}")
    print(f"एकूण: {sum(guna)}")
    print(f"इतर: {etar}")

mishra("अर्जुन", 85, 92, 78, 90, varg="१०वी", shala="ज्ञानदीप")


"""
========================================================
स्पष्टीकरण:
========================================================

*args:
   * म्हणजे "कितीही". args ला tuple मिळते.
   def f(*x):  -> x = (1, 2, 3) जर f(1,2,3) कॉल केले

**kwargs:
   ** म्हणजे "कितीही keyword". kwargs ला dict मिळते.
   def f(**d): -> d = {"naav": "राम", "vay": 15}

नावे args / kwargs ही फक्त परंपरा आहेत.
   *masale  आणि  **mahiti  असेही चालते.

क्रम:
   def f(positional, *args, default=x, **kwargs):
   १. साधे positional
   २. *args
   ३. default arguments
   ४. **kwargs
"""
