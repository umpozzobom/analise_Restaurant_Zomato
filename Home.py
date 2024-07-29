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
  ### Contéudo deste Growth Dashboard: 
      Visão Global: Métricas Globais de comportamento do negócio.

      Países: Acompanhamento do crescimento de negócio com foco nos países e suas avaliações registradas pelos usuários

      Cidades: Acompanhamento das principais cidades e sua relação com o tipo de restaurante, realização de reservas e entregas online, preço de pratos para dois,

      Restaurantes: Análise dos melhores e piores restaurantes segundo as métricas de Votos, Avaliações e Preço.

      Culinária: Comparações dos tipos de culinárias em relação a quantidade de avaliações, preço médio de cada país, e as melhores culinárias de acordo com a nota de avaliação
     
      -
    ### Ask to help - Ully Pozzobom - umpozzobom.costa@gmail.com
    """)
