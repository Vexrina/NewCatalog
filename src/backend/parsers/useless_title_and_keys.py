notuniq_titles = [
    'Основные характеристики',
    'Упаковка',
    'Дополнительные характеристики',
    'Особенности'
]
notuniq_keys = [
    'Вес упаковки (ед)',
    'Гарантия',
    'Тип поставки',
    'Габариты упаковки (ед) ДхШхВ',
]

motherboard_titles = [
    'Процессор', 'Оперативная память',
    'Слоты расширения', 'Дисковые контроллеры',
    'Разъемы на задней панели', 'Коммуникации и аудио',
    'Прочие характеристики',
    'Количество разъемов SATA III. Интерфейс SATA III пришел на смену интерфейсу SATA II. Он предназначен для подключения внутренних жестких дисков и оптических приводов имеющих такойже интерфейс. Скорость передачи данных через интерфейс SATA III составляет  6Gb/s, что в два раза больше чем у интерфейса SATA II.',
    'Наличие в чипсете материнской платы встроенного RAID контроллера. RAID контроллер позволяет управлять несколькими жесткими дисками, с помощью которого система определяет их как единым целым.',
    'Поддержка материнской платой массива RAID 0. Основным преимуществом RAID 0 является  повышенная производительность (от количества установленных дисков зависит кратность увеличения производительности). Недостатком RAID 0 является уменьшение надёжности, так как  отказ одного из дисков приводит к неработоспособности всего массива.',
    'Поддержка материнской платой массива RAID 1. Основными преймуществами RAID 1 является высокая надежность, данный массив работает до тех пор, пока функционирует хотя бы один диск. Так же к плюсам можно отнести повышение скорости чтения при распараллеливании запросов. Основным недостатком RAID 1 является то, что если накопитель имеет общий объем 4 Тб (оснащен двумя жесткими дисками по 2 Тб), то при активизации RAID 1 общий объем уменьшится в два раза, что не всегда экономически выгодно.',
    'Скорость работы слотов PCI-Ex16 в многоканальном режиме. Многие материнские платы имеют несколько слотов PCI-Ex16 для установки видеокарт. При этом если установить несколько видеокарт, то скорость работы (частота, скорость передачи данных) этих слотов может отличаться.  Таким образом, если материнская плата оснащена двумя слотами PCI-Ex16, то если установить в них две абсолютно одинаковые видеокарты, то одна из них может работать на скорости x16, а вторая на скорости х8.',
    'Поддерживаемые режимы работы оперативной памяти, установленной в материнской плате. Все современные материнские платы поддерживают двухканальный режим работы оперативной памяти. Для этого режима необходимо, что бы два модуля одинаковой емкости были установлены парами в соответствующие слоты. В двухканальном режиме модули оперативной памяти работают на 5-10% быстрее чем две такие-же планки памяти в одноканальном режиме. Топовые модели процессоров поддерживают работу в трехканальном режиме. Для этого режима необходимо, что бы три модуля одинаковой емкости были установлены в соответствующие слоты. Все материнские платы, которые поддерживают многоканальные режимы работы памяти могут работать и в одноканальном режиме.',
    'Максимальный объем оперативной памяти, который поддерживается материнской платой. Данное значение зависит от количества слотов для установки оперативной памяти.',
    'Максимальная частота оперативной памяти, поддерживаемая каждой конкретной материнской платой. Если материнская плата поддерживает максимальную частоту 1333 МГц, то если установить в нее память с частотой 1600 МГц, то эта память будет работать на частоте 1333 МГц.',
    'Тип оперативной памяти, поддерживаемый материнской платой. Подавляющее большинство материнских плат имеет разъемы для установки памяти DIMM. В последнее время стали встречаться материнские платы с разъемами для памяти SO-DIMM. Память SO-DIMM в основном устанавливается в ноутбуки, моноблоки или неттопы. Материнские платы со слотами памяти SO-DIMM имеют форм-фактор mini-ITX и предназначены для создания домашних цифровых центров, которые занимают мало места и имеют низкое энергопотребление и тепловыделение.',
    'Поддержка материнской платы возможности установить несколько дискретных видеокарт. Современные высокопроизводительные видеокарты имеют возможность объединения в систему SLI или CrossFire. Для этого в некоторых материнских платах имеется несколько слотов для установки видеокарт. Современные технологии позволяют установить до 4-х видеокарт с одним графическим процессором. При установке нескольких видеокарт значительно увеличивается производительность компьютера в играх и графических редакторах.',
    'Модель чипсета материнской платы. Чипсет это набор микросхем, который предназначен для огранизации работы процессора, оперативной памяти, видеокарты и т.д. Как правило чипсет состоит из северного и южного моста. Северный мост отвечает за взаимодействие центрального процессора, оперативной памяти и видеокарты. Если установить высокопроизводительные комплектующие на "слабый" чипсет, то он будет играть роль "бутылочного горлышка" и не позволит им раскрыть весь потенциал. Южный мост отвечает за дисковые накопители, устройства ввода-вывода и устройства, установленные в слотах расширения материнской платы (звуковая карта, RAID-контроллер).',
    'Тип гнезда для установки процессора. От типа сокета зависит какую серию процессоров можно установить в материнскую плату. Материнские платы для процессоров INTEL имеют socket LGA775, LGA1155, LGA1156, LGA1366. Обозначение LGA означает, что сам процессор не имеет ножек, которые установлены на сокете материнской платы. Данные сокеты не имеют совместимости, т.е. процессор LGA1156 не получится установить в материнскую плату  с сокетом LGA775. Материнские платы для процессоров AMD имеют socket AM2, AM2+, AM3, AM3+, FM1. Процессоры с Socket AM2 полностью совместимы с материнскими платами AM2 и AM2+. Если процессор имеет socket AM2+, то его совместимость с материнскими платами AM2 не гарантирована и необходимо проверить совместимость на сайте производителя материнской платы. Процессоры с socket AM3 будут работать на материнских платах с гнездом AM2+, обратная совместимость не возможна процессоры AM2, AM2+ не будут работать на материнских платах AM3.',
    'Количество слотов PCI-Express х1 имеющихся на материнской плате. Ширину пропускания канала PCI Express можно масштабировать за счет добавления каналов с данными, при этом получаются соответствующие модификации шины. Слоты PCI-Express предназначены для установки в них звуковых карт и других периферийных плат расширения.',
]
motherboard_keys = [
    'Поддержка частот оперативной памяти',
    'Кол-во внешних USB 2.0',
    'Разъемов HDMI',
    'Сетевой интерфейс',
    'Сетевой контроллер',
    'Поддерживаемые процессоры',
    'Поддерживаемые модули памяти',
    'Поддерживаемые диски и накопители',
    'Особенности внешних разъемов',
    'Слотов PCI-E x1', 'Аудио контроллер',
    'Слотов PCI-E 4.0&nbsp;x16',
    'Разъем PS/2','Разъемов D-Sub (VGA)',
    'Слотов PCI-E 3.0&nbsp;x16',
    'Скорость работы слотов PCI-E x16 в многоканальном режиме',
    'Поддержка Intel Optane',
    'Поддержка SATA RAID','Поддержка RAID 0',
    'Поддержка RAID 1','Поддержка RAID 10',
    'Поддержка SLI/CrossFire',
    'Кол-во внешних USB 3.1',
    'Кол-во внешних USB 3.2 (Type-C)',
    'WiFi в стандартной поставке',
    'Bluetooth в стандартной поставке',
]

