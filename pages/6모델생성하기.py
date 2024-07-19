import streamlit as st
import pandas as pd
import time
import pandas as pd
import datetime
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.metrics import accuracy_score


st.title("모델 생성하기")

st.write("학습데이터로 모델을 만들어봅시다.")

if 'data' not in st.session_state:
    st.session_state['data'] = pd.DataFrame()
if 'data_test' not in st.session_state:
    st.session_state['data_test'] = pd.DataFrame()

if 'train' not in st.session_state:
    st.session_state['train'] = pd.DataFrame()
    
if 'target' not in st.session_state:
    st.session_state['target'] = pd.DataFrame()


data = st.session_state['data'].copy()
data_test = st.session_state['data_test'].copy()
train = st.session_state['train'].copy()
target = st.session_state['target'].copy()
    
missing_cols = set(train.columns) - set(data_test.columns)
for col in missing_cols:
    data_test[col] = 0

data_test = data_test[train.columns]

def reload():
    progress_text = "잠시후에 데이터가 변환됩니다. 잠시만 기다리세요."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.02)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()
    st.rerun()

@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode("utf-8")

    
# if st.button("이전 단계로"):
#     reload()

if 'data' in st.session_state:
    st.write("모델 생성")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write("1. 의사결정 트리")
        st.caption("의사결정트리는 가지치기를 이용하여 분류하는 알고리즘입니다.")
        depth = st.number_input("나무 깊이", step=1, min_value=1, max_value=20)
        if st.button("모델 생성", key=1):
            dt = tree.DecisionTreeClassifier(max_depth=depth)
            dt.fit(train, target)
            pred = dt.predict(train)
            accuracy = accuracy_score(target, pred)
            st.write(f"의사결정 트리 정확도는 {round(accuracy,5)}입니다.")
            predictions = dt.predict(data_test)
            data_test['pred'] = predictions
            csv = convert_df(data_test)
            st.download_button(
    label="Download",
    data=csv,
    file_name="decisiontree.csv",
    mime="text/csv",
)



    with col2:
        st.write("2. 최근접이웃 분류")
        st.caption("최근접이웃 분류는 속성과 가까운 것의 속성을 다수결로 결정하는 방법입니다.")
        n_neighbors = st.number_input("이웃의 수", step=1, min_value=1, max_value=20)

        if st.button("모델 생성", key=2):
            knn = KNeighborsClassifier(n_neighbors=n_neighbors)
            knn.fit(train, target)
            pred = knn.predict(train)
            accuracy = accuracy_score(target, pred)
            st.write(f"최근접이웃 정확도는 {round(accuracy,5)}입니다.")
            predictions = knn.predict(data_test)
            data_test['pred'] = predictions
            csv = convert_df(data_test)
            st.download_button(
    label="Download",
    data=csv,
    file_name="kneighbors.csv",
            )

    with col3:
        st.write("3. SVM모델")
        st.caption("SVM은 속성을 구분하는 선을 그어 선에 해당하는 영역을 결정하는 알고리즘입니다.")
        C = st.number_input("패널티 값", min_value=1.00, max_value=5.00)
        if st.button("모델 생성", key=3):
            svm = svm.SVC(C=C)
            svm.fit(train, target)
            pred = svm.predict(train)
            accuracy = accuracy_score(target, pred)
            st.write(f"SVM모델 정확도는 {round(accuracy,5)}입니다.")
            predictions = svm.predict(data_test)
            data_test['pred'] = predictions
            csv = convert_df(data_test)
            st.download_button(
    label="Download",
    data=csv,
    file_name="SVM.csv",
            )
