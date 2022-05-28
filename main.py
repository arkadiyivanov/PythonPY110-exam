from config import json, random, Faker, MODEL

fake_ = Faker('ru_RU')

model = MODEL

pk = 1


def main():
    model_ = {"model": model, "pk": pk,
              "feilds": {"title": title(), "year": year(), "pages": pages(), "isbn13": isbn13(), "rating": rating(), "price": price(), "author": author()}}

    with open('model.txt', 'w', encoding='utf-8') as f:
        json.dump(model_, f, indent=4, ensure_ascii=False)


def title():
    title_ = {1: 'Сказки старого демона', 2: 'Путешествие назад', 3: 'Золото инков', 4: 'Притча', 5: 'Байки'}
    d = random.choice(title_)
    with open("books.txt", "w") as f:
        json.dump(d, f, indent=4, ensure_ascii=False)
    return d


def year():
    year_ = random.randint(1991, 2022)
    return year_


def pages():
    page = random.randrange(20, 1000)
    return page


def isbn13():
    return fake_.isbn13()


def rating():
    rating_ = random.random() * 5
    return rating_


def price():
    price_ = round(random.random(), 2) * 1000
    return price_


def author():
    for i in range(3):
        return fake_.name()


if __name__ == "__main__":
    main()
