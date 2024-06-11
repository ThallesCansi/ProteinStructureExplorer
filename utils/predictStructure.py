import streamlit as st
import requests


def preverEstrutura(sequencia: str) -> dict:
    url = "https://biolm.ai/api/v2/esmfold-multichain/predict/"
    data = {"items": [{"sequence": sequencia + ":"}]}
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Token " + st.secrets["TOKEN"],
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()
