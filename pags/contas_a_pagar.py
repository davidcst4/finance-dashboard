import streamlit as st
import plotly.express as px
import data

def format_currency(value):
    return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def contas_a_pagar():
    kpis = data.get_kpis_contas_pagar()
    
    kpi1, kpi2, kpi3, kpi4, kpi5, kpi6 = st.columns(6)
    kpi1.metric(value=format_currency(kpis['previsto_mes']), label="📅 Previsto no mês", border=True)
    kpi2.metric(value=format_currency(kpis['pago_mes']), label="✅ Pago no mês", border=True)
    kpi3.metric(value=format_currency(kpis['a_pagar_ano']), label="💳 A pagar no ano", border=True)
    kpi4.metric(value=format_currency(kpis['pago_ano']), label="💰 Pago no ano", border=True)
    kpi5.metric(value=format_currency(kpis['em_atraso']), label="⚠️ Em atraso", border=True)
    kpi6.metric(value=f"{kpis['percentual_atraso']:.1f}%", label="📊 % Atraso", border=True)

    col1, col2 = st.columns(2)
    with col1:
        fig1 = px.bar(data.get_contas_pagar(), x="Status", y="Valor", color="Fornecedor", text="Valor")
        st.plotly_chart(fig1, width="content")
    
    with col2:
        fig2 = px.pie(data.get_contas_pagar(), names="Categoria", values="Valor", hole=0.6)
        st.plotly_chart(fig2, width="content")

    st.dataframe(data.get_contas_pagar(), hide_index=True)