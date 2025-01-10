import requests
import configuration

#Переменная хранит параметр для get-запроса с трековым номером заказа. Можно подставить любой номер заказа, информацию по которому хотите получить
params = {
    't': '821695'
}
#функция для запроса на получение данных заказа по трековому номеру любого созданного заказа (номера из переменной params)
def check_order():
    response = requests.get(configuration.URL+configuration.GET_ORDER,
                        params=params)
    return response

#снять комментирование строки ниже для вывода результатов функции
#print(check_order().status_code, check_order().json())