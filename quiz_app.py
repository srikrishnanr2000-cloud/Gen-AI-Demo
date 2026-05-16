import streamlit as st
from datetime import date
import random

# ----------------------
# PAGE CONFIG
# ----------------------
st.set_page_config(page_title="THE QUIZ", page_icon="🧠")

# ----------------------
# SESSION STATE
# ----------------------
if "page" not in st.session_state:
    st.session_state.page = "register"

if "score" not in st.session_state:
    st.session_state.score = 0


# ----------------------
# REGISTER PAGE
# ----------------------
if st.session_state.page == "register":

    st.title("🧠 THE QUIZ")

    st.subheader("Registration Form")

    name = st.text_input("NAME")

    phone = st.text_input("Phone No.")

    email = st.text_input("Mail Address")

    dob = st.date_input(
        "DOB",
        min_value=date(1950, 1, 1),
        max_value=date.today()
    )

    if st.button("Register"):

        if name and phone and email:

            st.success("Registration Done ✅")

            st.session_state.page = "quiz"

            st.rerun()

        else:
            st.error("Please fill all fields")


# ----------------------
# QUIZ PAGE
# ----------------------
elif st.session_state.page == "quiz":

    st.title("📝 General Knowledge Quiz")

    st.write("Answer the following questions:")

    # Questions
    q1 = st.radio(
        "1. What is the capital of India?",
        ["Mumbai", "Delhi", "Chennai", "Kolkata"]
    )

    q2 = st.radio(
        "2. Which planet is known as the Red Planet?",
        ["Earth", "Mars", "Jupiter", "Venus"]
    )

    q3 = st.radio(
        "3. Who invented the light bulb?",
        ["Newton", "Einstein", "Thomas Edison", "Tesla"]
    )

    q4 = st.radio(
        "4. Which is the largest ocean in the world?",
        ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean"]
    )

    q5 = st.radio(
        "5. How many days are there in a leap year?",
        ["365", "366", "364", "360"]
    )

    # Submit button
    if st.button("Submit Quiz"):

        score = 0

        if q1 == "Delhi":
            score += 1

        if q2 == "Mars":
            score += 1

        if q3 == "Thomas Edison":
            score += 1

        if q4 == "Pacific Ocean":
            score += 1

        if q5 == "366":
            score += 1

        st.session_state.score = score

        # Popup Message
        st.balloons()

        st.success(f"🎉 Your Score is: {score} / 5")