storage_titles = [
    'Энергопотребление',
    'Скорость',
    'Ресурс',
    'Габариты, вес',
    'Обратите внимание: в ряде случаев срок гарантии может отличаться от срока, указанного на официальном сайте бренда. Такой товар чаще всего ввезен по процедуре «параллельного импорта», гарантия бренда на него не распространяется.</p><p>*Что такое «Параллельный импорт»?</p><p>Это товар, ввезенный на территорию Российской Федерации в рамках процедуры «параллельного импорта» без согласия правообладателя, но из стран, где продажа данного товара легальна и сертифицирована.',
    'Поскольку такой товар ориентирован для реализации на территории других государств, гарантийные обязательства производителя на него на территории Российской Федерации не действуют. Этот товар не принимается на гарантийное обслуживание авторизированными сервисными центрами производителя. Все претензии по качеству товара в течение указанного гарантийного срока необходимо предъявлять продавцу.</p></div></div></div></div><div class="Specifications__column Specifications__column_value">',
    'Гарантия продавца',
]
storage_keys = [
    'Особенность',
    'Уровень шума простоя',
    'Длина устройства',
    'Толщина',
    'Вес устройства',
    'Ударостойкость при работе',
    'Ударостойкость при хранении',
    'Гарантийное обслуживание',
    'Контроллер NAND',
]

