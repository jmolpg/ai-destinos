import random
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors
import streamlit as st


num_clientes = 500


destinos = pd.DataFrame([
    {'nome': 'Paris', 'pais': 'França', 'tipo': ['Cultura'], 'idioma': 'Francês', 'preco_moeda': 1.2, 'visto': 'Não', 'custo_medio': 15000},
    {'nome': 'Rio de Janeiro', 'pais': 'Brasil', 'tipo': ['Praia'], 'idioma': 'Português', 'preco_moeda': 1.0, 'visto': 'Não', 'custo_medio': 5000},
    {'nome': 'Nova York', 'pais': 'EUA', 'tipo': ['Cultura'], 'idioma': 'Inglês', 'preco_moeda': 1.1, 'visto': 'Sim', 'custo_medio': 18000},
    {'nome': 'Bangkok', 'pais': 'Tailândia', 'tipo': ['Gastronomia'], 'idioma': 'Tailandês', 'preco_moeda': 0.03, 'visto': 'Não', 'custo_medio': 9000},
    {'nome': 'Vancouver', 'pais': 'Canadá', 'tipo': ['Natureza'], 'idioma': 'Inglês', 'preco_moeda': 1.3, 'visto': 'Sim', 'custo_medio': 16000},
    {'nome': 'Barcelona', 'pais': 'Espanha', 'tipo': ['Cultura'], 'idioma': 'Espanhol', 'preco_moeda': 1.1, 'visto': 'Não', 'custo_medio': 14000},
    {'nome': 'Sydney', 'pais': 'Austrália', 'tipo': ['Natureza'], 'idioma': 'Inglês', 'preco_moeda': 1.5, 'visto': 'Sim', 'custo_medio': 20000},
    {'nome': 'Tokyo', 'pais': 'Japão', 'tipo': ['Cultura'], 'idioma': 'Japonês', 'preco_moeda': 1.0, 'visto': 'Sim', 'custo_medio': 18000},
    {'nome': 'Cancun', 'pais': 'México', 'tipo': ['Praia'], 'idioma': 'Espanhol', 'preco_moeda': 0.05, 'visto': 'Não', 'custo_medio': 8000},
    {'nome': 'Cape Town', 'pais': 'África do Sul', 'tipo': ['Natureza'], 'idioma': 'Inglês', 'preco_moeda': 0.2, 'visto': 'Sim', 'custo_medio': 15000},
    {'nome': 'Londres', 'pais': 'Reino Unido', 'tipo': ['Cultura'], 'idioma': 'Inglês', 'preco_moeda': 1.4, 'visto': 'Sim', 'custo_medio': 19000},
    {'nome': 'Roma', 'pais': 'Itália', 'tipo': ['Cultura'], 'idioma': 'Italiano', 'preco_moeda': 1.2, 'visto': 'Não', 'custo_medio': 14000},
    {'nome': 'Lisboa', 'pais': 'Portugal', 'tipo': ['Cultura'], 'idioma': 'Português', 'preco_moeda': 1.1, 'visto': 'Não', 'custo_medio': 13000},
    {'nome': 'Berlim', 'pais': 'Alemanha', 'tipo': ['Cultura'], 'idioma': 'Alemão', 'preco_moeda': 1.2, 'visto': 'Não', 'custo_medio': 15000},
    {'nome': 'Pequim', 'pais': 'China', 'tipo': ['Cultura'], 'idioma': 'Mandarim', 'preco_moeda': 0.15, 'visto': 'Sim', 'custo_medio': 16000},
    {'nome': 'Atenas', 'pais': 'Grécia', 'tipo': ['Cultura'], 'idioma': 'Grego', 'preco_moeda': 1.2, 'visto': 'Não', 'custo_medio': 14000},
    {'nome': 'Istambul', 'pais': 'Turquia', 'tipo': ['Cultura'], 'idioma': 'Turco', 'preco_moeda': 0.05, 'visto': 'Não', 'custo_medio': 13000},
    {'nome': 'Dubai', 'pais': 'Emirados Árabes', 'tipo': ['Compras'], 'idioma': 'Árabe', 'preco_moeda': 1.3, 'visto': 'Sim', 'custo_medio': 21000},
    {'nome': 'Moscou', 'pais': 'Rússia', 'tipo': ['Cultura'], 'idioma': 'Russo', 'preco_moeda': 0.014, 'visto': 'Sim', 'custo_medio': 15000},
    {'nome': 'Buenos Aires', 'pais': 'Argentina', 'tipo': ['Gastronomia'], 'idioma': 'Espanhol', 'preco_moeda': 0.004, 'visto': 'Não', 'custo_medio': 12000},
    {'nome': 'Seul', 'pais': 'Coreia do Sul', 'tipo': ['Cultura'], 'idioma': 'Coreano', 'preco_moeda': 0.0008, 'visto': 'Sim', 'custo_medio': 16000},
    {'nome': 'Los Angeles', 'pais': 'EUA', 'tipo': ['Praia'], 'idioma': 'Inglês', 'preco_moeda': 1.1, 'visto': 'Sim', 'custo_medio': 18000},
    {'nome': 'Bangalore', 'pais': 'Índia', 'tipo': ['Negócios'], 'idioma': 'Hindi', 'preco_moeda': 0.012, 'visto': 'Sim', 'custo_medio': 10000},
    {'nome': 'Cairo', 'pais': 'Egito', 'tipo': ['Cultura'], 'idioma': 'Árabe', 'preco_moeda': 0.064, 'visto': 'Não', 'custo_medio': 12000},
    {'nome': 'Amsterdã', 'pais': 'Holanda', 'tipo': ['Cultura'], 'idioma': 'Holandês', 'preco_moeda': 1.2, 'visto': 'Não', 'custo_medio': 15000},
    {'nome': 'Zurique', 'pais': 'Suíça', 'tipo': ['Natureza'], 'idioma': 'Alemão', 'preco_moeda': 1.5, 'visto': 'Não', 'custo_medio': 20000},
    {'nome': 'Praga', 'pais': 'República Tcheca', 'tipo': ['Cultura'], 'idioma': 'Tcheco', 'preco_moeda': 0.043, 'visto': 'Não', 'custo_medio': 13000},
    {'nome': 'Helsinque', 'pais': 'Finlândia', 'tipo': ['Natureza'], 'idioma': 'Finlandês', 'preco_moeda': 1.1, 'visto': 'Não', 'custo_medio': 15000},
    {'nome': 'Oslo', 'pais': 'Noruega', 'tipo': ['Natureza'], 'idioma': 'Norueguês', 'preco_moeda': 1.2, 'visto': 'Não', 'custo_medio': 16000},
    {'nome': 'Santiago', 'pais': 'Chile', 'tipo': ['Cultura'], 'idioma': 'Espanhol', 'preco_moeda': 0.05, 'visto': 'Não', 'custo_medio': 1200},
    {'nome': 'Miami', 'pais': 'EUA', 'tipo': ['Praia', 'Compras'], 'idioma': 'Inglês', 'preco_moeda': 1.1, 'visto': 'Sim', 'custo_medio': 17000},
    {'nome': 'San Francisco', 'pais': 'EUA', 'tipo': ['Cultura', 'Tecnologia'], 'idioma': 'Inglês', 'preco_moeda': 1.1, 'visto': 'Sim', 'custo_medio': 18000},
    {'nome': 'Chicago', 'pais': 'EUA', 'tipo': ['Cultura', 'Negócios'], 'idioma': 'Inglês', 'preco_moeda': 1.1, 'visto': 'Sim', 'custo_medio': 16000},
    {'nome': 'Toronto', 'pais': 'Canadá', 'tipo': ['Cultura', 'Natureza'], 'idioma': 'Inglês', 'preco_moeda': 1.3, 'visto': 'Sim', 'custo_medio': 15000},
    {'nome': 'Montreal', 'pais': 'Canadá', 'tipo': ['Cultura', 'Gastronomia'], 'idioma': 'Francês', 'preco_moeda': 1.3, 'visto': 'Sim', 'custo_medio': 14000},
    {'nome': 'Lyon', 'pais': 'França', 'tipo': ['Cultura', 'Gastronomia'], 'idioma': 'Francês', 'preco_moeda': 1.2, 'visto': 'Não', 'custo_medio': 14000},
    {'nome': 'Marselha', 'pais': 'França', 'tipo': ['Praia', 'Cultura'], 'idioma': 'Francês', 'preco_moeda': 1.2, 'visto': 'Não', 'custo_medio': 13500},
    {'nome': 'Nice', 'pais': 'França', 'tipo': ['Praia', 'Cultura'], 'idioma': 'Francês', 'preco_moeda': 1.2, 'visto': 'Não', 'custo_medio': 14000},
    {'nome': 'Valência', 'pais': 'Espanha', 'tipo': ['Praia', 'Cultura'], 'idioma': 'Espanhol', 'preco_moeda': 1.1, 'visto': 'Não', 'custo_medio': 13000},
    {'nome': 'Sevilha', 'pais': 'Espanha', 'tipo': ['Cultura', 'História'], 'idioma': 'Espanhol', 'preco_moeda': 1.1, 'visto': 'Não', 'custo_medio': 12500},
    {'nome': 'Malaga', 'pais': 'Espanha', 'tipo': ['Praia', 'Cultura'], 'idioma': 'Espanhol', 'preco_moeda': 1.1, 'visto': 'Não', 'custo_medio': 12000},
    {'nome': 'Bruxelas', 'pais': 'Bélgica', 'tipo': ['Cultura', 'Gastronomia'], 'idioma': 'Francês', 'preco_moeda': 1.2, 'visto': 'Não', 'custo_medio': 14000},
    {'nome': 'Antuérpia', 'pais': 'Bélgica', 'tipo': ['Cultura', 'Compras'], 'idioma': 'Holandês', 'preco_moeda': 1.2, 'visto': 'Não', 'custo_medio': 13500},
    {'nome': 'Bruges', 'pais': 'Bélgica', 'tipo': ['Cultura', 'História'], 'idioma': 'Holandês', 'preco_moeda': 1.2, 'visto': 'Não', 'custo_medio': 13000},
    {'nome': 'Zurique', 'pais': 'Suíça', 'tipo': ['Natureza', 'Luxo'], 'idioma': 'Alemão', 'preco_moeda': 1.5, 'visto': 'Não', 'custo_medio': 20000},
    {'nome': 'Genebra', 'pais': 'Suíça', 'tipo': ['Cultura', 'Natureza'], 'idioma': 'Francês', 'preco_moeda': 1.5, 'visto': 'Não', 'custo_medio': 19500},
    {'nome': 'Lucerna', 'pais': 'Suíça', 'tipo': ['Natureza', 'História'], 'idioma': 'Alemão', 'preco_moeda': 1.5, 'visto': 'Não', 'custo_medio': 18000},
    {'nome': 'Innsbruck', 'pais': 'Áustria', 'tipo': ['Montanha', 'Esportes'], 'idioma': 'Alemão', 'preco_moeda': 1.2, 'visto': 'Não', 'custo_medio': 15000},
    {'nome': 'Viena', 'pais': 'Áustria', 'tipo': ['Cultura', 'História'], 'idioma': 'Alemão', 'preco_moeda': 1.2, 'visto': 'Não', 'custo_medio': 16000},
    {'nome': 'Salzburg', 'pais': 'Áustria', 'tipo': ['Cultura', 'Montanha'], 'idioma': 'Alemão', 'preco_moeda': 1.2, 'visto': 'Não', 'custo_medio': 15500},
    {'nome': 'Budapeste', 'pais': 'Hungria', 'tipo': ['Cultura', 'História'], 'idioma': 'Húngaro', 'preco_moeda': 0.045, 'visto': 'Não', 'custo_medio': 12500},
    {'nome': 'Praga', 'pais': 'República Tcheca', 'tipo': ['Cultura', 'História'], 'idioma': 'Tcheco', 'preco_moeda': 0.043, 'visto': 'Não', 'custo_medio': 13000},
    {'nome': 'Varsóvia', 'pais': 'Polônia', 'tipo': ['Cultura', 'História'], 'idioma': 'Polonês', 'preco_moeda': 0.04,'visto': 'Não', 'custo_medio': 12000},
    {'nome': 'Cracóvia', 'pais': 'Polônia', 'tipo': ['Cultura', 'História'], 'idioma': 'Polonês', 'preco_moeda': 0.04,'visto': 'Não', 'custo_medio': 11500},
    {'nome': 'Estocolmo', 'pais': 'Suécia', 'tipo': ['Cultura', 'Natureza'], 'idioma': 'Sueco', 'preco_moeda': 1.2,'visto': 'Não', 'custo_medio': 15500},
    {'nome': 'Gotemburgo', 'pais': 'Suécia', 'tipo': ['Natureza', 'História'], 'idioma': 'Sueco', 'preco_moeda': 1.2,'visto': 'Não', 'custo_medio': 15000},
    {'nome': 'Copenhague', 'pais': 'Dinamarca', 'tipo': ['Cultura', 'História'], 'idioma': 'Dinamarquês','preco_moeda': 1.3, 'visto': 'Não', 'custo_medio': 16000},
    {'nome': 'Aarhus', 'pais': 'Dinamarca', 'tipo': ['Cultura', 'História'], 'idioma': 'Dinamarquês','preco_moeda': 1.3, 'visto': 'Não', 'custo_medio': 15000},
    {'nome': 'Helsinque', 'pais': 'Finlândia', 'tipo': ['Natureza', 'História'], 'idioma': 'Finlandês','preco_moeda': 1.1, 'visto': 'Não', 'custo_medio': 15000},
    {'nome': 'Reykjavik', 'pais': 'Islândia', 'tipo': ['Natureza', 'Aventura'], 'idioma': 'Islandês','preco_moeda': 1.4, 'visto': 'Não', 'custo_medio': 18000},
    {'nome': 'Oslo', 'pais': 'Noruega', 'tipo': ['Natureza', 'História'], 'idioma': 'Norueguês', 'preco_moeda': 1.2,'visto': 'Não', 'custo_medio': 16000},
    {'nome': 'Bergen', 'pais': 'Noruega', 'tipo': ['Natureza', 'Aventura'], 'idioma': 'Norueguês', 'preco_moeda': 1.2,'visto': 'Não', 'custo_medio': 15500},
    {'nome': 'Hanoi', 'pais': 'Vietnã', 'tipo': ['Cultura', 'Gastronomia'], 'idioma': 'Vietnamita','preco_moeda': 0.000042, 'visto': 'Não', 'custo_medio': 9000},
    {'nome': 'Ho Chi Minh', 'pais': 'Vietnã', 'tipo': ['Cultura', 'Gastronomia'], 'idioma': 'Vietnamita','preco_moeda': 0.000042, 'visto': 'Não', 'custo_medio': 9500},
    {'nome': 'Singapura', 'pais': 'Singapura', 'tipo': ['Cultura', 'Tecnologia'], 'idioma': 'Inglês','preco_moeda': 1.3, 'visto': 'Não', 'custo_medio': 20000},
    {'nome': 'Kuala Lumpur', 'pais': 'Malásia', 'tipo': ['Cultura', 'Compras'], 'idioma': 'Malaio', 'preco_moeda': 0.22,'visto': 'Não', 'custo_medio': 14000},
    {'nome': 'Bali', 'pais': 'Indonésia', 'tipo': ['Praia', 'Cultura'], 'idioma': 'Indonésio', 'preco_moeda': 0.000067,'visto': 'Não', 'custo_medio': 12000},
    {'nome': 'Jacarta', 'pais': 'Indonésia', 'tipo': ['Cultura', 'Negócios'], 'idioma': 'Indonésio','preco_moeda': 0.000067, 'visto': 'Não', 'custo_medio': 10000},
    {'nome': 'Doha', 'pais': 'Catar', 'tipo': ['Compras', 'Luxo'], 'idioma': 'Árabe', 'preco_moeda': 1.3, 'visto': 'Sim', 'custo_medio': 20000},
    {'nome': 'Riyadh', 'pais': 'Arábia Saudita', 'tipo': ['Negócios', 'Cultura'], 'idioma': 'Árabe', 'preco_moeda': 1.3, 'visto': 'Sim', 'custo_medio': 19000}
])

