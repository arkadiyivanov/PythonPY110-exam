from config import json, random, Faker, MODEL

fake_ = Faker('ru_RU')

model = MODEL

pk = 1


def main():
    model_ = {"model": model, "pk": pk,
              "feilds": {"title": title(), "year": year(), "pages": pages(), "isbn13": isbn13(), "rating": rating(),
                         "price": price(), "author": author()}}

    with open('model.txt', 'a', encoding='utf-8') as f:
        json.dump(model_, f, indent=4, ensure_ascii=False)


def title():
    """Список названия книг"""
    title_ = ['Сказки старого демона', 'Путешествие назад', 'Золото инков', 'Притча', 'Байки']
    d = random.choice(title_)
    with open("books.txt", "w", encoding='utf-8') as f:
        json.dump(title_, f, indent=4, ensure_ascii=False)

    return d


def year():
    """Случайное значение года"""
    year_ = random.randint(1991, 2022)
    return year_


def pages():
    """Случайное количество страниц"""
    page = random.randrange(20, 1000)
    return page


def isbn13():
    """Книжный номер"""
    return fake_.isbn13()


def rating():
    """Рэйтинг книги """
    rating_ = random.random() * 5
    return rating_


def price():
    """Цена книги"""
    price_ = round(random.random(), 2) * 1000
    return price_


def author():
    """Авторы """
    list_ = []
    for aut_ in range(1, 4):
        c = fake_.name()
        list_.append(c)

    k = random.randint(1, 3)
    return random.sample(list_, k)


for i in range(100):
    main()
    pk += 1

if __name__ == "__main__":
    main()
