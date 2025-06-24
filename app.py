import os

import streamlit as st
from factorial import fact


def load_users():
    """Đọc danh sách user từ file users.txt"""
    try:
        if os.path.exists("users.txt"):
            with open("users.txt", "r", encoding="utf-8") as f:
                users = [line.strip() for line in f.readlines() if line.strip()]
            return users
        else:
            st.error("File users.txt không tồn tại!")
            return []
    except Exception as e:
        st.error(f"Lỗi khi đọc file users.txt: {e}")
        return []


def login_page():
    """Login page"""
    st.title("Login")

    # Input user
    username = st.text_input("Nhập tên người dùng:")

    if st.button("Login"):
        if username:
            users = load_users()
            if username in users:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.rerun()
            else:
                # Nếu user không hợp lệ, hiển thị trang greeting
                st.session_state.show_greeting = True
                st.session_state.username = username
                st.rerun()
        else:
            st.warning("Vui lòng nhập tên người dùng!")


def factorial_calculate():
    st.title("Factorial Calculator")

    # Hiển thị thông tin user đã đăng nhập
    st.write(f"Xin chào, {st.session_state.username}!")

    # Nút đăng xuất
    if st.button("Log out"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()

    st.divider()

    # Chức năng tính giai thừa
    number = st.number_input("Enter a number:", min_value=0, max_value=900)
    if st.button("Calculate"):
        resutl = fact(number)
        st.write(f"The factorial of {number} is {resutl}")


def greeting_page():
    st.title("Xin chào!")
    st.write(f"Xin chào {st.session_state.username}")
    st.write("Bạn không có quyền truy cập tính năng này. Hãy liên hệ người quản lý!")

    if st.button("Quay lại đăng nhập"):
        st.session_state.show_greeting = False
        st.session_state.username = ""
        st.rerun()


def main():
    # Khởi tạo session state
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "username" not in st.session_state:
        st.session_state.username = ""
    if "show_greeting" not in st.session_state:
        st.session_state.show_greeting = False

    # Điều hướng dựa trên trạng thái đăng nhập
    if st.session_state.logged_in:
        factorial_calculate()
    elif st.session_state.show_greeting:
        greeting_page()
    else:
        login_page()


if __name__ == "__main__":
    main()
