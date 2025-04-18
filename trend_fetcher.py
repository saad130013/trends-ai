from pytrends.request import TrendReq

def get_trending_searches(country_code):
    pytrends = TrendReq(hl='en-US', tz=360)
    try:
        df = pytrends.trending_searches(pn=country_code.lower())
        return df[0].tolist()
    except Exception as e:
        print(f"خطأ في جلب الترندات: {e}")
        return []