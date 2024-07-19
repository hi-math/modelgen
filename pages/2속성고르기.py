import streamlit as st
import pandas as pd
import time
import pandas as pd
import datetime

st.title("속성 선택하기")

st.write("모델 학습에 사용될 속성만 남겨봅시다.")

if 'data' not in st.session_state:
    st.session_state['data'] = pd.DataFrame()
    
if 'data_test' not in st.session_state:
    st.session_state['data_test'] = pd.DataFrame()

if 'raw' not in st.session_state:
        st.write("raw")
        st.session_state['raw'] = st.session_state['data'].copy()

def reload():
    progress_text = "데이터가 변환됩니다. 잠시만 기다리세요."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.02)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()
    st.rerun()


if 'data' in st.session_state:
    st.session_state['data']
    data = st.session_state['data'].copy()
    data_test = st.session_state['data_test'].copy()
    del_column = st.selectbox("삭제할 속성을 선택하세요", list(data.columns.tolist()), index=None)    
    if st.button("삭제하기") and del_column:
        data.drop(del_column, axis=1, inplace=True)
        data_test.drop(del_column, axis=1, inplace=True)
        st.success('완료되었습니다!', icon="✅")
        st.session_state['data']=data.copy()
        st.session_state['data_test']=data_test.copy()
        reload()
        
if st.button("페이지 이동하기"):
    st.switch_page("pages/3전처리하기1.py")