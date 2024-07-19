import streamlit as st
import pandas as pd
import time
import pandas as pd
import datetime

if 'data' not in st.session_state:
    st.session_state['data'] = pd.DataFrame()
    
if 'data_test' not in st.session_state:
    st.session_state['data_test'] = pd.DataFrame()
    
    
st.title("파일 업로드 하기")

st.write("모델 학습을 위해 데이터를 업로드 해 봅시다.")

if 'data' not in st.session_state:
    st.session_state['data'] = pd.DataFrame()



st.write("먼저 train데이터를 업로드 해 봅시다.")

uploaded_files = st.file_uploader("Choose a CSV file", type=['csv'], accept_multiple_files=False, key=1)        
if uploaded_files is not None:
    try:
        data = pd.read_csv(uploaded_files)
        
        data
        st.session_state['data'] = data
        
        st.write("이제 test데이터를 업로드 해 봅시다.")
        uploaded_files_test = st.file_uploader("Choose a CSV file", type=['csv'], accept_multiple_files=False, key=2)        
        if uploaded_files_test is not None:
            try:
                data_test = pd.read_csv(uploaded_files_test)
        
                data_test
                st.session_state['data_test'] = data_test
            
            except Exception as e:
                st.error(f"An error occurred: {e}")
        
        
        
        if st.button("다음 페이지로"):
            st.switch_page("pages/2속성고르기.py")

        
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.warning("Please upload a CSV file.")