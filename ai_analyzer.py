from keybert import KeyBERT
from sentence_transformers import SentenceTransformer

# تحميل النموذج اللغوي يدويًا
sentence_model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
kw_model = KeyBERT(model=sentence_model)

def analyze_trends(trends, language):
    analysis = []
    for trend in trends:
        keywords = kw_model.extract_keywords(trend, top_n=2)
        insight = f"أهم الكلمات المفتاحية: {', '.join([k[0] for k in keywords])}" if language == "العربية" else f"Top keywords: {', '.join([k[0] for k in keywords])}"
        analysis.append({
            "keyword": trend,
            "insight": insight
        })
    return analysis
