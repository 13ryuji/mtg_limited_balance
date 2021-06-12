import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('./processed_data/data.csv')
df = df[
    (df['Format']=='OpenSealed_D1_Bo3') |
    (df['Format']=='TradDraft')
]
# graph_df = df[['Date', 'Format', 'wins', 'balance', 'ttl_balance']]

format_list = df['Format'].unique().tolist()

def app():
    st.text('BO3 wins histogram')

    options = st.multiselect(
        'Format', format_list, format_list,
    )

    sel_df = df[df['Format'].isin(options)]
    sel_df.reset_index(inplace=True)
    sel_df['ttl_balance'] = sel_df['balance'].cumsum()

    fig = px.histogram(
        sel_df,
        x='wins',
        color='Format',
        hover_data=sel_df.columns,
        nbins=8
    )
    st.plotly_chart(fig, use_container_width=True)

    st.text('Data')
    st.dataframe(sel_df)
