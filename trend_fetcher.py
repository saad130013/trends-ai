from pytrends.request import TrendReq
from pytrends.exceptions import ResponseError

def get_trending_searches(country_code):
    """جلب الترندات مع معالجة شاملة للأخطاء"""
    try:
        pytrends = TrendReq(
            hl='en-US', 
            tz=360,
            timeout=(10, 30),  # زيادة مهلة الاتصال
            retries=2  # إعادة المحاولة في حالة الفشل
        )
        df = pytrends.trending_searches(pn=country_code.lower())
        return df[0].tolist() if not df.empty else []
    except ResponseError as e:
        print(f"خطأ في استجابة جوجل: {e}")
        return []
    except Exception as e:
        print(f"خطأ غير متوقع: {e}")
        return []
