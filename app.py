import streamlit as st
import pandas as pd
import time
import pandas as pd
import datetime



st.title("인공지능 모델 만들기")

if 'name' not in st.session_state:
    st.session_state['name'] = ""
if 'data' not in st.session_state:
    st.session_state['data'] = pd.DataFrame()


st.write("인공지능 모델은 주어진 데이터를 학습하여 결과를 예측합니다. 먼저 이 프로젝트에서 사용할 이름을 입력해주세요.")

name = st.text_input("name")

if name:
    st.session_state["name"] = name



if st.button("페이지 이동하기") and st.session_state["name"] != "":
    st.switch_page("pages/1파일업로드.py")


