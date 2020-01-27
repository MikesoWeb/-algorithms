# Словари или подругому хэш таблицы

phone_book = {}

phone_book['police'] = 2
phone_book['emergency'] = 112
print(phone_book['police'])


# Программа при помощи словаря проверяет голосовал ли избиратель

voted = {}                          # список проголосовавших людей

def check_voter(name):              # человек приходит на избирательный участок
    if voted.get(name):             # если этот человек имеется в в нашем словаре
        print("fuck you bitch")     # отвечаем ему я твою маму ебал
    else:                           # иначе
        voted[name] = True          # делаем отметку о том что он проголосовал
        print("please vote guys")   # и кладем его в словарь

check_voter("rihard")
check_voter("mike")
check_voter("bily")
check_voter("rihard")


# Использование хеш таблиц при кешировании страниц

cache = {}                              # кэш памяти браузера

def get_page(url):                      # поступает гет запрос от пользователя
    if cache.get(url):                  # если этот запрос поступал ранее
        return cache[url]               # то из кеша достаем инфо и выдаем пользователю
    else:                               # иначе
       data = get_data_from_server(url) # делаем запрос к базе данным и получаем инфо
       cache[url] = data                # полученное инфо также кладем в кеш в виде словаря
       return data                      # выдаем клиенту инфо, следующий раз при таком запросе
                                        # мы по ключу словаря запросу выдадим со словаря всю информацию
