# Tiger & Leopards Detection in The Wild

По мотивам [хакатона](https://hacks-ai.ru/hakaton/samara)

Различает тигр или леопард на изображении. Моего кота принимает за тигра.

## Запуск
```
git clone https://github.com/JI411/tiger_or_leopard
cd tiger_or_leopard

docker built . -t tiger-or-leopard
docker run --rm -it tiger-or-leopard
```