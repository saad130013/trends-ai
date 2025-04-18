import streamlit as st
from trend_fetcher import get_trending_searches
from ai_analyzer import analyze_trends

st.set_page_config(page_title="📊 محلل الترندات", layout="wide")
st.title("📊 محلل الترندات باستخدام TF-IDF المحلي (بدون موديلات خارجية)")

COUNTRY_MAP = {
    "sa": "🇸🇦 السعودية",
    "us": "🇺🇸 أمريكا",
    "cn": "🇨🇳 الصين"
}

country = st.selectbox("اختر الدولة", list(COUNTRY_MAP.keys()), format_func=lambda x: COUNTRY_MAP[x])
language = st.radio("لغة التحليل", ["العربية", "الإنجليزية"], horizontal=True)

if st.button("بدء التحليل 🚀"):
    with st.spinner("جاري تحميل الترندات وتحليلها..."):
        trends = get_trending_searches(country)
    if not trends:
        st.warning("لم يتم العثور على ترندات.")
    else:
        st.success(f"تم العثور على {len(trends)} ترندات.")
        results = analyze_trends(trends, language)
        for idx, item in enumerate(results, 1):
            with st.expander(f"الترند رقم {idx}: {item['keyword']}", expanded=True):
                st.markdown("### التحليل:")
                st.info(item["insight"])