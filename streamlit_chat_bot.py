import streamlit as st
import random
import time

st.title("Простой чат-бот")

# Инициализация истории сообщений в сессии
if "messages" not in st.session_state:
    st.session_state.messages = []

# Отображаем историю сообщений
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Принимаем ввод пользователя
if prompt := st.chat_input("Напишите сообщение"):
    # Добавляем сообщение пользователя в историю
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Генерируем ответ бота (случайный из списка)
    responses = [
        "Привет! Чем могу помочь?",
        "Расскажите подробнее.",
        "Интересно, продолжайте.",
        "Я вас слушаю.",
        "Спасибо за сообщение!"
    ]
    response = random.choice(responses)

    # Показываем ответ с эффектом печати
    with st.chat_message("assistant"):
        for word in response.split():
            st.write(word, end=" ", flush=True)
            time.sleep(0.05)
        st.write("")  # перенос строки

    # Добавляем ответ бота в историю
    st.session_state.messages.append({"role": "assistant", "content": response})
