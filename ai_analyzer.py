from keybert import KeyBERT
from sentence_transformers import SentenceTransformer
from sklearn.feature_extraction.text import CountVectorizer

# تحميل نموذج محلي متعدد اللغات (لا يحتاج اتصالًا خارجيًا بعد التثبيت الأولي)
sentence_model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
kw_model = KeyBERT(model=sentence_model)

def analyze_trends(trends, language="العربية"):
    analysis = []
    for term in trends:
        try:
            # استخدام CountVectorizer لتحسين النتائج
            keywords = kw_model.extract_keywords(
                term, 
                vectorizer=CountVectorizer(), 
                top_n=2,
                stop_words=None  # إيقاف إزالة الكلمات الشائعة للغات غير الإنجليزية
            )
            keyword_list = ', '.join([k[0] for k in keywords])
            insight = (
                f"أهم الكلمات المفتاحية: {keyword_list}" 
                if language == "العربية" 
                else f"Top keywords: {keyword_list}"
            )
            analysis.append({"keyword": term, "insight": insight})
        except Exception as e:
            analysis.append({"keyword": term, "insight": f"❌ خطأ في التحليل: {str(e)}"})
    return analysis
