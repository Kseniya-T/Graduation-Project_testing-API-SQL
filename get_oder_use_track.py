import requests
import configuration
import create_new_order

#функция для запроса на получение данных заказа по его трековому номеру, сохраненному при создании этого заказа
def get_order():
    return requests.get(configuration.URL+configuration.GET_ORDER+str(create_new_order.track))

response_order = get_order()

#снять комментирование строки ниже для вывода результатов функции
#print(response_order.status_code, response_order.json())