import streamlit as st
from trend_fetcher import get_trending_searches
from ai_analyzer import analyze_trends

st.set_page_config(page_title="محلل الترندات", layout="wide")
st.title("📈 محلل الترندات باستخدام الذكاء الصناعي المحلي")

st.markdown("هذا المشروع يعرض الترندات من Google Trends ويحللها باستخدام نموذج محلي بدون أي اتصال خارجي.")

country = st.selectbox("اختر الدولة", ["sa", "us", "cn"], index=0, format_func=lambda x: {"sa": "🇸🇦 السعودية", "us": "🇺🇸 أمريكا", "cn": "🇨🇳 الصين"}[x])
language = st.radio("اختر اللغة", ["العربية", "الإنجليزية"])
run = st.button("جلب وتحليل الترندات")

if run:
    with st.spinner("جاري تحميل الترندات وتحليلها..."):
        trends = get_trending_searches(country)
        if not trends:
            st.warning("لم يتم العثور على ترندات.")
        else:
            results = analyze_trends(trends, language)
            for item in results:
                st.subheader(f"🔹 {item['keyword']}")
                st.markdown(item["insight"])