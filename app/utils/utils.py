import datetime

ABOUT_ME = """Скачат абаи клыщ рыил

Бот умеет:

-принимать контакты пользователя ⚙
-отправлять запросы на сервер id.vchern.me
-играть с пользоватем 💾
-хранить информацию о пользователях 📓

Последнее обновление: 22 марта 2025 года
"""

def create_profile_message(user: dict):
    if user:
        USER_MESSAGE = f"""привет, {user['name']}!
        
Сейчас: {datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")}

У вас на балансе: {user["baance"]} руб.
    """