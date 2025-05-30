from flask import Flask, request, jsonify, render_template
import requests
import os
from datetime import datetime, timezone, timedelta

app = Flask(__name__)

# Substitua pela sua chave da API do OpenWeatherMap
API_KEY = ("0153a042112f9529edbc2bad5372a198")

def converter_timestamp(timestamp, offset_segundos):
    # Cria um objeto datetime em UTC e aplica o offset do fuso horário
    dt = datetime.fromtimestamp(timestamp, tz=timezone.utc) + timedelta(seconds=offset_segundos)
    return dt.strftime('%H:%M')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/clima")
def obter_clima():
    cidade = request.args.get("cidade")
    lat = request.args.get("lat")
    lon = request.args.get("lon")

    # Se temos coordenadas, usamos elas em vez do nome da cidade
    if lat and lon:
        link = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&lang=pt_br&units=metric"
    elif cidade:
        link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br&units=metric"
    else:
        return jsonify({"erro": "Informe o nome da cidade ou coordenadas (lat/lon)"}), 400

    try:
        resposta = requests.get(link)
        resposta.raise_for_status()
        dados = resposta.json()
    except requests.exceptions.RequestException as e:
        return jsonify({"erro": f"Erro na requisição: {str(e)}"}), 500
    
    timezone_offset = dados.get('timezone', 0)

    try:
        resultado = {
            "cidade": dados["name"],
            "descricao": dados['weather'][0]['description'],
            "icone": dados['weather'][0]['icon'],
            "timezone": dados['timezone'],
            "temperatura": dados['main']['temp'],
            "sensacao": dados['main']['feels_like'],
            "temp_min": dados['main']['temp_min'],
            "temp_max": dados['main']['temp_max'],
            "pressao": dados['main']['pressure'],
            "umidade": dados['main']['humidity'],
            "nivel_mar": dados['main'].get('sea_level', 'não informado'),
            "visibilidade": dados['visibility'],
            "vento": dados['wind']['speed'],
            "nuvens": dados['clouds']['all'],
            "pais": dados['sys']['country'],
            "nascer_do_sol": converter_timestamp(dados['sys']['sunrise'], timezone_offset),
            "por_do_sol": converter_timestamp(dados['sys']['sunset'], timezone_offset),
            "latitude": dados['coord']['lat'],
            "longitude": dados['coord']['lon'],
        }
        
        return jsonify(resultado)
    except KeyError:
        return jsonify({"erro": "Erro ao ler os dados do clima"}), 500

@app.route("/geocode")
def geocode():
    lat = request.args.get("lat")
    lon = request.args.get("lon")
    
    if not lat or not lon:
        return jsonify({"erro": "Informe latitude e longitude"}), 400
    
    # Usamos a API de geocodificação reversa do OpenWeatherMap para obter o nome do local
    link = f"https://api.openweathermap.org/geo/1.0/reverse?lat={lat}&lon={lon}&limit=1&appid={API_KEY}"
    
    try:
        resposta = requests.get(link)
        resposta.raise_for_status()
        dados = resposta.json()
        
        if dados and len(dados) > 0:
            local = dados[0]
            resultado = {
                "nome": local.get("name", "Desconhecido"),
                "pais": local.get("country", ""),
                "estado": local.get("state", "")
            }
            return jsonify(resultado)
        else:
            return jsonify({"erro": "Local não encontrado"}), 404
    except requests.exceptions.RequestException as e:
        return jsonify({"erro": f"Erro na requisição: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
