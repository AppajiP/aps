"""
लॅब १ — Function ची मूळ रचना
=============================
"""

def namaskar():
    print("नमस्कार जग!")

namaskar()
namaskar()


def swagat(naav):
    print(f"स्वागत आहे, {naav}!")

swagat("राम")
swagat("सीता")


def vidyarthi_mahiti(naav, vay, varg):
    print(f"नाव: {naav}")
    print(f"वय: {vay}")
    print(f"वर्ग: {varg}")
    print("-" * 20)

vidyarthi_mahiti("अर्जुन", 15, "१०वी")
vidyarthi_mahiti("सीता", 14, "९वी")


"""
========================================================
स्पष्टीकरण:
========================================================

def           ->  function तयार करायचा keyword
namaskar      ->  function चे नाव
( )           ->  parameters साठी जागा (काही नसले तरी)
:             ->  block सुरू

namaskar()    ->  function 'call' करणे. हे लिहिल्याशिवाय
                  function चालत नाही!

naav          ->  parameter — function ला लागणारी माहिती
"राम"          ->  argument — call करताना दिलेली प्रत्यक्ष किंमत

multiple parameters:
   तीन parameters -> तीन arguments (क्रमाने)
"""