gpu_titles = [
    'Интерфейс видеокарты. Интерфейс шины PCI-Eх16 1.0 имеет пропускную способность (в одну/обе стороны) 32/64 Гбит/с, Интерфейс шины PCI-Eх16 2.0 имеет пропускную способность (в одну/обе стороны) 64/128 Гбит/с. Интерфейс шины PCI-Eх16 2.1 полностью соответствует интерфейсу PCI-Eх16 2.0, отличие касается только программной части, в которую добавлены функции планируемые к внедрению в версии PCI-Eх16 3.0.',
    'Производитель и модель графического процессора.',
    'Частота ядра графического процессора, установленного на видеокарте. Графический процессор видеокарты обрабатывает графическое изображение, что снижает нагрузку на центральный процессор компьютера. Чем выше частота графического процессора, тем производительнее видеокарта. При этом увеличивается энергопотребление и тепловыделение графического процессора, установленного на видеокарте.',
    'Частота ядра графического процессора, установленного на видеокарте. Графический процессор видеокарты обрабатывает графическое изображение, что снижает нагрузку на центральный процессор компьютера. Чем выше частота графического процессора, тем производительнее видеокарта. При этом увеличивается энергопотребление и тепловыделение  графического процессора, установленного на видеокарте.',
    'Технологический процесс, по которому изготовлен графический процессор. Техпроцесс определяет размеры полупроводниковых элементов, составляющих основу внутренних цепей графического процессора видеокарты.',
    'Объем видеопамяти, установленной на видеокарте. Видеопамять выполняет роль кадрового буфера, в котором хранится изображение, генерируемое графическим процессором и выводимое на экран монитора.',
    'Тип видеопамяти, установленной в видеокарте. Видеопамять бывает нескольких типов, различающихся по скорости доступа и рабочей частоте.',
    'Частота видеопамяти, установленной на видеокарте. Чем выше частота видеопамяти, тем производительнее видеокарта. При этом увеличивается энергопотребление и тепловыделение чипов памяти, установленных на видеокарте.',
    'Частота видеопамяти, установленной на видеокарте. Чем выше частота видеопамяти, тем производительнее видеокарта. При этом увеличивается энергопотребление и тепловыделение  чипов памяти, установленных на видеокарте.',
    'Разрядность шины видеопамяти, установленной в видеокарте. Означает количество бит информации, передаваемой за такт. Важный параметр в производительности видеокарты.',
    'Максимальное разрешение дисплея, поддерживаемое интерфейсными выходами видеокарты.',
    'Технологии',
    'Версии DirectX и OpenGL, которые поддерживает видеокарта. От версии DirectX и OpenGL зависит способность видеокарты на аппаратном уровне выполнять определенный набор функций.',
    'Разъемы',
    'Наличие в видеокарте разъема DVI (Dual-Link), который используется для передачи цифрового видеосигнала.',
    'Наличие в видеокарте разъема HDMI, который используется для передачи цифрового видеосигнала. Интерфейс HDMI разработан для передачи видео высокой четкости HDTV.',
    'Версия разъемов HDMI. В зависимости от версии, разъемы HDMI обладают различными характеристиками. Следует отметить, что изображение в формате 3D поддерживется только разъемами версии 1.4 и выше.',
    'Наличие в мониторе разъема Display Port, который используется для передачи цифрового видеосигнала. В отличии от разъемов DVI и HDMI, интерфейс Display Port имеет более широкий канал для передачи данных и большую максимальную длину кабеля.',
    'Версия разъемов Display Port. В зависимости от версии, разъемы Display Port обладают различными характеристиками.',
    'Питание',
    'Необходимость дополнительного питания видеокарты непосредственно от блока питания компьютера. Современные высокопроизводительные видеокарты потребляют значительное количество электроэнергии, поэтому электропитания через слот материнской платы для них недостаточно.',
    'Максимальное энергопотребление видеокарты. Чем производительнее видеокарта, тем выше ее энергопотребление.',
    'Рекомендуемая производителем видеокарты. Минимальная мощность блока питания компьютера, в котором будет установлена данная видеокарта.',
    'Система охлаждения графического процессора и видеопамяти. Чем выше производительность графического процессора и памяти, тем больше тепла они выделяют при работе. Система охлаждения позволяет надежно охлаждать видеокарту и отводить тепло из компьютерного корпуса.',
    'Использование в системе охлаждения видеокарты тепловых трубок (heatpipe), которые улучшают охлаждение графического процессора и видеопамяти.',
    'Видеокарты, имеющие тип поставки Retail (ret) поставляются в коробках и иногда имеют более богатую комплектацию (набор переходников, кабелей, рекламные материалы и т.п.). Видеокарты, имеющие тип поставки OEM/Bulk поставляются, как правило, в пакете, без дополнительной комплектации.',
    'Длина видеокарты от планки с видеовыходами, до окончания текстолита или системы охлаждения.',
    'Ширина видеокарты, характеризует сколько места в корпусе при установке займет конкретная видеокарта. Из-за сильного тепловыделения высокопроизводительных видеокарт система охлаждения может занимать несколько слотов расширения в компьютерном корпусе. При этом система охлаждения видеокарты перекрывает соседние разъемы на материнской плате и не позволяет их использовать.',
    'Размеры',
    'Данная характеристика указывает на заводской "разгон" (увеличение частот графического процессора и видеопамяти), который увеличивает производительность видеокарты, по сравнению с референсными видеокартами конкретной модели.',
]
gpu_keys = [
    'Интерфейс', 'Разрядность шины видеопамяти',
    'Поддержка технологий NVIDIA',
    'Ширина видеокарты', 'Версия разъема HDMI',
    'Версия разъема Display Port',
    'Использование тепловых трубок',
    'OverClock Edition', "Толщина видеокарты",
    'Высота видеокарты',
]

