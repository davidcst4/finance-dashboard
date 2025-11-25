import plotly.express as px
import streamlit as st
import data
from pags import contas_a_pagar, contas_a_receber

st.set_page_config(page_title="Dashboard Financeiro", page_icon="💰", layout="wide")

st.sidebar.image("https://www.fatturar.com/logo/files/17329041665945_f8456fd0-14f5-4f9c-b34e-44cbff70373c__1_.webp", width=128)

st.sidebar.title("Menu")

page = st.sidebar.selectbox("Selecione:", ["Contas a Pagar", "Contas a Receber"])

st.sidebar.title("Filtros")

filter_date_by = st.sidebar.selectbox("Período:",["Neste mês", "Neste ano", "Por período específico"])
if filter_date_by == "Por período específico":
    first_date = st.sidebar.date_input("Data inicial")
    last_date = st.sidebar.date_input("Data final")

st.sidebar.selectbox("Status:",["Todos", "Aberto", "Pago"])

st.title(f"Dashboard Financeiro - {page}")

if page == "Contas a Pagar":
    contas_a_pagar.contas_a_pagar()

elif page == "Contas a Receber":
    contas_a_receber.contas_a_receber()
