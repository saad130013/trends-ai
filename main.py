import streamlit as st
from trend_fetcher import get_trending_searches
from ai_analyzer import analyze_trends

# تهيئة واجهة المستخدم
st.set_page_config(
    page_title="محلل الترندات الذكي",
    layout="wide",
    page_icon="📊"
)

st.title("📊 محلل الترندات باستخدام الذكاء الاصطناعي المحلي")
st.markdown("""
**مميزات التطبيق:**
- تحليل ترندات Google Trends في الوقت الفعلي
- دعم اللغتين العربية والإنجليزية
- يعمل بدون اتصال بالإنترنت بعد تثبيت النماذج
""")

# إعداد خيارات البلدان مع أعلامها
COUNTRY_MAP = {
    "sa": "🇸🇦 السعودية",
    "us": "🇺🇸 أمريكا",
    "cn": "🇨🇳 الصين"
}

country = st.selectbox(
    "اختر الدولة",
    options=list(COUNTRY_MAP.keys()),
    format_func=lambda x: COUNTRY_MAP[x]
)

language = st.radio(
    "لغة التحليل",
    options=["العربية", "الإنجليزية"],
    horizontal=True
)

if st.button("بدء التحليل 🚀"):
    with st.spinner("جاري البحث عن أحدث الترندات..."):
        trends = get_trending_searches(country)
        
    if not trends:
        st.warning("لم يتم العثور على ترندات لهذه المنطقة.")
    else:
        st.success(f"تم العثور على {len(trends)} ترندات")
        results = analyze_trends(trends, language)
        
        # عرض النتائج بقالب احترافي
        for idx, item in enumerate(results, 1):
            with st.expander(f"الترند رقم {idx}: {item['keyword']}", expanded=True):
                st.markdown(f"### التحليل:")
                st.info(item["insight"])