cpu_titles = [
    'Спецификация памяти',
    'Спецификация PCI Express',
    'Встроенная графика',
]
cpu_keys = [
    'Ядро', 'Разрядность вычислений',
    'Поддержка памяти ECC', 'Версия PCI Express',
    'Количество каналов PCI Express', 'Пропускная способность шины (GT/s)',
    'Конфигурация PCI Express', 'Пропускная способность памяти',
    'Максимальный объем видеопамяти', 'Максимальный объем памяти',
    'Тепловыделение в режиме Turbo',
    'Частота процессора в режиме Turbo 3.0',
    'Частота энергоэффективных ядер',
    'Количество высокопроизводительных ядер',
    'Количество энергоэффективных ядер'

]

fan_titles = [
    'Размеры, вес',
    'Электропитание', 'Конструкция',
    'Совместимость', 'Основные параметры',
    'Вентилятор с изогнутыми лопастями',
]
fan_keys = [
    'Направление выдува', 'Воздушный поток',
    'Тип подшипника', '-', 'Вес',
    'Длина кулера', 'Ширина кулера', 'Толщина вентилятора',
    'Воздушный поток вентилятора',
    'Назначение кулера для бренда',
    'Разборное крепление', 'Термопаста в комплекте',
    'Предназначено для ЦП', 'Материал тепловых трубок',
    'Предназначено для корпуса', 'Количество светодиодов подсветки',
    'Подсветка', 'Срок службы вентилятора',
]

ram_titles = [
    'Общие характеристики',
    'Тестовые характеристики',
    'Характеристики SPD',
    'Конструкция',
    'Error Checking and Correction',
    'Скорость памяти в тестовом режиме.',
    'Автоматические настройки модуля памяти.',
    'Задержка памяти в тестовом режиме.',
    'Скорость памяти в тестовом режиме.',
    'Напряжение памяти в тестовом режиме.',
]
ram_keys = [
    'Показатель скорости', 'Буферизация',
    'Поддержка ECC', 'Скорость (SPD)',
    'Напряжение (SPD)', 'Задержка (SPD)',
    'Радиатор охлаждения',
    'Количество чипов', 'Конфигурация чипов',
    'Крепление чипов', 'Вес упаковки',
]

