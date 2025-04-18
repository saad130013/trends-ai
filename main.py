import streamlit as st
from trend_fetcher import get_trending_searches
from ai_analyzer import analyze_trends

st.set_page_config(page_title="محلل الترندات", layout="wide")
st.title("📈 محلل الترندات بالذكاء الاصطناعي - بدون اتصال خارجي")

country = st.selectbox("اختر الدولة", ["SA", "US", "CN"])
language = st.selectbox("اختر اللغة", ["العربية", "الإنجليزية"])
run = st.button("جلب وتحليل الترندات")

if run:
    st.info("جاري جلب وتحليل الترندات...")
    trends = get_trending_searches(country)
    if not trends:
        st.error("لم يتم العثور على ترندات.")
    else:
        analysis = analyze_trends(trends, language)
        for i, item in enumerate(analysis):
            st.subheader(f"{i+1}. {item['keyword']}")
            st.markdown(f"**تحليل:** {item['insight']}")