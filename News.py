# News_API documentation: https://newsapi.org/docs/endpoints/everything
# required packages:
#    1) streamlit (pip install streamlit)
#    2) streamlit_lottie (pip install streamlit_lottie)
#    3) requests 

import streamlit as st
from streamlit_lottie import st_lottie
import requests
from PIL import Image
import random
from datetime import date

today = date.today()
date_now = today.strftime("%Y-%m-%d")

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="News", page_icon=":newspaper:") # , layout="wide"

lang = st.selectbox("language:", ("Arabic", "English"))

# ---- HEADER SECTION ----
with st.container():
    if lang == "Arabic":
       st.title("صفحة الأخبار :sparkles:")
       st.write("!تابع الأحداث الجارية من مختلف المنافذ الإخبارية من جميع أنحاء العالم")
    else:
       st.title("News Website :sparkles:")
       st.write("Always Stay Up-to-Date with Current Events and News from all over the world!")

col1, col2 = st.columns(2)

# ---- Top News ----
with col1:

       if lang == "Arabic":
              st.subheader("أهم الأخبار")
              l = 'ar'
              keyword = st.text_input("كلمة مفتاحية:", value="حرب")
              number = st.number_input("عدد أهم الأخبار:", step=1, value=3)
              
       else: 
              st.subheader("Top News")
              l = 'en'
              keyword = st.text_input("Keyword:", value="war")
              number = st.number_input("Number of Top News:", step=1, value=3)

       url_top = ('https://newsapi.org/v2/everything?'
              f'q={keyword}&'
              f'language={l}&'
              'sortBy=popularity&'
              'apiKey=YOUR_API_KEY')

       response = requests.get(url_top)

       for i in range(int(number)):
              articles = response.json()["articles"][i]
              title = articles["title"]
              url = articles["url"]
              description = articles["description"]

              with st.container():
                     st.write(f"[{title}]({url})")
                     st.write(f"{description}")



# ---- Customized News ----
with col2:
       if lang == "Arabic":
              st.subheader("أخبار حسب الطلب")
              keyword = st.text_input("كلمة مفتاحية:", value="تقنية")
              ar_to_en = {"أعمال تجارية": "business", "ترفيه": "entertainment", "عام": "general", "صحة": "health", "علوم": "science", "رياضة": "sports", "التقنية": "technology"}
              category = st.selectbox(":نوع المقالة", ("التقنية", "أعمال تجارية", "ترفيه", "عام", "صحة", "علوم", "رياضة"))
              category = ar_to_en[category]
              countries = {"ألمانيا": "de", "فرنسا": "fr", "روسيا": "ru", "السعودية": "sa", "مصر": "eg"}
              country = st.selectbox(":الدولة", ("مصر", "ألمانيا", "فرنسا", "روسيا", "السعودية"))
              country = countries[country]
              number = st.number_input("عدد المقالات:", step=1, value=3)
              date_from = st.date_input("مقالات منذ:", value=today)
              date_to = st.date_input("مقالات حتي:", value=today)

       else: 
              st.subheader("Customized News")
              keyword = st.text_input("Keyword:", value="tech")
              category = st.selectbox("Category:", ("technology", "business", "entertainment", "general", "health", "science", "sports"))
              countries = {"Germany": "de", "France": "fr", "Russia": "ru", "Saudi Arabia": "sa", "Egypt": "eg"}
              country = st.selectbox("Country:", ("Egypt", "Germany", "France", "Russia", "Saudi Arabia"))
              country = countries[country]
              number = st.number_input("Number of Articles:", step=1, value=3)
              date_from = st.date_input("Articles from:")
              date_to = st.date_input("Articles to:")


       url_articles = ('https://newsapi.org/v2/top-headlines?'
              f'q={keyword}&'
              f'category={category}&'
              f'language={l}&'
              f'from={date_from}&'
              f'to={date_to}&'
              #f'country={country}&'
              'sortBy=relevancy&'
              'apiKey=YOUR_API_KEY')

       response = requests.get(url_articles)

       for i in range(number):
              articles = response.json()["articles"][i]
              title = articles["title"]
              url = articles["url"]
              description = articles["description"]

              with st.container():
                     st.write(f"[{title}]({url})")
                     st.write(f"{description}")

