import streamlit as st
from matplotlib import image
import os



st.title("A Little Bit About :red[Myself]")


btn_click = st.button ("Click to Know Me!!")

if btn_click == True:

    st.text("Full Name : Karthikeyan Radhakrishnan")

    st.text("Most People Call me: Karthik")

    st.text("City : Ottawa, Canada")

    st.text("Occupation: Senior Lead Manufacturing Engineer")

    st.text("Email: Karthikmiie@gmail.com")

    st.text("Linkedin: https://www.linkedin.com/in/karthikeyan-radhakrishnan21/?original_referer= ")

    st.balloons()

btn_click_2 = st.button("Click to Know About my Experience!!")

if btn_click_2 == True:

    st.text ("Experienced Industrial Engineer with 5+ years of expertise overseeing the end-to-end project planning and optimization of multi-million dollar commercial Manufacturing Engineering projects.")

    st.text("Experienced in defining and implementing workflows, resolving complex logistics and operational problems. Specialized in establishing and managing engineering projects across all levels of an organization (Procurement, Planning, Distribution, Human Resources, CRM, and Sales).")

    st.text("Progressive communicator with stellar results in ensuring on-time and on-budget project performance. A polished leader and business partner to all levels of an organization with an exceptional ability to mobilize high-impact teams within and across complex production logistics.")

    st.balloons()