import requests


API_KEY = "0153a042112f9529edbc2bad5372a198"

cidade =  "olinda"


link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}"

requisicao = requests.get(link)

requisicao_dic = requisicao.json()


print (requisicao_dic)