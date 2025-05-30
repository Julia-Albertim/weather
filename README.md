# Clima Interativo

Este é um aplicativo web que permite consultar o clima atual de qualquer cidade do mundo, seja através de pesquisa direta ou clicando em qualquer ponto do mapa.

## Funcionalidades

- Pesquisa de clima por nome de cidade
- Obtenção do clima clicando em qualquer ponto do mapa
- Exibição detalhada de informações meteorológicas:
  - Temperatura atual e sensação térmica
  - Temperaturas mínima e máxima
  - Umidade e velocidade do vento
  - Horários de nascer e pôr do sol
  - Visibilidade
- Interface responsiva e moderna
- Marcadores no mapa para localização selecionada

## Tecnologias Utilizadas

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Mapa**: Leaflet.js
- **API de Clima**: OpenWeatherMap

## Como Executar

1. Certifique-se de ter o Python instalado
2. Instale as dependências:
   ```
   pip install flask requests
   ```
3. Execute o aplicativo:
   ```
   python app.py
   ```
4. Acesse no navegador: `http://localhost:5000`

## Estrutura de Arquivos

- `app.py` - Aplicação Flask com rotas para obtenção de dados climáticos
- `templates/index.html` - Interface do usuário com mapa interativo
- `static/` - Diretório para arquivos estáticos (se necessário)

## API Key

O aplicativo utiliza a API do OpenWeatherMap. A chave API já está configurada no código.

## Personalização

Você pode personalizar ainda mais o visual do aplicativo modificando o CSS no arquivo `index.html`.
