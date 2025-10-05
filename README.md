# ai-destinos
aplicação interativa de recomendação de destinos de viagem construída com Python, Streamlit e scikit-learn
O sistema sugere destinos personalizados com base no perfil do usuário, histórico de outros clientes e preferências individuais.

Funcionalidades

Recomendação de destinos com base em idade, frequência de viagens, gasto médio, idioma preferido, tipo de viagem, se viaja com criança, exigência de visto e valorização da moeda.

Pontuação dinâmica que leva em consideração similaridade com clientes existentes.

Interface interativa em Streamlit com filtros na barra lateral.

Destinos destacados com cores para indicar custo médio (vermelho = alto, verde = baixo, azul = médio) e visto necessário (vermelho se exigido).

Tecnologias Utilizadas: Python 3.x, Pandas, Scikit-learn (StandardScaler e NearestNeighbors), Streamlit

Como Executar:

Clone este repositório, Instale as dependências:

pip install pandas scikit-learn streamlit

Execute a aplicação:

streamlit run main.py

main.py - Código principal da aplicação Streamlit.

destinos - DataFrame com informações de destinos, incluindo país, idioma, tipo de viagem, custo médio, preço da moeda e exigência de visto.

df_clientes - DataFrame simulado de clientes com atributos pessoais e histórico de destinos visitados.

Funções de pré-processamento de dados e cálculo de similaridade usando KNN.

Lógica de filtragem e pontuação para determinar os destinos recomendados.

Uso:

Ajuste os filtros na barra lateral (idade, frequência de viagens, gasto médio, idioma, preferência, etc.).

A aplicação exibirá os destinos recomendados com base no perfil e nas pontuações calculadas.

Caso nenhum destino satisfaça todos os filtros, o sistema sugere o destino mais recomendado de clientes similares.

Personalização

Limites de cores e custos podem ser ajustados para refletir o perfil do usuário ou as condições de viagem.

Pesos na pontuação (peso_idioma, peso_visto, peso_pref, etc.) podem ser alterados para dar mais importância a certos critérios.

Exemplo de Tela

Destinos recomendados aparecem em cards estilizados com:

Nome do destino e país

Idioma principal

Preferências (tipo de viagem)

Custo médio (vermelho = alto, verde = baixo, azul = médio)

Visto necessário (vermelho se exigido)