idiomas_unicos = sorted(destinos['idioma'].unique())
idiomas = ['Todos'] + idiomas_unicos

preferencias_unicas = sorted({tipo for tipos in destinos['tipo'] for tipo in tipos})
preferencias = ['Todos'] + preferencias_unicas
filtro_visto = ['Todos', 'Sim', 'Não']
filtro_moeda = ['Todos', 'Valorizada', 'Desvalorizada']

def gerar_clientes():
    clientes = []
    for i in range(num_clientes):
        idade = random.randint(18, 65)
        freq_viagem = random.randint(1, 10)
        gasto = round(random.uniform(500, 20000), 2)
        idioma = random.choice(idiomas[1:])
        pref = random.choice(preferencias[1:])
        visitados = [random.choice([0, 1]) for _ in range(len(destinos))]
        recomenda = [random.choice([0, 1]) for _ in range(len(destinos))]
        crianca = random.choice([0, 1])
        moeda = random.choice(['Valorizada', 'Desvalorizada'])
        clientes.append([i, idade, freq_viagem, gasto, idioma, pref, crianca, moeda] + visitados + recomenda)
    colunas = ['cliente_id', 'idade', 'freq_viagem', 'gasto_medio', 'idioma', 'preferencia', 'crianca', 'moeda'] + \
              destinos['nome'].tolist() + [nome + '_recomenda' for nome in destinos['nome'].tolist()]
    return pd.DataFrame(clientes, columns=colunas)

