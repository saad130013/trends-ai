def analyze_trends(trends, language="العربية"):
    results = []
    for trend in trends:
        insight = f"هذا الترند قد يشير إلى توجه حديث في السوق." if language == "العربية" else "This trend may indicate a new direction in the market."
        results.append({"keyword": trend, "insight": insight})
    return results
