import streamlit as st
import pandas as pd
import time
import pandas as pd
import datetime

st.title("결측치 제거하기")

st.write("데이터에서 비어있는 수치를 삭제해봅시다.")

if 'data' not in st.session_state:
    st.session_state['data'] = pd.DataFrame()

data = st.session_state['data']
    
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
    st.write("결측치의 개수")
    st.bar_chart(data.isnull().sum())
    
    num_null = sum(list(data.isnull().sum().values))
    
    if num_null !=0:
        null_column = st.selectbox("어떤 열을 처리할까요?", list(data.columns[data.isnull().any()].tolist()), index=None)
    
        if null_column:
            how = st.radio(label = '어떻게 처리할까요', options = ["삭제하기", "평균으로 채우기", "중앙값으로 채우기", "특정값으로 채우기"])
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            
            if how == "특정값으로 채우기":
                num = st.text_input("숫자를 입력하세요", "0")
                try:
                    num = float(num)
            
                except ValueError:
                    st.warning("Error: '{num}' 숫자가 아닙니다.")
                    raise ValueError(f"Error: '{num}' is not a valid number")
        
        if null_column and how:
            if how == "특정값으로 채우기" and num:
                if st.button("변환하기"):
                    data[null_column].fillna(float(num), inplace=True)
                    st.success('완료되었습니다!', icon="✅")
                    st.session_state['raw'] = st.session_state['data']
                    st.session_state['data']=data
                    data
                    reload()

            elif how == "평균으로 채우기":
                if st.button("변환하기"):
                    data[null_column].fillna(data[null_column].mean(), inplace=True)
                    st.success('완료되었습니다!', icon="✅")
                    st.session_state['raw'] = st.session_state['data']
                    st.session_state['data']=data
                    data
                    reload()
                    
            elif how == "중앙값으로 채우기":
                if st.button("변환하기"):
                    data[null_column].fillna(data[null_column].median(), inplace=True)
                    st.success('완료되었습니다!', icon="✅")
                    st.session_state['raw'] = st.session_state['data']
                    st.session_state['data']=data
                    data
                    reload()
            else:
                if st.button("변환하기"):
                    data =  data.dropna(subset=[null_column])
                    st.success('완료되었습니다!', icon="✅")
                    st.session_state['raw'] = st.session_state['data']
                    st.session_state['data']=data
                    data
                    reload()
        
        
        
    else:
        if st.button("페이지 이동하기"):
            st.switch_page("pages/5라벨정하기.py")
