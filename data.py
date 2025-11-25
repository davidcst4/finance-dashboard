import pandas as pd
from datetime import datetime, date

def get_contas_pagar():
    return pd.DataFrame({
        "Fornecedor": ["Fornecedor A", "Fornecedor B", "Fornecedor C", "Fornecedor B", "Fornecedor A"],
        "Valor": [1500, 2300, 900, 1000, 1200],
        "Vencimento": ["2025-11-10", "2025-11-12", "2025-11-25", "2025-11-12", "2025-11-10"],
        "Status": ["Aberto", "Aberto", "Pago", "Aberto", "Pago"],
        "Categoria": ["Compras de Mercadoria", "Informática", "Serviços", "Compras de Mercadoria", "Serviços"]
    })

def get_kpis_contas_pagar():
    df = get_contas_pagar()
    df["Vencimento"] = pd.to_datetime(df["Vencimento"])
    
    hoje = datetime.now().date()
    mes_atual = hoje.month
    ano_atual = hoje.year
    
    # Previsto no mês: soma de todas as contas com vencimento no mês atual
    previsto_mes = df[df["Vencimento"].dt.month == mes_atual]["Valor"].sum()
    
    # Pago no mês: soma das contas pagas no mês atual
    pago_mes = df[(df["Status"] == "Pago") & (df["Vencimento"].dt.month == mes_atual)]["Valor"].sum()
    
    # A pagar no ano: soma de todas as contas abertas do ano
    a_pagar_ano = df[(df["Status"] == "Aberto") & (df["Vencimento"].dt.year == ano_atual)]["Valor"].sum()
    
    # Pago no ano: soma de todas as contas pagas do ano
    pago_ano = df[(df["Status"] == "Pago") & (df["Vencimento"].dt.year == ano_atual)]["Valor"].sum()
    
    # Em atraso: soma das contas em aberto com vencimento anterior à data atual
    em_atraso = df[(df["Status"] == "Aberto") & (df["Vencimento"].dt.date < hoje)]["Valor"].sum()
    
    # Total a pagar: soma de todas as contas em aberto
    total_a_pagar = df[df["Status"] == "Aberto"]["Valor"].sum()

    # Total de todas: soma de todas contas do ano
    total_de_todas = df["Status"].count()

    # Total de todas em atraso: soma de todas as contas em atraso
    total_em_atraso = df[df["Status"] == "Aberto"]["Valor"].count()
    
    # % Atraso: percentual de atraso (valor em atraso / total a pagar * 100)
    percentual_atraso = (total_em_atraso / total_de_todas * 100) if total_de_todas > 0 else 0
    
    return {
        "previsto_mes": previsto_mes,
        "pago_mes": pago_mes,
        "a_pagar_ano": a_pagar_ano,
        "pago_ano": pago_ano,
        "em_atraso": em_atraso,
        "percentual_atraso": percentual_atraso
    }

def get_contas_receber():
    return pd.DataFrame({
        "Cliente": ["Cliente X", "Cliente Y", "Cliente Z"],
        "Valor": [2200, 1800, 950],
        "Vencimento": ["2025-11-05", "2025-11-18", "2025-11-27"],
        "Status": ["Pago", "Aberto", "Aberto"],
    })

def get_kpis_contas_receber():
    df = get_contas_receber()
    df["Vencimento"] = pd.to_datetime(df["Vencimento"])
    
    hoje = datetime.now().date()
    mes_atual = hoje.month
    ano_atual = hoje.year
    
    # Previsto no mês: soma de todas as contas com vencimento no mês atual
    previsto_mes = df[df["Vencimento"].dt.month == mes_atual]["Valor"].sum()
    
    # Recebido no mês: soma das contas recebidas no mês atual
    recebido_mes = df[(df["Status"] == "Pago") & (df["Vencimento"].dt.month == mes_atual)]["Valor"].sum()
    
    # A receber no ano: soma de todas as contas abertas do ano
    a_receber_ano = df[(df["Status"] == "Aberto") & (df["Vencimento"].dt.year == ano_atual)]["Valor"].sum()
    
    # Recebido no ano: soma de todas as contas recebidas do ano
    recebido_ano = df[(df["Status"] == "Pago") & (df["Vencimento"].dt.year == ano_atual)]["Valor"].sum()
    
    # Em atraso: soma das contas em aberto com vencimento anterior à data atual
    em_atraso = df[(df["Status"] == "Aberto") & (df["Vencimento"].dt.date < hoje)]["Valor"].sum()
    
    # Total a receber: soma de todas as contas em aberto
    total_a_receber = df[df["Status"] == "Aberto"]["Valor"].sum()

    # Total de todas: soma de todas contas do ano
    total_de_todas = df["Status"].count()

    # Total de todas em atraso: soma de todas as contas em atraso
    total_em_atraso = df[df["Status"] == "Aberto"]["Valor"].count()
    
    # % Atraso: percentual de atraso (valor em atraso / total a receber * 100)
    percentual_atraso = (total_em_atraso / total_de_todas * 100) if total_de_todas > 0 else 0
    
    return {
        "previsto_mes": previsto_mes,
        "recebido_mes": recebido_mes,
        "a_receber_ano": a_receber_ano,
        "recebido_ano": recebido_ano,
        "em_atraso": em_atraso,
        "percentual_atraso": percentual_atraso
    }

def get_dre():
    return pd.DataFrame({
        "Categoria": ["Receita Bruta", "Deduções", "Custos", "Despesas"],
        "Valor": [100000, -15000, -30000, -12000]
    })
