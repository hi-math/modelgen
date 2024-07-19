import streamlit as st
import pandas as pd
import time
import pandas as pd
import datetime

st.title("숫자가 아닌 데이터를 처리합니다.")

st.write("수치데이터가 아닌 것은 처리할 수 없습니다. 그림과 같은 방법으로 처리합니다.")

st.image(".\img\Get_Dummies.png")

if 'data' not in st.session_state:
    st.session_state['data'] = pd.DataFrame()
if 'data_test' not in st.session_state:
    st.session_state['data_test'] = pd.DataFrame()
    
data = st.session_state['data'].copy()
data_test = st.session_state['data_test'].copy()

def reload():
    progress_text = "잠시후에 데이터가 변환됩니다. 잠시만 기다리세요."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.02)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()
    st.rerun()
    
    
# if st.button("이전 단계로"):
#     reload()

if 'data' in st.session_state:
    st.session_state['data']
    st.write("수치데이터가 아닌 데이터를 변환해봅시다.")
    data = st.session_state['data'].copy()
    data_test = st.session_state['data_test'].copy()
    non_numeric_columns = data.select_dtypes(exclude=['number']).columns
    nn_column = st.selectbox("변환할 속성을 선택하세요", list(non_numeric_columns.tolist()), index=None)    
    
    if nn_column:
        if st.button("변환하기"):
            data = pd.get_dummies(data, columns=[nn_column], drop_first=True)
            data_test = pd.get_dummies(data_test, columns=[nn_column], drop_first=True)
            st.success('완료되었습니다!', icon="✅")
            st.session_state['data']=data.copy()
            st.session_state['data_test']=data_test.copy()
            reload()

    else:
        if st.button("페이지 이동하기"):
            st.switch_page("pages/4전처리하기2.py")

