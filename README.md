# NewCatalog
Analogue of e-katalog for Russia with additional features.

Аналог e-katalog для России с дополнительными фичами

# Design

https://www.figma.com/file/ik1wdwDS8ztPV5PDgJHSfd/newCatalog?node-id=0%3A1&t=xkhCAUcCIYev1bTW-1

# Stack

FastAPI, Sqlite, Selenium, BeautifulSoup4, Jinja2

# Roadmap//Дорожная карта

0.1. ~~~Make a working website with clickable pseudo-products and transitions to a new page.~~~

0.2. Collect product data (CPU, GPU, RAM, etc.) from official sites ~~~(AMD, NVIDIA, INTEL, etc.)~~~

0.3. ~~~Make price data collection in the largest retailers - DNS, Citilink, Online-Trade, Regard ~~~

0.4. Make an average performance data collection in synthetics

0.5. Make data collection on average performance in video games

1.0. launch?
___
0.1 ~~~Сделать рабочий сайт, с кликабельными псевдотоварами и переходами на новую страницу.~~

0.2 Сделать сбор данных о товарах (CPU, GPU, RAM, др.) с оффициальных сайтов ~~~(AMD, NVIDIA, INTEL, др.)~~~ 

0.3 ~~~Сделать сбор данных о ценах в крупнейших ретейлерах - DNS, Citilink, Online-Trade, Regard~~~

0.4 Сделать сбор данных о средней производительности в синтетике

0.5 Сделать сбор данных о средней производительности в видеоиграх

1.0 Запуск?

# Maded by Vexrina

0.2 версия претерпела изменения, ввиду того, что каждое новое поколение процессоров на сайте ark.intel.com имеет другую версию html верстки, было принято решение поискать другой сайт, где html верстка одинаковая. Одним из таких сайтов оказался - citilink.ru.

Update parser: 

gpu_useless_lines.txt -- при парсинге ситилинка со страницами GPU появились проблемы. Их "ознакомительные строки", т.е. информация для не очень опытных юзеров, такие как "Что такое частота видеопамяти, Версии HDMI" - заполняют очень много места и не дают спокойно сделать dict. Файл хранит в себе строки, ненужные для парсинга и, соответственно, сайта. Т.к. в коде хранить их было бы сверх неудобно, перенес их в файл.