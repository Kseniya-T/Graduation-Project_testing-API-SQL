#Трифонова Ксения, 25-я когорта — Финальный проект. Инженер по тестированию плюс
import configuration
from create_new_order import new_order
import requests

#Функция для создания тестового заказа и извлечения его трекового номера, а так же изменение его типа данных на строку
def current_params():
    test_order = new_order()
    test_params = test_order.json()['track']
    return str(test_params)

t = current_params()
#Сохранение трекового номера в переменную для дальнейшего использования в качестве параметра для get-запроса
track = {'t':t}

#Функция на получение информации по трековому номеру, полученному в качестве параметра, созданного ранее заказа.
def get_order():
    return requests.get(configuration.URL + configuration.GET_ORDER,
                 params=track)
response_test = get_order()

#Проверка успешного получение информации по трековому номеру, полученному в качестве параметра, созданного ранее заказа – код ответа 200
def test_code_200_get_order():
    assert response_test.status_code == 200