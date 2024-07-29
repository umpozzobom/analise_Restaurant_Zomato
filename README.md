# Apresentação da Zomato Restaurant App

    A Zomato API é uma plataforma de análises mais úteis para os amantes da gastronomia que querem provar as melhores culinárias de todas as partes do mundo que cabem no seu orçamento. É também para aqueles que querem encontrar restaurantes com boa relação custo-benefício em várias partes do país para as culinárias. Além disso, atende às necessidades de pessoas que estão se esforçando para obter a melhor culinária do país e qual localidade desse país serve essas culinárias com o número máximo de restaurantes. 
Informações valiosas sobre métricas de negócio podem ser exploradas neste conjunto de dados através do link: https://www.kaggle.com/datasets/shrutimehta/zomato-restaurants-data


# 1. Problema de negócio

      A Zomato Restaurant App é um aplicativo que possui informações de diversos países,cidades, e tipos de culinária em escala global, e com isso gera muitos dados úteis para serem analisados e gerar novos insights visando o crescimento da empresa e melhoria para o usuário. De forma hipotética, fui contratada como Cientista de Dados da empresa Fome Zero (Zomato Restaurant App), e a minha principal tarefa nesse momento é ajudar o CEO Kleiton Guerra a identificar pontos chaves da empresa, respondendo às perguntas que ele fizer
utilizando dados! A empresa Fome Zero é uma marketplace de restaurantes. Ou seja, seu core business é facilitar o encontro e negociações de clientes e restaurantes. Os restaurantes fazem o cadastro dentro da plataforma da Fome Zero, que disponibiliza informações como endereço, tipo de culinária servida, se possui reservas, se faz entregas e também uma nota de avaliação dos serviços e produtos do restaurante, dentre outras informações. O CEO Guerra também foi recém contratado e precisa entender melhor o negócio para conseguir tomar as melhores decisões estratégicas e alavancar ainda mais a Fome Zero, e para isso, ele precisa que seja feita uma análise nos dados da empresa e que sejam gerados dashboards, a partir das analises, e que sejam respondidas algumas perguntas sobre gerais sobre o negócios e mais específicas envolvendo os países, cidades, restaurantes e tipos de culinária de cada localidade.

# 2. Premissas do negócio

* As analises foram realizadas com dados referente a primeira quinzena do mês de Abril/2024

* As principais visões do negócio foram: Informações Globais,Visão País, Visão Cidade, Visão Restaurantes e Visão Tipos de Culinária

    
# 3. Estratégia da solução

O painel estratégico foi desenvolvido utilizando as métricas que refletem as 5 principais visões do modelo de negócio da empresa:
  
  Visão Global: Métricas Globais de comportamento do negócio.

  Países: Acompanhamento do crescimento de negócio com foco nos países e suas avaliações registradas pelos usuários

  Cidades: Acompanhamento das principais cidades e sua relação com o tipo de restaurante, realização de reservas e entregas online, preço de pratos para dois, 

  Restaurantes: Análise dos melhores e piores restaurantes segundo as métricas de Votos, Avaliações e Preço.

  Tipos de Culinária: Comparações dos tipos de culinárias em relação a quantidade de avaliações, preço médio de cada país, e as melhores culinárias de acordo com a nota de avaliação 
     
# 4. Top 3 Insights de dados

  *A Índia possui a maior quantidade de registros de cidades, restaurantes, e notas de avaliação;
  *Cidades como: Bimingham, Doha, Houston e São Paulo possuem mais tipos de culinárias;
  * Restaurantes brasileiros localizados em Brasília possuem menor média de avaliação;
  *Em geral, culinária do tipo Continental, European, BBQ e North Indian possuem maior quantidade de avaliações realizadas na plataforma.
      

# 5. O produto final do projeto
    O produto final é um painel online, hospedado em um Cloud e disponível para acesso em qualquer dispositivo conectado à internet.
    O painel pode ser acessado através desse link: https://zomato-restaurant.streamlit.app/
    
# 6. Conclusão

  O objetivo desse projeto é criar um conjunto de gráficos e/ou tabelas que exibam essas métricas da melhor forma possível para o CEO.

  * Podemos concluir que 15 países e 125 cidades estão cadastradas na plataforma, totalizado 6.929 restaurantes cadastrados, compreendendo as principais cidades mais turisticas de cada país;
  * A Índia lidera com o número de maior número de cidades, restaurantes e tipos de culinárias registrados na plataforma;
  * Apesar da diferença em relação a moeda corrente entre os países, Adelaide foi considerada a cidade com maior preço médio de prato para dois;
  * A Índia possui os restaurantes com menor nota de avaliação segundo os usuários;
  * Em geral, poucos restaurantes brasileiros possuem avaliações acima de 4.0, provavelmente devido a baixa adesão dos usuários em classificar os restaurantes após a sua visita;
  * A culinária Continental possui a maior quantidade de votos registrados na plataforma, podendo indicar a maior preferência dos usuário da plataforma. 


# 7. Próximo passos

    1. Reduzir o número de métricas e padronizar a moeda em Dollar através da padronização das moedas dos demais países
    2. Criar novos filtros para identificar possíveis insight relacionados aos restaurantes e tipos culinários referente à preferência do cliente.
    3. Adicionar novas visões de negócio, utilizando análises estatisticas mais refinadas.
