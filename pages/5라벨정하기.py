import streamlit as st
import pandas as pd
import time
import pandas as pd
import datetime

st.title("라벨정하기")

st.write("판단의 기준이 되는 속성을 정해봅시다.")

if 'data' not in st.session_state:
    st.session_state['data'] = pd.DataFrame()

if 'train' not in st.session_state:
    st.session_state['train'] = pd.DataFrame()
    
if 'target' not in st.session_state:
    st.session_state['target'] = pd.DataFrame()


data = st.session_state['data'].copy()
    
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
    data = st.session_state['data'].copy()
    target_column = st.selectbox("타겟 속성을 선택하세요.", list(data.columns.tolist()), index=None)    
    if st.button("선택하기") and target_column:
        target = data[target_column].copy()
        data.drop(target_column, axis=1, inplace=True)
        train = data.copy()
        st.session_state['target']=target.copy()
        st.session_state['train']=train.copy()
        st.success('완료되었습니다!', icon="✅")
        st.caption('target data')
        st.session_state['target']
        st.caption('train data')
        st.session_state['train']


        no_missing_values = not st.session_state['train'].isnull().values.any()
        all_numeric = st.session_state['train'].apply(lambda s: pd.api.types.is_numeric_dtype(s)).all()

        if no_missing_values and all_numeric:
            st.success('모델 생성을 위한 준비가 완료되었습니다!', icon="✅")
            if st.button("페이지 이동하기"):
                st.switch_page("pages/6모델생성하기.py")