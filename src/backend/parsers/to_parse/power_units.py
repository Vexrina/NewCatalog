to_parse = [
'https://www.citilink.ru/product/blok-pitaniya-aerocool-vx-plus-500w-500vt-120mm-chernyi-retail-vx-500-1049256/properties/',
'https://www.citilink.ru/product/blok-pitaniya-aerocool-vx-plus-600w-600vt-120mm-chernyi-retail-vx-600-1049258/properties/',
'https://www.citilink.ru/product/blok-pitaniya-aerocool-vx-plus-750w-750vt-120mm-chernyi-retail-vx-750-1049261/properties/',
'https://www.citilink.ru/product/blok-pitaniya-aerocool-vx-plus-650w-650vt-120mm-chernyi-retail-vx-650-1049259/properties/',
'https://www.citilink.ru/product/blok-pitaniya-aerocool-vx-plus-350vt-120mm-chernyi-retail-vx-350-plus-1049253/properties/',
'https://www.citilink.ru/product/blok-pitaniya-aerocool-vx-plus-400w-400vt-120mm-chernyi-retail-vx-400-1049254/properties/',
'https://www.citilink.ru/product/blok-pitaniya-aerocool-kcas-plus-800-800vt-120mm-chernyi-retail-kcas-8-1049270/properties/',
'https://www.citilink.ru/product/blok-pitaniya-aerocool-vx-plus-450w-450vt-120mm-chernyi-retail-vx-450-1049255/properties/',
'https://www.citilink.ru/product/blok-pitaniya-accord-acc-500w-np-500vt-120mm-acc-500-np-1208698/properties/',
'https://www.citilink.ru/product/blok-pitaniya-aerocool-vx-plus-700w-700vt-120mm-chernyi-retail-vx-700-1049260/properties/',
'https://www.citilink.ru/product/blok-pitaniya-aerocool-vx-plus-550w-550vt-120mm-chernyi-retail-vx-550-1049257/properties/',
'https://www.citilink.ru/product/blok-pitaniya-accord-acc-350w-12-350vt-120mm-acc-350-12-877950/properties/',
'https://www.citilink.ru/product/blok-pitaniya-aerocool-kcas-plus-700-700vt-120mm-chernyi-retail-kcas-7-1049265/properties/',
'https://www.citilink.ru/product/blok-pitaniya-aerocool-kcas-plus-gold-850w-rgb-850vt-120mm-retail-acpg-1440796/properties/',
'https://www.citilink.ru/product/blok-pitaniya-accord-acc-400w-12-400vt-120mm-acc-400-12-877951/properties/',
'https://www.citilink.ru/product/blok-pitaniya-zalman-atx-750w-zm750-gvii-80-bronze-20-4pin-apfc-135mm-1774705/properties/',
'https://www.citilink.ru/product/blok-pitaniya-accord-acc-450w-12-450vt-120mm-acc-450-12-877952/properties/',
'https://www.citilink.ru/product/blok-pitaniya-aerocool-kcas-plus-600-600vt-120mm-chernyi-retail-kcas-6-1049264/properties/',
'https://www.citilink.ru/product/blok-pitaniya-accord-atx-600w-acc-600w-np-24-4-4pin-120mm-fan-4xsata-1479118/properties/',
'https://www.citilink.ru/product/blok-pitaniya-thermaltake-lt-650p-650vt-120mm-chernyi-retail-ltp-0650p-305161/properties/',
'https://www.citilink.ru/product/blok-pitaniya-aerocool-aero-bronze-750vt-120mm-chernyi-retail-aero-bro-1207087/properties/',
'https://www.citilink.ru/product/blok-pitaniya-aerocool-eco-500-500vt-120mm-seryi-retail-1170085/properties/',
'https://www.citilink.ru/product/blok-pitaniya-aerocool-cylon-500-500vt-120mm-chernyi-retail-1111163/properties/',
'https://www.citilink.ru/product/blok-pitaniya-aerocool-eco-550-550vt-120mm-retail-1184523/properties/',
'https://www.citilink.ru/product/blok-pitaniya-aerocool-cylon-600-600vt-120mm-chernyi-retail-1111164/properties/',
'https://www.citilink.ru/product/blok-pitaniya-gigabyte-atx-650w-gp-p650b-80-bronze-24-4-4pin-apfc-120m-1422402/properties/',
'https://www.citilink.ru/product/blok-pitaniya-aerocool-kcas-plus-500-500vt-120mm-chernyi-retail-kcas-5-1049262/properties/',
'https://www.citilink.ru/product/blok-pitaniya-thermaltake-tr2-s-650vt-120mm-chernyi-retail-ps-trs-0650-365400/properties/',
'https://www.citilink.ru/product/blok-pitaniya-aerocool-cylon-700-700vt-120mm-chernyi-retail-1111165/properties/',
'https://www.citilink.ru/product/blok-pitaniya-gigabyte-atx-750w-gp-ud750gm-80-gold-24-2x-4-4-pin-apfc-1777099/properties/',
'https://www.citilink.ru/product/blok-pitaniya-aerocool-eco-450-450vt-120mm-seryi-retail-1144283/properties/',
'https://www.citilink.ru/product/blok-pitaniya-aerocool-aero-white-650vt-120mm-chernyi-retail-aero-whit-1207080/properties/',
'https://www.citilink.ru/product/blok-pitaniya-gigabyte-atx-850w-gp-ud850gm-80-gold-24-2x-4-4-pin-apfc-1777105/properties/',
'https://www.citilink.ru/product/blok-pitaniya-zalman-atx-700w-zm700-lxii-24-4-4pin-apfc-120mm-fan-6xsa-1775090/properties/',
'https://www.citilink.ru/product/blok-pitaniya-thermaltake-lt-550p-550vt-120mm-chernyi-retail-lt-0550p-365375/properties/',
'https://www.citilink.ru/product/blok-pitaniya-cooler-master-mwe-white-v2-750w-750vt-120mm-retail-mpe-7-1466350/properties/',
'https://www.citilink.ru/product/blok-pitaniya-cooler-master-mwe-white-v2-700vt-120mm-retail-mpe-7001-a-1468756/properties/',
'https://www.citilink.ru/product/blok-pitaniya-thermaltake-tr2-s-600vt-120mm-chernyi-retail-ps-trs-0600-365399/properties/',
'https://www.citilink.ru/product/blok-pitaniya-aerocool-atx-1000w-kcas-plus-1000gm-v2-24-8-4-4pin-apfc-1699844/properties/',
'https://www.citilink.ru/product/blok-pitaniya-thermaltake-smart-rgb-500-500vt-120mm-chernyi-retail-ps-480509/properties/',
'https://www.citilink.ru/product/blok-pitaniya-thermaltake-tr2-s-500vt-120mm-chernyi-retail-ps-trs-0500-365392/properties/',
'https://www.citilink.ru/product/blok-pitaniya-aerocool-sx-400-400vt-80mm-chernyi-retail-388484/properties/',
'https://www.citilink.ru/product/blok-pitaniya-aerocool-aero-white-600vt-120mm-chernyi-retail-aero-whit-1207079/properties/',
'https://www.citilink.ru/product/blok-pitaniya-formula-formula-ap600-80-600vt-120mm-chernyi-retail-1179260/properties/',
'https://www.citilink.ru/product/blok-pitaniya-thermaltake-smart-rgb-600-600vt-120mm-chernyi-retail-ps-482447/properties/',
'https://www.citilink.ru/product/blok-pitaniya-aerocool-eco-400-400vt-120mm-retail-1127630/properties/',
'https://www.citilink.ru/product/blok-pitaniya-aerocool-aero-bronze-550vt-120mm-chernyi-retail-aero-bro-1207083/properties/',
'https://www.citilink.ru/product/blok-pitaniya-linkworld-lw2-350w-lpe-case-350vt-80mm-retail-lw2-350wlp-80255/properties/',
'https://www.citilink.ru/product/blok-pitaniya-zalman-atx-650w-zm650-gvii-80-bronze-20-4pin-apfc-135mm-1775083/properties/',
'https://www.citilink.ru/product/blok-pitaniya-zalman-atx-500w-zm500-xeii-20-4pin-apfc-120mm-fan-4xsata-1775086/properties/',
'https://www.citilink.ru/product/blok-pitaniya-chieftech-atx-500w-i-arena-apb-500b8-20-4pin-apfc-120mm-1123737/properties/',
'https://www.citilink.ru/product/blok-pitaniya-aerocool-kcas-plus-gold-650w-rgb-650vt-120mm-retail-acpg-1440793/properties/',
'https://www.citilink.ru/product/blok-pitaniya-gigabyte-atx-750w-aorus-gp-ap750gm-80-gold-24-4-4pin-apf-1422467/properties/',
'https://www.citilink.ru/product/blok-pitaniya-thermaltake-tr2-s-550vt-120mm-chernyi-retail-ps-trs-0550-365398/properties/',
'https://www.citilink.ru/product/blok-pitaniya-aerocool-cylon-400-400vt-120mm-chernyi-retail-1111162/properties/',
'https://www.citilink.ru/product/blok-pitaniya-zalman-atx-600w-zm600-xeii-20-4pin-apfc-120mm-fan-4xsata-1775087/properties/',
'https://www.citilink.ru/product/blok-pitaniya-cooler-master-mwe-bronze-650w-v2-650vt-120mm-chernyi-ret-1446161/properties/',
'https://www.citilink.ru/product/blok-pitaniya-aerocool-aero-white-550vt-120mm-chernyi-retail-aero-whit-1207088/properties/',
'https://www.citilink.ru/product/blok-pitaniya-gigabyte-atx-450w-gp-p450b-80-bronze-24-4-4pin-apfc-120m-1422333/properties/',
'https://www.citilink.ru/product/blok-pitaniya-cooler-master-mwe-bronze-750w-v2-750vt-120mm-chernyi-ret-1446125/properties/',
]