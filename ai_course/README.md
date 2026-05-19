# Azone Academy — AI अभ्यासक्रम (मराठी)

**रचना:** Appaji Patil
**लक्ष्य:** महाराष्ट्र राज्य शिक्षण मंडळ — इयत्ता ८ ते १२

ब्राउझरमध्येच चालणारा संपूर्ण कृत्रिम बुद्धिमत्ता (AI) अभ्यासक्रम — मराठी भाषेत.
प्रत्येक धड्यासोबत Python-आधारित **हँड्स-ऑन लॅब** (Pyodide) आणि शेवटी **४ अंगभूत प्रकल्प**.

## कसे चालवायचे?

कोणतीही स्थापना (installation) आवश्यक नाही.

1. हा `ai_course/` फोल्डर डाउनलोड / क्लोन करा.
2. कोणतेही साधे स्थानिक HTTP सर्व्हर चालवा (Python वापरून):

```bash
cd ai_course
python3 -m http.server 8000
```

3. ब्राउझरमध्ये उघडा: <http://localhost:8000>

> टीप: `index.html` थेट डबल-क्लिक करूनही उघडता येते, पण `file://` योजनेमध्ये काही ब्राउझर्स Pyodide ब्लॉक करतात. म्हणून स्थानिक सर्व्हर वापरणे श्रेयस्कर.

## संरचना

```
ai_course/
├── index.html              # मुख्यपृष्ठ
├── syllabus.html           # अभ्यासक्रमाचा आराखडा
├── glossary.html           # AI शब्दकोश (इंग्रजी ↔ मराठी)
├── about.html              # आझोन ॲकॅडमी व Appaji Patil बद्दल
├── chapters/
│   ├── chapter01.html  ... chapter12.html      # १२ धडे
├── projects/
│   ├── index.html
│   ├── project1_chatbot.html
│   ├── project2_sentiment.html
│   ├── project3_iris.html
│   └── project4_predict.html
├── css/styles.css
└── js/
    ├── script.js     # लॅब रन, थीम, प्रगती
    └── includes.js   # सामायिक navbar / footer
```

## अभ्यासक्रम

1. कृत्रिम बुद्धिमत्तेची ओळख
2. AI चा इतिहास व उत्क्रांती
3. AI चे प्रकार
4. AI चे दैनंदिन उपयोग
5. AI साठी Python मूलतत्त्वे
6. डेटा — AI चे इंधन
7. मशीन लर्निंगची ओळख
8. Supervised / Unsupervised / Reinforcement
9. न्यूरल नेटवर्क्स
10. नैसर्गिक भाषा प्रक्रिया (NLP)
11. संगणक दृष्टी (Computer Vision)
12. AI नैतिकता व भविष्य

## प्रकल्प

1. साधा नियमाधारित चॅटबॉट
2. भावना विश्लेषक (मराठी)
3. Iris फूल वर्गीकरण (k-NN)
4. गुण अंदाज (Linear Regression)

## तंत्रज्ञान

- शुद्ध **HTML + CSS + JavaScript** — कोणताही build step नाही.
- **Pyodide v0.26.2** ने Python थेट ब्राउझरमध्ये चालतो.
- Google Fonts — *Noto Sans Devanagari*.

© Azone Academy. सर्व हक्क राखीव.