df_clientes = gerar_clientes()

preferencia_map = {p: i for i, p in enumerate(preferencias[1:])}
idioma_map = {i: n for n, i in enumerate(idiomas[1:])}

df_clientes['preferencia_num'] = df_clientes['preferencia'].map(preferencia_map)
df_clientes['idioma_num'] = df_clientes['idioma'].map(idioma_map)

features = ['idade', 'freq_viagem', 'gasto_medio', 'preferencia_num', 'idioma_num']
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df_clientes[features])

knn = NearestNeighbors(n_neighbors=5)
knn.fit(X_scaled)

st.title("Recomendação Inteligente de Destinos")

idade = st.sidebar.slider("Idade", 18, 65, 30)
freq_viagem = st.sidebar.slider("Frequência de viagens/ano", 1, 10, 3)
gasto_medio = st.sidebar.slider("Gasto médio por viagem (R$)", 500, 20000, 9000)
idioma_cliente = st.sidebar.selectbox("Idioma preferido", idiomas)
preferencia_cliente = st.sidebar.selectbox("Preferência de viagem", preferencias)
crianca = st.sidebar.checkbox("Viajando com criança")
visto_cliente = st.sidebar.selectbox("O destino exige visto?", filtro_visto)
moeda_cliente = st.sidebar.selectbox("Moeda valorizada/desvalorizada", filtro_moeda)

