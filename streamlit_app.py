# streamlit 라이브러리를 불러옵니다. 'st'라는 별칭으로 사용할 것입니다.
import streamlit as st
# 리스트에서 무작위로 하나를 선택하기 위해 random 라이브러리를 불러옵니다.
import random

# --- 앱의 기본 설정 ---
# 웹페이지의 제목(탭에 표시되는 이름)과 아이콘을 설정합니다.
st.set_page_config(page_title="교사용 응원 카드", page_icon="💌")

# --- 앱 제목 ---
# 앱의 메인 제목을 화면에 표시합니다.
st.title("💌 교사용 응원 카드")
st.write("버튼을 누르고 오늘 하루를 위한 응원의 메시지를 받아보세요!")

# --- 응원 문구 리스트 ---
# 선생님들이 직접 응원 문구를 추가하거나 수정할 수 있는 부분입니다.
# 리스트 안에 원하는 문구를 따옴표로 감싸서 추가하면 됩니다.
quotes = [
    "선생님의 열정은 학생들에게 가장 큰 선물입니다.",
    "작은 씨앗을 위대한 나무로 키우는 선생님, 정말 멋져요!",
    "오늘도 아이들의 세상을 넓혀주셔서 감사합니다.",
    "선생님의 따뜻한 한마디가 누군가에겐 평생의 빛이 됩니다.",
    "가르침은 두 번 배우는 것입니다. 오늘도 성장하는 하루 되세요!",
    "흔들리지 않고 피는 꽃이 어디 있으랴. 지금의 고민도 성장의 과정입니다.",
    "선생님의 존재만으로도 아이들은 안정감을 느낍니다.",
    "아이들의 웃음 속에서 행복을 찾는 하루가 되길 바랍니다.",
    "완벽하지 않아도 괜찮아요. 선생님은 이미 최고의 선생님입니다."
]

# --- 세션 상태(Session State) 초기화 ---
# 세션 상태는 사용자가 앱과 상호작용하는 동안 데이터를 기억하는 공간입니다.
# 'last_quote'라는 이름으로 마지막에 본 응원 문구를 저장할 공간을 만듭니다.
# 만약 아직 저장된 문구가 없다면, 빈 값(None)으로 시작합니다. [4, 6]
if 'last_quote' not in st.session_state:
    st.session_state.last_quote = None
if 'current_quote' not in st.session_state:
    st.session_state.current_quote = "버튼을 눌러주세요."

# --- 메인 버튼 ---
# "오늘의 응원 받기" 버튼을 만듭니다.
# 이 버튼을 누르면 if 구문 안의 코드가 실행됩니다.
if st.button("오늘의 응원 받기", type="primary"):
    # 이전 응원 문구를 'last_quote'에 저장합니다.
    st.session_state.last_quote = st.session_state.current_quote
    # quotes 리스트에서 문구 하나를 무작위로 선택합니다. [1, 2, 5]
    random_quote = random.choice(quotes)
    # 선택된 문구를 'current_quote'에 저장합니다.
    st.session_state.current_quote = random_quote

# --- 현재 응원 문구 표시 ---
# 선택된 현재 응원 문구를 화면에 큰 글씨(헤더)로 보여줍니다.
st.header(st.session_state.current_quote)

# 구분선을 추가하여 시각적으로 분리합니다.
st.divider()

# --- 최근 응원 문구 다시 보기 ---
# 이전에 봤던 응원 문구가 저장되어 있는지 확인합니다.
if st.session_state.last_quote and st.session_state.last_quote != "버튼을 눌러주세요.":
    # "최근 응원 문구 다시 보기" 버튼을 만듭니다.
    if st.button("최근 응원 문구 다시 보기"):
        # 버튼이 눌리면 이전에 저장해둔 'last_quote'를 화면에 보여줍니다.
        st.info(f"최근에 본 문구: {st.session_state.last_quote}")