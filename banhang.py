import streamlit as st

st.set_page_config(page_title='Vương quốc mô hình', page_icon=':sparkles:')
if 'page' not in st.session_state:
    st.session_state.page = None

with st.sidebar:
    st.title('Vương quốc mô hình')
    st.header('Chào mừng bạn đến Vương quốc mô hình!')
    st.image('vuongquocmohinh.jpg')
    st.write('Chúng tôi chuyên bán các mô hình nhân vật hoạt hình chất lượng...')
    st.write(':house: Địa chỉ cửa hàng:')
    st.write(':phone: Điện thoại liên hệ')

st.title('Vương quốc mô hình')
coll, col2, col3, col4 = st.columns(4)

with coll:
    if st.button('Dragon Ball'):
        st.session_state.page = 'dragonball'
with col2:
    if st.button('Naruto'):
        st.session_state.page = 'naruto'
with col3:
    if st.button('One Piece'):
        st.session_state.page = 'onepiece'
with col4:
    if st.button('Attack on Titan'):
        st.session_state.page = 'attackontitan'
if st.session_state.page == 'dragonball':
    st.header('Danh sách mô hình Dragon Ball')
    col4, col5, col6 = st.columns(3)
    with col4:
        st.image('gokuultra.jpg', caption='Goku Ultra Instinct – Mã số: 001')
    with col5:
        st.image('vegataultra.jpg', caption='Vegeta Super Saiyan – Mã số: 002')
    with col6:
        st.image('picolo.jpg', caption='Picolo – Mã số: 003')
elif st.session_state.page == 'naruto':
    st.header('Danh sách mô hình Naruto')
    col4, col5, col6 = st.columns(3)
    with col4:
        st.image('naruto.jpg', caption='Uzumaki Naruto – Mã số: 001')
    with col5:
        st.image('kakasi.jpg', caption='Uchiha Sasuke – Mã số: 002')
    with col6:
        st.image('sasuke.jpg', caption='Hatake Kakashi – Mã số: 003')
elif st.session_state.page == 'onepiece':
    st.header('Danh sách mô hình One Piece')
    col4, col5, col6 = st.columns(3)
    with col4:
        st.image('luffy.jpg', caption='Monkey D. Luffy – Mã số: 001')
    with col5:
        st.image('zoro.jpg', caption='Roronoa Zoro – Mã số: 002')
    with col6:
        st.image('nami.jpg', caption='Nami – Mã số: 003')
elif st.session_state.page == 'attackontitan':
    st.header('Danh sách mô hình Attack on Titan')
    col4, col5, col6 = st.columns(3)
    with col4:
        st.image('eren.jpg',caption='Eren Yeager - Mã số: 001')
    with col5:
        st.image('misaka.jpg',caption='Mikasa Ackerman - Mã số: 002')
    with col6:
        st.image('armin.jpg',caption='Armin Arlert - Mã số: 003')
st.header('Đặt hàng')
with st.form('Đơn đặt hàng'):
    topics = ('Dragon Ball', 'Naruto', 'One Piece')
    option_topic = st.selectbox('Chủ đề mô hình', topics)

    codes = ('001', '002', '003')
    option_code = st.selectbox('Mã số mô hình', codes)

    nums = st.slider('Số lượng bạn muốn đặt:', 0, 10, 0)

    name = st.text_input('Họ và tên')

    phone = st.text_input('Số điện thoại nhà riêng')

    address = st.text_input('Địa chỉ giao hàng')

    bill = {
        'Loại mô hình:': option_topic,
        'Mã số:': option_code,
        'Số lượng:': nums,
        'Họ tên khách hàng:': name,
        'Số điện thoại liên hệ:': phone,
        'Địa chỉ giao hàng:': address
    }

    submitted = st.form_submit_button("Xác nhận")
    if submitted:
        st.header('Bạn đã chọn:')
        for x, y in bill.items():
            st.write(x, y)
print_bill = st.checkbox('In hoá đơn')
if print_bill:
    ans = ''
    for x in bill:
        ans += str(x) + ' ' + str(bill[x]) + '\n'
    st.download_button('In hoá đơn', ans)