novo_cliente = pd.DataFrame({
    'idade': [idade],
    'freq_viagem': [freq_viagem],
    'gasto_medio': [gasto_medio],
    'preferencia_num': [preferencia_map.get(preferencia_cliente, 0)],
    'idioma_num': [idioma_map.get(idioma_cliente, 0)]
})
novo_scaled = scaler.transform(novo_cliente[features])
_, indices = knn.kneighbors(novo_scaled)
vizinhos = df_clientes.iloc[indices[0]].copy()

peso_idioma = 5
peso_visto = 4
peso_pref = 1
peso_moeda = 1
peso_idade = 1
peso_freq = 1
peso_gasto = 1
peso_crianca = 3

def calcular_pontuacao(destino, vizinhos, idade, freq_viagem, gasto_medio, crianca):
    pontuacao = 0
    tipos_destino = destino['tipo'] if isinstance(destino['tipo'], list) else [destino['tipo']]
    destino_idioma = destino['idioma']
    destino_visto = destino.get('visto', '')
    destino_moeda = 'Valorizada' if destino['preco_moeda'] >= 1 else 'Desvalorizada'

    for vizinho in vizinhos:
        if vizinho.get('idioma', '') == destino_idioma:
            pontuacao += peso_idioma * vizinho[destino['nome'] + '_recomenda']
        if any(t == vizinho['preferencia'] for t in tipos_destino):
            pontuacao += peso_pref * vizinho[destino['nome'] + '_recomenda']
        if vizinho.get('visto', '') == destino_visto:
            pontuacao += peso_visto * vizinho[destino['nome'] + '_recomenda']
        if vizinho.get('moeda', '') == destino_moeda:
            pontuacao += peso_moeda * vizinho[destino['nome'] + '_recomenda']
        if idade - 5 <= vizinho['idade'] <= idade + 5:
            pontuacao += peso_idade * vizinho[destino['nome'] + '_recomenda']
        if freq_viagem - 1 <= vizinho['freq_viagem'] <= freq_viagem + 1:
            pontuacao += peso_freq * vizinho[destino['nome'] + '_recomenda']
        if gasto_medio * 0.8 <= vizinho['gasto_medio'] <= gasto_medio * 1.2:
            pontuacao += peso_gasto * vizinho[destino['nome'] + '_recomenda']
        if crianca and vizinho['crianca'] == 1:
            pontuacao += peso_crianca * vizinho[destino['nome'] + '_recomenda']

    return pontuacao

