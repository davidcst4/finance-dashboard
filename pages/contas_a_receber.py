import streamlit as st
import plotly.express as px
import data

def format_currency(value):
    return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def contas_a_receber():
    kpis = data.get_kpis_contas_receber()
    
    kpi1, kpi2, kpi3, kpi4, kpi5, kpi6 = st.columns(6)
    kpi1.metric(value=format_currency(kpis['previsto_mes']), label="📅 Previsto no mês", border=True)
    kpi2.metric(value=format_currency(kpis['recebido_mes']), label="✅ Recebido no mês", border=True)
    kpi3.metric(value=format_currency(kpis['a_receber_ano']), label="💳 A receber no ano", border=True)
    kpi4.metric(value=format_currency(kpis['recebido_ano']), label="💰 Recebido no ano", border=True)
    kpi5.metric(value=format_currency(kpis['em_atraso']), label="⚠️ Em atraso", border=True)
    kpi6.metric(value=f"{kpis['percentual_atraso']:.1f}%", label="📊 % Atraso", border=True)

    col1, col2 = st.columns(2)
    with col1:
        fig1 = px.bar(data.get_contas_receber(), x="Status", y="Valor")
        st.plotly_chart(fig1, width="content")
    
    with col2:
        fig2 = px.pie(data.get_contas_receber(), names="Status", values="Valor", hole=0.5)
        st.plotly_chart(fig2, width="content")

    st.dataframe(data.get_contas_receber(), hide_index=True)