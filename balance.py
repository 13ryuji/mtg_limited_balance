import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('./processed_data/data.csv')
# graph_df = df[['Date', 'Format', 'wins', 'balance', 'ttl_balance']]

format_list = df['Format'].unique().tolist()

def app():
    st.title("Limited Balance")

    options = st.multiselect(
        'Format', format_list, format_list,
    )

    sel_df = df[df['Format'].isin(options)]
    sel_df.reset_index(inplace=True)
    sel_df['ttl_balance'] = sel_df['balance'].cumsum()

    st.text('Balance par event')
    st.bar_chart(data=sel_df[['balance',]])

    st.text('Total Balance')
    st.line_chart(data=sel_df['ttl_balance'])
