import requests
import data
import configuration

#функция для запроса на создание нового заказа
def new_order():
    return requests.post(configuration.URL + configuration.NEW_ORDER,
                         json=data.body_order)
response_new_order = new_order()

#снять комментирование строки ниже для вывода результатов функции
#print(response_order.status_code, response_order.json())

#в переменную track сохраняется номер трека созданного заказа
track = response_new_order.json()['track']