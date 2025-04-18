from sklearn.feature_extraction.text import TfidfVectorizer

def analyze_trends(trends, language="العربية"):
    vectorizer = TfidfVectorizer(stop_words="english" if language == "الإنجليزية" else None)
    try:
        X = vectorizer.fit_transform(trends)
        terms = vectorizer.get_feature_names_out()
        scores = X.sum(axis=0).A1
        word_scores = dict(zip(terms, scores))
        sorted_keywords = sorted(word_scores.items(), key=lambda x: x[1], reverse=True)

        result = []
        for term in trends:
            top_words = [word for word in sorted_keywords if word[0].lower() in term.lower()]
            top_text = ', '.join([w[0] for w in top_words]) or "لا توجد كلمات مفتاحية واضحة"
            insight = f"أهم الكلمات: {top_text}" if language == "العربية" else f"Top keywords: {top_text}"
            result.append({"keyword": term, "insight": insight})
        return result
    except Exception as e:
        return [{"keyword": term, "insight": f"❌ خطأ في التحليل: {str(e)}"} for term in trends]