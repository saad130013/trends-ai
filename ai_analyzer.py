from keybert import KeyBERT
from sklearn.feature_extraction.text import CountVectorizer

kw_model = KeyBERT()

def analyze_trends(trends, language="العربية"):
    analysis = []
    for term in trends:
        try:
            keywords = kw_model.extract_keywords(term, vectorizer=CountVectorizer(), top_n=2)
            keyword_list = ', '.join([k[0] for k in keywords])
            insight = f"أهم الكلمات المفتاحية: {keyword_list}" if language == "العربية" else f"Top keywords: {keyword_list}"
            analysis.append({"keyword": term, "insight": insight})
        except Exception as e:
            analysis.append({"keyword": term, "insight": f"❌ خطأ في التحليل: {str(e)}"})
    return analysis