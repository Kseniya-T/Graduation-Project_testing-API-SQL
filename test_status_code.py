#Трифонова Ксения, 25-я когорта — Финальный проект. Инженер по тестированию плюс

import get_oder_use_track

#проверяем, что при запросе на получение информации о созданном заказе по трековому номеру возвращается статус кода 200
def test_code_200():
    current_response = get_oder_use_track.get_order()
    assert current_response.status_code == 200