vizinhos = vizinhos.loc[:, ~vizinhos.columns.duplicated()]
vizinhos_dict = vizinhos.to_dict(orient='records')

recomendacoes = []

for _, d in destinos.iterrows():
    tipos_destino = d['tipo'] if isinstance(d['tipo'], list) else [d['tipo']]
    idioma_ok = idioma_cliente == 'Todos' or d['idioma'] == idioma_cliente
    pref_ok = preferencia_cliente == 'Todos' or preferencia_cliente in tipos_destino
    visto_ok = visto_cliente == 'Todos' or d.get('visto', '') == visto_cliente
    if moeda_cliente == 'Valorizada':
        moeda_ok = d['preco_moeda'] >= 1
    elif moeda_cliente == 'Desvalorizada':
        moeda_ok = d['preco_moeda'] < 1
    else:
        moeda_ok = True
    gasto_ok = d['custo_medio'] <= gasto_medio * 1.5
    crianca_ok = True

    if idioma_ok and pref_ok and visto_ok and moeda_ok and gasto_ok and crianca_ok:
        recomendacoes.append(d.to_dict())

if not recomendacoes:
    destinos_alternativos = []
    for _, d in destinos.iterrows():
        idioma_ok = idioma_cliente == 'Todos' or d['idioma'] == idioma_cliente
        visto_ok = visto_cliente == 'Todos' or d.get('visto', '') == visto_cliente
        if idioma_ok and visto_ok:
            destinos_alternativos.append(d.to_dict())

    if destinos_alternativos:
        destinos_alternativos.sort(
            key=lambda x: calcular_pontuacao(x, vizinhos_dict, idade, freq_viagem, gasto_medio, crianca),
            reverse=True
        )
        destino_sugerido = destinos_alternativos[0]
        st.warning(
            f"Não encontramos nenhum destino compatível com todos os filtros, "
            f"mas outras pessoas parecidas com seu perfil recomendam o destino: {destino_sugerido['nome']}"
        )
        recomendacoes.append(destino_sugerido)
    else:
        st.error(
            "Não encontramos nenhum destino compatível com os filtros, "
            "tente alterar suas preferências."
        )

