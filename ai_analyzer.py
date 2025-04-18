from keybert import KeyBERT

kw_model = KeyBERT()

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