pu_titles = [
    'Общие характеристики',
    'Версия стандарта АТХ и EPS, который поддерживает блок питания. Спецификации стандарта АТХ и EPS характеризуют наличие линий питания материнской платы, процессора, видеокарты.',
    'Максимальная отдаваемая мощность блока питания. Самый важный параметр, чем мощнее блок питания, тем больше высокопроизводительных комплектующих можно от него запитать.',
    'Наличие в блоке питания активной коррекции коэффициента мощности (Power Factor Correction, PFC). Коэффициент мощности - это отношение мощности, идущей на полезную работу к полученной. При наличии активного PFC коэффициент мощности достигает значения от 0.95 до 0.99.',
    'Коэффициент полезного действия (отношение выходной мощности к потребляемой). Чем выше данное значение, тем выше эффективность работы блока питания и тем меньше потери электроэнергии.',
    'Сертификация блока питания по стандарту 80 PLUS подразумевает соответствие его определённым нормативам по эффективности энергопотребления. При сертификации 80 PLUS КПД должен быть не менее 80% при 20%, 50% и 100% нагрузке, относительно номинальной мощности блока питания. При сертификации 80 PLUS BRONZE, КПД должен быть не менее 82% при аналогичной нагрузке, относительно номинальной мощности блока питания. При сертификации 80 PLUS SILVER, КПД должен быть не менее 85% при аналогичной нагрузке. При сертификации 80 PLUS GOLD, КПД должен быть не менее 87%. При сертификации 80 PLUS PLATINUM, КПД должен быть не менее 90%.',
    'Сертификация блока питания по стандарту 80 PLUS подразумевает соответствие его определённым нормативам по эффективности энергопотребления. При сертификации 80 PLUS КПД должен быть не менее 80% при 20%, 50% и 100% нагрузке, относительно номинальной мощности блока питания.  При сертификации 80 PLUS BRONZE, КПД должен быть не менее 82% при аналогичной нагрузке, относительно номинальной мощности блока питания. При сертификации 80 PLUS SILVER, КПД должен быть не менее 85% при аналогичной нагрузке. При сертификации 80 PLUS GOLD, КПД должен быть не менее 87%. При сертификации 80 PLUS PLATINUM, КПД должен быть не менее 90%.',
    'Цвет корпуса блока питания.',
    'Разъемы подключения',
    'Количество и тип разъемов БП, необходимых для питания материнской платы и процессора(ов). Все современные блоки питания имеют питание материнской платы 24 pin. В зависимости от версии стандарта ATX12V электропитание процессора может иметь как один 4 pin разъем, так и два разъема (4 pin + 4 pin), расположенных на одной линии питания. Разъем 8 pin по спецификации EPS12V предназначен для питания материнской платы и процессора.',
    'Длина линии питания 24 pin от блока питания до начала разъема.',
    'Количество и тип разъемов БП, необходимых для питания одной или нескольких видеокарт. Современные видеокарты имеют по несколько разъемов дополнительного питания. Если блок питания не имеет специальных разъемов, то приходится использовать переходники 2xPeripheral (Molex) на 6pin. Использование таких переходников занимает разъемы Peripheral (Molex), что может ограничить установку другого периферийного оборудования (жесткие диски, оптические приводы, устройства охлаждения).',
    'Количество разъемов SATA блока питания.',
    'Количество разъемов Peripheral (Molex) блока питания.',
    'Охлаждение',
    'Размер вентилятора, установленного в блоке питания. При одинаковой производительности вентилятор имеющий больший размер издает меньше шума.',
    'Количество вентиляторов, установленных в блоке питания. Часто блоки питания имеют один вентилятор (от 120 мм и выше), расположенный на нижней стенке. Но встречаются блоки питания которые имеют систему охлаждения состоящую из 2-х или 3-х вентиляторов размером 80 мм.',
    'Наличие в блоке питания регулятора оборотов вентилятора. В зависимости от нагрузкина блок питания, автоматически регулирует скорость вращения вентилятора, что заметно снижает уровень шума.',
    'Комплектация и размеры',
    'Наличие в комплекте поставки БП кабеля для подключения его к домашней электросети.',
    'Тип поставки блока питания. Блоки питания с типом поставки OEM, упакованы в пакет и как правило не имеют в комплекте сетевого кабеля. Блоки питания с типом поставки RET, упакованы в коробку и имеют в комплекте сетевой кабель, стяжки для укладки кабелей, винты крепления к корпусу и прочие полезные принадлежности.',
    'Наличие функции cable management позволяет отстегивать от блока неиспользуемые кабели питания. Это позволяет освободить место внутри корпуса, что улучшает циркуляцию воздуха внутри корпуса и упрощает сборку компьютера. В блоках питания с cable management отстегнуть можно только кабели питания периферийного оборудования (SATA, Molex) и видеокарты. Кабели питания материнской платы и процессора, в таких блоках, не имеют такой возможности.',
    'Средняя продолжительность работы блока питания между ремонтами.',
    'Габаритные размеры блока питания. Блоки питания АТХ имеют стандартные значения по ширине и высоте. Глубина показывает, сколько места блок питания займет внутри корпуса. Данная информация пригодится как для тех, кто планирует установить БП в небольшой компьютерный корпус, или посчитать не перекроет ли блок питания места для крепления верхних (или нижних) корпусных вентиляторов.',
    'Количество разъемов 4pin для подключения дисковода FDD.',
    'Тип подшипника вентилятора(ов), установленного в блоке питания.',
    'Максимальный уровень шума блока питания, заявленный производителем.',

]
pu_keys = [
    'Версия ATX',
    'Цвет',
    'Подшипник вентилятора(ов)',
    'Размер вентилятора(ов)',
    'Размеры (ШхВхГ)',
    'Разъемы для FDD',
    'Сетевой кабель',
    'Уровень шума',
    'Терморегулятор оборотов',
    'Количество вентиляторов',
]
