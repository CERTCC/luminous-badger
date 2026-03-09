import streamlit as st
import requests as r
import json

st.title("hello world")

fastapi_url = st.text_input(
    "FastAPI URL",
    value="http://localhost:9000"
    )

if st.button("GET from FastAPI"):
    try:
        response = r.get(f"{fastapi_url}")
        if response.status_code == 200:
            data = response.json()
            st.json(data)
        else:
            st.error(f"Error code {response.status_code}")
            st.text(response.text)
    except r.exceptions.ConnectionError:
        st.error("Connection Error: Could not connect to FastAPI. Make sure it's running!")
    except Exception as e:
        st.error(f"Error: {str(e)}")
