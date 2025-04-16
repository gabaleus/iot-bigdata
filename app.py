import pandas as pd
import streamlit as st
import plotly.express as px
import os
from sqlalchemy import create_engine


# setando as configs da página
st.set_page_config(
    layout="wide",
    page_title="Data")





# criando a conexão
connection_string = os.getenv('DATABASE_URL')
DB_TABLE_NAME = 'data'

# criando a engine, não faço ideia de como funciona
engine = create_engine(connection_string)

# lendo meu csv
df = pd.read_csv('IOT-temp.csv')

# enviando para o banco de dados
df.to_sql('data', engine, if_exists='replace')

# criando um select para pegar os dados do banco
query = f"SELECT * FROM {DB_TABLE_NAME}"

# pegando os dados do banco
df_data = pd.read_sql(query, engine)


# convertendo a coluna noted_date para datetime
df_data['date'] = pd.to_datetime(df_data['noted_date'],format='mixed', dayfirst=True)
df_data['hour'] = df_data['date'].dt.hour
df_data['day'] = df_data['date'].dt.day 
df_data['month'] = df_data['date'].dt.month
df_data['year'] = df_data['date'].dt.year   


# Título do dashboard
st.title('Dashboard de Temperaturas IoT')

col0 = st.columns(1)[0]
col1, col2 = st.columns([1, 1])

# Gráfico 1: Média de temperatura por dispositivo
col0.header('Média de Temperatura por Dispositivo')
df_avg_temp = df_data['temp'].groupby(df_data['id']).mean().reset_index()
df_avg_temp.columns = ['id', 'temp']
fig1 = px.bar(df_avg_temp, x='id', y='temp', labels={'id': 'Dispositivo', 'temp': 'Temperatura Média'})
col0.plotly_chart(fig1)

# Gráfico 2: Temperaturas máximas e mínimas por dia
col1.header('Temperaturas Máximas e Mínimas por Dia')
df_daily_max_min_temp = df_data.groupby('date').agg({'temp': ['max', 'min']}).reset_index()
df_daily_max_min_temp.columns = ['date', 'temp_max', 'temp_min']

color_map = {
    'temp_max': 'red',
    'temp_min': 'blue'
}
col1.plotly_chart(px.line(df_daily_max_min_temp, x='date', y=['temp_max', 'temp_min'], labels={'value': 'Temperatura', 'variable': 'Tipo'}, color_discrete_map=color_map))

# Gráfico 3: Média de temperatura por hora
col2.header('Média de Temperatura por Hora')
df_avg_temp_hour = df_data.groupby('hour').agg({'temp': 'mean'}).reset_index()
df_avg_temp_hour.columns = ['hour', 'temp']
fig3 = px.line(df_avg_temp_hour, x='hour', y='temp', labels={'hour': 'Hora', 'temp': 'Temperatura Média'})
col2.plotly_chart(fig3)




