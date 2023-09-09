import streamlit as st
from PIL import Image
st.set_page_config(
    page_title = '곰이 되고 싶은 사람',
    page_icon = '🐻',
    layout='wide'

)
menu = st.selectbox('MENU',['자기소개','학교소개','취미 & 관심분야'])

if menu == '자기소개':
    st.title('자기소개')
    st.subheader('저는 청구고등학교를 다니고 있는 2학년 박병관 입니다!')
    st.subheader('저의 생년월일은 2006년 7월 29일 입니다.')
    st.subheader('제가 제일 좋아하는 동물은 곰입니다!')
    image1 = Image.open('gom.png')
    st.image(image1, caption='곰 일러스트')
    st.subheader('저의 꿈은 정보보안 전문가로 안철수님의 V3처럼 백신프로그램을 만들어서 약자들한테 배포해주는게 꿈입니다.')
    image1 = Image.open('whitehack_img_1.png')
    st.image(image1, width=600,caption='정보보안전문가 일러스트')
    st.subheader('정보보안 전문가 관련 영상')
    st.video('https://youtu.be/arcynoCFVAA?si=V0ybZ75Lgh-vIoML')


elif menu == '학교소개':
    st.title('학교소개')
    st.subheader('제가 다니고 있는 학교인 청구고등학교 입니다.')
    image2 = Image.open('cheonggu.png')
    st.image(image2, width=800, caption='청구고등학교')

    col1, col2, col3 = st.columns(3)
    with col1:
        st.write('설립연도 ')
        st.checkbox('1954년 12월 31일')
        image3 = Image.open('mm.png')
        st.image(image3,width=300,caption='청구고등학교 마크')
    with col2:
        st.write('학교 위치')
        st.checkbox('대구광역시 동구 신천3동')
        image4 = Image.open('학교.png')
        st.image(image4,width=300,caption='학교위치')
    with col3:
        st.write('상징')
        st.checkbox('교목: 향나무, 교화: 개나리')
        image5 = Image.open('나무 꽃.png')
        st.image(image5,width=300,caption='향나무, 개나리')
    st.subheader('오시는 방법 518,724 버스를 타시고 청구고등학교 앞에서 하차하시면 됩니다.')

elif menu == '취미 & 관심분야':
    st.title('취미 & 관심분야')
    st.subheader('저의 취미는 발로란트하기, 노래듣기, 프로그래밍하기 입니다.')
    st.subheader('제가 관심 있어하는 분야로는 정보보안쪽으로 백신프로그램 개발입니다.')
    st.subheader('제가 제일 좋아하는 노래는 밑에 있는 HIGH HOPES, Little star입니다.')
    st.video('https://youtu.be/P8b47hZdvVY?si=EYDv9xLOMr2nuiFB')
    st.video('https://youtu.be/MW7UZu4q5cw?si=QoFuTWqc4hSVwybG')