import requests




API_KEY = "0153a042112f9529edbc2bad5372a198"


cidade = "olinda"


link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

requisicao = requests.get(link)

requisicao_dic = requisicao.json()



descricao = requisicao_dic['weather'][0]
tempereatura = requisicao_dic['main']['temp']
sensacao = requisicao_dic['main']['feels_like']
temp_min = requisicao_dic['main']['temp_min']
temp_max = requisicao_dic['main']['temp_max']
pressao = requisicao_dic['main']['pressure']
umidade = requisicao_dic['main']['humidity']
nivel_mar = requisicao_dic['main']['sea_level']


print(descricao, tempereatura, sensacao, temp_min, temp_max, pressao, umidade, nivel_mar)

"""print(requisicao.json())"""