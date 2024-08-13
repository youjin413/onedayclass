import streamlit as st

st.title("😁상호작용을 위한 앱 만들기")

st.link_button("유튜브 영상 바로가기","https://www.youtube.com/playlist?list=PLSTJuHaq4hGVL0elWMRIuepBmKHq_QCpg")

col1, col2 = st.columns(2)
with col1:
    st.image("https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExZGg2Zm1sc3E1M3k1aWJkeWdmd29la2FlaDFseTF2dmhoYWc3djZubCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/GvjRy6pUMUjQxiKNlh/giphy.webp")
with col2:
    st.success("누구의 생일일까요?")
    answer = st.text_input("이 캐릭터의 이름을 써주세요!")
    if answer =="쪼랩":
        st.success("정답입니다!")
    else:
        st.error("다시 생각해보세요")


st.latex("2x^2+48=90")

tab1, tab2 = st.tabs(["봄","여름"])
tab1.success("봄이에요")
tab2.error("여름입니다")