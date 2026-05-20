# रोबोटिक्स अभ्यासक्रम (मराठी) — Azone Academy

महाराष्ट्र राज्य शिक्षण मंडळातील विद्यार्थ्यांसाठी मराठी भाषेत संपूर्ण रोबोटिक्स अभ्यासक्रम.

**अभ्यासक्रम रचना:** Appaji Patil  
**तयार केले:** Azone Academy साठी

## सुरुवात कशी करावी?

1. हा संपूर्ण `robotics_course/` फोल्डर डाउनलोड करा.
2. `index.html` कोणत्याही आधुनिक ब्राउझरमध्ये (Chrome / Firefox / Edge / Safari) उघडा.
3. — हे सर्व आहे! कोणतीही स्थापना (installation) किंवा सर्व्हर लागत नाही.

```bash
# ऐच्छिक — local server मध्ये चालवायचे असेल तर:
cd robotics_course
python3 -m http.server 8000
# ब्राउझरमध्ये http://localhost:8000 उघडा
```

## संरचना

```
robotics_course/
├── index.html              मुख्यपृष्ठ
├── syllabus.html           अभ्यासक्रम
├── about.html              आमच्याबद्दल / लेखक
├── glossary.html           शब्दकोश
├── components.html         घटक कॅटलॉग
├── chapters/
│   ├── chapter01.html …    १६ धडे — ७ पाया + ९ प्रकल्प
│   └── chapter16.html
├── projects/index.html     ९ प्रकल्प गॅलरी
├── css/styles.css
└── js/
    ├── script.js           theme/progress/quiz
    ├── includes.js         shared navbar + footer
    └── labs.js             प्रत्येक प्रकल्पाचे सिम्युलेटर
```

## अभ्यासक्रमाचा आराखडा

**पाया (Foundation) — ७ धडे**

1. रोबोटिक्सची ओळख
2. रोबोचे प्रकार व उपयोग
3. विद्युत व ओहमचा नियम
4. घटक व ब्रेडबोर्ड (रंगकोडासह)
5. सेन्सर्सची ओळख (IR, LDR, Touch, Tilt, Ultrasonic, PIR)
6. अ‍ॅक्ट्युएटर्स (DC motor, Servo, Relay, L293D, PWM)
7. Arduino — पहिले पाऊल

**९ प्रकल्प (विषय क्र. १६ – २४)**

| # | प्रकल्प |
|---|--------|
| १६ | Tilt sensor using obstacle sensor |
| १७ | Light Controlled Machine |
| १८ | Cliff Avoiding Robot |
| १९ | Line Follower Robot |
| २० | Touch Me Not Robot |
| २१ | Advanced Automation — Smart Street Light |
| २२ | Light Seeking Robot |
| २३ | Remote Controlled Lamp & Buzzer |
| २४ | Remote Controlled Fan |

## वैशिष्ट्ये

- 🌗 गडद/उजळ थीम (theme toggle)
- 📊 तुमची प्रगती ब्राउझरमध्ये जतन (localStorage)
- 🧪 प्रत्येक प्रकल्पात स्वतंत्र ब्राउझर-आधारित सिम्युलेटर
- 📝 प्रत्येक धड्याच्या शेवटी quiz व स्वाध्याय
- 📱 मोबाइल-अनुकूल (responsive) डिझाईन
- 🎨 सुंदर मराठी फॉन्ट्स (Noto Sans Devanagari)

## लायसन्स

© Azone Academy. शैक्षणिक वापरासाठी मुक्त. व्यावसायिक वापरासाठी संपर्क साधा.
