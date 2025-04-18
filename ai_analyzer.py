from sklearn.feature_extraction.text import TfidfVectorizer

def analyze_trends(trends, language="العربية"):
    vectorizer = TfidfVectorizer()
    try:
        X = vectorizer.fit_transform(trends)
        terms = vectorizer.get_feature_names_out()
        scores = X.sum(axis=0).A1
        term_scores = dict(zip(terms, scores))
        sorted_terms = sorted(term_scores.items(), key=lambda x: x[1], reverse=True)

        results = []
        for trend in trends:
            top_words = [word for word, score in sorted_terms if word in trend.lower()]
            insight = f"أهم الكلمات: {', '.join(top_words)}" if language == "العربية" else f"Top keywords: {', '.join(top_words)}"
            results.append({"keyword": trend, "insight": insight})
        return results
    except Exception as e:
        return [{"keyword": trend, "insight": f"❌ Error: {str(e)}"} for trend in trends]