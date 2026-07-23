![Texto alternativo](https://raw.githubusercontent.com/evmpython/Minicurso_queimadas_UNIFEI_INPE_NOTTUS_2026/main/04_logos/banner_queimadas.png)
---

# 💻 Minicurso: 
*Processamento e Visualização de Dados de Queimadas*
---

### Ministrantes:
- Dr. Enrique Mattos (UNIFEI)
- Dr. Guilherme Martins (NOTTUS Meteorologia)
- Dra. Vanúcia Schumacher (INPE)
- Paulo Cunha (INPE)

### Colaboradores:
- Diego Souza (INPE)

---

## 📋 Informações Gerais

- **Formato:** Online 
- **Data:** 29, 30 e 31 de julho de 2026
- **Horário:** 08:30 às 12:00 horas 
- **Vagas disponíveis:** 150 vagas via RNP e ilimitado via RNP Play
- **Carga Horária:** 10,5 horas

---

## 🎯 Objetivo do Curso
<p align="justify"> O curso tem como objetivo ensinar aos alunos como acessar e analisar dados de focos de calor de queimadas detectadas por satélites polares e geoestacionários. O curso terá duas componentes: teórica e prática. Na componente teórica serão abordados os fundamentos da detecção de focos de calor por satélite, tipos de satélites disponíveis e canal espectral utilizado. Na componente prática será empregado a linguagem de programação Python e o Google Colab, onde os alunos aprenderão a baixar os dados, processar, gerar gráficos e analisar os resultados. A base de dados da aula prática consiste dos dados de focos de calor processados e disponibilizados pelo INPE e os dados de queimadas disponibilizados pela Plataforma Google Earth Engine (GEE). </p>

Ao final do curso os alunos terão a capacidade de: 

- Analisar séries temporais de focos de calor
- Gerar análises climatológicas do acumulado e anomalia de focos de calor
- Analisar risco de fogo 
- Analisar imagens de satélite para identificação visual de queimadas
- Trabalhar com índices espectrais para detecção de queimadas
- Calcular tamanho da área queimada


---

## 📊 Programação do Curso:
![Texto alternativo](https://raw.githubusercontent.com/evmpython/Minicurso_queimadas_UNIFEI_INPE_NOTTUS_2026/main/04_logos/programacao_gif.jpg)

---

## 🛰️ Conteúdo Programático

- ### Visão Geral do Programa Queimadas (INPE)

### Atividades de Pesquisa Relacionadas a Queimadas e Aerossóis 

### Aula Teórica I: Introdução sobre Estimativa de Queimadas por Satélites 

### Aula Teórica II: Sattélites Sentinel e Landsat 

### Atividade Prática I: Processamento e Visualização de Dados de Focos de Calor disponibilizados pelo INPE
1. Exploração e padronização de dados de focos de queimadas.
2. Manipulação de GeoDataFrames da América do Sul e do Brasil.
3. Sistemas de referência de coordenadas (CRS) e reprojeção.
4. Filtragem espacial e temporal de focos de queimadas.
5. Agregação de dados em diferentes escalas temporais.
6. Visualização dos resultados por meio de tabelas, gráficos e mapas estáticos e interativos.

### Atividade Prática II: Processamento e Visualização de Dados de Queimadas com Google Earth Engine (GEE)
1.  Conhecendo o Google Earth Engine (GEE)
2.  Mapas Interativos com Geemap
3.  Carregando Dados no Google Earth Engine (GEE)
4.  Detecção de Focos de Calor com os Dados FIRMS
5.  Detecção de Focos de Calor com os Dados VIIRS (NOAA-20)
6.  Detecção de Focos de Calor com os Dados GOES-16
7.  Visualização das Cicatrizes das Queimadas Através da Composição de Bandas do Sentinel-2
8.  Normalized Difference Vegetation Index (NDVI)
9.  Normalized Burn Ratio (NBR)
10.  Analytical Burned Area Index (ABAI)
11. Detecção de Área Queimada e Geração de Séries Temporais com os Satélites Landsat
12. Produtos MOD14A1, MYD14A1 e MCD64A1 de Queimadas do Sensor MODIS
13. Produto MCD19A2 de Aerossol dos Satélites AQUA e TERRA
14. Produtos de Gases Amosféricos Estimados pelo Sentinel-5P
15. Principais Imagens e Índices numa Única Figura

---

## 🎓 Público-Alvo

Estudantes de graduação, pós-graduação e profissionais da área de Meteorologia e Ciências Ambientais.

---
> [!WARNING]
> Pré-requisitos necessários para executar os códigos: 
  > 1. Possuir uma conta de E-mail do Gmail
  > 2. Possuir uma conta no Google Earth Engine: https://earthengine.google.com/. Veja vídeo explicando como criar uma conta no GEE e a ID do projeto: https://www.youtube.com/watch?v=RuKTG0rHHSw&t=6s 

---
> [!TIP]
> Conhecimento básico de Python (desejável)

---

## 📁 Material do Curso

Todo o material está disponível no GitHub:  
https://github.com/evmpython/Minicurso_queimadas_UNIFEI_INPE_NOTTUS_2026

---

## 📂 Estrutura do Repositório do Curso
O repositório do curso possui as seguintes diretórios e códigos python:

- **Diretórios:**
   > - **01_utils:** funções extras utilizadas nos códigos das aulas
   > - **02_figuras_produzidas:** exemplos das figuras que serão produzidas no curso
   > - **03_material_complementar:** material de leitura teórico complementar 
   > - **04_logos:** logos/figura utilizadas dentros dos códigos
 
- **Códigos:**
   > - **AULA_1_Queimadas_com_Dados_do_INPE.ipynb:** código python da Aula 01 - Processamento e Visualização de Dados de Focos de Calor Disponibilizados pelo INPE
   > - **AULA_2_Queimadas_com_Google_Earth_Engine.ipynb:** código python da Aula 02 - Processamento e Visualização de Dados de Queimadas com Google Earth Engine (GEE)
   > - **01_Material_Pre_Aula_02.pdf:** material pré-curso da atividade II. 
---

## Observações
- Os materiais do curso serão disponibilizados no Moodle do INPE: https://moodle.cptec.inpe.br/
- A atividade pré-curso será disponibilizada na semana anterior ao treinamento
- As sessões online serão realizadas através da ferramenta Conferência Web da RNP (o link de acesso será enviado previamente)
- A sala será aberta 10 minutos antes do início das sessões
---

## 🏫 Instituições Envolvidas

- **Universidade Federal de Itajubá (UNIFEI)**
- **Nottus Meteorologia**
- **Instituto Nacional de Pesquisas Espaciais (INPE)**
---

### 📧 Contato
Para mais informações, entre em contato através dos e-mails: 
- Enrique Mattos - enrique@unifei.edu.br
- Guilherme Martins - jgmasantos@gmail.com
- Diego Souza - diego.souza@inpe.br



