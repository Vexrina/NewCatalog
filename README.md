# NewCatalog
Analogue of e-katalog for Russia with additional features.

Аналог e-katalog для России с дополнительными фичами

# Design

https://www.figma.com/file/ik1wdwDS8ztPV5PDgJHSfd/newCatalog?node-id=0%3A1&t=xkhCAUcCIYev1bTW-1

# Stack

FastAPI, Sqlite, Selenium, Jinja2

# Roadmap//Дорожная карта

- [X] ~~Make a working website with clickable pseudo-products and transitions to a new page.~~

- [X] ~~Collect product data (CPU, GPU, RAM, etc.) from official sites (AMD, NVIDIA, INTEL, etc.)~~

- [X] ~~Make price data collection in the largest retailers - DNS, Citilink, Online-Trade, Regard~~

- [ ] Make an average performance data collection in synthetics

- [ ] Make data collection on average performance in video games

- [ ] launch?
___
- [X] ~~Сделать рабочий сайт, с кликабельными псевдотоварами и переходами на новую страницу.~~

- [X] ~~Сделать сбор данных о товарах (CPU, GPU, RAM, др.) с оффициальных сайтов AMD, NVIDIA, INTEL, др.)~~ 

- [X] ~~Сделать сбор данных о ценах в крупнейших ретейлерах - DNS, Citilink, Online-Trade, Regard~~

- [ ] Сделать сбор данных о средней производительности в синтетике

- [ ] Сделать сбор данных о средней производительности в видеоиграх

- [ ] Запуск?

# Maded by Vexrina

0.2 Версия претерпела изменения, ввиду того, что каждое новое поколение процессоров на сайте ark.intel.com имеет другую версию html верстки, было принято решение поискать другой сайт, где html верстка одинаковая. Одним из таких сайтов оказался - citilink.ru.

0.2.1 Поднят DockerContainer для поднятия API для будущих изучений или новвоведений в дизайн

0.3 Убрана Jinja2 и HTML-templates ввиду потребности в NextJS для университета

Update parser: 

useless_titles_and_keys.py - модуль пайтона который хранит в себе всевозможные ненужные строки для каждой категории