recomendacoes.sort(
    key=lambda x: calcular_pontuacao(x, vizinhos_dict, idade, freq_viagem, gasto_medio, crianca),
    reverse=True
)

st.subheader("Destinos recomendados")
st.markdown("---")

for destino in recomendacoes:
    cor_visto = "#d9534f" if destino.get('visto', 'Não') == 'Sim' else "#5bc0de"

    if destino['custo_medio'] > 5000:
        cor_custo = "#d9534f"
    elif destino['custo_medio'] < 2000:
        cor_custo = "#5cb85c"
    else:
        cor_custo = "#337ab7"

    st.markdown(f"""
    <div style="padding: 15px; margin-bottom: 20px; border-radius: 15px; background-color: #f9f9f9; box-shadow: 2px 2px 5px rgba(0,0,0,0.1);">
        <h3 style="margin: 0; color: #1f4e79;">{destino['nome']}, {destino['pais']}</h3>
        <p style="margin: 5px 0; color: #2b7a78;"><b>Idioma:</b> {destino['idioma']}</p>
        <p style="margin: 5px 0; color: #3a3a3a;"><b>Preferências:</b> {', '.join(destino['tipo'])}</p>
        <p style="margin: 5px 0; color: {cor_custo};"><b>Custo médio:</b> R$ {destino['custo_medio']:,}</p>
        <p style="margin: 5px 0; color: {cor_visto};"><b>Visto necessário:</b> {destino.get('visto', 'Não')}</p>
    </div>
    """, unsafe_allow_html=True)
