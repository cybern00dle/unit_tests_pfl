# Запускаем юнит-тесты на GitHub!
Итак, представим, что в нашем красивом репозитории уже написаны все функции и тесты к ним. Теперь мы хотим, чтобы Гитхаб их автоматически тестировал. Как это сделать?

### Первые шаги: .github/workflows
Первым делом нам надо создать директорию, где будет храниться шаблон нашего рабочего процесса в формате YAML-файла. Это должна быть директория `.github/workflows`.

Выглядеть всё должно примерно так:
```
unit_tests_pfl/
│
├── .github/
    └── workflows
```

### Создаём YAML-файл
В директории `workflows` нам надо создать файл с расширением .yml. У нас это будет `say_hi_check.yml`.

### Заполняем файл
Начнём с имени и разрешений:
```yaml
name: CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]
```
Дальше начнём заполнять `jobs`. Начнём с использования версии Python.
```yaml
jobs:
  build:

    # на чём работает наша машина
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4
      # задаём шаг установки Python
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          # используем нужную версию
          python-version: '3.10'
```
Дальше нам нужно установить зависимости.
```yaml
steps:
  - uses: actions/checkout@v4
  - name: Set up Python
    uses: actions/setup-python@v5
    with:
      python-version: '3.10'
  - name: Install dependencies
    run: |
      # обновляем pip
      python -m pip install --upgrade pip
      # устанавливаем зависимости из requirements
      pip install -r requirements.txt
```
И теперь запускаем тесты!
```yaml
steps:
  - uses: actions/checkout@v4
  - name: Set up Python
    uses: actions/setup-python@v5
    with:
      python-version: '3.10'
  - name: Install dependencies
    run: |
      python -m pip install --upgrade pip
      pip install -r requirements.txt
  - name: Run tests
    run: python -m pytest tests
```
