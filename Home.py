import streamlit as st
from PIL import Image
st.set_page_config(
  page_title="Home")

  
image = Image.open('zomato.png')
st.sidebar.image(image, width=120)

st.sidebar.markdown('# Zomato Restaurant Apps - Projeto Fome Zero')

st.sidebar.markdown("""---""")

st.write('# Zomato Restaurant Apps Dashboard')

st.markdown(
  """
  Zomato Restaurant Dashboard foi construído para compreender e acompanhar as métricas de crescimento do negócio em diferentes âmbitos - Países, Cidades, Restaurantes e Tipos de culinária.
  ### Como utilizar esse Growth Dashboard;?
   - Visão Global: Métricas Globais de comportamento do negócio.
   - Países: Acompahamento do crescimento de negócio com foco nos países e suas avaliações
   - Cidades: Acompanhamento das principais cidades cadastradas na base de dados
   - Restaurantes: Insights melhores e piores restaurantes segundo as métricas de Votos, Avaliações e Preço.
   - Tipos de Culinária: Insights das melhores culinárias por país, restaurante, e tipo de culinárias
     
      -
    ### Ask to help - Ully Pozzobom - umpozzobom.costa@gmail.com
    """)