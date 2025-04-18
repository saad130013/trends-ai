import streamlit as st
from trend_fetcher import get_trending_searches
from ai_analyzer import analyze_trends

st.set_page_config(page_title="محلل الترندات", layout="wide")

st.title("📊 محلل الترندات - نسخة مبنية من الصفر")

st.markdown("اختر الدولة واللغة، ثم اضغط زر التحليل لعرض الترندات وتحليلها.")

country = st.selectbox("الدولة", ["sa", "us", "cn"], format_func=lambda x: {"sa": "🇸🇦 السعودية", "us": "🇺🇸 أمريكا", "cn": "🇨🇳 الصين"}[x])
language = st.radio("اللغة", ["العربية", "الإنجليزية"])

if st.button("تحليل الترندات"):
    st.info("جاري جلب الترندات...")
    trends = get_trending_searches(country)
    if not trends:
        st.warning("لا توجد ترندات متاحة حالياً.")
    else:
        results = analyze_trends(trends, language)
        for i, res in enumerate(results, 1):
            st.subheader(f"{i}. {res['keyword']}")
            st.write(res["insight"])